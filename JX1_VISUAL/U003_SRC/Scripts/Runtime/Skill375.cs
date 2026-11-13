using System.Collections.Generic;
using UnityEngine;

namespace U003
{
    public class Missile181
    {
        public int castId, k; public Vector2 pos; public float spawnT, startT, endT; public int delayTicks;
        public bool started, done, collided, bzDone; public float bzT; public GameObject go; public SpriteRenderer sr;
    }
    public class Missile193
    {
        public int castId, aoeId, fromK; public Vector2 pos; public float spawnT, activateT; public bool hitDone, done;
        public GameObject go; public SpriteRenderer sr;
    }
    public class Fx
    {
        public SprSheet sheet; public GameObject go; public SpriteRenderer sr; public float t0, dur; public int frames;
    }
    public class PendingCast { public int castId; public float eventT; public Vector2 target; public bool spawned; }

    // Skill 375 Loi Dong Cuu Thien. Chuoi hinh anh theo goc (375 -> 16x181 -> va cham -> 193); luat sat thuong la U003 (DESIGN):
    //  - 181 KHONG gay sat thuong; 193 tao AOE doc lap, 2 tick (+500ms, +1000ms), 20 dmg/quai song trong 3x3 o, cong don.
    public class Skill375
    {
        public readonly List<Missile181> m181 = new List<Missile181>();
        public readonly List<Missile193> m193 = new List<Missile193>();
        public readonly List<Fx> fxs = new List<Fx>();
        readonly List<PendingCast> pending = new List<PendingCast>();
        public int castCount, spawned181, collided181, spawned193, aoeTicks, damageEvents; public long totalDamage; public int lastCastId;
        public int aoeSeq; public bool fixedSeed = false;
        SprSheet s181, s193, sBz;
        Game g;
        public Skill375(Game game)
        {
            g = game;
            s181 = SprSheet.Load("spr/m181"); s193 = SprSheet.Load("spr/m193"); sBz = SprSheet.Load("spr/bz_dian3");
        }

        public int ActiveAoe { get { int n = 0; foreach (var a in m193) if (!a.done) n++; return n; } }
        public int Active181 { get { int n = 0; foreach (var m in m181) if (m.started && !m.done) n++; return n; } }
        public int Pending181 { get { int n = 0; foreach (var m in m181) if (!m.started && !m.done) n++; return n; } }

        public int BeginCast(float now, Vector2 targetMps)
        {
            int id = ++castCount; lastCastId = id;
            pending.Add(new PendingCast { castId = id, eventT = now + Cfg.CastSeconds * Cfg.CastEventFraction, target = targetMps });
            Evt.Log(now, "cast#" + id + " begin target=" + (int)targetMps.x + "," + (int)targetMps.y);
            return id;
        }

        // Do tre RANDONORDER: WaitTime + k*Data + (rand(2)==1 ? +rand(Data) : -rand(Data/2)), WaitTime=2, Data=5 (S/KSkills.cpp:3272-3312)
        static int DelayTicks(System.Random rng, int k)
        {
            const int wait = 2, data = 5;
            if (rng.Next(2) == 1) return wait + k * data + rng.Next(data);
            return wait + k * data - rng.Next(data / 2);
        }

