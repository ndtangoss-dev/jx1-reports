"""XƯỞNG JX1 — khung M0. Giao diện web cục bộ, chỉ nghe 127.0.0.1, có mã truy cập.
Chạy: python -I -X utf8 TOOLS/xuong/app.py   (hoặc bấm đúp XuongJX1.bat)
Mỗi khu là một mô-đun; mô-đun hỏng không làm sập app."""
import os, sys, html, hashlib, hmac, secrets, traceback, importlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import nhatky  # noqa: E402

VERSION = '0.1'
GOC_KHO = os.path.dirname(os.path.dirname(AQUI))          # .../JX1_OPS
BUGS = os.path.join(GOC_KHO, 'BUGS')
KHU = [  # (id, tên, mô-đun, mô tả, mốc)
    ('hieu', 'HIỂU', None, 'Tra cứu mã nguồn, gói tin, tri thức.', 'M1'),
    ('sua', 'SỬA NỘI DUNG', None, 'Sửa bảng dữ liệu, script Lua, ảnh (không cần code).', 'M2'),
    ('build', 'BUILD & TRIỂN KHAI', None, 'Build server/APK, cài vào LDPlayer, đẩy lên VM thử.', 'M3'),
    ('vanhanh', 'VẬN HÀNH', None, 'Bật/tắt cụm server, xem cổng, log, tài khoản.', 'M4'),
    ('suasau', 'SỬA SÂU', None, 'Quy trình sửa C++ có hướng dẫn.', 'M5'),
]
CSS = ('body{font:15px system-ui,sans-serif;margin:0;background:#f6f4ee;color:#1d1b16}'
       'header{background:#2b2a24;color:#f2e9d0;padding:10px 16px;display:flex;gap:14px;flex-wrap:wrap;align-items:center}'
       'header a{color:#f2e9d0;text-decoration:none;padding:4px 8px;border-radius:4px}header a:hover,header a.on{background:#5a4a1e}'
       'main{padding:16px;max-width:900px}.xanh{color:#1a7f37}.vang{color:#9a6700}.do{color:#cf222e}'
       'table{border-collapse:collapse;width:100%}td,th{border-bottom:1px solid #d8d2c0;padding:6px;text-align:left}'
       'textarea,input{font:inherit;width:100%;box-sizing:border-box}button{font:inherit;padding:6px 14px}'
       '.hop{background:#fff;border:1px solid #d8d2c0;padding:12px;margin:10px 0;border-radius:6px}')


def khoa_phien(ma):
    return hashlib.sha256(('xuong|' + ma).encode()).hexdigest()


def trang(tieu_de, noi_dung, dang_o=''):
    menu = ['<a href="/" class="%s">Sức khỏe</a>' % ('on' if dang_o == '' else '')]
    for k, ten, _, _, moc in KHU:
        menu.append('<a href="/khu/%s" class="%s">%s</a>' % (k, 'on' if dang_o == k else '', html.escape(ten)))
    menu.append('<a href="/khu/goi" class="%s">Gói tin</a>' % ('on' if dang_o == 'goi' else ''))
    menu.append('<a href="/baoloi">Báo lỗi</a>')
    return ('<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>Xưởng JX1 — %s</title><style>%s</style><header><b>XƯỞNG JX1 %s</b>%s</header><main>%s</main>'
            % (html.escape(tieu_de), CSS, VERSION, ''.join(menu), noi_dung)).encode('utf-8')


def trang_suc_khoe():
    try:
        import suckhoe
        importlib.reload(suckhoe)
        ds = suckhoe.kiem_tra(GOC_KHO)
    except Exception as e:  # mô-đun hỏng không làm sập app
        nhatky.ghi('SUC-KHOE', 'lỗi mô-đun', traceback.format_exc())
        return '<div class="hop do">Mô-đun Sức khỏe lỗi: %s. Đã ghi nhật ký; bấm Báo lỗi.</div>' % html.escape(str(e))
    nhan = {'xanh': 'ĐẠT', 'vang': 'CHÚ Ý', 'do': 'LỖI'}
    hang = ''.join('<tr><td>%s</td><td class="%s"><b>%s</b></td><td>%s</td></tr>' % (html.escape(t), s, nhan[s], html.escape(g)) for t, s, g in ds)
    do = sum(1 for _, s, _ in ds if s == 'do')
    tong = '<p class="%s"><b>%s</b></p>' % ('do' if do else 'xanh', ('%d mục lỗi — xem bảng.' % do) if do else 'Mọi mục bắt buộc đều đạt.')
    return '<h2>Sức khỏe</h2>' + tong + '<table><tr><th>Mục</th><th>Kết quả</th><th>Chi tiết</th></tr>%s</table>' % hang


