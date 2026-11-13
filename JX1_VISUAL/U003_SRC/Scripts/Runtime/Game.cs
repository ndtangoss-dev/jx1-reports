using System.Collections.Generic;
using System.IO;
using System.Text;
using UnityEngine;

namespace U003
{
    public class DmgNum { public GameObject go; public SpriteRenderer[] srs; public float t0; public Vector3 start; public float jitter; }

    // U003 first playable: dieu phoi mo phong co dinh (Cfg.SimStep), quai, nhan vat, skill 375, damage number.
    public class Game : MonoBehaviour
    {
        public static Game I;
        public MapView map; public Skill375 skill; public GameUI ui; public Camera cam;
        public readonly List<Monster> monsters = new List<Monster>();
        public PlayerChar pl; PartSheets ps = new PartSheets();
        SprSheet a_st, a_wlk, a_bat, a_die, a_at;
        string[][] order8;
        public float simTime, acc; public long simSteps;
        public float viewH = 540f;
        public int totalMonsterKills, monsterRespawns, playerDeaths; public long totalDamageAll;
        public bool testMode;   // seed co dinh
        public bool freezeAI;
        public string startupLog = "";
        System.Random rng = new System.Random(Cfg.TestSeed);
        static Sprite whiteSp; Sprite[] digitSp = new Sprite[10]; Vector2[] digitSize = new Vector2[10];
        readonly List<DmgNum> nums = new List<DmgNum>(); public int dmgNumbersSpawned;
        public Vector2[] spawnPoints = new Vector2[15];
        const float MonsterSpeed = 70f, PlayerSpeed = 140f, AggroPx = 100000f /* quai tu tim nhan vat tren toan ban do */, AttackRangePx = 52f, PlayerRangePx = 70f, SkillRangePx = 320f;

        static Sprite White()
        {
            if (whiteSp == null)
            {
                var t = new Texture2D(2, 2, TextureFormat.RGBA32, false); t.SetPixels32(new Color32[] { Color.white, Color.white, Color.white, Color.white }); t.Apply();
                whiteSp = Sprite.Create(t, new Rect(0, 0, 2, 2), new Vector2(0f, 0.5f), 2f, 0, SpriteMeshType.FullRect);
            }
            return whiteSp;
        }

        void Awake() { I = this; Application.targetFrameRate = 60; Screen.sleepTimeout = SleepTimeout.NeverSleep; }

        void Start()
        {
            testMode = System.Environment.GetEnvironmentVariable("U003_AUTOTEST") != null;
            var camGo = new GameObject("Main Camera"); camGo.tag = "MainCamera"; cam = camGo.AddComponent<Camera>();
            cam.orthographic = true; cam.orthographicSize = viewH / 2f; cam.backgroundColor = new Color(0.05f, 0.05f, 0.07f); cam.clearFlags = CameraClearFlags.SolidColor;
            camGo.transform.position = new Vector3(0, 0, -10);

            map = new GameObject("Map").AddComponent<MapView>();
            if (!map.Build()) { Debug.LogError("[U003] khong dung duoc map"); return; }
            startupLog += "map regions=" + map.map.regions.Length + " sprites=" + map.sprites + " objects=" + map.ObjectsDrawn + "\n";

            a_st = SprSheet.Load("spr/ani001_st"); a_wlk = SprSheet.Load("spr/ani001_wlk"); a_bat = SprSheet.Load("spr/ani001_bat");
            a_die = SprSheet.Load("spr/ani001_die"); a_at = SprSheet.Load("spr/ani001_at");
            LoadDigits();
            LoadOrder();
            BuildPlayer();
            BuildSpawns();
            skill = new Skill375(this) { fixedSeed = testMode };
            ui = gameObject.AddComponent<GameUI>(); ui.g = this;
            startupLog += "sheets=" + SprSheet.LoadedCount + "\n";
            Debug.Log("[U003] ready\n" + startupLog);
            if (testMode) gameObject.AddComponent<AutoTest>();
        }

        // ---------- khoi tao ----------
        void LoadOrder()
        {
            var ta = Resources.Load<TextAsset>("U003/char_order");
            var w = JsonUtility.FromJson<OrderWrap>(ta.text);
            order8 = new string[8][];
            for (int d = 0; d < 8; d++) order8[d] = w.order[d].items;
        }

