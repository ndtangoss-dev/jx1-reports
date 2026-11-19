-- [B-035] Cuong hoa +1..+15 (ban nhap, CHUA chay, CHUA dung gs001). Dat o gs\script\system\qianghua.lua tren Test-36 (.bak truoc).
-- Can ham C++ moi: GetEquipIdx(part), CountBagItemExact(detail), ConsumeBagItemExact(detail,n) (xem QH-B035-server.patch).
-- Thuy tinh = vat pham genre 4, detail: 239 Tu(hong) / 240 Luc / 238 Lam (questkey.txt dong 240-242, goods 1309-1311).
QH_CRYSTAL = { 239, 240, 238 }
QH_MAX = 15
QH_X = 100                          -- diem tai phu moi +1
QH_PARTS = {0,1,2,3,4,5,6,7,8,9}   -- head,body,belt,weapon,foot,cuff,amulet,ring1,ring2,pendant (N=10)
QH_SILVER_CAP = 2000000000          -- 20 uc (tien 32 bit, Q-87)

function qh_price(n)    -- gia len +n: so thuy tinh MOI LOAI, bac
	local c = 1
	for i = 2, n do c = c * 2 end
	local s = c * 2000000            -- 200 van
	if s > QH_SILVER_CAP then s = QH_SILVER_CAP end
	return c, s
end

function qh_rate(n)
	return 100 - 5 * (n - 1)
end

function qh_wealth()    -- diem tai phu = X * tong cap +N cac mon dang mac
	local sum = 0
	for i = 1, getn(QH_PARTS) do
		local idx = GetEquipIdx(QH_PARTS[i])
		if idx > 0 then sum = sum + GetItemEnChance(idx) end
	end
	return QH_X * sum
end

-- 0 thanh cong, 1 that bai (giu cap), 2 thieu thuy tinh, 3 thieu bac, 4 da toi da, 5 o khong hop le/trong
function QhEnhance(part)
	local ok = 0
	for i = 1, getn(QH_PARTS) do if QH_PARTS[i] == part then ok = 1 end end
	if ok == 0 then return 5 end
	local idx = GetEquipIdx(part)
	if idx <= 0 then return 5 end
	local lv = GetItemEnChance(idx)
	if lv >= QH_MAX then return 4 end
	local n = lv + 1
	local c, s = qh_price(n)
	for k = 1, 3 do
		if CountBagItemExact(QH_CRYSTAL[k]) < c then return 2 end
	end
	if GetCash() < s then return 3 end
	for k = 1, 3 do ConsumeBagItemExact(QH_CRYSTAL[k], c) end
	Pay(s)
	if random(1, 100) <= qh_rate(n) then
		SetItemEnChance(idx, 1, 1)
		return 0
	end
	return 1
end

-- Goi tu opensysui(2, a, b): a=10 cuong hoa o b; a=11 xem truoc o b; a=12 diem tai phu. Tra ve dong "[QH]|..." (xem A-B.md hop dong v3).
function QhHandle(a, b)
	if a == 12 then
		Msg2Player("[QH]|W|" .. qh_wealth())
		return
	end
	local idx = GetEquipIdx(b)
	local lv = 0
	if idx > 0 then lv = GetItemEnChance(idx) end
	if a == 11 then
		local n = lv + 1
		if n > QH_MAX then n = QH_MAX end
		local c, s = qh_price(n)
		Msg2Player("[QH]|P|" .. b .. "|" .. lv .. "|" .. qh_rate(n) .. "|" .. c .. "|" .. s .. "|" .. qh_wealth())
		return
	end
	local code = QhEnhance(b)
	local nl = 0
	local idx2 = GetEquipIdx(b)
	if idx2 > 0 then nl = GetItemEnChance(idx2) end
	local n = nl + 1
	if n > QH_MAX then n = QH_MAX end
	local c, s = qh_price(n)
	Msg2Player("[QH]|E|" .. code .. "|" .. b .. "|" .. nl .. "|" .. qh_rate(n) .. "|" .. c .. "|" .. s .. "|" .. qh_wealth())
end
