import os, sys, tempfile, threading, unittest, urllib.request, urllib.error, http.client

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
os.environ['XUONG_DATA'] = tempfile.mkdtemp()
import nhatky, app, suckhoe  # noqa: E402


class T(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sv = app.tao_may_chu(0, 'matest')
        cls.port = cls.sv.server_address[1]
        threading.Thread(target=cls.sv.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.sv.shutdown()

    def req(self, method, path, body=None, cookie=None, host=None):
        c = http.client.HTTPConnection('127.0.0.1', self.port, timeout=10)
        h = {'Host': host or '127.0.0.1:%d' % self.port}
        if cookie:
            h['Cookie'] = cookie
        if body is not None:
            h['Content-Type'] = 'application/x-www-form-urlencoded'
        c.request(method, path, body, h)
        r = c.getresponse()
        return r.status, r.read().decode('utf-8'), r.getheader('Set-Cookie')

    def test_bind_loopback(self):
        self.assertEqual(self.sv.server_address[0], '127.0.0.1')

    def test_can_dang_nhap(self):
        s, b, _ = self.req('GET', '/')
        self.assertIn('mã truy cập', b)

    def test_sai_ma_va_dung_ma(self):
        s, _, _ = self.req('POST', '/dangnhap', 'ma=sai')
        self.assertEqual(s, 403)
        s, _, ck = self.req('POST', '/dangnhap', 'ma=matest')
        self.assertEqual(s, 303)
        self.assertTrue(ck.startswith('xuong='))

    def test_suc_khoe_va_5_khu(self):
        _, _, ck = self.req('POST', '/dangnhap', 'ma=matest')
        ck = ck.split(';')[0]
        s, b, _ = self.req('GET', '/', cookie=ck)
        self.assertEqual(s, 200)
        self.assertIn('Sức khỏe', b)
        for k in ('hieu', 'sua', 'build', 'vanhanh', 'suasau'):
            s, _, _ = self.req('GET', '/khu/' + k, cookie=ck)
            self.assertEqual(s, 200, k)

    def test_chan_host_la(self):
        s, _, _ = self.req('GET', '/', host='evil.example')
        self.assertEqual(s, 403)

    def test_bao_loi_loc_bi_mat(self):
        d = tempfile.mkdtemp()
        nhatky.ghi('TEST', 'password=hunter2 token: abcdef')
        p, ma = nhatky.bao_loi(d, '0.0', '/x', 'api_key=SECRET123 gặp lỗi')
        t = open(p, encoding='utf-8').read()
        self.assertNotIn('hunter2', t)
        self.assertNotIn('SECRET123', t)
        self.assertTrue(ma.startswith('XUONG-'))
        p2, ma2 = nhatky.bao_loi(d, '0.0', '/x', 'lần 2')
        self.assertNotEqual(ma, ma2)

    def test_suc_khoe_modul(self):
        ds = suckhoe.kiem_tra(os.path.dirname(os.path.dirname(AQUI)))
        self.assertTrue(any(t == 'Python' for t, _, _ in ds))


if __name__ == '__main__':
    unittest.main()