        void LoadDigits()
        {
            var tex = Resources.Load<Texture2D>("U003/ui/number_16_r");
            var fnt = Resources.Load<TextAsset>("U003/ui/number_16_r.fnt");
            foreach (var line in fnt.text.Split('\n'))
            {
                if (!line.StartsWith("char ")) continue;
                int id = Field(line, "id"), x = Field(line, "x"), y = Field(line, "y"), w = Field(line, "width"), h = Field(line, "height");
                if (id >= 48 && id <= 57)
                {
                    int d = id - 48;
                    digitSp[d] = Sprite.Create(tex, new Rect(x, tex.height - y - h, w, h), new Vector2(0.5f, 0f), 1f, 0, SpriteMeshType.FullRect);
                    digitSize[d] = new Vector2(w, h);
                }
            }
        }
        static int Field(string line, string key)
        {
            int i = line.IndexOf(key + "=");
            if (i < 0) return 0;
            i += key.Length + 1; int j = i;
            while (j < line.Length && (char.IsDigit(line[j]) || line[j] == '-')) j++;
            return int.Parse(line.Substring(i, j - i));
        }

        void BuildPlayer()
        {
            pl = new PlayerChar();
            ps.st = SprSheet.Load("spr/man_bd_st"); // placeholder, thay theo tung bo phan ben duoi
            pl.partNames = new string[] { "bd", "lh", "rh", "hd", "hr" };
            pl.go = new GameObject("Player");
            pl.parts = new SpriteRenderer[5];
            for (int i = 0; i < 5; i++)
            {
                var p = new GameObject(pl.partNames[i]); p.transform.SetParent(pl.go.transform, false);
                pl.parts[i] = p.AddComponent<SpriteRenderer>();
            }
            pl.pos = new Vector2(map.PlayCells.center.x * Mps.Cell - 1400, map.PlayCells.center.y * Mps.Cell + 900);
            pl.dir = 0;
            pl.castFx = new GameObject("castfx"); pl.castFxSr = pl.castFx.AddComponent<SpriteRenderer>(); pl.castFx.SetActive(false);
        }

        void BuildSpawns()
        {
            // 15 diem spawn co dinh: luoi 5x3 quanh trung tam vung choi, lech co dinh (seed 12345), cach nhau ~520 x 760 MPS
            var r = new System.Random(Cfg.TestSeed);
            float cx = map.PlayCells.center.x * Mps.Cell, cy = map.PlayCells.center.y * Mps.Cell;
            int n = 0;
            for (int j = 0; j < 3; j++)
                for (int i = 0; i < 5; i++)
                {
                    var p = new Vector2(cx + (i - 2) * 520f + r.Next(-120, 121), cy + (j - 1) * 760f + r.Next(-160, 161));
                    spawnPoints[n] = p;
                    var m = new Monster { id = n, spawn = p, pos = p, hp = Cfg.MonsterHp, state = MState.Idle, dir = r.Next(8) };
                    m.go = new GameObject("ani001_" + n); m.sr = m.go.AddComponent<SpriteRenderer>();
                    m.hpBg = new GameObject("hpbg"); m.hpBg.transform.SetParent(m.go.transform, false); m.hpBgSr = m.hpBg.AddComponent<SpriteRenderer>();
                    m.hpFg = new GameObject("hpfg"); m.hpFg.transform.SetParent(m.go.transform, false); m.hpFgSr = m.hpFg.AddComponent<SpriteRenderer>();
                    m.hpBgSr.sprite = White(); m.hpFgSr.sprite = White();
                    m.hpBgSr.color = new Color(0, 0, 0, 0.7f); m.hpFgSr.color = new Color(0.9f, 0.1f, 0.1f, 1f);
                    m.hpBg.transform.localPosition = new Vector3(-22, 80, 0); m.hpFg.transform.localPosition = new Vector3(-21, 80, 0);
                    m.hpBg.transform.localScale = new Vector3(22f, 6f, 1f);
                    monsters.Add(m); n++;
                }
        }

