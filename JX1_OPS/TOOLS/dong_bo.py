"""Một lệnh đồng bộ git cho Sonnet A và B (#244). Chạy trong worktree của mình:
  python -I JX1_OPS/TOOLS/dong_bo.py [--push]
Làm: bỏ thay đổi cục bộ ở file Tổng quản tự sinh (nó sinh lại) -> thấy file khác còn sửa dở thì DỪNG (commit trước)
-> fetch -> rebase origin/jx1-ops. Xung đột: file Tổng quản sinh = lấy bản origin; file chỉ-nối-thêm = gộp union;
file khác = DỪNG, in tên, rebase còn dang dở để người xử lý. Không dùng autostash, không xóa stash."""
import os, subprocess, sys

BR = 'jx1-ops'
SINH = ['JX1_OPS/STATE/SONNET-SONG.md', 'JX1_OPS/STATE/TIEU-YEU.md', 'JX1_OPS/STATE/KHOA-XINGCHI.md',
        'JX1_OPS/STATE/TIEN-DO.md', 'JX1_OPS/STATE/TONG-QUAN-GHI.md', 'JX1_OPS/STATE/BAN-GIAO.md']
NOI = ['JX1_OPS/STATE/QUYET-DINH.md', 'JX1_OPS/STATE/BAI-HOC.md', 'JX1_OPS/HOP-THU/VONG.md',
       'JX1_OPS/HOP-THU/NHAT-KY-CHAT.md', 'JX1_OPS/HOP-THU/TU-SONNET.md', 'JX1_OPS/HOP-THU/TU-SONNET-B.md', 'JX1_OPS/HOP-THU/A-B.md']
NOI_TIEN_TO = ('JX1_OPS/STATE/NHAT-KY',)


def git(*a, ok=False):
    r = subprocess.run(['git', *a], capture_output=True, text=True, encoding='utf-8', errors='replace')
    if r.returncode and not ok:
        print('git', *a, '->', r.returncode, (r.stderr or r.stdout).strip()[:300])
    return r.returncode, r.stdout.strip()


def la_noi(p):
    return p in NOI or p.startswith(NOI_TIEN_TO)


def conflicts():
    return [l[3:] for l in git('status', '--porcelain', ok=True)[1].splitlines() if l[:2] in ('UU', 'AA', 'DU', 'UD', 'AU', 'UA')]


def main():
    root = git('rev-parse', '--show-toplevel')[1]
    os.chdir(root)
    git('checkout', 'HEAD', '--', *SINH, ok=True)
    dirty = [l for l in git('status', '--porcelain', '--untracked-files=no')[1].splitlines() if l.strip()]
    if dirty:
        print('DUNG: con file sua do chua commit (commit hoac git stash tay roi chay lai):')
        print('\n'.join(dirty)); sys.exit(2)
    git('fetch', '-q', 'origin', BR)
    rc, _ = git('rebase', f'origin/{BR}', ok=True)
    while conflicts():
        stop = []
        for p in conflicts():
            if p in SINH:
                git('checkout', '--ours', '--', p)  # trong rebase, "ours" = origin
                git('add', '--', p)
            elif la_noi(p):
                tmp = {}
                for n, st in (('base', 1), ('ours', 2), ('theirs', 3)):
                    r = subprocess.run(['git', 'show', f':{st}:{p}'], capture_output=True)
                    tmp[n] = r.stdout if r.returncode == 0 else b''
                d = os.path.join(root, '.git_dongbo_tmp'); os.makedirs(d, exist_ok=True)
                fs = {}
                for n in tmp:
                    fs[n] = os.path.join(d, n); open(fs[n], 'wb').write(tmp[n])
                cur = os.path.join(root, p)
                open(cur, 'wb').write(tmp['ours'])
                subprocess.run(['git', 'merge-file', '--union', cur, fs['base'], fs['theirs']])
                git('add', '--', p)
            else:
                stop.append(p)
        if stop:
            print('DUNG: xung dot o file can nguoi xu ly (rebase dang do, git rebase --abort de huy):')
            print('\n'.join(stop)); sys.exit(3)
        rc, out = git('-c', 'core.editor=true', 'rebase', '--continue', ok=True)
    gd = git('rev-parse', '--git-dir')[1]
    if any(os.path.isdir(os.path.join(gd, d)) for d in ('rebase-merge', 'rebase-apply')):
        print('DUNG: rebase con dang do (git status de xem), chua day len.'); sys.exit(5)
    if os.path.isdir(os.path.join(root, '.git_dongbo_tmp')):
        import shutil; shutil.rmtree(os.path.join(root, '.git_dongbo_tmp'), ignore_errors=True)
    if '--push' in sys.argv:
        rc, _ = git('push', '-q', 'origin', f'HEAD:{BR}')
        if rc:
            sys.exit(4)
    print('dong_bo OK:', git('log', '--oneline', '-1')[1])


if __name__ == '__main__':
    main()
