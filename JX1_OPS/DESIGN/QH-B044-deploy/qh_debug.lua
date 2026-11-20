-- [B-055] Lua go loi cuong hoa/tai phu (CHUA CHAY). Nap nong cung qianghua.lua; goi qh_debug() tu lenh bai GM hoac console.
-- In: tung o 0..9 -> GetEquipIdx, GetItemEnChance; sau do qh_wealth() (can qianghua.lua da nap).
function qh_debug()
	for p = 0, 9 do
		local idx = GetEquipIdx(p)
		local lv = 0
		if idx > 0 then lv = GetItemEnChance(idx) end
		Msg2Player("[QHDBG]|part=" .. p .. "|idx=" .. idx .. "|+" .. lv)
	end
	if qh_wealth ~= nil then
		Msg2Player("[QHDBG]|wealth=" .. qh_wealth())
	else
		Msg2Player("[QHDBG]|qh_wealth CHUA NAP (qianghua.lua cu)")
	end
end