        // ---------- vong lap ----------
        void Update()
        {
            if (map == null) return;
            acc += Mathf.Min(Time.deltaTime, 0.25f);
            while (acc >= Cfg.SimStep) { acc -= Cfg.SimStep; Step(Cfg.SimStep); }
            Render();
        }

        void Step(float dt)
        {
            simTime += dt; simSteps++;
            UpdatePlayer(dt);
            foreach (var m in monsters) UpdateMonster(m, dt);
            skill.Step(simTime);
        }

        float Dist(Vector2 a, Vector2 b) { return new Vector2(a.x - b.x, (a.y - b.y) * 0.5f).magnitude; }   // khoang cach tren man hinh (px)

        public bool PlayerSkillReady { get { return pl.state != PlayerChar.S.Dead && pl.state != PlayerChar.S.Cast && simTime >= pl.cooldownEnd; } }
        public float CooldownLeft { get { return Mathf.Max(0f, pl.cooldownEnd - simTime); } }

        public Monster Nearest(Vector2 from, float maxPx)
        {
            Monster best = null; float bd = maxPx;
            foreach (var m in monsters) { if (!m.Alive) continue; float d = Dist(from, m.pos); if (d < bd) { bd = d; best = m; } }
            return best;
        }

        public void TryCast()
        {
            if (!PlayerSkillReady) return;
            var t = Nearest(pl.pos, 450f);
            Vector2 target;
            if (t != null) { target = t.pos; FaceTo(t.pos); }
            else
            {   // khong co muc tieu: diem phia truoc nhan vat 160 px
                Vector2 f = DirVec(pl.dir); target = pl.pos + new Vector2(f.x * 160f, -f.y * 160f * 2f);
            }
            pl.state = PlayerChar.S.Cast; pl.stateT = 0; pl.stateDur = Cfg.CastSeconds; pl.castStart = simTime;
            pl.cooldownEnd = simTime + Cfg.CooldownSeconds;           // tinh tu luc bat dau cast
            skill.BeginCast(simTime, target);
        }

        static Vector2 DirVec(int d)
        {   // vector tren man hinh (y len tren) tu huong sprite 0..7
            switch (d) { case 0: return new Vector2(0, -1); case 1: return new Vector2(-0.707f, -0.707f); case 2: return new Vector2(-1, 0); case 3: return new Vector2(-0.707f, 0.707f);
                case 4: return new Vector2(0, 1); case 5: return new Vector2(0.707f, 0.707f); case 6: return new Vector2(1, 0); default: return new Vector2(0.707f, -0.707f); }
        }
        void FaceTo(Vector2 mpsTarget) { var d = mpsTarget - pl.pos; pl.dir = Dir8.FromScreen(d.x, -d.y * 0.5f); }

        void ClampPlayer()
        {
            float x0 = map.map.x0 * Mps.RegionW + 256, x1 = (map.map.x1 + 1) * Mps.RegionW - 256, y0 = map.map.y0 * Mps.RegionH + 512, y1 = (map.map.y1 + 1) * Mps.RegionH - 512;
            pl.pos.x = Mathf.Clamp(pl.pos.x, x0, x1); pl.pos.y = Mathf.Clamp(pl.pos.y, y0, y1);
        }

        void MovePlayer(Vector2 screenDir, float dt)
        {   // screenDir: vector man hinh don vi (y len tren); doi sang MPS (y gap doi, huong xuong)
            pl.pos += new Vector2(screenDir.x, -screenDir.y * 2f) * PlayerSpeed * dt; ClampPlayer();
        }

