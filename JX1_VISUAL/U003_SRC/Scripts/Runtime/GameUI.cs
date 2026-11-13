using System.Text;
using UnityEngine;

namespace U003
{
    // UI IMGUI: joystick (yaoganz/yaoganx goc), nut skill (icon 375 goc), nut AUTO, HP, debug overlay.
    public class GameUI : MonoBehaviour
    {
        public Game g; public Vector2 JoyVec; public bool showOverlay = true;
        Texture2D joyBase, joyStick, icon, white;
        int joyId = -99; Vector2 joyStart;
        float S { get { return Screen.height / 540f; } }
        Rect SkillRect { get { float s = S; return new Rect(Screen.width - 120 * s, Screen.height - 140 * s, 96 * s, 96 * s); } }
        Rect AutoRect { get { float s = S; return new Rect(Screen.width - 215 * s, Screen.height - 110 * s, 76 * s, 60 * s); } }
        Rect DbgRect { get { float s = S; return new Rect(Screen.width - 80 * s, 8 * s, 70 * s, 40 * s); } }
        Vector2 JoyCenter { get { float s = S; return new Vector2(140 * s, Screen.height - 140 * s); } }
        GUIStyle label, btn; float lastFps; int frames; float fpsT; public float fps;

        void Start()
        {
            joyBase = Resources.Load<Texture2D>("U003/ui/yaoganz"); joyStick = Resources.Load<Texture2D>("U003/ui/yaoganx");
            icon = Resources.Load<Texture2D>("U003/spr/icon375");
            white = Texture2D.whiteTexture;
        }

        void Update()
        {
            frames++; fpsT += Time.unscaledDeltaTime; if (fpsT >= 0.5f) { fps = frames / fpsT; frames = 0; fpsT = 0; }
            var kb = Vector2.zero;
            if (Input.GetKey(KeyCode.A) || Input.GetKey(KeyCode.LeftArrow)) kb.x -= 1; if (Input.GetKey(KeyCode.D) || Input.GetKey(KeyCode.RightArrow)) kb.x += 1;
            if (Input.GetKey(KeyCode.W) || Input.GetKey(KeyCode.UpArrow)) kb.y += 1; if (Input.GetKey(KeyCode.S) || Input.GetKey(KeyCode.DownArrow)) kb.y -= 1;
            if (Input.GetKeyDown(KeyCode.Space)) g.TryCast();
            if (Input.GetKeyDown(KeyCode.Tab)) g.pl.autoOn = !g.pl.autoOn;
            if (kb != Vector2.zero) { JoyVec = kb.normalized; return; }
            if (Input.touchCount > 0)
            {
                for (int i = 0; i < Input.touchCount; i++)
                {
                    var t = Input.GetTouch(i); var p = new Vector2(t.position.x, Screen.height - t.position.y);
                    if (t.phase == TouchPhase.Began) Press(t.fingerId, p);
                    else if (t.phase == TouchPhase.Ended || t.phase == TouchPhase.Canceled) Release(t.fingerId);
                    else Drag(t.fingerId, p);
                }
            }
            else
            {
                var p = new Vector2(Input.mousePosition.x, Screen.height - Input.mousePosition.y);
                if (Input.GetMouseButtonDown(0)) Press(-1, p); else if (Input.GetMouseButtonUp(0)) Release(-1); else if (Input.GetMouseButton(0)) Drag(-1, p);
            }
        }

        void Press(int id, Vector2 p)
        {
            if (SkillRect.Contains(p)) { g.TryCast(); return; }
            if (AutoRect.Contains(p)) { g.pl.autoOn = !g.pl.autoOn; return; }
            if (DbgRect.Contains(p)) { showOverlay = !showOverlay; return; }
            if (p.x < Screen.width * 0.5f && joyId == -99) { joyId = id; Drag(id, p); }
        }
        void Drag(int id, Vector2 p)
        {
            if (id != joyId) return;
            var v = (p - JoyCenter) / (60f * S); v.y = -v.y;      // y man hinh di xuong -> y len tren
            if (v.magnitude > 1f) v.Normalize();
            JoyVec = v;
        }
        void Release(int id) { if (id == joyId) { joyId = -99; JoyVec = Vector2.zero; } }

