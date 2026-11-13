using System;
using System.Collections.Generic;
using UnityEngine;

namespace U003
{
    [Serializable] public class GroundJ { public int h, v, f; public string id; }
    [Serializable] public class CoverJ { public int x, y, w, h, f, order, layer; public string id; }
    [Serializable] public class BuildJ { public string id; public int x, y, z, props, frame, n, speed, order; public float nod; }
    [Serializable] public class RegionJ { public int rx, ry; public GroundJ[] ground; public CoverJ[] cover; public BuildJ[] build; }
    [Serializable] public class MapJ { public int x0, y0, x1, y1; public RegionJ[] regions; }

    public class SpriteAnim : MonoBehaviour
    {
        public SprSheet sheet; public int first, count; public float msPerFrame; SpriteRenderer sr; float t0;
        void Awake() { sr = GetComponent<SpriteRenderer>(); t0 = UnityEngine.Random.value * 5f; }
        void Update()
        {
            if (sheet == null || count <= 1 || msPerFrame <= 0) return;
            int i = first + (int)(((Time.time + t0) * 1000f) / msPerFrame) % count;
            sr.sprite = sheet.Get(i);
        }
    }

    // Ve ban do 45 (vung x=96..107, y=95..102). KIpoTree CHUA port: doi tuong ve theo thu tu Y (tam thoi) -- xem bao cao 59.
    public class MapView : MonoBehaviour
    {
        public const int OrderGround = -20000, OrderCover = -19000, OrderObjectBase = 1000, OrderTop = 30000;
        public MapJ map; public int y0mps; public int sprites;
        readonly List<GameObject> regionGos = new List<GameObject>(); readonly List<Rect> regionRects = new List<Rect>();
        public RectInt PlayCells;  // pham vi o logic
        public int ObjectsDrawn, TreesInMap, LinesInMap, PointsInMap, AboveInMap;

        // Khoang thu tu cho vat the dong (nhan vat, quai, dan): theo toa do y MPS (nho -> ve truoc)
        public int OrderForY(float mpsY) { return OrderObjectBase + Mathf.Clamp(Mathf.RoundToInt((mpsY - y0mps) / 8f), 0, 1500) * 16; }

        public static Sprite TopLeftSprite(SprSheet s, int i)
        {
            var f = s.meta.frames[i];
            var rect = new Rect(f.x, s.meta.atlasH - f.y - f.h, f.w, f.h);
            return Sprite.Create(s.tex, rect, new Vector2(0f, 1f), 1f, 0, SpriteMeshType.FullRect);
        }

        public bool Build()
        {
            var ta = Resources.Load<TextAsset>("U003/map45");
            if (ta == null) { Debug.LogError("[U003] thieu map45.json"); return false; }
            map = JsonUtility.FromJson<MapJ>(ta.text);
            y0mps = map.y0 * Mps.RegionH;
            PlayCells = new RectInt(map.x0 * Mps.RegionW / Mps.Cell, map.y0 * Mps.RegionH / Mps.Cell,
                (map.x1 - map.x0 + 1) * Mps.RegionW / Mps.Cell, (map.y1 - map.y0 + 1) * Mps.RegionH / Mps.Cell);
            var idCache = new Dictionary<string, SprSheet>();
            Func<string, SprSheet> get = id =>
            {
                if (string.IsNullOrEmpty(id)) return null;
                SprSheet s; if (idCache.TryGetValue(id, out s)) return s;
                s = SprSheet.Load("map/" + id); idCache[id] = s; return s;
            };
            foreach (var r in map.regions)
            {
                var rg = new GameObject("region_" + r.rx + "_" + r.ry);
                rg.transform.SetParent(transform, false);
                float left = r.rx * Mps.RegionW, top = r.ry * Mps.RegionH;
                // Ground: (h*CellWidth + left, v*CellHeight*2 + top) -- KScenePlaceRegionC.cpp:789-790
                foreach (var g in r.ground)
                {
                    var s = get(g.id); if (s == null) continue;
                    var sp = TopLeftSprite(s, Mathf.Clamp(g.f, 0, s.FrameCount - 1));
                    var go = new GameObject("g"); go.transform.SetParent(rg.transform, false);
                    go.transform.position = Mps.ToWorld(g.h * Mps.Cell + left, g.v * Mps.Cell * 2 + top);
                    var sr = go.AddComponent<SpriteRenderer>(); sr.sprite = sp; sr.sortingOrder = OrderGround; sprites++;
                }
                int ci = 0;
                foreach (var c in r.cover)
                {
                    var s = get(c.id); if (s == null) continue;
                    var sp = TopLeftSprite(s, Mathf.Clamp(c.f, 0, s.FrameCount - 1));
                    var go = new GameObject("c"); go.transform.SetParent(rg.transform, false);
                    go.transform.position = Mps.ToWorld(c.x, c.y);
                    var sr = go.AddComponent<SpriteRenderer>(); sr.sprite = sp; sr.sortingOrder = OrderCover + c.order * 16 + Mathf.Clamp(c.layer, 0, 15) + (ci++ % 4); sprites++;
                }
                foreach (var b in r.build)
                {
                    var s = get(b.id); if (s == null) continue;
                    int fr = Mathf.Clamp(b.frame, 0, s.FrameCount - 1);
                    var go = new GameObject("o"); go.transform.SetParent(rg.transform, false);
                    go.transform.position = Mps.ToWorld(b.x, b.y, b.z);
                    var sr = go.AddComponent<SpriteRenderer>(); sr.sprite = s.Get(fr);
                    sr.sortingOrder = OrderForY(b.y) - 1;   // TAM THOI: Y-sort (KIpoTree chua port)
                    if (b.n > 1 && b.speed > 0)
                    { var an = go.AddComponent<SpriteAnim>(); an.sheet = s; an.first = 0; an.count = Mathf.Min(b.n, s.FrameCount); an.msPerFrame = b.speed; }
                    sprites++; ObjectsDrawn++; PointsInMap++;
                }
                regionGos.Add(rg);
                regionRects.Add(new Rect(left, -(top + Mps.RegionH) * 0.5f, Mps.RegionW, Mps.RegionH * 0.5f));
            }
            return true;
        }

        // Chi bat cac vung nam trong khung nhin (giam so renderer)
        public void UpdateVisible(Rect view)
        {
            for (int i = 0; i < regionGos.Count; i++)
            {
                var rr = regionRects[i];
                bool vis = rr.Overlaps(view);
                if (regionGos[i].activeSelf != vis) regionGos[i].SetActive(vis);
            }
        }
    }
}
