#!/usr/bin/env python
"""Hook Stop cua Claude Code (Q-21): PM dinh dung luot ma BACKLOG con task chua xong va khong bi chan boi viec can chu du an
thi chan dung va nhac lam task ke tiep. Doc STATE/TRANG-THAI.md, TASKS/BACKLOG.md, TASKS/<ID>.md. Chi doc, khong ghi file nao trong repo.

Cho phep dung (thoat 0, khong in gi) khi:
  1. Chu du an go /ket-thuc-ca o tin nhan nguoi dung cuoi (doc transcript).
  2. Codex cham tran ngay: dong "Hôm nay: N USD" trong muc Ngan sach Codex >= tran ngay (mac dinh 200), hoac Da dung >= 1000 USD / 7 ngay,
     hoac co the [CODEX-CHAM-TRAN] trong TRANG-THAI.md.
  3. Moi task con lai deu bi chan: task loi 3 lan lien tiep (TASKS/<ID>.md co dong "lỗi liên tiếp: 3", hoac ghi chu bang tien do co "lỗi 3 lần"),
     hoac dang cho chu du an (ghi chu/trang thai co "chờ chủ" hoac "cần chủ").
  4. Co the [DUNG-CAN-CHU yyyy-mm-dd HH:MM] trong TRANG-THAI.md, con hieu luc 12 gio. PM PHAI ghi the nay (kem ly do) truoc khi dung, xoa khi lam tiep.
  6. (Q-29) Con thu chua xu ly trong HOP-THU/CHO-SONNET.md thi CHAN (tru khi 1-3 o tren); thu cho ket qua danh dau [ĐANG CHỜ] trong tieu de thi khong chan.
  5. Het task, hoac da chan >= 60 lan trong mot phien (an toan chong vong lap vo han), hoac loi bat ky cua hook (an toan: khong chan).
Chan: in JSON {"decision":"block","reason":...} ra stdout.
"""
import json, os, re, sys, time, tempfile

HOPTHU = 'HOP-THU'

ROOT = os.environ.get('JX1_OPS_ROOT', r'D:\jx1-ops-wt\JX1_OPS')
DAILY_CAP, WEEK_CAP, MAX_BLOCKS, MARK_HOURS = 200.0, 1000.0, 60, 12


def allow():
    sys.exit(0)


def last_user_text(path):
    try:
        last = ''
        with open(path, encoding='utf-8') as f:
            for ln in f:
                try:
                    o = json.loads(ln)
                except ValueError:
                    continue
                m = o.get('message') or {}
                if o.get('type') == 'user' and m.get('role') == 'user':
                    c = m.get('content')
                    t = c if isinstance(c, str) else ' '.join(x.get('text', '') for x in c if isinstance(x, dict) and x.get('type') == 'text')
                    if t.strip() and '<system-reminder>' not in t[:20] and '<task-notification>' not in t[:40]:
                        last = t
        return last
    except OSError:
        return ''


def num(s):
    return float(s.replace('.', '').replace(',', '.')) if re.search(r'[.,]\d{3}\b', s) else float(s.replace(',', '.'))