class Handler(BaseHTTPRequestHandler):
    ma = ''
    server_version = 'XuongJX1'

    def log_message(self, *a):
        pass

    def _gui(self, code, body, extra=None):
        self.send_response(code)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Cache-Control', 'no-store')
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def _dang_nhap(self):
        ck = self.headers.get('Cookie', '')
        for p in ck.split(';'):
            k, _, v = p.strip().partition('=')
            if k == 'xuong' and hmac.compare_digest(v, khoa_phien(self.ma)):
                return True
        return False

    def _form(self):
        n = min(int(self.headers.get('Content-Length') or 0), 65536)
        return {k: v[0] for k, v in parse_qs(self.rfile.read(n).decode('utf-8', 'replace')).items()}

    def _chan_nguon(self):
        h = (self.headers.get('Host') or '').split(':')[0]
        return h not in ('127.0.0.1', 'localhost', '[::1]')

    def do_GET(self):
        if self._chan_nguon():
            return self._gui(403, b'Chi cho phep localhost')
        u = urlparse(self.path)
        if not self._dang_nhap():
            return self._gui(200, trang('Đăng nhập', '<h2>Nhập mã truy cập</h2><form method="post" action="/dangnhap"><input name="ma" type="password" autofocus><p><button>Vào</button></p></form><p>Mã nằm trong D:\\JX-xuong\\ma.txt (hoặc biến XUONG_CODE).</p>'))
        try:
            if u.path == '/':
                nhatky.ghi('SUC-KHOE', 'mở trang')
                return self._gui(200, trang('Sức khỏe', trang_suc_khoe()))
            if u.path.startswith('/khu/'):
                k = u.path[5:]
                if k == 'goi':
                    import goi
                    importlib.reload(goi)
                    qs = parse_qs(u.query)
                    nhatky.ghi('GOI', 'mở trang')
                    return self._gui(200, trang('Gói tin', goi.trang(GOC_KHO, qs.get('q', [''])[0], qs.get('n', [''])[0]), 'goi'))
                if k == 'hieu':
                    import hieu
                    importlib.reload(hieu)
                    qs = parse_qs(u.query)
                    nhatky.ghi('HIEU', 'mở khu')
                    return self._gui(200, trang('HIỂU', hieu.trang(GOC_KHO, qs.get('f', [''])[0], qs.get('q', [''])[0]), 'hieu'))
                for kid, ten, _, mt, moc in KHU:
                    if kid == k:
                        nhatky.ghi(kid.upper(), 'mở khu')
                        return self._gui(200, trang(ten, '<h2>%s</h2><div class="hop">%s<p>Mốc <b>%s</b> — <i>chưa làm</i>.</p></div>' % (html.escape(ten), html.escape(mt), moc), kid))
            if u.path == '/baoloi':
                tr = parse_qs(u.query).get('tu', [''])[0]
                return self._gui(200, trang('Báo lỗi', '<h2>Báo lỗi</h2><form method="post" action="/baoloi"><input type="hidden" name="trang" value="%s"><p>Chuyện gì đã xảy ra? (ghi nguyên văn)</p><textarea name="mota" rows="6"></textarea><p><button>Gửi báo lỗi</button></p></form><p>Sẽ tạo BUGS/XUONG-NNN.md kèm 200 dòng nhật ký (đã lọc khóa/mật khẩu) và chụp màn hình lưu ngoài kho.</p>' % html.escape(tr or self.headers.get('Referer', ''))))
            return self._gui(404, trang('Không thấy', '<h2>Không thấy trang</h2>'))
        except Exception as e:
            nhatky.ghi('LOI', self.path, traceback.format_exc())
            return self._gui(500, trang('Lỗi', '<div class="hop do">Có lỗi — đã ghi lại, bấm <a href="/baoloi">Báo lỗi</a>.<br>%s</div>' % html.escape(str(e))))

    def do_POST(self):
        if self._chan_nguon():
            return self._gui(403, b'Chi cho phep localhost')
        u = urlparse(self.path)
        f = self._form()
        if u.path == '/dangnhap':
            if hmac.compare_digest(f.get('ma', ''), self.ma):
                nhatky.ghi('DANG-NHAP', 'đúng mã')
                return self._gui(303, b'', {'Location': '/', 'Set-Cookie': 'xuong=%s; HttpOnly; SameSite=Strict; Path=/' % khoa_phien(self.ma)})
            nhatky.ghi('DANG-NHAP', 'sai mã')
            return self._gui(403, trang('Sai mã', '<h2>Sai mã.</h2><a href="/">Thử lại</a>'))
        if not self._dang_nhap():
            return self._gui(403, b'Chua dang nhap')
        if u.path == '/baoloi':
            try:
                p, ma = nhatky.bao_loi(BUGS, VERSION, f.get('trang', ''), f.get('mota', ''))
                return self._gui(200, trang('Đã báo lỗi', '<div class="hop xanh">Đã tạo <b>%s</b> (%s). Sonnet sẽ nhận khi đẩy lên kho.</div>' % (ma, html.escape(p))))
            except Exception as e:
                nhatky.ghi('LOI', 'baoloi', traceback.format_exc())
                return self._gui(500, trang('Lỗi', '<div class="hop do">Không tạo được báo lỗi: %s</div>' % html.escape(str(e))))
        return self._gui(404, trang('Không thấy', '<h2>Không thấy</h2>'))


def tao_may_chu(port=8770, ma=None):
    Handler.ma = ma or nhatky.ma_truy_cap()
    return ThreadingHTTPServer(('127.0.0.1', port), Handler)   # CỐ ĐỊNH loopback


def main():
    port = int(os.environ.get('XUONG_PORT', '8770'))
    sv = tao_may_chu(port)
    nhatky.ghi('APP', 'khởi động v%s cổng %d' % (VERSION, port))
    print('Xuong JX1 v%s: http://127.0.0.1:%d/  (ma truy cap: D:\\JX-xuong\\ma.txt)' % (VERSION, port))
    try:
        sv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