        void UpdatePlayer(float dt)
        {
            var p = pl;
            if (p.state == PlayerChar.S.Dead)
            {
                if (simTime - p.deadAt >= 3f) { p.hp = Cfg.PlayerHp; p.state = PlayerChar.S.Idle; p.stateT = 0; Evt.Log(simTime, "player respawn"); }
                return;
            }
            p.stateT += dt;
            if (p.state == PlayerChar.S.Cast) { if (p.stateT >= p.stateDur) { p.state = PlayerChar.S.Idle; p.stateT = 0; } return; }
            var joy = ui != null ? ui.JoyVec : Vector2.zero;
            if (joy.magnitude > 0.2f)
            {
                var d = joy.normalized; p.dir = Dir8.FromScreen(d.x, d.y);
                if (p.state != PlayerChar.S.Walk) { p.state = PlayerChar.S.Walk; p.stateT = 0; }
                MovePlayer(d, dt); return;
            }
            if (p.state == PlayerChar.S.Attack)
            {
                if (!p.attackDealt && p.stateT >= p.stateDur * 0.6f)
                {
                    p.attackDealt = true;
                    if (p.attackTarget >= 0 && monsters[p.attackTarget].Alive && Dist(p.pos, monsters[p.attackTarget].pos) < PlayerRangePx + 30f)
                    {
                        bool hit = rng.Next(100) < 65;   // xac suat Hit don thuong DoHurt=80: 65% (S/KNpc.cpp:3000, bao cao 58 muc A2)
                        DamageMonster(monsters[p.attackTarget], 30, simTime, hit, "basic");
                    }
                }
                if (p.stateT >= p.stateDur) { p.state = PlayerChar.S.Idle; p.stateT = 0; }
                return;
            }
            if (p.autoOn)
            {
                var t = Nearest(p.pos, 650f);
                if (t != null)
                {
                    float dd = Dist(p.pos, t.pos);
                    if (PlayerSkillReady && dd < SkillRangePx) { TryCast(); return; }
                    if (dd > PlayerRangePx)
                    {
                        var v = new Vector2(t.pos.x - p.pos.x, -(t.pos.y - p.pos.y) * 0.5f).normalized;
                        p.dir = Dir8.FromScreen(v.x, v.y);
                        if (p.state != PlayerChar.S.Walk) { p.state = PlayerChar.S.Walk; p.stateT = 0; }
                        MovePlayer(v, dt); return;
                    }
                    if (simTime >= p.nextAttack)
                    {
                        FaceTo(t.pos); p.state = PlayerChar.S.Attack; p.stateT = 0; p.stateDur = 0.8f; p.attackDealt = false; p.attackTarget = t.id; p.nextAttack = simTime + 1.0f; return;
                    }
                }
            }
            if (p.state != PlayerChar.S.Idle) { p.state = PlayerChar.S.Idle; p.stateT = 0; }
        }

        public void DamageMonster(Monster m, int dmg, float now, bool hitAnim, string src)
        {
            if (!m.Alive) return;
            m.hp -= dmg; totalDamageAll += dmg;
            SpawnDamageNumber(m, dmg, now);
            if (m.hp <= 0)
            {
                m.hp = 0; m.state = MState.Die; m.stateT = 0; m.respawnAt = now + Cfg.RespawnSeconds; totalMonsterKills++;
                Evt.Log(now, "monster#" + m.id + " die (" + src + ")");
            }
            else if (hitAnim && m.state != MState.Hit) { m.state = MState.Hit; m.stateT = 0; }
        }

        void UpdateMonster(Monster m, float dt)
        {
            m.stateT += dt;
            switch (m.state)
            {
                case MState.Die:
                    if (m.stateT >= a_die.meta.interval * a_die.FramesPerDir / 1000f) { m.state = MState.Dead; m.sr.enabled = false; m.hpBg.SetActive(false); m.hpFg.SetActive(false); }
                    break;
                case MState.Dead:
                    if (simTime >= m.respawnAt)
                    {
                        m.hp = Cfg.MonsterHp; m.pos = m.spawn; m.state = MState.Idle; m.stateT = 0; m.sr.enabled = true; m.hpBg.SetActive(true); m.hpFg.SetActive(true); monsterRespawns++;
                        Evt.Log(simTime, "monster#" + m.id + " respawn");
                    }
                    break;
                case MState.Hit:
                    if (m.stateT >= 8f / Cfg.LogicHz) { m.state = MState.Idle; m.stateT = 0; }
                    break;
                case MState.Idle:
                case MState.Chase:
                    if (freezeAI) break;
                    if (pl.state == PlayerChar.S.Dead) { if (m.state != MState.Idle) { m.state = MState.Idle; m.stateT = 0; } break; }
                    float d = Dist(m.pos, pl.pos);
                    if (d < AttackRangePx && simTime >= m.nextAttack) { m.state = MState.Attack; m.stateT = 0; m.attackDealt = false; m.nextAttack = simTime + 1.5f; var v0 = new Vector2(pl.pos.x - m.pos.x, -(pl.pos.y - m.pos.y) * 0.5f); m.dir = Dir8.FromScreen(v0.x, v0.y); }
                    else if (d < AggroPx && d >= AttackRangePx)
                    {
                        var v = new Vector2(pl.pos.x - m.pos.x, -(pl.pos.y - m.pos.y) * 0.5f).normalized; m.dir = Dir8.FromScreen(v.x, v.y);
                        m.pos += new Vector2(v.x, -v.y * 2f) * MonsterSpeed * dt;
                        if (m.state != MState.Chase) { m.state = MState.Chase; m.stateT = 0; }
                    }
                    else if (m.state == MState.Chase) { m.state = MState.Idle; m.stateT = 0; }
                    break;
                case MState.Attack:
                    float dur = a_at.meta.interval * a_at.FramesPerDir / 1000f;
                    if (!m.attackDealt && m.stateT >= dur * 0.6f)
                    {
                        m.attackDealt = true;
                        if (pl.state != PlayerChar.S.Dead && Dist(m.pos, pl.pos) < AttackRangePx * 1.6f) { pl.hp = Mathf.Max(0, pl.hp - 8); if (pl.hp == 0) { pl.state = PlayerChar.S.Dead; pl.deadAt = simTime; playerDeaths++; Evt.Log(simTime, "player die"); } }
                    }
                    if (m.stateT >= dur) { m.state = MState.Idle; m.stateT = 0; }
                    break;
            }
        }