        void OnGUI()
        {
            if (g == null || g.pl == null) return;
            float s = S;
            if (label == null) { label = new GUIStyle(GUI.skin.label); btn = new GUIStyle(GUI.skin.box); }
            label.fontSize = Mathf.RoundToInt(14 * s); label.normal.textColor = Color.white; btn.fontSize = Mathf.RoundToInt(15 * s); btn.normal.textColor = Color.white; btn.alignment = TextAnchor.MiddleCenter;
            // joystick
            var c = JoyCenter; float bs = 134 * s * 0.9f, ss = 66 * s * 0.9f;
            GUI.DrawTexture(new Rect(c.x - bs / 2, c.y - bs / 2, bs, bs), joyBase);
            var sc = c + new Vector2(JoyVec.x, -JoyVec.y) * 45f * s;
            GUI.DrawTexture(new Rect(sc.x - ss / 2, sc.y - ss / 2, ss, ss), joyStick);
            // nut skill
            var r = SkillRect;
            GUI.color = g.PlayerSkillReady ? Color.white : new Color(1, 1, 1, 0.55f);
            GUI.DrawTextureWithTexCoords(r, icon, new Rect(0f, 2f / 38f, 36f / 38f, 36f / 38f));
            GUI.color = Color.white;
            float cd = g.CooldownLeft;
            if (cd > 0)
            {
                GUI.color = new Color(0, 0, 0, 0.55f); float h = r.height * Mathf.Clamp01(cd / Cfg.CooldownSeconds);
                GUI.DrawTexture(new Rect(r.x, r.y, r.width, h), white); GUI.color = Color.white;
                GUI.Label(new Rect(r.x + r.width * 0.3f, r.y + r.height * 0.3f, r.width, r.height * 0.5f), cd.ToString("F1"), label);
            }
            GUI.Box(AutoRect, g.pl.autoOn ? "AUTO\nON" : "AUTO\nOFF", btn);
            GUI.Box(DbgRect, showOverlay ? "DBG\nON" : "DBG\nOFF", btn);
            // HP nhan vat
            float hp = g.pl.hp / (float)Cfg.PlayerHp;
            GUI.color = new Color(0, 0, 0, 0.6f); GUI.DrawTexture(new Rect(10 * s, 10 * s, 220 * s, 22 * s), white);
            GUI.color = new Color(0.85f, 0.1f, 0.1f); GUI.DrawTexture(new Rect(12 * s, 12 * s, 216 * s * hp, 18 * s), white); GUI.color = Color.white;
            GUI.Label(new Rect(14 * s, 10 * s, 220 * s, 24 * s), "HP " + g.pl.hp + "/" + Cfg.PlayerHp, label);
            if (g.pl.state == PlayerChar.S.Dead) GUI.Label(new Rect(Screen.width / 2 - 80 * s, Screen.height / 2 - 20 * s, 300 * s, 40 * s), "DA CHET - hoi sinh sau 3s", label);
            if (showOverlay) DrawOverlay(s);
        }

        public string OverlayText()
        {
            var sk = g.skill; var sb = new StringBuilder();
            sb.AppendLine("FPS " + fps.ToString("F0") + "  tick(18Hz) " + Mathf.FloorToInt(g.simTime * Cfg.LogicHz) + "  sim " + g.simTime.ToString("F2") + "s");
            sb.AppendLine("quai song " + g.AliveMonsters + "/15  chet(tong) " + g.totalMonsterKills + "  hoi sinh " + g.monsterRespawns);
            var n = g.Nearest(g.pl.pos, 100000f);
            sb.AppendLine("HP nguoi " + g.pl.hp + "/" + Cfg.PlayerHp + (n != null ? "  HP quai gan nhat " + n.hp + "/" + Cfg.MonsterHp : ""));
            sb.AppendLine("tong damage " + g.totalDamageAll + "  (skill " + sk.totalDamage + ", " + sk.damageEvents + " lan)");
            sb.AppendLine("cast " + sk.castCount + " (id gan nhat " + sk.lastCastId + ")  CD " + g.CooldownLeft.ToString("F2"));
            sb.AppendLine("181: sinh " + sk.spawned181 + " dang " + sk.Active181 + " cho " + sk.Pending181 + " cham " + sk.collided181);
            sb.AppendLine("193/AOE: sinh " + sk.spawned193 + " dang " + sk.ActiveAoe + "  so damage dang bay " + g.ActiveNums);
            sb.AppendLine("nguoi MPS " + (int)g.pl.pos.x + "," + (int)g.pl.pos.y + "  o " + Mps.CellOf(g.pl.pos.x) + "," + Mps.CellOf(g.pl.pos.y));
            string rs = ""; foreach (var m in g.monsters) if (m.state == MState.Dead) rs += " #" + m.id + ":" + Mathf.Max(0, m.respawnAt - g.simTime).ToString("F1");
            sb.AppendLine("hoi sinh" + (rs == "" ? " -" : rs));
            return sb.ToString();
        }

        void DrawOverlay(float s)
        {
            string t = OverlayText();
            GUI.color = new Color(0, 0, 0, 0.55f); GUI.DrawTexture(new Rect(8 * s, 40 * s, 470 * s, 150 * s), white); GUI.color = Color.white;
            label.fontSize = Mathf.RoundToInt(12 * s);
            GUI.Label(new Rect(12 * s, 42 * s, 470 * s, 150 * s), t, label);
        }
    }
}