def pending_letters():
    """Thu chua xu ly trong HOP-THU/CHO-SONNET.md (muc 'Chua xu ly'); bo qua thu co the [DANG CHO]."""
    try:
        s = open(os.path.join(ROOT, HOPTHU, 'CHO-SONNET.md'), encoding='utf-8').read()
    except OSError:
        return []
    a = s.find('## Chưa xử lý')
    if a < 0:
        return []
    b = s.find('## Đã xử lý', a)
    sec = s[a:b if b > 0 else len(s)]
    return [h.strip() for h in re.findall(r'^## (#\d+[^\n]*)', sec, re.M) if '[ĐANG CHỜ]' not in h]


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = {}
    sys.path.insert(0, os.path.join(ROOT, 'TOOLS'))
    import bang_tien_do as B
    if 'ket-thuc-ca' in last_user_text(data.get('transcript_path', '')).lower().replace('_', '-'):
        allow()
    state = B.read(os.path.join(ROOT, 'STATE', 'TRANG-THAI.md'))
    # 0. Hop thu (Q-29): con thu chua xu ly thi lam truoc khi dung (khong qua mat cac dieu kien dung cung ben duoi neu tran Codex)
    letters = pending_letters()
    # 4. dung can chu du an (hieu luc co han)
    for m in re.finditer(r'\[DUNG-CAN-CHU\s+(\d{4}-\d\d-\d\d)\s+(\d\d:\d\d)\]', state):
        try:
            t = time.mktime(time.strptime(m.group(1) + ' ' + m.group(2), '%Y-%m-%d %H:%M'))
            if time.time() - t < MARK_HOURS * 3600: allow()
        except ValueError:
            pass
    # 2. Codex cham tran
    if '[CODEX-CHAM-TRAN]' in state: allow()
    bud = B.section(state, 'Ngân sách Codex')
    m = re.search(r'Hôm nay:\s*([\d.,]+)\s*USD', bud)
    if m and num(m.group(1)) >= DAILY_CAP: allow()
    b = B.budget(state)
    if b['used7'] is not None and b['used7'] >= WEEK_CAP: allow()
    if letters:
        sf0 = os.path.join(tempfile.gettempdir(), 'jx_stop_guard_%s.json' % re.sub(r'\W', '', data.get('session_id', 'x'))[:40])
        try:
            n0 = json.load(open(sf0))['n']
        except Exception:
            n0 = 0
        if n0 < MAX_BLOCKS:
            try:
                json.dump({'n': n0 + 1}, open(sf0, 'w'))
            except OSError:
                pass
            print(json.dumps({'decision': 'block', 'reason': 'HOP-THU (Q-29): còn %d thư chưa xử lý trong HOP-THU/CHO-SONNET.md: %s. Làm các thư này trước, chuyển xuống mục "Đã xử lý" kèm giờ và 1 dòng kết quả, trả lời ngắn vào TU-SONNET.md nếu thư yêu cầu. Không dừng lượt.' % (len(letters), '; '.join(x[:80] for x in letters))}))
            return
    # 3/5. task con lai
    phases = B.parse_backlog(B.read(os.path.join(ROOT, 'TASKS', 'BACKLOG.md')))
    table = B.status_table(state)
    raw = {}
    for ln in B.section(state, 'Tiến độ task').splitlines():
        if ln.startswith('|'):
            c = B.cells(ln)
            if c: raw[c[0]] = ln.lower()
    todo, blocked = [], []
    for ph in phases:
        for t in ph['tasks']:
            tid = t['id']
            st = table[tid][0] if tid in table else (B.front(ROOT, tid) or 'cho')
            if st == 'xong': continue
            note = raw.get(tid, '')
            tf = B.read(os.path.join(ROOT, 'TASKS', tid + '.md')).lower()
            fails = [int(x) for x in re.findall(r'lỗi liên tiếp:\s*(\d+)', tf)] + [int(x) for x in re.findall(r'lỗi (\d+) lần', note)]
            why = None
            if fails and max(fails) >= 3: why = 'lỗi 3 lần liên tiếp'
            elif 'chờ chủ' in note or 'cần chủ' in note: why = 'cần chủ dự án'
            (blocked if why else todo).append((tid, t['title'], st, why))
    if not todo: allow()
    # an toan chong vong lap
    sf = os.path.join(tempfile.gettempdir(), 'jx_stop_guard_%s.json' % re.sub(r'\W', '', data.get('session_id', 'x'))[:40])
    try:
        n = json.load(open(sf))['n']
    except Exception:
        n = 0
    if n >= MAX_BLOCKS: allow()
    try:
        json.dump({'n': n + 1}, open(sf, 'w'))
    except OSError:
        pass
    # task dang chay uu tien, roi task dau tien trong BACKLOG theo thu tu
    nxt = next((x for x in todo if x[2] == 'dang chay'), todo[0])
    msg = ('KHÔNG DỪNG LƯỢT (Q-21, hook Stop): BACKLOG còn %d task chưa xong và chưa bị chặn. Làm tiếp ngay: %s – %s [%s]. '
           'Không kết thúc lượt bằng câu hỏi: việc nhỏ hoặc có mặc định thì tự quyết và ghi STATE/QUYET-DINH.md; chỉ hỏi khi không đảo ngược được hoặc cần quyền của chủ. '
           'Chỉ được dừng khi: Codex chạm trần ngày, một task lỗi 3 lần liên tiếp, hoặc đến việc bắt buộc cần chủ dự án (ghi thẻ [DUNG-CAN-CHU yyyy-mm-dd HH:MM] + lý do vào TRANG-THAI.md trước), hoặc chủ gõ /ket-thuc-ca.'
           ) % (len(todo), nxt[0], nxt[1][:140], nxt[2])
    if blocked:
        msg += ' (Đang bị chặn, bỏ qua: ' + ', '.join('%s (%s)' % (x[0], x[3]) for x in blocked) + '.)'
    print(json.dumps({'decision': 'block', 'reason': msg}))


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        raise
    except Exception:
        sys.exit(0)
