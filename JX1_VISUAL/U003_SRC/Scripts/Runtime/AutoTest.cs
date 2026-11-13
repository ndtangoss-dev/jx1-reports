using System.Collections;
using System.IO;
using System.Text;
using UnityEngine;

namespace U003
{
    // Che do tu kiem tra (chi chay khi dat bien moi truong U003_AUTOTEST=<thu_muc_ra>): chup anh, ghi log that, khong dung du lieu gia.
    public class AutoTest : MonoBehaviour
    {
        string dir; Game g; StringBuilder res = new StringBuilder();

        void Start()
        {
            dir = System.Environment.GetEnvironmentVariable("U003_AUTOTEST"); g = Game.I; g.pl.autoOn = false; Directory.CreateDirectory(dir);
            StartCoroutine(Run());
        }

        IEnumerator Shot(string name)
        {
            yield return new WaitForEndOfFrame();
            ScreenCapture.CaptureScreenshot(Path.Combine(dir, name + ".png"));
            yield return null; yield return null;
        }

        Texture2D cropTex;
        IEnumerator CropPlayer(float w, float h)
        {
            yield return new WaitForEndOfFrame();
            var full = ScreenCapture.CaptureScreenshotAsTexture();
            float s = Screen.height / 540f; int cw = (int)(w * s), ch = (int)(h * s);
            int x0 = Mathf.Clamp(Screen.width / 2 - cw / 2, 0, Screen.width - cw), y0 = Mathf.Clamp(Screen.height / 2 - ch / 2 - (int)(20 * s), 0, Screen.height - ch);
            cropTex = new Texture2D(cw, ch, TextureFormat.RGBA32, false); cropTex.SetPixels(full.GetPixels(x0, y0, cw, ch)); cropTex.Apply();
            Destroy(full);
        }

        IEnumerator Run()
        {
            Debug.Log("[U003][AUTOTEST] start dir=" + dir + " screen=" + Screen.width + "x" + Screen.height);
            res.AppendLine("screen " + Screen.width + "x" + Screen.height + " unity " + Application.unityVersion + " platform " + Application.platform);
            res.AppendLine(g.startupLog);
            yield return new WaitForSeconds(1.0f);
            g.ui.showOverlay = false;
            g.pl.autoOn = false;
            // --- G1: anh canh tong, 8 huong nhan vat (strip) va 8 huong ani001
            g.pl.autoOn = false; g.freezeAI = true;
            yield return Shot("g1_01_scene_player");
            var strip = new Texture2D(8 * 220, 260, TextureFormat.RGBA32, false);
            for (int d = 0; d < 8; d++)
            {
                g.pl.dir = d; yield return null; yield return null;
                yield return CropPlayer(220, 260);
                strip.SetPixels(d * 220, 0, 220, 260, cropTex.GetPixels(0, 0, 220, 260));
            }
            strip.Apply(); File.WriteAllBytes(Path.Combine(dir, "g1_02_player_8dirs.png"), strip.EncodeToPNG());
            // ani001 8 huong: dat 8 quai quanh nguoi o khoang cach co dinh
            g.pl.dir = 0;
            for (int i = 0; i < 8; i++)
            {
                var m = g.monsters[i]; m.state = MState.Idle; m.dir = i;
                float ang = i * Mathf.PI / 4f; m.pos = g.pl.pos + new Vector2(Mathf.Sin(ang) * 170f, -Mathf.Cos(ang) * 170f * 2f * 0.6f);
            }
            yield return null; yield return null;
            yield return Shot("g1_03_ani001_8dirs");
            // test che khuat co ban: nhan vat di qua cay/nha (xem cac anh keo theo)
            res.AppendLine("g1: shots done");
            g.freezeAI = true;   // bai test skill: quai dung yen de ket qua tai lap duoc
            // dua quai ve cho cu
            for (int i = 0; i < 8; i++) { var m = g.monsters[i]; m.pos = m.spawn; }
            // --- G2: skill 375
            g.pl.pos = new Vector2(g.spawnPoints[7].x - 260, g.spawnPoints[7].y + 220); g.pl.dir = 6; g.ui.showOverlay = true;
            yield return new WaitForSeconds(0.5f);
            int hp0 = 0; foreach (var m in g.monsters) hp0 += m.hp;
            res.AppendLine("skill test: tong HP quai truoc = " + hp0 + " cast count " + g.skill.castCount);
            g.TryCast();
            float t0 = g.simTime;
            g.ui.showOverlay = false;
            yield return new WaitForSeconds(0.7f); yield return Shot("g2_01_cast");
            yield return new WaitForSeconds(0.6f); yield return Shot("g2_02_missiles");
            yield return new WaitForSeconds(0.8f); yield return Shot("g2_03_collide");
            yield return new WaitForSeconds(1.5f); yield return Shot("g2_04_aoe");
            g.ui.showOverlay = true; yield return Shot("g2_04b_aoe_overlay"); g.ui.showOverlay = false;
            yield return new WaitForSeconds(2.0f); yield return Shot("g2_05_numbers");
            // cho het hieu ung
            float wait = 0; while ((g.skill.Active181 + g.skill.Pending181 + g.skill.ActiveAoe) > 0 && wait < 10f) { wait += 0.1f; yield return new WaitForSeconds(0.1f); }
            int hp1 = 0; foreach (var m in g.monsters) hp1 += m.hp;
            var sk = g.skill;
            res.AppendLine("cast#" + sk.lastCastId + " spawned181=" + sk.spawned181 + " collided=" + sk.collided181 + " spawned193=" + sk.spawned193 + " aoeTicks=" + sk.aoeTicks + " damageEvents=" + sk.damageEvents + " totalDamage(skill)=" + sk.totalDamage);
            res.AppendLine("tong HP quai sau = " + hp1 + " (giam " + (hp0 - hp1) + ")  dmgNumbersSpawned=" + g.dmgNumbersSpawned + " totalDamageAll=" + g.totalDamageAll);
            res.AppendLine("sim " + g.simTime.ToString("F2") + "s steps " + g.simSteps + " fps(avg last) " + g.ui.fps.ToString("F1") + " mem(MB, GC) " + (System.GC.GetTotalMemory(false) / 1048576));
            // canh o cho trong: dat quai gan nhat o khoang trong ben phai, cast lai, chup chuoi anh tia set
            var mo = g.Nearest(g.pl.pos, 100000f);
            mo.pos = g.pl.pos + new Vector2(240f, 100f);
            yield return new WaitForSeconds(0.3f);
            g.TryCast();
            yield return new WaitForSeconds(0.9f);
            for (int s = 0; s < 8; s++) { yield return Shot("g2_06_strike_" + s); yield return new WaitForSeconds(0.2f); }
            res.AppendLine("--- events ---"); res.Append(g.DumpEvents());
            File.WriteAllText(Path.Combine(dir, "autotest_result.txt"), res.ToString());
            Debug.Log("[U003][AUTOTEST] done");
            Application.Quit();
        }
    }
}
