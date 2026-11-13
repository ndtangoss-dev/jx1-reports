using System.Collections.Generic;
using UnityEngine;

namespace U003
{
    public enum MState { Idle, Chase, Attack, Hit, Die, Dead }

    // Quai ani001: mot sprite, 5 clip (st, wlk, at, bat, die), 8 huong, anchor (160,192) + offset khung (bao cao 58 muc E).
    public class Monster
    {
        public int id; public Vector2 spawn, pos; public int hp; public MState state; public float stateT, respawnAt, nextAttack; public int dir;
        public bool attackDealt; public int hitCount;
        public GameObject go; public SpriteRenderer sr; public GameObject hpBg, hpFg; public SpriteRenderer hpBgSr, hpFgSr;
        public bool Alive { get { return state != MState.Die && state != MState.Dead; } }
        public int CellX { get { return Mps.CellOf(pos.x); } }
        public int CellY { get { return Mps.CellOf(pos.y); } }
    }

    // Nhan vat: 5 bo phan (bd, lh, rh, hd, hr), 8 huong, thu tu ve theo char_order.json (bang bao cao 54, section DEFAULT).
    public class PlayerChar
    {
        public Vector2 pos; public int dir; public int hp = Cfg.PlayerHp; public bool autoOn = true;
        public enum S { Idle, Walk, Attack, Cast, Dead }
        public S state; public float stateT, stateDur; public float nextAttack, cooldownEnd, castStart, deadAt;
        public bool attackDealt; public int attackTarget = -1;
        public GameObject go; public SpriteRenderer[] parts; public string[] partNames;
        public GameObject castFx; public SpriteRenderer castFxSr;
        public float walkAccum;
    }

    public class PartSheets
    {
        public SprSheet st, walk, at, mg, ij, de;
        public SprSheet For(string act)
        {
            switch (act) { case "st": return st; case "walk": return walk; case "at": return at; case "mg": return mg; case "ij": return ij; default: return de; }
        }
    }

    [System.Serializable] public class OrderJ { public string note; public string[] order0, order1; }
    [System.Serializable] public class OrderWrap { public string note; public OrderRow[] order; }
    [System.Serializable] public class OrderRow { public string[] items; }
}