        // ---------- hien thi ----------
        int ActFrame(SprSheet s, float t, float msPerFrame, bool loop)
        {
            int n = s.FramesPerDir; int f = (int)(t * 1000f / msPerFrame);
            return loop ? f % n : Mathf.Min(f, n - 1);
        }

        void Render()
        {
            // camera
            var pw = Mps.ToWorld(pl.pos.x, pl.pos.y);
            cam.orthographicSize = viewH / 2f;
            cam.transform.position = new Vector3(pw.x, pw.y, -10f);
            float hh = cam.orthographicSize, hw = hh * cam.aspect;
            map.UpdateVisible(new Rect(pw.x - hw - 320, pw.y - hh - 320, 2 * hw + 640, 2 * hh + 640));
            RenderPlayer();
            foreach (var m in monsters) RenderMonster(m);
            UpdateNums();
        }

        void RenderMonster(Monster m)
        {
            if (m.state == MState.Dead) return;
            SprSheet s; int fr; float t = m.stateT;
            switch (m.state)
            {
                case MState.Chase: s = a_wlk; fr = ActFrame(s, t, s.meta.interval, true); break;
                case MState.Attack: s = a_at; fr = ActFrame(s, t, s.meta.interval, false); break;
                case MState.Hit: s = a_bat; fr = Mathf.Min((int)(t / (8f / Cfg.LogicHz) * s.FramesPerDir), s.FramesPerDir - 1); break;   // bat 8 khung ep vao thoi luong Hit 8 tick
                case MState.Die: s = a_die; fr = ActFrame(s, t, s.meta.interval, false); break;
                default: s = a_st; fr = ActFrame(s, simTime - m.id * 0.13f, s.meta.interval, true); break;
            }
            m.sr.sprite = s.Get(m.dir * s.FramesPerDir + fr);
            m.go.transform.position = Mps.ToWorld(m.pos.x, m.pos.y);
            m.sr.sortingOrder = map.OrderForY(m.pos.y) + 4;
            float f = Mathf.Clamp01(m.hp / (float)Cfg.MonsterHp);
            m.hpFg.transform.localScale = new Vector3(20f * f, 4f, 1f);
            m.hpBgSr.sortingOrder = MapView.OrderTop; m.hpFgSr.sortingOrder = MapView.OrderTop + 1;
            m.hpBg.SetActive(m.state != MState.Die); m.hpFg.SetActive(m.state != MState.Die);
        }

