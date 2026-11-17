import json, sys, time, urllib.request
key = open(r'C:\Users\PC\.jx1keys\JX-GROQ.txt').read().strip()
model = sys.argv[1] if len(sys.argv) > 1 else 'openai/gpt-oss-120b'
PROMPT = "Tóm tắt trong khoảng 400 từ tiếng Việt: lịch sử ngắn của trò chơi nhập vai trực tuyến thập niên 2000 ở châu Á, gồm cách chơi, mô hình thu phí, và lý do chúng được yêu thích."
body = json.dumps({"model": model, "stream": True, "max_tokens": 1500,
                   "messages": [{"role": "user", "content": PROMPT}],
                   "stream_options": {"include_usage": True}}).encode()
req = urllib.request.Request('https://api.groq.com/openai/v1/chat/completions', body,
    {'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json', 'User-Agent': 'jx1-speedtest/1.0'})
t0 = time.time(); ttft = None; chunks = 0; usage = None
try:
    with urllib.request.urlopen(req, timeout=120) as r:
        for line in r:
            line = line.decode('utf-8', 'ignore').strip()
            if not line.startswith('data:') or line.endswith('[DONE]'): continue
            d = json.loads(line[5:])
            if d.get('usage') or (d.get('x_groq') or {}).get('usage'): usage = d.get('usage') or d['x_groq']['usage']
            ch = d.get('choices') or []
            if ch and (ch[0].get('delta') or {}).get('content'):
                chunks += 1
                if ttft is None: ttft = time.time() - t0
    total = time.time() - t0
    out = (usage or {}).get('completion_tokens', chunks)
    print(json.dumps({"model": model, "ttft": round(ttft or -1, 2), "total": round(total, 2), "out_tok": out,
        "tok_s_gen": round(out / max(total - (ttft or 0), 0.01), 1), "usage": usage}, ensure_ascii=False))
except urllib.error.HTTPError as e:
    print(json.dumps({"model": model, "http": e.code, "body": e.read()[:300].decode('utf-8', 'ignore')}))
