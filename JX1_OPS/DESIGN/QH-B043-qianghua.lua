-- [B-043 / Q-95] BAN NHAP, CHUA CHAY, CHUA NAP. Thay ham sysqianghua(nItemID,nNalla,nNum) cua qianghua.lua goc (UI KuiGive_New: c2s_lockitem ->
-- c2s_playergiveback nKind=3 -> day). Giu chuoi goc: UI khoa do trong TUI -> Lua nay -> luat Q-86 -> SetItemEnChance -> KItem::EnChance -> SynPlayerItem.
-- Do dang MAC khong vao duoc UI (UI chi liet ke do trong tui); Lua van tu choi them cho chac.
-- Khong C++ moi: dung CountBagItemExact / ConsumeBagItemExact / GetEquipIdx da co tu B-035 (chi chay khi nguoi choi bam cuong hoa).
Include("\script\lib\string.lua");
Include("\script\lib\basic.lua");

QH_CRYSTAL = { 239, 240, 238 }
QH_MAX = 15
QH_CRYSTAL_CAP = 1000
QH_SILVER_CAP = 2000000000

function qh_price(n)
	local c = 1
	for i = 2, n do c = c * 2 end
	local s = c * 2000000
	if c > QH_CRYSTAL_CAP then c = QH_CRYSTAL_CAP end
	if s > QH_SILVER_CAP then s = QH_SILVER_CAP end
	return c, s
end
function qh_rate(n) return 100 - 5 * (n - 1) end

-- ma tra ve: 0 OK, 1 hut (mat NL+bac, giu cap), 2 thieu thuy tinh, 3 thieu bac, 4 da toi da, 5 khong hop le / dang mac
function sysqianghua(nItemID, nNalla, nNum)
	local Idx = split(nItemID)
	local idx = 0
	local cnt = 0
	for ii = 1, nNum do
		local id = tonum(Idx[ii], -1)
		local arr = split(GetItemProp(id))
		local kind = tonumber(arr[1])       -- 0 = trang bi (nhu qianghua.lua goc)
		local a8, a6 = tonumber(arr[8]), tonumber(arr[6])
		if kind == 0 and (a8 == 1 or a6 > 0) then idx = id cnt = cnt + 1 end
	end
	if cnt ~= 1 or nNum ~= 1 then Msg2Player("[QH]|E|5|0|0|0|0|0|0") Talk(1, "", "Chi dat 1 trang bi (xanh/tim/vang) vao o cuong hoa.") return end
	for p = 0, 9 do
		if GetEquipIdx(p) == idx then Msg2Player("[QH]|E|5|0|0|0|0|0|0") Talk(1, "", "Hay thao trang bi ra roi cuong hoa.") return end
	end
	local lv = GetItemEnChance(idx)
	if lv >= QH_MAX then Msg2Player("[QH]|E|4|" .. lv .. "|0|0|0|0|0") Talk(1, "", "Da toi da +15.") return end
	local n = lv + 1
	local c, s = qh_price(n)
	for k = 1, 3 do
		if CountBagItemExact(QH_CRYSTAL[k]) < c then Msg2Player("[QH]|E|2|" .. lv .. "|" .. qh_rate(n) .. "|" .. c .. "|" .. s .. "|0|0") Talk(1, "", "Thieu thuy tinh (can " .. c .. " moi loai).") return end
	end
	if GetCash() < s then Msg2Player("[QH]|E|3|" .. lv .. "|" .. qh_rate(n) .. "|" .. c .. "|" .. s .. "|0|0") Talk(1, "", "Thieu bac.") return end
	for k = 1, 3 do ConsumeBagItemExact(QH_CRYSTAL[k], c) end
	Pay(s)
	local code = 1
	if random(1, 100) <= qh_rate(n) then
		SetItemEnChance(idx, 1, 1)        -- KItem::EnChance(+1): gia tri goc*(1+5%*N), +14/+15 ky nang o Apply khi mac
		code = 0
		lv = n
	end
	local n2 = lv + 1
	if n2 > QH_MAX then n2 = QH_MAX end
	local c2, s2 = qh_price(n2)
	Msg2Player("[QH]|E|" .. code .. "|0|" .. lv .. "|" .. qh_rate(n2) .. "|" .. c2 .. "|" .. s2 .. "|0")
end