        void RenderPlayer()
        {
            var p = pl; string act = "st"; float fps = 8f; bool loop = true; float t = p.stateT;
            switch (p.state)
            {
                case PlayerChar.S.Walk: act = "walk"; fps = 15f; break;
                case PlayerChar.S.Attack: act = "at"; fps = 18f / p.stateDur; loop = false; break;
                case PlayerChar.S.Cast: act = "mg"; fps = 12f / p.stateDur; loop = false; break;
                case PlayerChar.S.Dead: act = "de"; fps = 12f; loop = false; t = simTime - p.deadAt; break;
                default: t = simTime; break;
            }
            string[] ord = order8[p.dir];
            for (int i = 0; i < 5; i++)
            {
                var sheet = Sheet(p.partNames[i], act);
                if (sheet == null) continue;
                int n = sheet.FramesPerDir; int f = (int)(t * fps); f = loop ? f % n : Mathf.Min(f, n - 1);
                p.parts[i].sprite = sheet.Get(p.dir * n + f);
                int idx = System.Array.IndexOf(ord, p.partNames[i]);
                p.parts[i].sortingOrder = map.OrderForY(p.pos.y) + 5 + (idx < 0 ? 0 : idx);
            }
            p.go.transform.position = Mps.ToWorld(p.pos.x, p.pos.y);
            if (p.state == PlayerChar.S.Cast)
            {
                var cs = SprSheet.Load("spr/cast_kl16");
                p.castFx.SetActive(true);
                p.castFxSr.sprite = cs.Get(Mathf.Clamp((int)(p.stateT / p.stateDur * cs.FrameCount), 0, cs.FrameCount - 1));
                p.castFx.transform.position = Mps.ToWorld(p.pos.x, p.pos.y); p.castFxSr.sortingOrder = map.OrderForY(p.pos.y) + 12;
            }
            else p.castFx.SetActive(false);
        }

        readonly Dictionary<string, SprSheet> partCache = new Dictionary<string, SprSheet>();
        SprSheet Sheet(string part, string act)
        {
            string key = "spr/man_" + part + "_" + act; SprSheet s;
            if (!partCache.TryGetValue(key, out s)) { s = SprSheet.Load(key); partCache[key] = s; }
            return s;
        }

        // ---------- damage number (moi lan ap dung sat thuong = 1 so rieng) ----------
        void SpawnDamageNumber(Monster m, int dmg, float now)
        {
            string txt = dmg.ToString();
            var n = new DmgNum { go = new GameObject("dmg"), t0 = now, start = Mps.ToWorld(m.pos.x, m.pos.y) + new Vector3(0, 95f, 0) };
            n.jitter = ((dmgNumbersSpawned % 5) - 2) * 7f;
            n.srs = new SpriteRenderer[txt.Length];
            float w = 0; foreach (char c in txt) w += digitSize[c - '0'].x + 1;
            float x = -w / 2f;
            for (int i = 0; i < txt.Length; i++)
            {
                int d = txt[i] - '0';
                var go = new GameObject("d"); go.transform.SetParent(n.go.transform, false);
                var sr = go.AddComponent<SpriteRenderer>(); sr.sprite = digitSp[d]; sr.sortingOrder = MapView.OrderTop + 10;
                go.transform.localPosition = new Vector3(x + digitSize[d].x / 2f, 0, 0); go.transform.localScale = Vector3.one * 1.6f;
                x += digitSize[d].x + 1; n.srs[i] = sr;
            }
            n.go.transform.position = n.start + new Vector3(n.jitter, 0, 0);
            nums.Add(n); dmgNumbersSpawned++;
        }

        void UpdateNums()
        {
            for (int i = nums.Count - 1; i >= 0; i--)
            {
                var n = nums[i]; float el = simTime - n.t0;
                if (el >= Cfg.DamageNumberSeconds) { Destroy(n.go); nums.RemoveAt(i); continue; }
                float k = el / Cfg.DamageNumberSeconds;
                n.go.transform.position = n.start + new Vector3(n.jitter, 40f * k, 0);
                var c = new Color(1, 1, 1, 1f - k * k); foreach (var sr in n.srs) sr.color = c;
            }
        }
        public int ActiveNums { get { return nums.Count; } }
        public int AliveMonsters { get { int n = 0; foreach (var m in monsters) if (m.Alive) n++; return n; } }

        public string DumpEvents()
        {
            var sb = new StringBuilder(); foreach (var l in Evt.Lines) sb.AppendLine(l); return sb.ToString();
        }
    }
}
