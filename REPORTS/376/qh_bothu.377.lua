-- [Q-101 / #303 TEST-36 ONLY] Sach "Ho tro thu nghiem": chi nhan vat ten bat dau 'atest'.
-- Vat pham sach = item script co san (6,1,0) "bao vat box"; script \script\item\baowubox.lua goi qhbv_menu().
-- Dang nhap (OnLine trong online.lua) tu cap lai sach neu thieu (QHBV_Book).
-- Nut Cuong hoa tro lai mo UI Give goc (opensysui.lua khong con hook).
-- Go bo: xoa dong Include o opensysui.lua (goc .bak-q97), xoa dong QHBV_Book o online.lua, xoa baowubox.lua va file nay.

QHBV_BLUE = {
	{7, 0, 1, 0},   -- non
	{2, 0, 1, 0},   -- ao
	{6, 0, 1, 0},   -- dai
	{0, 0, 1, 0},   -- vu khi can chien
	{5, 0, 1, 0},   -- giay
	{8, 0, 1, 0},   -- bao tay
	{4, 0, 1, 0},   -- day chuyen
	{3, 0, 1, 0},   -- nhan 1
	{3, 1, 2, 0},   -- nhan 2
	{9, 0, 1, 0},   -- ngoc boi
}
QHBV_ML = 6
QHBV_GOLD_FROM = 9
QHBV_GOLD_TO = 18
QHBV_CRYSTAL = { 239, 240, 238 }   -- tim, luc, lam

-- #313/B-058: cap 21 tham so nhu the gm (IsWhere + y,m,d,h,mi hien tai)
function qhbv_add(g,d,p,lv,se,lk,l1,l2,l3,l4,l5,l6,st,en,pt)
	return AddItem(g,d,p,lv,se,lk,l1,l2,l3,l4,l5,l6,st,en,pt,0,2030,1,1,0,0)
end

function qhbv_isbook(g, d, p)
	return g == 6 and d == 1 and p == 0
end

-- dem sach trong hanh trang; neu del=1 thi xoa moi vat pham KHONG PHAI sach
function qhbv_scan(del)
	local books, removed = 0, 0
	for i = 0, 9 do
		for j = 0, 9 do
			local idx, g, d, p = FindItemEx(3, i, j)
			if idx and idx > 0 then
				if qhbv_isbook(g, d, p) then
					books = books + 1
				elseif del == 1 then
					if RemoveItemByIndex(idx) ~= 0 then removed = removed + 1 end
				end
			end
		end
	end
	return books, removed
end

function QHBV_Book()
	if 1 == 1 then return end -- #321
	if strsub(GetName(), 1, 5) ~= "atest" then return end
	local books = qhbv_scan(0)
	if books < 1 then
		AddItem(6, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0)
		Msg2Player("[TEST36] da cap sach Ho tro thu nghiem (vat pham trong tui)")
	end
end

function qhbv_menu()
	local t = {
		"Don hanh trang (giu lai sach) /qhbv_clear",
		"Do XANH (10 mon, co dong thuoc tinh) /qhbv_blue",
		"Do VANG (10 mon) /qhbv_gold",
		"Tien (bac toi da) /qhbv_money",
		"[#317] Cua hang Bao Vat 1 bac /qhbv_shop",
		"Thuy tinh TIM x600 /qhbv_tim",
		"Thuy tinh LUC x600 /qhbv_luc",
		"Thuy tinh LAM x600 /qhbv_lam",
		"Thiet lap Thieu Lam suc manh 300 /qhbv_setup",
		"[#306] Nap lai Lua nong /qhbv_reload",
		"[#368] Tru bac con 100 Van /qhbv_bac100",
		"[#368] Tra bac 8 Uc 3400 Van /qhbv_bacvc",
		"[#370] 1 mon tui len +9 /qhbv_en9",
		"[#376] Phi phong 11 cap /qhbv_pf",
		"[#376] Len cap 60 /qhbv_lv60",
		"[#377] Moi mon +15 /qhbv_en15",
		"Dong /qhbv_none",
	}
	Say("<c=yellow>[TEST-36] Ho tro thu nghiem<c>: lay bao nhieu cung duoc. Chon:", getn(t), t)
end

-- #306: nap lai file nay ngay tren gs001 dang chay (LocalScript -> ReLoadScript, khong restart)
function qhbv_reload()
	local n = LocalScript("\\script\\system\\qh_bothu.lua")
	Msg2Player("[TEST36] da nap lai qh_bothu.lua, ket qua=" .. tostring(n))
end

-- #303: muc trong sach Tan thu (lenhbaitanthu.lua) -> chi ten 'atest' moi mo menu
function qhbv_menu_book()
	-- #375: bo cong ten atest (chu dung tk khac; Test-36 only)
	qhbv_menu()
end

function qhbv_shop()
	Sale(92)
end

function qhbv_none()
end

function qhbv_blue()
	local n = 0
	for i = 1, getn(QHBV_BLUE) do
		local b = QHBV_BLUE[i]
		local m = QHBV_ML
		local idx = qhbv_add(0, b[1], b[2], b[3], b[4], 1000, m, m, m, m, m, m, 1, 0, 0)
		if idx and idx > 0 then n = n + 1 end
	end
	Msg2Player("[TEST36] bo xanh: " .. n .. "/" .. getn(QHBV_BLUE) .. " mon")
end

function qhbv_gold()
	local n = 0
	for g = QHBV_GOLD_FROM, QHBV_GOLD_TO do
		local idx = AddGoldItem(g)
		if idx and idx > 0 then
			SetAndSycItem(idx, -1, -1, -1, 1, 0, -2, 0)
			n = n + 1
		end
	end
	Msg2Player("[TEST36] bo vang: " .. n .. " mon")
end

function qhbv_crystal()
	for k = 1, 3 do
		qhbv_add(4, QHBV_CRYSTAL[k], 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 200, 0, 0)
	end
	Msg2Player("[TEST36] +200 thuy tinh tim, luc, lam")
end

function qhbv_cry(k, name)
	for r = 1, 3 do
		qhbv_add(4, QHBV_CRYSTAL[k], 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 200, 0, 0)
	end
	Msg2Player("[TEST36] +600 thuy tinh " .. name)
end
function qhbv_tim() qhbv_cry(1, "tim") end
function qhbv_luc() qhbv_cry(2, "luc") end
function qhbv_lam() qhbv_cry(3, "lam") end

function qhbv_money()
	local want = 2000000000
	if GetCash() < want then Earn(want - GetCash()) end
	Msg2Player("[TEST36] bac day")
end

function qhbv_clear()
	local b, r = qhbv_scan(1)
	Msg2Player("[TEST36] don hanh trang: xoa " .. r .. " vat pham, giu " .. b .. " sach")
end

function qhbv_setup()
	SetSeries(0)
	SetFaction("shaolin")
	SetCamp(1)
	SetCurCamp(1)
	SetRank(72)
	ResetBaseAttrib(0, 300)
	ResetBaseAttrib(1, 100)
	ResetBaseAttrib(2, 100)
	ResetBaseAttrib(3, 100)
	Msg2Player("[TEST36] Thieu Lam, suc manh 300")
end

-- #368: CHI atestqhhai. Tru bac xuong 100 Van de chup anh Thieu bac; tra lai dung 8 Uc 3400 Van.
function qhbv_bac100()
	if GetName() ~= "atestqhhai" then return end
	local c = GetCash()
	if c > 1000000 then Pay(c - 1000000) end
	Msg2Player("[TEST36] bac truoc=" .. c .. " bac nay=" .. GetCash())
end
function qhbv_bacvc()
	if GetName() ~= "atestqhhai" then return end
	local want = 834000000
	local c = GetCash()
	if c < want then Earn(want - c) elseif c > want then Pay(c - want) end
	Msg2Player("[TEST36] bac tra=" .. GetCash())
end

-- #370: CHI atestqhhai. Dua DUNG 1 mon trong tui (mon dau tien dang +0) len +9 de thu thao tac go khoi o giua.
function qhbv_en9()
	if GetName() ~= "atestqhhai" then return end
	for i = 0, 9 do
		for j = 0, 9 do
			local idx, g, d, p = FindItemEx(3, i, j)
			if idx and idx > 0 and g == 0 and GetItemEnChance(idx) == 0 then
				SetItemEnChance(idx, 9, 1)
				Msg2Player("[TEST36] +9 cho mon o (" .. i .. "," .. j .. ") idx=" .. idx)
				return
			end
		end
	end
	Msg2Player("[TEST36] khong co mon +0 de nang")
end

-- #376: CHI atestqhhai. 11 phi phong GoldItem 3465..3475 (dong 3467-3477 theo B) de thu client PP-02.
function qhbv_pf()
	if GetName() ~= "atestqhhai" then return end
	local n = 0
	for k = 1, 11 do
		local idx = AddGoldItem(3464 + k)
		if idx and idx > 0 then n = n + 1 end
	end
	Msg2Player("[TEST36] phi phong: " .. n .. "/11")
end

function qhbv_lv60()
	if GetName() ~= "atestqhhai" then return end
	SetLevel(60)
	Msg2Player("[TEST36] cap: "..GetLevel())
end

-- #377: CHI atestqhhai. Nang +15 moi mon (g==0) o phong 0 va 3 de du diem tai phu mac phi phong (Test-36 only).
function qhbv_en15()
	if GetName() ~= "atestqhhai" then return end
	local n = 0
	for r = 0, 3, 3 do
		for i = 0, 9 do
			for j = 0, 9 do
				local idx, g = FindItemEx(r, i, j)
				if idx and idx > 0 and g == 0 then
					SetItemEnChance(idx, 15, 1)
					n = n + 1
				end
			end
		end
	end
	Msg2Player("[TEST36] +15 cho " .. n .. " mon")
end
