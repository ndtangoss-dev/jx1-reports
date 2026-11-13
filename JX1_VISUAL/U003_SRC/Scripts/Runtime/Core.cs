using System;
using System.Collections.Generic;
using UnityEngine;

namespace U003
{
    // Toa do: MPS (logic, y gap doi man hinh). 1 world unit = 1 pixel man hinh goc.
    // screen_x = mps_x ; screen_y = mps_y/2 - z*887/1024 (KSubWorld.cpp:188-192, bao cao 58). Unity y huong len => dao dau.
    public static class Mps
    {
        public const int Cell = 32;               // o logic 32x32 MPS
        public const int RegionW = 512, RegionH = 1024;
        public static Vector3 ToWorld(float mx, float my, float z = 0f) { return new Vector3(mx, -(my * 0.5f) + z * 887f / 1024f, 0f); }
        public static Vector2 FromWorld(Vector2 w) { return new Vector2(w.x, -w.y * 2f); }
        public static int CellOf(float v) { return Mathf.FloorToInt(v / Cell); }
    }

    public static class Cfg
    {
        // Luat U003 (bao cao 59, muc 3) -- DESIGN, khong phai du lieu goc
        public const float LogicHz = 18f;            // 18 tick/giay: lua chon prototype, KHONG khang dinh Hz client goc
        public const float SimStep = 1f / 60f;       // buoc mo phong co dinh cho timer/damage, khong phu thuoc FPS render
        public const int MonsterHp = 1000;
        public const int PlayerHp = 500;
        public const float CastSeconds = 1.0f;
        public const float CooldownSeconds = 1.0f;   // tinh tu luc bat dau cast
        public const float CastEventFraction = 0.6f; // goc: IsReachFrame(60) (KNpc.cpp:6852). Gia dinh ap dung cho cast 1 s.
        public const int AoeDamage = 20;
        public const float AoeTick1 = 0.5f, AoeTick2 = 1.0f;
        public const float RespawnSeconds = 2.0f;
        public const float DamageNumberSeconds = 1.0f;
        public const int Missile181Life = 12;        // khung logic (goc LifeTime=12)
        public const int Delay193 = 5;               // khung logic (goc WaitTime=5)
        public const int GridN = 4;                  // luoi 4x4 = 16 dan 181
        public const int TestSeed = 12345;
    }

    // ---- Atlas SPR (da xuat boi Tools/export_spr.py) ----
    [Serializable] public class FrameRec { public int x, y, w, h, ox, oy; }
    [Serializable] public class SourceRec { public string pak, entryId, path, flag, how; }
    [Serializable]
    public class SprMeta
    {
        public string id; public SourceRec source;
        public int W, H, cx, cy, dirs, framesPerDir, frameCount, interval, atlasW, atlasH;
        public FrameRec[] frames;
    }

    public class SprSheet
    {
        public SprMeta meta; public Texture2D tex; public Vector2 anchor; Sprite[] cache;
        static readonly Dictionary<string, SprSheet> all = new Dictionary<string, SprSheet>();
        public static int LoadedCount { get { return all.Count; } }

        public static SprSheet Load(string resPath)
        {
            SprSheet s;
            if (all.TryGetValue(resPath, out s)) return s;
            var ta = Resources.Load<TextAsset>("U003/" + resPath);
            var tex = Resources.Load<Texture2D>("U003/" + resPath);
            if (ta == null || tex == null) { Debug.LogError("[U003] thieu atlas " + resPath); return null; }
            s = new SprSheet();
            s.meta = JsonUtility.FromJson<SprMeta>(ta.text);
            s.tex = tex;
            tex.filterMode = FilterMode.Bilinear; tex.wrapMode = TextureWrapMode.Clamp;
            var m = s.meta;
            // Anchor theo ccgetTxtData (KgameWorld.cpp:8115-8183, bao cao 58 muc E): header Center != 0 -> dung Center;
            // nguoc lai neu Width > 160 -> (160,192); nguoc lai (0,0). Offset khung cong them qua pivot.
            if (m.cx != 0 || m.cy != 0) s.anchor = new Vector2(m.cx, m.cy);
            else if (m.W > 160) s.anchor = new Vector2(160, 192);
            else s.anchor = Vector2.zero;
            s.cache = new Sprite[m.frames.Length];
            all[resPath] = s;
            return s;
        }

        public int FramesPerDir { get { return meta.framesPerDir; } }
        public int FrameCount { get { return meta.frames.Length; } }

        public Sprite Get(int i)
        {
            if (i < 0 || i >= cache.Length) return null;
            var sp = cache[i];
            if (sp != null) return sp;
            var f = meta.frames[i];
            if (f.w <= 0 || f.h <= 0) return null;
            float px = anchor.x - f.ox;               // pivot tinh tu goc trai-duoi cua khung
            float py = f.h - (anchor.y - f.oy);
            var rect = new Rect(f.x, meta.atlasH - f.y - f.h, f.w, f.h);
            sp = Sprite.Create(tex, rect, new Vector2(px / f.w, py / f.h), 1f, 0, SpriteMeshType.FullRect);
            cache[i] = sp;
            return sp;
        }
    }

    public static class Rand { }

    public static class Dir8
    {
        // huong sprite 0..7: 0=xuong(S) 1=xuong-trai 2=trai 3=len-trai 4=len(N) 5=len-phai 6=phai 7=xuong-phai (g05_dirmap, bao cao 55)
        public static int FromScreen(float dx, float dy)  // dy > 0 la di len tren man hinh
        {
            float a = Mathf.Atan2(-dx, -dy) * Mathf.Rad2Deg;
            if (a < 0) a += 360f;
            return Mathf.RoundToInt(a / 45f) % 8;
        }
    }

    // Nhat ky su kien (phuc vu test, truy vet castId/aoeId)
    public static class Evt
    {
        public static readonly List<string> Lines = new List<string>();
        public static void Log(float t, string s)
        {
            string l = t.ToString("F3") + " " + s;
            Lines.Add(l);
            if (Lines.Count > 20000) Lines.RemoveRange(0, 5000);
        }
    }
}