        long lastTick = -1;
        public void Step(float now)
        {
            long tk = (long)Mathf.Floor(now * Cfg.LogicHz); bool newTick = tk != lastTick; lastTick = tk; float qNow = tk / Cfg.LogicHz;   // luoi tick logic
            // 1) sinh 16 dan 181 tai moc su kien cast
            for (int i = pending.Count - 1; i >= 0; i--)
            {
                var p = pending[i];
                if (now < p.eventT) continue;
                pending.RemoveAt(i);
                var rng = new System.Random(fixedSeed ? Cfg.TestSeed + p.castId : (System.Environment.TickCount ^ (p.castId * 7919)));
                float bx = p.target.x - Cfg.GridN * Mps.Cell / 2f, by = p.target.y - Cfg.GridN * Mps.Cell / 2f;
                for (int a = 0; a < Cfg.GridN; a++)
                    for (int b = 0; b < Cfg.GridN; b++)
                    {
                        int k = a * Cfg.GridN + b;
                        var m = new Missile181 { castId = p.castId, k = k, pos = new Vector2(bx + b * Mps.Cell, by + a * Mps.Cell), spawnT = now };
                        m.delayTicks = DelayTicks(rng, k);
                        m.startT = now + m.delayTicks / Cfg.DataHz; m.endT = m.startT + Cfg.Missile181Life / Cfg.DataHz;
                        m181.Add(m); spawned181++;
                    }
                Evt.Log(now, "cast#" + p.castId + " spawn 16x181");
            }
            // 2) 181: bat dau, kiem tra va cham 5x5 o. Chuoi sat thuong chay ngay khi va ccham, con HINH tia set van chay du 6 khung
            //    (khung 2-5 cham dat) roi no Bz_dian3 luc tia set cham dat (startT + 4 tick = khung 2).
            for (int i = m181.Count - 1; i >= 0; i--)
            {
                var m = m181[i];
                if (m.done) { Cleanup(m); m181.RemoveAt(i); continue; }
                if (!m.started && newTick && now >= m.startT)
                {
                    m.started = true;
                    m.go = new GameObject("m181_" + m.castId + "_" + m.k); m.sr = m.go.AddComponent<SpriteRenderer>();
                    m.go.transform.position = Mps.ToWorld(m.pos.x, m.pos.y);
                    m.sr.sortingOrder = g.map.OrderForY(m.pos.y) + 8;
                }
                if (!m.started) continue;
                int fi = Mathf.Clamp((int)(Mathf.Max(0f, qNow - m.startT) * Cfg.DataHz / 2f), 0, s181.FrameCount - 1);   // AnimFile2 "6,1,2": 2 tick/khung
                if (m.sr != null) m.sr.sprite = s181.Get(fi);
                if (!m.collided && newTick)
                {
                    int cx = Mps.CellOf(m.pos.x), cy = Mps.CellOf(m.pos.y);
                    bool hit = false;
                    foreach (var mo in g.monsters)
                        if (mo.Alive && Mathf.Abs(mo.CellX - cx) <= 2 && Mathf.Abs(mo.CellY - cy) <= 2) { hit = true; break; }
                    if (hit)
                    {
                        HitMonstersInRange(now, cx, cy, "cast#" + m.castId + " 181[" + m.k + "]", false);
                        m.collided = true; collided181++; m.bzT = Mathf.Max(now, m.startT + 4f / Cfg.DataHz);
                        var a = new Missile193 { castId = m.castId, aoeId = ++aoeSeq, fromK = m.k, pos = m.pos, spawnT = now, activateT = now + Cfg.Delay193 / Cfg.DataHz };
                        m193.Add(a); spawned193++;
                        Evt.Log(now, "cast#" + m.castId + " 181[" + m.k + "] collide -> 193 aoe#" + a.aoeId + " activate@" + a.activateT.ToString("F3"));
                    }
                }
                if (m.collided && !m.bzDone && now >= m.bzT) { m.bzDone = true; SpawnBz(now, m.pos); }
                if (now >= m.endT)
                {
                    if (!m.collided) Evt.Log(now, "cast#" + m.castId + " 181[" + m.k + "] expire");
                    if (m.collided && !m.bzDone) { m.bzDone = true; SpawnBz(now, m.pos); }
                    m.done = true;
                }
            }
            // 3) 193: sau 5 tick bat dau; moi tick logic kiem tra va cham (+-2 o); va cham dau tien gay damage 1 lan (goc: ColVanish);
            //    hinh 27 khung chay het doi 12 tick roi no Bz_dian3 (khong cat som, nhu 181).
            for (int i = m193.Count - 1; i >= 0; i--)
            {
                var a = m193[i];
                if (a.done) { if (a.go != null) Object.Destroy(a.go); m193.RemoveAt(i); continue; }
                if (now < a.activateT) continue;
                if (a.go == null)
                {
                    a.go = new GameObject("m193_" + a.aoeId); a.sr = a.go.AddComponent<SpriteRenderer>();
                    a.go.transform.position = Mps.ToWorld(a.pos.x, a.pos.y);
                    a.sr.sortingOrder = g.map.OrderForY(a.pos.y) + 9;
                }
                float el = now - a.activateT, life = Cfg.Missile193Life / Cfg.DataHz;
                a.sr.sprite = s193.Get(Mathf.Clamp((int)(el / life * s193.FrameCount), 0, s193.FrameCount - 1));
                if (!a.hitDone && newTick)
                {
                    int n = HitMonstersInRange(now, Mps.CellOf(a.pos.x), Mps.CellOf(a.pos.y), "cast#" + a.castId + " 193#" + a.aoeId, true);
                    if (n > 0) a.hitDone = true;
                }
                if (el >= life) { a.done = true; SpawnBz(now, a.pos); }
            }
            // 4) hieu ung phu (no)
            for (int i = fxs.Count - 1; i >= 0; i--)
            {
                var f = fxs[i]; float el = now - f.t0;
                if (el >= f.dur) { Object.Destroy(f.go); fxs.RemoveAt(i); continue; }
                f.sr.sprite = f.sheet.Get(Mathf.Clamp((int)(el / f.dur * f.frames), 0, f.frames - 1));
            }
        }

        void SpawnBz(float now, Vector2 pos)
        {
            var f = new Fx { sheet = sBz, t0 = now, frames = sBz.FrameCount, dur = sBz.FrameCount * sBz.meta.interval / 1000f };
            f.go = new GameObject("bz"); f.sr = f.go.AddComponent<SpriteRenderer>();
            f.go.transform.position = Mps.ToWorld(pos.x, pos.y); f.sr.sortingOrder = g.map.OrderForY(pos.y) + 10;
            fxs.Add(f);
        }

        System.Random dmgRng;
        // Moi va cham: moi quai trong vung va cham (+-2 o) nhan damage rieng ngau nhien 15..25. Tra ve so quai trung.
        int HitMonstersInRange(float now, int cx, int cy, string src, bool from193)
        {
            if (dmgRng == null) dmgRng = new System.Random(fixedSeed ? Cfg.TestSeed + 777 : System.Environment.TickCount);
            int n = 0;
            foreach (var mo in g.monsters)
            {
                if (!mo.Alive) continue;
                if (Mathf.Abs(mo.CellX - cx) <= 2 && Mathf.Abs(mo.CellY - cy) <= 2)
                {
                    int d = dmgRng.Next(Cfg.DamageMin, Cfg.DamageMax + 1);
                    n++; damageEvents++; totalDamage += d; if (from193) aoeTicks++;
                    Evt.Log(now, src + " hit monster#" + mo.id + " dmg=" + d);
                    g.DamageMonster(mo, d, now, false, src + " dmg=" + d);
                }
            }
            return n;
        }

        void Cleanup(Missile181 m) { if (m.go != null) Object.Destroy(m.go); }
    }
}
