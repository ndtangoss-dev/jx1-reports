-----------Script*Cover*by**ThongJx*0347058065----------
------Desrition: LB GM--------------------

Include("\\script\\lib\\basic.lua");
Include("\\script\\lib\\string.lua");
Include("\\script\\log_game\\save_log.lua")
Include("\\script\\admin.lua")
----------------------------------------------------------------------------------------------------
Include("\\script\\warlord\\preload.lua");
Include("\\script\\item\\gmb.lua");
Include("\\script\\header\\taskid.lua")
Include("\\script\\tnlteam\\lib\\function.lua")
Include("\\script\\Global\\checkgm.lua");
Include("\\script\\lib\\lib_ham.lua");
Include("\\script\\subject\\demhuyhoang\\event.lua");
Include("\\script\\subject\\bosstieuhk\\bosstieuhk.lua");
----------------------------------------------------------------------------------------------------
-- Include("\\script1\\item\\ib\\lbbosstruongtuyen.lua");


function AddItemID(nItemIdx,nItemGenre, nDetailType, nParticulType,nLevel, nSeries, pLucky,nMgLevel)
		if nMgLevel == 1 then
		local nItemIdx = AddItem(nItemGenre, nDetailType,nParticulType, nLevel, nSeries, pLucky,1,0,0,0,0,0,0,0,0);
		elseif nMgLevel == 2 then
		local nItemIdx = AddItem(nItemGenre, nDetailType,nParticulType, nLevel, nSeries, pLucky,2,2,0,0,0,0,0,0,0);
		elseif nMgLevel == 3 then
		local nItemIdx = AddItem(nItemGenre, nDetailType,nParticulType, nLevel, nSeries, pLucky,3,3,3,0,0,0,0,0,0);
		elseif nMgLevel == 4 then
		local nItemIdx = AddItem(nItemGenre, nDetailType,nParticulType, nLevel, nSeries, pLucky,4,4,4,4,0,0,0,0,0);
		elseif nMgLevel == 5 then
		local nItemIdx = AddItem(nItemGenre, nDetailType,nParticulType, nLevel, nSeries, pLucky,5,5,5,5,5,0,0,0,0);
		elseif nMgLevel == 6 then
		local nItemIdx = AddItem(nItemGenre, nDetailType,nParticulType, nLevel, nSeries, pLucky,6,6,6,6,6,6,0,0,0);
		elseif nMgLevel == 7 then
		local nItemIdx = AddItem(nItemGenre, nDetailType,nParticulType, nLevel, nSeries, pLucky,7,7,7,7,7,7,0,0,0);
		elseif nMgLevel == 8 then
		local nItemIdx = AddItem(nItemGenre, nDetailType,nParticulType, nLevel, nSeries, pLucky,8,8,8,8,8,8,0,0,0);
		elseif nMgLevel == 9 then
		local nItemIdx = AddItem(nItemGenre, nDetailType,nParticulType, nLevel, nSeries, pLucky,9,9,9,9,9,9,0,0,0);
		elseif nMgLevel == 10 then
		local nItemIdx = AddItem(nItemGenre, nDetailType,nParticulType, nLevel, nSeries, pLucky,10,10,10,10,10,10,0,0,0);
		end
end

AWARD_ITEM = {--phÇn th­ëng nhiÖm vô
[1]={2,134},	--Tam tam tuong anh phu
[2]={2,22},		--Hoa hong
[3]={2,16},		--Phao hoa
[4]={2,23},		--Thiet la han
[5]={2,18},		--Ban nhuoc tam kinh
[6]={2,68},	--phuc duyen tieu
[7]={2,69},	--phuc duyen trung 
[8]={2,70},	--phuc duyen dai
[9]={2,64},		--tien thao lo
[10]={2,66},	--thien son bao lo
[11]={2,65},	--bach qua lo
}



function tbtest(szInput)
	--local tbData = lib:Split(szInput, ",")
	--if tbData[1] == "1" then
    --    Talk(1, "", "Du lieu khong hop le")
	--else
    --tonumber(tbData[2]), tonumber(tbData[3]), tonumber(tbData[4]),tonumber(tbData[5]), 0,  0)
	Msg2Player("AddItem: "..szInput.." !")
	--end
end

function OnEnterKey(input)

	Msg2Player("AddItem: "..GetMapName(input).." !")
end

--diem phuc sinh mon phai
MONPHAI_ARRAY = {
{103	,	"ThiÕu L©m ph¸i"			,52},
{59		,	"Thiªn V­¬ng bang"	,21},
{25		,	"§­êng M«n"				,15},
{183	,	"Ngò §éc gi¸o"				,71},
{13		,	"Nga My ph¸i"				,13},
{154	,	"Thóy Yªn m«n"			,61},
{115	,	"C¸i Bang"						,53},
{49		,	"Thiªn NhÉn gi¸o"		,28},
{81		,	"Vâ §ang ph¸i"				,40},
{131	,	"C«n L«n ph¸i"				,57}
};

MonPhaivaThanhThi={
[1]={51104,102592},--thanh thi
[11]={99840,163840},
[37]={55232,99200},
[78]={50208,103328},
[80]={56256,96960},
[162]={50528,100320},
[176]={44640,106176},

[20]={113472,199232},
[53]={52032,101696},
[54]={53280,100832},
[99]={52160,102368},
[100]={51616,101920},
[101]={54048,100896},
[121]={64000,143200},
[153]={52256,103520},
[174]={52960,105472}, -- long tuyen thon
[175]={53440, 101440}, -- tay son thon

[103]={59040,95456},-- mon phai
[59]={50144,103232},
[25]={128896,165856},
[183]={47712,101664},
[13]={62336,157568},
[154]={12896,43552},
[115]={48032,117504},
[49]={54016,101376},
[81]={53376,100096},
[131]={50624,101600}
}

AWARD_ITEM = {--phÇn th­ëng nhiÖm vô
[1]={2,134},	--Tam tam tuong anh phu
[2]={2,22},		--Hoa hong
[3]={2,16},		--Phao hoa
[4]={2,23},		--Thiet la han
[5]={2,18},		--Ban nhuoc tam kinh
[6]={2,68},	--phuc duyen tieu
[7]={2,69},	--phuc duyen trung 
[8]={2,70},	--phuc duyen dai
[9]={2,64},		--tien thao lo
[10]={2,66},	--thien son bao lo
[11]={2,65},	--bach qua lo
}




function append()
	GiveItemUI(""," Test give", "ok_append", "no")
end

function ok_append(szParams, snParams, nCount, njb, njxb, inval, invala)
	local Idx = split(szParams);

	if nCount > 1 then
		Talk(1,"","Ng­¬i bá nhiÒu qu¸ hoa hÕt c¶ m¾t ta k thÓ ghÐp ®c vui lßng bá vµ 1 c¸i x5 trë lªn")
	return end

	local nIndex = tonumber(Idx[1]);

	--SetItemMagicAttrib(nIndex,1,50)



		for i=0,5 do
			local nMagicType, p1, p2, p3 = GetItemMagicAttrib(nIndex, i);
			local _AttribType,_Ver_1,_,_=GetItemMagicAttrib(nIndex,i)--(0-5)
			--Msg2Player(format("nMagicType: Thu: %d  %d-%d-%d ",i, nMagicType,p1,p2,p3));
			Msg2Player(format("nMagicType: Thu: %d  %d-%d ",i, _AttribType,_Ver_1));
		end
end

TIEUXA_TEMPLET = {
{2084, " Tiªu Xa [§ång]"},
{2085, " Tiªu Xa [B¹c]"},
{2086, " Tiªu Xa [Vµng]"},
}
	
function timxe()
		TASK_NPCVANTIEU = 1500
	local nTask = GetTask(TASK_NPCVANTIEU)
	local nNpcIdx = FindAroundNpc(nTask)
	if (nNpcIdx > 0) then
		Talk(1,"","Kh«ng ph¶i tiªu xa cña ng­¬i ®ang ë ngay ®©y sao!")
	return end
	nNpcIdx = FindNpc(nTask)
	if(nNpcIdx > 0) then
		local x,y,w = GetNpcPos(nNpcIdx)
		NewWorld(w,(x/32),(y/32))
	else
		Talk(1,"","Kh«ng thÊy tin tøc! Tiªu xa cña ng­¬i cã lÏ ®· mÊt!")
	end
end
function batdau()
		TASK_NPCVANTIEU = 1500
		local nName = GetName()
		local nCamp = GetCurCamp();
		local w,x,y = GetWorldPos()
		local n = MATH_Random(2)
		local nRand = n+1
		local nId = AddNpcNew(TIEUXA_TEMPLET[nRand][1],1,w,x*32,y*32,"\\script\\subject\\van_tieu\\tieuxa.lua",0,nil,nil,5,0,500000)
		SetNpcOwner(nId,nName,1)
		SetNpcName(nId,nName..TIEUXA_TEMPLET[nRand][2]);
		--SetNpcTimeout(nId,108);
		SetNpcTimeLive(nId,10);
		SetNpcValue(nId,GetUUID());
		SetTask(TASK_NPCVANTIEU, GetNpcID(nId))
		--SetNpcLiveTime(nId,30,0,SubWorldID2Idx(w),1)
end		

function FnThuHoach(szParma, szParmb, inparm, inNulla, inNulab, inNullc, inNulld)
    local nNpcIdx = tonumber(szParma)
    if (nNpcIdx <= 0 or nNpcIdx == nil) then 
	return end
	Msg2Player(" szParma: "..nNpcIdx.." ");
end	


function tbTest_Xanh()
		genre = 0
		detail = 0
		particular = 4
		level = 10
		series = 2
		lucky = 200
	
		local nPiont = 7 -- so dong do tim
		local nSeed = 200
		
		local AttribTypeTable = {}
		--AttribTypeTable[1] = 24  	-- loai thuoc tinh 1
		--AttribTypeTable[2] = 221  	-- loai thuoc tinh 2
		--AttribTypeTable[3] = 167  	--
		--AttribTypeTable[4] = 311
		--AttribTypeTable[5] = 72
		--AttribTypeTable[6] = 218

		AttribTypeTable[1] = 72  	-- loai thuoc tinh 1
		AttribTypeTable[2] = 130  	-- loai thuoc tinh 2
		AttribTypeTable[3] = 0  	--
		AttribTypeTable[4] = 0
		AttribTypeTable[5] = 0
		AttribTypeTable[6] = 0


		-- G?i t?o item trang b? lo?i 2 c?p 10, s? lu?ng 1
		local nItemIndex = AddItemEx(
			genre, detail, particular, level, series, -- genre, detail, particular, level, series
			lucky, -- lucky
			AttribTypeTable[1], AttribTypeTable[2], AttribTypeTable[3],
			AttribTypeTable[4], AttribTypeTable[5], AttribTypeTable[6],
			1, -- nStackNum,
			0, -- nEnChance,  cuong hoa +
			nPiont, -- nPoint
			0, 0, 0, 0, 0, 0, -- time
			1,               -- login
			nSeed            -- random
			)
end

function truyconglenh()
	local nHour = 20--tonumber(GetLocalDate("%H"))
	if (nHour == 20) then -- gio vang se x2 phan thuong
		local tbOptions = {
			"Giao nép truy c«ng lÖnh 60 v¹n/truyconglenhvan",
			"Giao nép truy c«ng lÖnh 6 Xu/truyconglenhxu",
			"§ãng. /no"
		};
		SayNew("Xin mêi lùa chän giao nép truy c«ng lÖnh tiÒn v¹n hoÆc xu ", getn(tbOptions), tbOptions);
	else
		local tbOptions = {
			"Giao nép truy c«ng lÖnh 30 v¹n/truyconglenhvan_giovang",
			"Giao nép truy c«ng lÖnh 3 Xu/truyconglenhxu_giovang",
			"§ãng. /no"
		};
		SayNew("Xin mêi lùa chän giao nép truy c«ng lÖnh tiÒn v¹n hoÆc xu ", getn(tbOptions), tbOptions);
	end

end

function truyconglenhvan(param)
	Msg2Player("param: %d");
	local nTaskValue = GetTask(TASK_RESET_4)
	local nTask = MATH_GetBit(2,nTaskValue,2)
	
	if (nTask >= 2) then
		Talk(1, "", format("H«m nay ng­¬i ®· giao %d/2, kh«ng thÓ giao ®­îc n÷a n÷a.", nTask))
	return end
	
	local nHave = GetItemCount(3, 2, 1, 212, -1, 0);
	if (nHave >= 1 and GetCash() >= 500000) then
		DelItemCount(3, 1, 2, 1, 212, -1, -1);
		Pay(500000)
		AddOwnExp(5000000);
		SetTask(TASK_RESET_4,MATH_SetBit(2,GetTask(TASK_RESET_4),2,nTask+1))
		Msg2Player("B¹n nhËn ®­îc 5.000.000 EXP");
	else
		Talk(1,"","Ng­¬i kh«ng cã truy c«ng lÖnh hoÆc kh«ng ®ñ 50 v¹n l­îng!")
	end
end

function truyconglenhxu()
	local nTaskValue = GetTask(TASK_RESET_4)
	local nTask = MATH_GetBit(2,nTaskValue,2)
	
	if (nTask >= 2) then
		Talk(1, "", format("H«m nay ng­¬i ®· giao %d/2, kh«ng thÓ giao ®­îc n÷a n÷a.", nTask))
	return end
	
	local nHave = GetItemCount(3, 2, 1, 212, -1, 0);
	if (nHave >= 1 and GetXu() >= 3) then
		DelItemCount(3, 1, 2, 1, 212, -1, -1);
		PayXu(3)
		AddOwnExp(10000000);
		SetTask(TASK_RESET_4,MATH_SetBit(2,GetTask(TASK_RESET_4),2,nTask+1))
		Msg2Player("B¹n nhËn ®­îc 10.000.000 EXP");
	else
		Talk(1,"","Ng­¬i kh«ng cã truy c«ng lÖnh hoÆc kh«ng ®ñ 3 Xu!")
	end
end






function truyconglenh()
	local nHour = tonumber(GetLocalDate("%H"))
	if (nHour == 20) then -- gio vang se x2 phan thuong
		local tbOptions = {
			"Giao nép truy c«ng lÖnh 60 v¹n/truyconglenhvan",
			"Giao nép truy c«ng lÖnh 6 Xu/truyconglenhxu",
			"§ãng. /no"
		};
		SayNew("Xin mêi lùa chän giao nép truy c«ng lÖnh tiÒn v¹n hoÆc xu (Giê vµng phÇn th­ëng x2)", getn(tbOptions), tbOptions);
	else
		local tbOptions = {
			"Giao nép truy c«ng lÖnh 30 v¹n/truyconglenhvan",
			"Giao nép truy c«ng lÖnh 3 Xu/truyconglenhxu",
			"§ãng. /no"
		};
		SayNew("Xin mêi lùa chän giao nép truy c«ng lÖnh tiÒn v¹n hoÆc xu", getn(tbOptions), tbOptions);
	end
end

function truyconglenhvan(param)
	local nHour = tonumber(GetLocalDate("%H"))
	local nTaskValue = GetTask(TASK_RESET_4)
	local nTask = MATH_GetBit(2, nTaskValue, 2)
	
	if (nTask >= 2) then
		Talk(1, "", format("H«m nay ng­¬i ®· giao %d/2, không thÓ giao ®­îc n÷a.", nTask))
	return end

	local nHave = GetItemCount(3, 2, 1, 212, -1, 0);
	if (nHave >= 1 and GetCash() >= (nHour == 20 and 600000 or 300000)) then
		DelItemCount(3, 1, 2, 1, 212, -1, -1);
		Pay(nHour == 20 and 600000 or 300000)
		AddOwnExp(nHour == 20 and 10000000 or 5000000)
		SetTask(TASK_RESET_4, MATH_SetBit(2, GetTask(TASK_RESET_4), 2, nTask + 1))
		Msg2Player(nHour == 20 and "B¹n nhËn ®­îc 10.000.000 EXP" or "B¹n nhËn ®­îc 5.000.000 EXP")
	else
		Talk(1, "", "Ng­¬i kh«ng cã truy c«ng lÖnh hoÆc kh«ng ®ñ ".. (nHour == 20 and "60 v¹n" or "30 v¹n") .." l­îng!")
	end
end

function truyconglenhxu()
	local nHour = tonumber(GetLocalDate("%H"))
	local nTaskValue = GetTask(TASK_RESET_4)
	local nTask = MATH_GetBit(2, nTaskValue, 2)

	if (nTask >= 2) then
		Talk(1, "", format("Hôm nay nguoi dã giao %d/2, không thÓ giao ®­îc n÷a.", nTask))
		return
	end

	local nHave = GetItemCount(3, 2, 1, 212, -1, 0);
	if (nHave >= 1 and GetXu() >= (nHour == 20 and 6 or 3)) then
		DelItemCount(3, 1, 2, 1, 212, -1, -1);
		PayXu(nHour == 20 and 6 or 3)
		AddOwnExp(nHour == 20 and 20000000 or 10000000)
		SetTask(TASK_RESET_4, MATH_SetBit(2, GetTask(TASK_RESET_4), 2, nTask + 1))
		Msg2Player(nHour == 20 and "B¹n nhËn ®­îc 20.000.000 EXP" or "B¹n nhËn ®­îc 10.000.000 EXP")
	else
		Talk(1, "", "Ng­¬i kh«ng cã truy c«ng lÖnh hoÆc kh«ng ®ñ ".. (nHour == 20 and "6 Xu" or "3 Xu") .."!")
	end
end



AWARD_ITEM = {--phÇn th­ëng nhiÖm vô
	[1]={2,134},	--Tam tam tuong anh phu
	[2]={2,22},		--Hoa hong
	[3]={2,16},		--Phao hoa
	[4]={2,23},		--Thiet la han
	[5]={2,18},		--Ban nhuoc tam kinh
	[6]={2,68},		--phuc duyen tieu
	[7]={2,69},		--phuc duyen trung 
	[8]={2,70},		--phuc duyen dai
	[9]={2,64},		--tien thao lo
	[10]={2,66},	--thien son bao lo
	[11]={2,65},	--bach qua lo
}
	
	


tbUseGourd_ItemAward = {
    -- Pho bien: tong 600
    {szName="X¸ lîi Kim §¬n.", tbProp={2,1,255,1,0,0}, nCount=1, nRate=100},
    {szName="ThiÕt La H¸n.", tbProp={2,1,23,1,0,0}, nCount=1, nRate=100},
    {szName="Lam Thñy Tinh.", tbProp={4,238,1,1,0,0}, nCount=1, nRate=100},
    {szName="Tö Thñy Tinh.", tbProp={4,239,1,1,0,0}, nCount=1, nRate=100},
    {szName="Lôc Thñy Tinh.", tbProp={4,240,1,1,0,0}, nCount=1, nRate=100},
    {szName="Tiªn Th¶o Lé.", tbProp={2,1,64,1,0,0}, nCount=1, nRate=100},

    -- Trung binh: tong 250
    {szName="LÖnh Bµi Danh Väng tiÓu", tbProp={2,1,266,1,0,0}, nCount=1, nRate=50},
    {szName="Phóc Duyªn Lé (TiÓu).", tbProp={2,1,68,1,0,0}, nCount=1, nRate=100},
    {szName="Tinh Hång B¶o Th¹ch.", tbProp={4,353,1,1,0,0}, nCount=1, nRate=100},

    -- Hiem: tong 20
    {szName="Tiªn Th¶o lé DÆc BiÖt.", tbProp={2,1,254,1,0,0}, nCount=1, nRate=10},
    {szName="Bµn Nh­îc T©m Kinh.", tbProp={2,1,18,1,0,0}, nCount=1, nRate=10},
}


function OpenGourdAward()
    local totalRate = 0
    for i = 1, getn(tbUseGourd_ItemAward) do
        totalRate = totalRate + tbUseGourd_ItemAward[i].nRate
    end

    local rand = MATH_Random(totalRate) -- random t? 1 d?n totalRate
    local cumulative = 0

    for i = 1, getn(tbUseGourd_ItemAward) do
        local item = tbUseGourd_ItemAward[i]
        cumulative = cumulative + item.nRate
        if rand <= cumulative then
            for j = 1, item.nCount or 1 do
                local itemIndex
                if item.nQuality then
                    itemIndex = AddGoldItem(unpack(item.tbProp))
                else
                    itemIndex = AddItem(unpack(item.tbProp))
                end
                if item.nExpiredTime and item.nExpiredTime > 0 then
                    SetItemUseTimeNew(itemIndex, item.nExpiredTime)
                end
            end
            Msg2Player("B¹n nhËn ®­îc: " .. item.szName .. " (rand=" .. rand .. ")")
            return
        end
    end
end


tbUseGourd_ItemAwardEvent = {
    {szName="X¸ lîi Kim §¬n.", tbProp={2,1,255,1,0,0}, nCount=1, nRate=0.03},
    {szName="Bµn Nh­îc T©m Kinh.", tbProp={2,1,18,1,0,0}, nCount=1, nRate=0.03},
    {szName="ThiÕt La H¸n.", tbProp={2,1,23,1,0,0}, nCount=1, nRate=0.03},
    {szName="Tiªn Th¶o lé DÆc BiÖt.", tbProp={2,1,254,1,0,0}, nCount=1, nRate=0.03},
    {szName="Lam Thñy Tinh.", tbProp={4,238,1,1,0,0}, nCount=1, nRate=0.03},
    {szName="Tö Thñy Tinh.", tbProp={4,239,1,1,0,0}, nCount=1, nRate=0.03},
    {szName="Lôc Thñy Tinh.", tbProp={4,240,1,1,0,0}, nCount=1, nRate=0.03},
    {szName="Tinh Hång B¶o Th¹ch.", tbProp={4,353,1,1,0,0}, nCount=1, nRate=0.03},
    {szName="Tiªn Th¶o Lé.", tbProp={2,1,64,1,0,0}, nCount=1, nRate=0.03},
    {szName="LÖnh Bµi Danh Väng.", tbProp={2,1,266,1,0,0}, nCount=1, nRate=0.03},
    {szName="Phóc Duyªn Lé (TiÓu).", tbProp={2,1,68,1,0,0}, nCount=1, nRate=0.03},
    {szName="ItemGold", tbProp={3465,0}, nCount=1, nRate=0.01},
	{szName= "§iÓm Kinh NghiÖm", nExp=7000000, nRate = 25},
}

function OpenGourdAwardEvent()--an even ra item exp pho bien
    local totalRate = 0
	for i = 1, getn(tbUseGourd_ItemAwardEvent) do
        local item = tbUseGourd_ItemAwardEvent[i]
        totalRate = totalRate + item.nRate
    end

	local rand = MATH_Random(totalRate * 1000) / 1000
    local cumulative = 0
	for i = 1, getn(tbUseGourd_ItemAwardEvent) do
        local item = tbUseGourd_ItemAwardEvent[i]
        cumulative = cumulative + item.nRate
        if rand <= cumulative then
            if item.nExp then
                AddOwnExp(item.nExp)
                Msg2Player("B¹n nhËn ®­îc: "..rand.." " .. item.szName .. " " .. item.nExp .. " EXP")
            elseif item.tbProp then
                for j = 1, item.nCount or 1 do
                    local itemIndex
                    if item.nQuality then
                        itemIndex = AddGoldItem(unpack(item.tbProp))
                    else
						itemIndex = AddItem(unpack(item.tbProp))
                    end
                    if item.nExpiredTime and item.nExpiredTime > 0 then
                        SetItemUseTimeNew(itemIndex, item.nExpiredTime)
                    end
                end
                Msg2Player("B¹n nhËn ®­îc: "..rand.." " .. item.szName)
            end
            return
        end
    end
end

TRAPTHIENBAOKHO = {
{395,45088,102208},
{395,45120,102208},
{395,45152,102208},
{395,45184,102208},
{395,45216,102208},
{395,45248,102208},
{395,45280,102208},
{395,45312,102208},
{395,45344,102208},
{395,45376,102208},
{395,45408,102208},
{395,45440,102208},
{395,45088,102240},
{395,45120,102240},
{395,45152,102240},
{395,45184,102240},
{395,45216,102240},
{395,45248,102240},
{395,45280,102240},
{395,45312,102240},
{395,45344,102240},
{395,45376,102240},
{395,45408,102240},
{395,45440,102240}
}

function testtrap()
	SayEx({"Chµo Admin! ThÇy cÇn g×?",
		"AddtrapEx1/addtrapex1",
		"DeltrapEx1/deltrapex1",
		"KÕt thóc ®æi tho¹i/no"})
end

function addtrapex1()
	w,x,y = GetWorldPos();
	AddObjEx1(469,w,x,y,5,"","",0,0)
end

function deltrapex1()
	w,x,y = GetWorldPos();
	DelObjEx1(w,x,y,5)
end

BOSSTIEU_ARRAY={
{"DiÖu Nh­",513,2,{1,6}},
{"LiÔu Thanh Thanh",523,1,{2,5}},
{"Tr­¬ng T«ng ChÝnh",511,4,{3,4}}
};





POS_TEST={
{1680,3247},
{1677,3247},
{1674,3247},
{1671,3247},
{1668,3247},
{1665,3247},
{1662,3247},
{1659,3247},
{1656,3247},
{1653,3247},

{1680,3250},
{1677,3250},
{1674,3250},
{1671,3250},
{1668,3250},
{1665,3250},
{1662,3250},
{1659,3250},
{1656,3250},
{1653,3250},


{1680,3253},
{1677,3253},
{1674,3253},
{1671,3253},
{1668,3253},
{1665,3253},
{1662,3253},
{1659,3253},
{1656,3253},
{1653,3253},

{1680,3256},
{1677,3256},
{1674,3256},
{1671,3256},
{1668,3256},
{1665,3256},
{1662,3256},
{1659,3256},
{1656,3256},
{1653,3256},

{1680,3259},
{1677,3259},
{1674,3259},
{1671,3259},
{1668,3259},
{1665,3259},
{1662,3259},
{1659,3259},
{1656,3259},
{1653,3259},

{1680,3262},
{1677,3262},
{1674,3262},
{1671,3262},
{1668,3262},
{1665,3262},
{1662,3262},
{1659,3262},
{1656,3262},
{1653,3262},


{1680,3265},
{1677,3265},
{1674,3265},
{1671,3265},
{1668,3265},
{1665,3265},
{1662,3265},
{1659,3265},
{1656,3265},
{1653,3265},

{1680,3268},
{1677,3268},
{1674,3268},
{1671,3268},
{1668,3268},
{1665,3268},
{1662,3268},
{1659,3268},
{1656,3268},
{1653,3268},

{1680,3271},
{1677,3271},
{1674,3271},
{1671,3271},
{1668,3271},
{1665,3271},
{1662,3271},
{1659,3271},
{1656,3271},
{1653,3271},

{1680,3274},
{1677,3274},
{1674,3274},
{1671,3274},
{1668,3274},
{1665,3274},
{1662,3274},
{1659,3274},
{1656,3274},
{1653,3274}




};


function tbCall_NpcCocGo()
		local W,X,Y = GetWorldPos();
		local nMapId = W;
		for i = 1, getn(POS_TEST) do
			--local nNpcIdx = AddNpc(413,95,SubWorldID2Idx(W), POS_TEST[i][1] * 32, POS_TEST[i][2] * 32, 8 , "TestDame", 0,0);
			local nNpcIdx = AddNpc(1038, 95, SubWorldID2Idx(W), POS_TEST[i][1] * 32, POS_TEST[i][2] * 32, 8 , "TestDame", 0,0);
				if nNpcIdx > 0 then
					SetNpcLiveTime(nNpcIdx,10,0,SubWorldID2Idx(W),1);
					SetNpcSeries(nNpcIdx, random(0,4))
					--SetNpcDeathScript(nNpcIdx,BOSTIEU_DEATH);
					--SetNpcScript(nNpcIdx, BOSTIEU_DEATH) --- duong dan boss chet
					--LoldDropRate(nNpcIdx, BOSTIEU_DROP)---duong dan rot vat pham
					SetNpcCurlife(nNpcIdx, 90000, 90000)---mau boss min, max
					--SetNpcItemCount(nNpcIdx, 30) -----vat pham rot 30
					--SetNpcCurDefend(nNpcIdx, 1, 1)---khang min, max
					--SetNpcPhanDame(nNpcIdx, 20)
					--SetSetNpcExper(nNpcIdx, 30000, 1)---kinh nghiem
					-- SetNpcParam(nNpcIdx, 0, 1); --boss truong tuyen set 1
				end
		end
end

function tbCall_NpcTest()
		local W,X,Y = GetWorldPos();
		local nMapId = W;
			local nNpcIdx = AddNpc(413,95,SubWorldID2Idx(W), X * 32, Y * 32, 2 , "TestDame", 0,0);
				if nNpcIdx > 0 then
					SetNpcLiveTime(nNpcIdx,30,0,SubWorldID2Idx(W),1);
					SetNpcSeries(nNpcIdx, random(0,4))
					--SetNpcDeathScript(nNpcIdx,BOSTIEU_DEATH);
					--SetNpcScript(nNpcIdx, BOSTIEU_DEATH) --- duong dan boss chet
					--LoldDropRate(nNpcIdx,BOSTIEU_DROP)---duong dan rot vat pham
					SetNpcCurlife(nNpcIdx,500,500)---mau boss min, max
					--SetNpcItemCount(nNpcIdx,30) -----vat pham rot 30
					--SetNpcCurDefend(nNpcIdx,1,1)---khang min, max
					--SetNpcPhanDame(nNpcIdx,20)
					--SetSetNpcExper(nNpcIdx,30000,1)---kinh nghiem
					-- SetNpcParam(nNpcIdx, 0, 1); --boss truong tuyen set 1
					UpdataDropRate(nNpcIdx, "\\settings\\droprate\\goldennpc\\golden_lv90.ini");
				end
end



function tbTrieuHoi()	 
local  roleName=GetName()
	 if  FindTbName(roleName)==1 then
   Talk(1,"","Nh¾c nhë:<c=cyan> Ta kh«ng cã nhí lÇm, ®· cã sñng vËt!<c>!")
	   return
	 end
	 
local w,x,y=GetWorldPos()	
local bb=GetCamp()
local cc=GetNpcIndexid()   --ÈËÎïÔÚNPCÖÐµÄË÷Òý
local npcmapindex= SubWorldID2Idx(w)
local boosid=random(1869,1872)

local sexid=random(0,4)
local level=random(85,95)
local nNpcid=Addyabiao(boosid,level,npcmapindex,x*32,y*32,0,bb,cc,2)  --1ÎªÑºïÚ 2 ÎªÍ¬°é
    if  nNpcid>0 then
      SetNpcScript(nNpcid,"\\script\\deadth\\Í¬°éËÀÍö\\tongyong.lua")
      SetNpcSeries(nNpcid,sexid)
      LoldDropRate(nNpcid,"\\settings\\droprate\\kong.ini")
      SetTonBanNun(GetNpcDwidx(nNpcid))
      SetNpcCurCamp(nNpcid,bb)
	  
	  SetNpcLiveTime(nNpcid,3600,0,0)  --Ãë
	  --1132	0|30	1143	0|30	1142	0|30	1161	0|30
	  SetNpcSkill(nNpcid,1,1132,40)
	  SetNpcSkill(nNpcid,2,1143,40)
	  SetNpcSkill(nNpcid,3,1142,40)
	  SetNpcSkill(nNpcid,4,1161,40)
	  
	  SetNpcAttackFrame(nNpcid,10,0,boosid,level)
			
	  setNpcLockMap(nNpcid,38)   --Ëø¶¨ÔÚµØÍ¼
	  setNpcDamageRatio(nNpcid,1000)  --¹¥»÷10±¶
	  SetNpcCurDefend(nNpcid,140,150)
	  
	  SetNpcName(nNpcid, roleName.."[ Båi luyÖn ]")
      Msg2Player("Nh¾c nhë: §ång b¹n triÖu ho¸n thµnh c«ng!")
	 else
	 Msg2Player("Nh¾c nhë: §ång b¹n triÖu ho¸n thÊt b¹i!")
	 end
end





SKILL120=
{
	709,708,710,711,712,713,714,715,716,717,1365,1662,1712
}

function tbTest_boss()
	for i = 1,50 do
		w,x,y = GetWorldPos();--MATH_RandomC(513,523,511)
		nNpcIndex = AddNpcNew(MATH_RandomC(513,523,511), 100, w, x*32, y*32, nil, 5,nil,1, random(0,4),300000,8000000,5000,8000,nil,nil,nil,nil,nil,80,8,nil);
		--PhanDame1,PhanDame2,PhanDame3,PhanDame4 = GetNpcPhanDame(nNpcIndex);
		--print(format("PhanDame1: %d,PhanDame2: %d,PhanDame3: %d,PhanDame4: %d",PhanDame1,PhanDame2,PhanDame3,PhanDame4));
	end
end

function Goi_NpcTestNew()	
	for i = 1,50 do
		local W,X,Y = GetWorldPos();
		local nMapId = W;	--																		--Loai boss
		local nNpcIdx = AddNpc(496,95,SubWorldID2Idx(W), (X +  random(1,20))* 32, (Y +  random(1,20))* 32, 0);
				if nNpcIdx > 0 then
					SetNpcLiveTime(nNpcIdx, 10, 0, SubWorldID2Idx(W), 1);
					SetNpcSeries(nNpcIdx, random(0,4))
					--LoldDropRate(nNpcIdx,BOSTIEU_DROP)---duong dan rot vat pham
					--SetNpcCurlife(nNpcIdx,900000000,900000000)---mau boss min, max
					--SetNpcItemCount(nNpcIdx,30) -----vat pham rot 30
					--SetNpcCurDefend(nNpcIdx,350,350)---khang min, max
					--SetSetNpcExper(nNpcIdx,30000,1)---kinh nghiem
					--SetNpcParam(nNpcIdx, 0, 1); --boss truong tuyen set 1
					--SetNpcAttackFrame(nNpcIdx,18,0,1083,GetLevel(nNpcIdx))
					SetNpcDmgEx(nNpcIdx,10, 10, 10, 10, 10)
					
				end
	end
end

function tbTest_GM()
--	local nlv = 10;
--	nIndex = AddItem(0 ,8, 1, 10, 1, 10, 90, nlv, nlv, nlv, nlv, nlv, nlv, 0, 0);	
--	SetMagicAttrib(nIndex,1,115,30)
--	SetMagicAttrib(nIndex,2,123,100)
--	SetMagicAttrib(nIndex,3,126,100)
--	PlaceItem(nIndex)







	--AddMagic(331,20)

	--Goi_NpcTestNew();
	--SetPos(1703, 3260)
	--SetPos(1705,3261)

	--Msg2Player("GetFactionNo:  "..GetFactionNo().."  GetTask(130): "..GetTask(130).." ");
	--SetFaction("tianwang");
	--SetTask(130,2)
	--NewWorld(121,1967,	4506)
	
	--DelMagic(tb_90skill[0][1])
	--DelMagic(tb_90skill[0][2])
	--DelMagic(tb_90skill[0][3])


	--SetTask(TASK_TAN_THU, 0)
	--local nLastFacId = GetFactionNo()
	--AddMagic(SKILL120[nLastFacId], 5)
	
	--tbTrieuHoi()
	--LocalScript("\\script\\mineitem\\quehoatuu.lua")

	--AddOwnExp(10000)
	--AddSkillState(89, 50, 1, 64800 * 12 * 1);
	--AddMagic(89,50)
	--tbCall_NpcTest()
	--ForbidChangePK(0);
	--for i = 2944,2955 do
	--for i = 3164,3184 do
	--	AddGoldItem(i);
	--end
	
	--AddGoldItem(3879);--han huyet long cau
	--AddItem(0,12,0,14,0,5,0,0) -- phi phong gm
	
	
	
	--NewWorld(173,1556,3050) tu dao hiep 
	--NewWorld(173,1556,3050)
	--NewWorld(24,2104,3326)
	--NewWorld(90,1810,3290)
	--SetTask(TASK_NVST, MATH_SetBit(2,GetTask(TASK_NVST),3,10))		
	--local scripts1 = "\\script\\subject\\hoang_kim\\lethuy.lua";
	--Msg2Player(scripts1)
	--LocalScript(scripts1)	

	--AddMagic(1420,20)
	--SetPlayerTitle(400, 24);
	--tbTest_boss()
	--tbCall_NpcTest()
	--AddMagic(331,20)
	
	--nIndex = AddItem(0, 8, 1, 5, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0);	
	--Sale(51)
	
	--NewWorld(21, 74688/32, 109888/32);
	
	--SetTask(TASK_DATAU_NUM, 200000)
	--for i = 419,428 do
	--	AddMagic(i,5)
	--end
	--AddEventItem(400)
	--DelItem(400)
 	--local myinfo = format("%s,%d","ConLon",300);
 	--AddLadder_Bang(400, myinfo);

	--nItemIdx = AddMineItem(286,1,0,199)
	--SetItemLock(nItemIdx); --khoa vinh vien
	
	--testtrap()
	--w,x,y = GetWorldPos();
	
	--AddObj(469,SubWorldID2Idx(w),x*32,y*32,0,0,"´¢ÎïÏä") 
    --local StartPos = random(1, getn(TIEUXA_STARTPOS))
    --NewWorld(21, 78957/32, 124476/32)

	--AddObjEx3(469,21,1864,3674,5,"","",0,0)
	--AddObjEx4(469,21,2452,3867,5,"","",0,0)
	--AddObjEx1(469,21,2253,3803,5,"","",0,0)
	--AddObjEx2(469,21,1974,3758,5,"","",0,0)
	
	--NewWorld(21, 1862, 3690)
	--AddObjEx3(469,21,1862, 3690,5,"","",0,0)

		--local nP = FindPlayerByName("VoDang01", 0)
		--Msg2Player("idx: "..nP.."")
		--if(nP > 0) then
		--	PlayerIndex = nP
		--	SetTask(TASK_NPCVANTIEU, GetNpcID(nId))
		--end

	--NewPayExtPoint("iMoney",1)
	--Msg2Player("GetExpoint: "..NewGetExtPoint("iMoney").." ");
	--PayExtPoint(499)
	--truyconglenh();
	--SetTask(TASK_RESET_4,1)

		
			--local W,X,Y = GetWorldPos();
			--local nMapId = W;
			--isboss = 0
			--local nNpcIdx = AddNpc(724,95,SubWorldID2Idx(W), X * 32, (Y +  5)* 32, isboss , "Thñy TÆc", 0,0);
			--if nNpcIdx > 0 then
			--	SetSetNpcExper(nNpcIdx, 8000, 1)--chinh exp
			--	SetNpcSeries(nNpcIdx, random(0,4))
				--SetNpcScript(nNpcIdx, BOSTIEU_DEATH) --- duong dan boss chet
			--	SetNpcParam(nNpcIdx, 1, 4)
			--	SetNpcLiveTime(nNpcIdx,11,0,SubWorldID2Idx(mapid),1)
			--end

	--for i=1,500 do
	--	PlayerIndex = i;
	--	if(FindAroundPlayer() > 0) then
	--		Msg2SubWorld(" "..i..": Player trong Pham Vi: 1000 "..GetName().."")
	--	end
	--end
	--OldPlayerIndex = PlayerIndex
	--for i = 1, 200 do
	--	PlayerIndex = i
	--	local idx = FindAroundNpc(PlayerIndex)
	--	if idx > 0 then
	--		Msg2SubWorld(" "..idx..": Player trong Pham Vi: 1000 "..GetName())
	--	end
	--end

	
	--SetLeagueObjName("ChienDoi");
	--Msg2Player("GetLeagueObjName: "..GetLeagueObjName().."_");
	--Name = "TenTruongNhom";
	--AddLeagueMemObj(Name,"Thanh vien 1")

	--MISSIONID = 13
	--Msg2MSPlayer(MISSIONID, "B¹n ®· vµo tr­êng ®Êu, 10 gi©y sau sÏ chÝnh thøc b¾t ®Çu.", PIdx2MSDIdx(MISSIONID, PlayerIndex) )
	--MS_ROUND = 4	--¼ÇÂ¼µ±ÌìÈüÊÂµÄÂÖ´Î
	--SetMissionV(MS_ROUND, 8)
	--Msg2Player("MS_ROUND: "..GetMissionV(MS_ROUND)..".")
--tbTest_Xanh()
--batdau()
--timxe()
		
--PaceBar("§ang h¸i qu¶...", "FnThuHoach",2, 123)   
--	local w,x,y = GetWorldPos()
--	HATHH_FILE = "\\script\\subject\\demhuyhoang\\hathuyhoang.lua"
--	nNpcIdx = AddNpcNew(1110,1,w,x*32,y*32,HATHH_FILE,6)
--	SetNpcParam(nNpcIdx,1,1);
--	SetNpcTimeout(nNpcIdx, 10)

	--append()
	--local nIndex = AddItem(0, 0, 2, 10, 1, 90, 10, 10, 10, 10, 10, 10, 1, 0, 0);
	--local nIndex = AddItem(0, 0, 2, 10, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0);
	
	--Name = GetName();
	--NameuId = FileName2Id(Name)
	
	--local success = AddLeagueMemObj(NameuId, Name)
	--if success == 1 then
	--	print(format("Thêm thành viên thành công ho?c dã t?n t?i. %d", NameuId))
	--else
	--	print(format("Nhóm không t?n t?i. %d", NameuId))
	--end
	
	--SetDataGr(idx, NameuId, 10, 20, 30, 40, "Bang Chu") --ham set data
	--SaveDataFile();
	--SetLock(0)

	--SetPlayerTitle( 400, 24);







	--AddMineItem(6,1,0,5)


	--Msg2Player("TASK_PLAYER_DHTK: "..GetTask(TASK_PLAYER_DHTK).." ");
	--J_VARV_TIME = 3        -- GetTask, TASK_PLAYER_DHTK
	--SetMissionV(SJ_VARV_TIME, 85); -- phut tran dau
	--SetTaskTemp(402,462)
	--SetTaskTemp(402,GetTaskTemp(402)+1)
	--SetPlayerTitle(GetTaskTemp(402), 24);
	
	--SetPlayerTitle(399, 24);

	--Sale(102)
	--local nNameId, v0, v1, v2, v3, name1, name2 = GetDataGr(0)
	--print(format("ID: %d v0: %d, v1: %d, v2: %d, v3: %d, name1: %s, name2: %s", nNameId, v0, v1, v2, v3, name1, name2))

	--SetPlayerTitle(400,1)
	
	--AddSkillState(541, 1, 1, 108*2)

	--SetGlbMissionV(27,1)
	--Msg2Player(format("GetGlbMissionV(28): %d  ", GetGlbMissionV(28) ));

	uId = 103
	
--NewWorld(11,FRESHMANMAPS[1]/32,FRESHMANMAPS[2]/32)
    if MonPhaivaThanhThi[uId] and getn(MonPhaivaThanhThi[uId]) > 0 then
        local nMapX = MonPhaivaThanhThi[uId][1] / 32
        local nMapY = MonPhaivaThanhThi[uId][2] / 32
        --Msg2Player(format(" %d , %d ", nMapX, nMapY))
		--NewWorld(uId,nMapX,nMapY)
    else
       --Msg2Player("Nill")
    end


	--AddObjEx3(469,21,1864,3674,30,"","",0,0)
	--AddObjEx4(469,21,2452,3867,25,"","",0,0)
	--AddObjEx1(469,21,2253,3803,30,"","",0,0)
	--AddObjEx2(469,21,1974,3758,30,"","",0,0)

	TASK_DIADOCHI = 14
	TASK_DATAU_ACCEPT = 16
	--ForbidChangePK(0)--set che do f9 pk toan sv
	--AddTermini(1)
	--SetTask(1028,1)
	--SetLevel(80)
	--nLevel = GetLevel();
	--SetTask(1020,Get0)
	--local nTaskDone = GetTask(29)
	--nTaskDone = MATH_SetBit(3, nTaskDone, 1, 0)
	--nTaskDone = MATH_GetBit(3,nTaskValue,2)
	--SetTask(29, nTaskDone)
	
	--nTaskDone = MATH_GetBit(3,GetTask(TASK_DIADOCHI),2)
	
	--Msg2SubWorld("alooooooooooooo  "..(nTaskDone).."    oooooooooo(:01)")
	for i = 269,279 do
		--AddMineItem(i, 1, 0)
	end
	
	--local nItemIdx = AddItem(0, 11, random(0,11), 1, 0, 0); -- 566 577
	--SetItemUseTimeNew(nItemIdx,10080)
	--Msg2Player("GetAccoutName(): "..GetAccoutName().."");
	
	--AddSkillState(1488, 1, 1, 500);
	--SetNpcTitle(337,64800)
	--id,nTime = GetNpcTitle()

	--SetPlayerTitle(400,24)
	--SetPlayerTitleSkills();
	--id,nTime,nTime2 = GetPlayerTitle()
	--Msg2Player("GetPlayerTitle: "..id.." - "..nTime..". "..KSG_GetCurSec().."")
	--nXu = 1;
	--for i = 1, nXu do
		--local nItemIdx = AddItem(2, 1, 245, 0, 0, 0);
	--	if nItemIdx ~= 0 then
	--		_w_log_Trade(LOG_STATUS_SUCCESS, "add_item", "Rót KNB", "payiyuanbao", nXu, nItemIdx, 1);
	--	end
	--end

	
	--local nTaskValue = GetTask(TASK_NVST)
	--local nValue = MATH_GetBit(2,nTaskValue,2)
	--SetTask(TASK_NVST, MATH_SetBit(2,GetTask(TASK_NVST),2,0))
	--Msg2Player("  nValue: "..nValue.."    ("..GetTask(TASK_NVST)..")   ");
	
	--local nNewItem = AddItem(2, 1, 64, 1, 0, 0);--tien thao lo
	--SetItemLock(nNewItem); --khoa vinh vien
	
	--local nNewItem = AddMineItem(64)
	--SetItemLock(nNewItem);
	
	--local nRandomSeed	 =100;
	--local nEnChance      =10;
	--for i = 1,3 do
	--AddGoldItemID(185,1,10,nRandomSeed,nEnChance,1)
	--end
	
	SetTask(TASKVALUE_LIXIAN,0)
	
	local nRitemTab		={32, 54, 90, 33, 46, 64}
	local nLevelTab		={79, 54, 90, 33, 46, 64}
	local nSeed 		= 10;
	local nEnChance		= 0;
	local nRpiont		= 6;
	local pLucky		= 100;
	for i = 1, 1 do
	  --AddGoldItemEx(3000,1,1,0,0,0,0,0,
	  --nLevelTab[0],nLevelTab[1],nLevelTab[2],nLevelTab[3],nLevelTab[4],nLevelTab[5],
	 -- nRpiont,nEnChance,nSeed,
	  --nRitemTab[0],nRitemTab[1],nRitemTab[2],nRitemTab[3],nRitemTab[4],nRitemTab[5],1)
	  
	  --AddItem(0, 2, 3, 10, 1, pLucky, nRitemTab[0],nRitemTab[1],nRitemTab[2],nRitemTab[3],nRitemTab[4],nRitemTab[5], 0, nEnChance, nRpiont);
	end
	
		--nItemIdx = AddItem(2, 1, 11, 0, 0, 0); --khai quang chan kinh
		--SetItemUseTimeNew(nItemIdx, 60*24*7);--7 ngay
	--DelMagic(492)
	--UseSkill(492, 1,1, 1080*3);
	--CastSkill(492,1,1080*3,0)
	--Msg2Player("GetSkillState(492): "..GetSkillStateTime(492).." ")
	--AddMagic(314,1)
	--AddSkillState(314, 1, 1, 1080*60)
	--AddSkillState(315,1,500,0)
	--AddFusionItem(200,10,0)
	
	--AddSkillState(1249,1,1,500)
		
	--AddSkillState(314, 1, 1, 64800 * 24 * 7);

	--AddMagic(372,1)
	--AddMagic(375,1)

	--AddSkillExp(372,5000,1)

	--RollbackSkill()
	--UpdateSkillList()
	
	
	--AddMagic(40,20)
 	--if (GetLastFactionNumber() == -1)then
	--	Talk(1,"","§¹i hiÖp ch­a gia nhËp m«n ph¸i kh«ng thÓ nhÆt <c=red>T¸n l¹c tiªu<c>!")
	--	return
	--end
	
	--{"GetLastFactionNumber", LuaGetLastFactionNumber},
	--{"GetFactionNo",	LuaGetLastFactionNumber},
	--{"GetFactionCamp",	LuaGetPlayerFactionCamp},
	--{"GetFaction",		LuaGetPlayerFaction},    //GetFaction()»ñµÃÍæ¼ÒµÄÃÅÅÉÃû
	
	--Talk(1,"","B¹n ®· sö dông <c=yellow>: "..GetLastFactionNumber().." "); 


	
	--j353 = CalcItemCount(3,4,353,0,-1)
	--check = DelItemCount(3, 1, 4, 353, 1, 1, 0)
	--j353 = GetItemCount(3,2,1,245,1,0)
	--check = DelItemCount(3, j353, 2, 1, 245, 1, 0)
	--check = ConsumeItem(3, j353, 4,353, 0, -1) -- del tinh hong
	--Talk(1,"","B¹n ®· sö dông <c=yellow>j353<c>: "..j353..". "..check.." . ");
	
	--AddMagic(390,1)
		-- Gia nhËp m«n ph¸i míi lªn thuyÒn Modified - by AnhHH - 20110724
	--if (GetLastFactionNumber() == -1)then
	--	Talk(1,"","§¹i hiÖp ch­a gia nhËp m«n ph¸i kh«ng thÓ lªn thuyÒn "..GetLastFactionNumber().." ")
	--	return
	--end
	
	--	Talk(1,"","§¹i hiÖp ch­a gia nhËp m«n ph¸i kh«ng thÓ lªn thuyÒn "..GetFaction().." ")

	--for i = 1,2000 do 	
	--	DelMagic(i)
	--end
		


	--AddMagic(1369,20) --15x
	--AddMagic(1384,20)--15x



	--AddMagic(210,1)
	
	
	--AddItem(4,353, 1, 1, 1,0);
	--nTranLevle = 80;
	--AddReBorn(80,nTranLevle)---ÏÈÉèÖÃ×ªÉúµÄµÈ¼¶
   
	--SetLevel(80)       ---ÉèÖÃµÈ¼¶Îª1
	
	--Talk(1,"","B¹n ®· sö dông <c=yellow>HaveMagic(272)<c>,: "..HaveMagic(372)..". AddReBorn: "..GetReBorn().."_ "..nReBornNum..". ");
	
	--SetPK(10);
	--Talk(1,"","B¹n ®· sö dông <c=yellow>Th­ ®Æc x¸ triÒu ®×nh<c>, gi¸ trÞ PK hiÖn t¹i cña b¹n lµ "..GetPK()..". ");
		
		
	--DelMagic(717);
	--AddMagic(717,1);
	--AddMagic(445,1);		
	
	
	--AddGoldItemID(MATH_Random(168,176),random(0,4),1,5,0,1)

	--AddMagic(419, 50)
	--AddMagic(424, 50)
	
	--SetTask(TASK_RESET_1, 0)	
		--SetTask(TASK_RESET_1, MATH_SetBit(1,GetTask(TASK_RESET_1),4,1))
		
			--nTaskValue = MATH_GetBit(1,GetTask(TASK_RESET_1),3) - MATH_GetBit(1,GetTask(TASK_RESET_1),4)
			--if (nTaskValue > 1) then
			--	Talk(1,"","h«m nay ®· tham gia ®ñ sè lÇn")
			--	Msg2Team("h«m nay ®· tham gia ®ñ sè lÇn")
			--return end
	
					--		nTaskValue2 = MATH_GetBit(1,GetTask(TASK_RESET_1),3)
					--	nItem = MATH_GetBit(1,GetTask(TASK_RESET_1),4)
					--	if (nTaskValue2 > 1) then
					--	--	SetTask(TASK_RESET_1, MATH_SetBit(1,GetTask(TASK_RESET_1),4,nItem-1))
					--	else
						--	SetTask(TASK_RESET_1, MATH_SetBit(1,GetTask(TASK_RESET_1),3,nTaskValue2+1))
					--	end
	
				--		nTaskValue = MATH_GetBit(1,GetTask(TASK_RESET_1),3)
				--		nItem = MATH_GetBit(1,GetTask(TASK_RESET_1),4)
						--if (nTaskValue > 1) then
						--	SetTask(TASK_RESET_1, MATH_SetBit(1,GetTask(TASK_RESET_1),4,nItem-1))
						--else
						--	SetTask(TASK_RESET_1, MATH_SetBit(1,GetTask(TASK_RESET_1),3,nTaskValue+1))
						--end
	
					--	Msg2Player("  nTaskValue: "..nTaskValue.."  nItem: "..nItem.."  ");




	for i=1,50 do
	local tbProp = {1,2,0,5,0,0};
	--ItemIndex = AddItem(unpack(tbProp));
	end
	
	--VARV_BOARD = 3
	--VARV_BATCHSTATE = 4
	--VARV_BATCH = 5
	--local batch = GetMissionV(VARV_BATCH);
	--SetMissionV(VARV_BATCH, 27);

	
	
	
	
	
	
	
	--local nTotalTask = GetTask(TASK_RESET_3)
	--local nTaskValue = MATH_GetBit(1,nTotalTask,7)	
	--Msg2Player("nTaskValue: "..nTaskValue.."  nTotalTask: "..nTotalTask.." ")
	--SetTask(TASK_RESET_3, MATH_SetBit(1,nTotalTask, 7, 0))

	--local i = 11;
	--AddItem(AWARD_ITEM[i][1],1,AWARD_ITEM[i][2],1,0,0)

	--for i=1,1 do
	--	AddItem(2,1,131,100,0,0);
	--	AddItem(2,1,131,100,1,0);
	--	AddItem(2,1,131,100,2,0);
	--	AddItem(2,1,131,100,3,0);
	--	AddItem(2,1,131,100,4,0);
	--end
	
	

	--local i = MATH_Random(1,11)
	--AddItem(AWARD_ITEM[i][1],1,AWARD_ITEM[i][2],1,0,0)
	
	--SetMSGroup(1); --add by tuanln
	--SetMissionS(1, GetName());
	
	--for i = 1,10 do
	--	local result ="";
	--	local name, ucGroup, data = GetMSLadder(1, i);
	--	if (name == nil) then
	--		name = "unknow";
	--	end
		
	--	Msg2Player("func_npc_getname: "..name.." i:"..i.." ");
	--end

	
	--AddMagic(419, 50)
	--AddMagic(424, 50)
	
	--NewWorld(123,50203/32,103868/32)

	--AddFusionItem(10,10)

	--AddGoldItemID(3487,random(0,4),9,10,0,0)
	
	--AddItem(2,1,132,90,4,0);
	
	
	--AddEventItem(458)
	--DelItem(460);
	--	Msg2Player("   HaveItem  ("..HaveItem(460)..")   ");
	--AddGoldItem(177)	--Kh«i
	--AddGoldItem(178)	--ao 
	--AddGoldItem(179)	--day chuyen
	--AddGoldItem(180)	--nhan 1
	--AddGoldItem(181)	--®¸i
	--AddGoldItem(182)	--bao tay
	--AddGoldItem(183)	--Ngäc boi
	--AddGoldItem(184)	--giay
	--AddGoldItem(185)	--nhan 2
	
	--AskClientForNumber("OnEnterKey", "Vui lßng nhËp sè l­îng", 0, 256, "null")

	
		--	if(GetSex() == 0) then
		--		AddItem(0,7,2,1,4,0,0)
		--	Msg2Player("NhËn ®­îc mét chiÕc mò.")
		--	else
		--		AddItem(0,7,8,1,4,0,0)
		--	Msg2Player("NhËn ®­îc mét chiÕc tr©m.")
		--	end
	--for i = 1020,1026 do
	--SetTask(i,123456)
	--Msg2Player("__________ "..i..": "..GetTask(i).."___________");
	--end
	
	--SetTask(TASK_DATAU_NUM,50000)
	
	
	--TASK_RESET_2 = 1025;
	
	--SetTask(TASK_RESET_2,MATH_SetBit(3,GetTask(TASK_RESET_2),1,0))
	
	--AddMagic(630,20)
	
	--SetExBox(GetExBox()+1);
	--Msg2SubWorld("GetExBox()  "..GetExBox().."    oooooooooo(:01)")
	
	--AddEventItem(182)
	--Msg2SubWorld("HaveItem(182)  "..HaveItem(182).."    oooooooooo(:01)")
	--DelItem(182)
	
			--Talk(1,"","§éng §×nh hå nµy cßn ®­îc gäi lµ 'V©n Méng Tr¹ch', phÝa B¾c gi¸p Tr­êng Giang, Nam gi¸p bèn con s«ng T­¬ng, T­, Nguyªn, Phong, danh hiÖu lµ 'B¸t B¸ch Lý §éng §×nh Hå'. ")
		--elseif (i == 1) then
	
	--Talk(2, "", "§©y ch¼ng ph¶i lµ ngäc béi cña con l·o? LÏ nµo?lÏ nµo? huhuhu..., con cña l·o chÕt th¶m qu¸, thö hái mét bµ giµ nh­ l·o sÏ sèng sao ®©y??",
	--"C¶m ¬n ng­¬i ®· gióp ta t×m ®­îc miÕng ngäc béi nµy, nh×n nã ta cã c¶m gi¸c con trai ta ®ang ë bªn c¹nh! Bøc th­ ph¸p nµy ta tÆng cho ng­­¬i. Huhuhu??")
	
	--AddItem(4,118,1,0,0,0)
	
	--SetTask(TASK_DIADOCHI, MATH_SetBit(3,GetTask(TASK_DIADOCHI),2,0))
	--Msg2SubWorld("MATH_SetBit  Map: "..MATH_GetBit(3,GetTask(TASK_DIADOCHI),1).." soluong: "..MATH_GetBit(3,GetTask(TASK_DIADOCHI),2).."-"..MATH_GetBit(3,GetTask(TASK_DIADOCHI),3).."  (:01)")	
	
	--AddItem(4,MATH_Random(238,240),1,0,0,0)
	--AddItem(4,353,1,0,0,0)
	
	--AddItem(2,1,MATH_Random(1,10),1,0,0,0,0)--thuoc lac
	
	
	--local nRand = MATH_Random(3)
	--if(nRand == 2) then
	--AddItem(4,353,1,0,0,0)
	--end


	--AddDiemTongKim(-500)


	--Msg2Player("NewRandom: "..DelItemCount(3, 1, 2, 1, 237, 1).."")
	
	

	--AddItem(4,353,1,-1,0,0)	
		--AddItem(4,353,1,1,1,0)	AddItem(4,353,1,1,1,0)	AddItem(4,353,1,1,1,0)	AddItem(4,353,1,1,1,0)	AddItem(4,353,1,1,1,0)
	--Count = CalcItemCount(3,4,353,0,-1)
	
	--AddItem(4,353,1,1,1,0)
	--Count = GetItemCount(3,4,353,0,-1)
	
	
	--if(Count < 5) then
	--	Talk(1,"","GetItemCount: "..Count.." ")
	--return end
	--DelItemCount(3, 5, 4, 353, 0, -1) 
	
	
	
	--DelItemCount(5,4,0,353,-1)
	--local i = random(1,11)
	--AddItem(AWARD_ITEM[i][1],1,AWARD_ITEM[i][2],1,0,0)
	--AddItem(2,1,187,1,0,0); -- Lenh Bai GM
	
	--SetLevel(80)
	
	---SetTask(1021,1)	
	--SetTask(1030,19)	
	--SetTask(1020, 2816)
	
	--local nYr, nMth, nDay, nHr, nMi, nSec = GetTimenow()
	--Msg2Player(format("nYr: %d, nMth: %d, nDay: %d, nHr: %d, nMi: %d, nSec: %d",nYr, nMth, nDay, nHr, nMi, nSec))

	--AddGlobalCountNews("TrËn ®¸nh Tèng Kim h×nh thøc "..GetMissionName(11).." ®ang hÕt søc c¨ng th¼ng, tr­íc m¾t ®ang ë giai ®o¹n b¸o danh, nh÷ng ai muèn tham chiÕn xin h·y nhanh chãng ®Õn T­¬ng D­¬ng hoÆc Chu Tiªn trÊn ®¨ng ký b¸o danh; HoÆc sö dông Tèng Kim chiªu th­ ®Ó nhanh chãng ®Õn ®iÓm b¸o danh. §iÒu kiÖn tham gia: ®¼ng cÊp tõ 40. phÝ b¸o danh 3000 l­îng",3);

	--resual = GetMissionName(11);
	--Msg2Player("TrËn ®¸nh Tèng Kim h×nh thøc "..resual.." ", 2)

	--SubWorldName()
	--local w,x,y = GetWorldPos();
    --AddSkillState(541, 1, 1, 108)
  -- local msgfk = format("§¹i hiÖp <c=green> [ %s ]<c> ®· tiªu diÖt <c=yellow>§¹i Thuû TÆc §Çu LÜnh<c>  trªn <c=pink>[ ThuyÒn PLD ], chóc mõng <c> !!!", GetName())
    --Msg2SubWorld(msgfk)
	--MsgToSubWorldMap(w,"ThongBaoMap",msgfk)
	
	--AddItem(2, 1, 131, 0, 0, 0) ---lenh bai gm
	--AddEventItem(36)
	--AddMineItem(147,2,0) --huyen tinh
	--AddMineItem(147,100,0) --huyen tinh
	--for i = 149,154 do AddMineItem(i, 2) end
	--for i = 131,132 do AddMineItem(i,2,2) end
	
	--for i =1, 5 do 
	--AddMineItem(131,0,0)
	--AddMineItem(132,0,0)
	--end
	
	--for i =1, 5 do 
	--AddMineItem(147,1)
	--end
	
	--AddMineItem(162,100,2) 
	--AddMineItem(163,1000,2) 
	--for i = 1,201 do
	--	idx = AddMineItem(147,100
	--,0,0,0,0,0,0,0
	--,2026,10,10,10,10) 
	--end
	--SetItemUseTime(idx,0,0,0,1,0)
	
	--for i = 1,200 do
	--AddMineItem(132,90,0) 
	--end
	--SetFaction("")
	--Msg2Player("Mon phai:"..GetFaction()..".")
	--SetRevPos(68);
	--LocalScript("\\script\\Global\\Station.lua")
	--NewWorld(78, 1592, 3377);

	--AddMagic(723,1)
	--AddSkillState(723, 1, 1, 108)
	--AddSkillState(723, 20, 100, 108)
	
	--AddMagic(368,20)
	--AddMagic(1078,20) --vd
	--AddMagic(1079,20)
	
	--AddMagic(1058,20) --tv
	--AddMagic(1059,20)
	--AddMagic(1060,20)
	
	--AddMagic(1061,20) --nm
	--AddMagic(1062,20)

	--AddMagic(325,21)

	--AddSkillState(717, 20, 100, 108)
	--AddMagic(630,20)

	--nItemIdx = AddItem(2, 1, 199, 1, 0, 0); -- ThÇn Hµnh Phï
	--SetItemUseTimeNew(nItemIdx, 60*24*7)--7 ngay
	--SyncItem(nItemIdx)--Sync hien thi item
	
	--nItemIdx = AddItem(2, 1, 199, 1, 0, 0); -- ThÇn Hµnh Phï
	--nItemIdx = AddItem(0,12,0,14,0,5,0,0)
	--SetItemLock(nItemIdx,-1);
	--SyncItem(nItemIdx)--Sync hien thi item
	--if nItemIdx > 0 then
	--	SetItemUseTimeNew(nItemIdx, 60*24*7)--7 ngay
	--	LockItem(nItemIdx,2);
	--	SyncItem(nItemIdx)--Sync hien thi item
		--SetItemLock(nItemIdx, 2); --khoa vinh vien
		--_w_log_Trade(LOG_STATUS_SUCCESS, "add_item", "NhËn th­ëng giftcode", "PhanThuongGiftCodeOK", 0, nItemIdx, 1);
	--	Msg2Player(format("Chóc mõng b¹n ®· nhËn ®­îc 1 %s (khãa)! ", GetItemName(nItemIdx)));
	--end
 
 	--nIdx,GsNumber = getSerVerInfo();
	--Msg2Player("CurSerIdx: "..nIdx..",nCurGsNumber: "..GsNumber.." ");
		
	
		--local nItemIdx = AddItem(2,1,199,1,0,0); -- Lenh Bai Tan Thu ---ThongJx*0347058065
		--SetItemLock(nItemIdx); --khoa vinh vien

		--if CalcItemCount(-1,2,1,199,-1) == 0 then
		--	idx = AddMineItem(147,1)
			--local nItemIdx = AddItem(2,1,199,1,0,0); -- Lenh Bai Tan Thu ---ThongJx*0347058065
			--SetAndSycItem(nItemIdx, -1, 1, 1, -1, -1, -2, 0); -- Khaa, phUm t¾t
		--end
	
	
	--	idx = AddMineItem(147,100
	--,0,0,0,0,0,0,0
	--,2026,10,10,10,10) 
	--end
	--SetItemUseTime(idx,0,0,0,1,0)
	
	--DelMagic(717)	
	--AddMagic(717,20)
	
	--DelMagic(1075)	
	
	--nSWID, nRevID = GetPlayerRev();
	--nCityIndex = GetTaskTemp(101);
	
	--SetRevPos(1,1);
	
	--AddMineItem(165, 1, 0)
	--AddMineItem(162, 1, 100)
	
	--for i = 3175,3184 do 
	--AddGoldItem(i);
	--end
	
	--for i = 3065,3074 do -- thuy yen
	--AddGoldItem(i);
	--end
	
	--AddItem(0,12,0,14,0,5,0,0) -- phi phong gm
	
	--AddItem(0, 2, 15, 2, 0, 0)

	--for i = 0,15 do
	--AddItem(0,12,0,i,0,2,0,0)
	--end
	
	
	--Msg2SubWorld("aaaaaa aaaaa aaaaaaa aaaaaa aaaaaaaaa aaaaaaaaaaa aaaaaaaa aaaaaaaaaaaa aaaa aaaaaaa")
	
	
	--Msg2Player("SWID: "..nSWID.." nSWID: "..nSWID.." zaaa")
--	local W,X,Y = GetWorldPos();
--	local nNpcIdx = AddNpc(414,95,SubWorldID2Idx(W), X * 32, (Y +  5)* 32, 8 , "TestDame", 0,0);
--			if nNpcIdx > 0 then
--				SetNpcSeries(nNpcIdx, random(0,4))
--				--SetNpcScript(nNpcIdx, BOSTIEU_DEATH) --- duong dan boss chet
--				SetNpcParam(nNpcIdx, 1, 4)
--				SetNpcLiveTime(nNpcIdx,30,0,SubWorldID2Idx(mapid),1);
--				IsBoss(nNpcIdx,2)
--			end

	--local nItemIdx = AddItem(0, 2,3, 10, 1, 100, 79, 54,90,33,46,64,0, 0, 6);
	--nNpcIndex =  PlayerIndex
	--DropItem_map(nNpcIndex, AddItem(2, 1, 131, 1, 0, 0) ) --sat thu lenh
--	local w,x,y = GetWorldPos();
--	local nItemIdx = DropItem_map(SubWorldID2Idx(w), x, y, nNpcIndex, 2, 1, 131, 1, 0, 0, 0, 0, 0, 0, 0, 0);
	--DropOneItem(nNpcIndex,2, 1, 131, 1, 0, 0,1)
	--SyncItem(nItemIdx);
	--AddItem(2, 1, 131, 1, 0, 0)
	--AddItem(6, 1, 1480, 0, 0, 0)
	--AddItem(4, 5, 1, 1,  0, 0) -- sat thu lenh
end

function tb_LocalScript()
	local r1 = LocalScript("\\script\\item\\baowubox.lua")
	local r2 = LocalScript("\\script\\system\\qh_bothu.lua")
	Msg2Player("[TEST36] LocalScript baowubox="..tostring(r1).." qh_bothu="..tostring(r2))
	--local scripts1 = "\\script\\mineitem\\tasklink_goods.lua";
	--local scripts2 = "\\script\\mineitem\\tasklink_goods_secret.lua";	
	--local scripts1 = "\\script\\Global\\seasonnpc.lua";
	--local scripts1 = "\\script\\mineitem\\pack.lua";
	--local scripts1 = "\\script\\subject\\hoang_kim\\m_macsau.lua";
	
	--local scripts1 = "\\script\\subject\\hoang_kim\\macsau.lua";
	--local scripts1 = "\\script\\mineitem\\tieuthanhbikip90.lua";

	--local scripts1 = "\\script\\mineitem\\collectmeat.lua";
	--Msg2Player(scripts1)
	--LocalScript(scripts1)	
	--Msg2Player(scripts2)
	--LocalScript(scripts2)	
	--dofile("script/Global/npcchucnang/thanbithuongnhan.lua");


	--Msg2Player(scripts2)	--LocalScript("\\script\\missions\\ÈÎÎñ\\Ò°ÛÅ¶Ô»°.lua")
	--LocalScript(scripts2)	
	--LocalScript("\\script\\missions\\ÈÎÎñ\\Ò°ÛÅ¶Ô»°.lua")
	--LocalScript("\\script\\missions\\ÈÎÎñ\\Ò°ÛÅ¶Ô»°Í·ÎÄ¼þ.lua")
	--LocalScript("\\script\\global\\seasonnpc.lua");
	
	--LocalScript("\\script\\global\\Station.lua");
end

function fixloitrikinhnghiem()
	local n_level = GetTask(1033);
	local n_exp = GetTask(2574) * 1e5 + GetTask(1034);
	--Msg2Player("n_level: "..n_level.."  n_exp: "..n_exp.."   ")
	SetTask(1027,5)
	
	local nCurExp = GetExp()
	SetTask(1033, GetLevel())
	SetTask(2574, floor(nCurExp / 1e5))
	SetTask(1034, mod(nCurExp, 1e5))
	Msg2Player(" da fix loi da tau xong ")
	--Msg2Player("SetTask(1033): "..GetTask(1033)..", GetTask(2574): "..GetTask(2574)..", SetTask(1034): "..GetTask(1034).." ")
end


function tb_NWGM()
	POSITION_ARRAY={
	{78,42878,106214},--78_name=T­¬ng D­¬ng
	{37,45312,113152},--37_name=BiÖn Kinh
	{1,53760,88576},--pt
	{125,53680,98949},--luutien
	{123,51478,102982},--laoho
	{9,73241,184375}--truonggiang
	};

	NewWorld(37,45312/32,113152/32)--tu den vÞ trÝ boss sat thu
	
end






function main(szIiemName,snGsName,inIdx,inMgID,inGenre,inDetail,inParticular,inStackNum,inItemX,inItemY,inNulla,inNullb)
local nidx = tonumber(inIdx)
	dofile("script/mineitem/gmroleitem.lua");
	
	--AddItem(4,6,1,0,0,0)---vat pham nhanh
	local nW, nX, nY = GetWorldPos()
	local w,x,y = GetWorldPos();
	local serIdx, gsNumber = getSerVerInfo()
	local offline,online = GetPlayerCountOffLive();
	local nIdPlay = PlayerIndex
if (CHECKGM()==1)  then	
	local tbOptions = {
		--"Test_gm/tbTest_GM",
		--"New_World/tb_NWGM",
		"Admin Qu¶n Lý 1/main_chucnang",
		"Admin Qu¶n Lý 2/system",
		"ReloadScript GM V2-NAPNONG/tb_LocalScript",
		"NhËn C¸c Lo¹i §iÓm/tb_CacLoaiDiem",
		--"Command GM/GMDOSTRING",
		--"Reload /_wgm_ReloadScript",
		--"LB-PLD /tbLB_PLD",
		--"Admin Qu¶n Lý/ChucNangAdmin",
		--"Admin Qu¶n Lý/system",
		--"LÊy Item Theo ID/tbLay_Item",
		--"Test Boss Timer/tbCall_BossTmer",
		--"Test Cäc Gç/Goi_CocGo",
		"Goi npc test/Goi_NpcTest",
		--"Test Boss TiÓu/GoiBoss_Tieu",
		--"Test Rot VP/tbRotVP",
		--"Test Boss/tbGoiBosT",
		--"Test 100 boss/GoiBossDai",
		--"Test 100 boss/mainBossDai",
		--"SkillGM /SkillGM",
		"SetFightState /tbSetPK",
		"Qu¶n Lý Server /tbQuanLySv",
		--"LÖnh Bµi Boss /LenhBaiBoss",
		"§æi mµu - PK - Hç trî GM/doimauphe",		
		
		-- "TEST/TEST1",
		-- "MOVE /TEST2",
		-- "Write /TEST3",
		-- "Items /items",
		-- "TK Read/readfile",
		-- "Ba lang huyen /balanghuyengo",
		--"Vuot Ai  30/ai30",
		-- "Point /points",

		
		--"NPC /HOATDONG",
		-- "CreateNPc /TAONPC",
		-- "ITEM /TEST2",
		-- "Dialog /TEST3",
		-- "OpenMission /TEST4",
		-- "CloseMission /TEST5",
		-- "Reload /TEST6",
		
		--"ReloadScript /ReloadScript",
		
		-- PLD
		-- "Dialog - PLD/DialogPLD",
		-- "Reload - PLD/ReloadPLD",
		-- "GetrPOS - PLD/PosPLD",

		--"Call player/callallplayer",
		
		-- VUOT AI
		-- "Tham gia VA/ThamGiaVuotAiKhongChet",
		-- "Reload VA/ReloadScriptVuotAi",
		"Reset sè lÇn v­ît ·i/tbCall_SatThu",
		"Open C¸c TÝnh N¨ng Game/tbOpenMissionGame",
		--"Open Cau ca/MoVuotAi",
		--"Close Cau ca/TatVuotAi",
		--"AddTieuXa/batdau",
		--"T×m Xe Tiªu/timxe",
		"§ãng. /no"
	};
	SayNew("ID:"..nIdPlay.." \n GsNumber: ("..gsNumber..") Online/offline: <c=green>"..online.." - "..offline.."<c> [HiÖn §ang cã: "..GetPlayerCountInMap(w).." Online! \n Trong Map ID Map:<c=red> "..w.."<c>]\n Täa §é: <c=red>"..x.."/"..y.."<c> \n  X/Y*32: <c=red>"..floor(x*32).."/"..floor(y*32).." - "..floor(x/8).."/"..floor(y/16).." - "..floor(x/8*8).."/"..floor(y/16*16).."\r \n  ", getn(tbOptions), tbOptions);
	else
	RemoveItemByIndex(nidx);
	Msg2Player("Nguoi khong phai la nguoi quan tri vien");
	end
end;


function tbOpenMissionGame()
	local tbOptions = {
		"Open   - Phong L¨ng §é/OpenPLD",
		"Close  - Phong L¨ng §é/ClosePLD",
		"Open   - Vuot ai/OpenVA",
		"Close  - Vuot ai/CloseVA",
		"Open   - Tèng Kim/songjin",
		"Close  - Tèng Kim/endsongjin",
		"Open   - Hat Huy Hoµng/addhhh",
		"Open   - Liªn §Êu/OpenLienDau",
		"Close  - Liªn §Êu/CloseLienDau",
		"Goi Boss - TiÓu/releasebosstieu",
		"Trang tr­íc. /main",
		"§ãng. /no"
	};
	Say("Xin mêi lùa chän Open NhiÖm Vô OpenMissionGame  ", getn(tbOptions), tbOptions);
	return 1;
end;

function tb_CacLoaiDiem()
	local tbOptions = {
		"NhËn CÊp §é/tb_Capdo",
		"C¸c Lo¹i §iÓm /tbCacLoai_Diem",
		"NhËn Kü N¨ng 15x/tb_KyNang15x",
		"Trang tr­íc. /main",
		"§ãng. /no"
	};
	Say("Xin mêi lùa chän C¸c lo¹i ®iÓm !", getn(tbOptions), tbOptions);
	return 1;
end;

function tbXacNhanItem(inputString, null, null)
	Msg2Player(inputString)
end




function tbLay_Item()
	local tbOptions = {
		--"AddItem(SL,gare,detai,prti,ser,lv)/tbLay_AddItem",
		--"AddItemMine/tbLay_AddItemMine",
		--"B¶o r­¬ng Online 30p/#AddItemTest(200,298)",
		"B¶o r­¬ng LÔ VËt V­ît ¶i/#AddItemTest(200,209)",
		"B¶o R­¬ng - §ång/#AddItemTest(200,224)",			
		"B¶o R­¬ng - B¹ch Kim/#AddItemTest(200,225)",
		"B¶o R­¬ng - Hoµng Kim/#AddItemTest(200,226)",			
		"§ãng. /no"
	};
	Say("Vui lßng chän ID lÊy Item !", getn(tbOptions), tbOptions);
	return 1;
end;

function tbLay_AddItem()
    AskClientForString("tbXacNhanItem", "AddItem(SL,gare,detai,prti,ser,lv)", 0, 256, "null")
end

function tbXacNhanItem(szInput)
	local tbData = split(szInput, ",")
   --if tbData[1] == "1" then
    --    Talk(1, "", "Du lieu khong hop le")
   --else
   for i = 1,tonumber(tbData[1]) do
        AddItem(tonumber(tbData[2]), tonumber(tbData[3]), tonumber(tbData[4]),tonumber(tbData[5]), 0,  0)
	end
		--AddItem(4,240,1,0,0,0)
	--end
		Msg2Player("AddItem: "..szInput.." !")
end

function tbLay_AddItemMine()
    AskClientForString("tbXacNhanItemMine", "AddMine(SL,ID)", 0, 256, "null")
end

function tbXacNhanItemMine(szInput)
	local tbData = split(szInput, ",")
	local Ser,Lv;
	Ser = tonumber(tbData[3]);
	Lv  = tonumber(tbData[4]);
	if Ser == nil then
		Ser = 0
	end
	if Lv == nil then
		Lv = 0
	end	
    AddMineItem(tonumber(tbData[2]), Ser, Lv, tonumber(tbData[1]))
	Msg2Player("AddMineItem: "..szInput.." x"..tbData[1].." !")
end

function AddItemTest(null, szInput)
	local tbData = split(szInput, ",")
    AddMineItem(tonumber(tbData[2]), Ser, Lv, tonumber(tbData[1]))
end


function tb_Capdo()
		--if (GetLevel() < 150) then
		--	while (GetLevel() < 150) do
		--	AddOwnExp(90000000)
		--	end
		--end
    AskClientForNumber("tb_CapdoXacNhan", "Nhap Cap Do", 1, 200, "null")
end
function tb_CapdoXacNhan(szInput)
	SetLevel(szInput);
end


function DoTaskYes_main()
	Msg2Player("aaaaaaaaaaaaaaaaaaaaaaaaa")
end

function tbCall_SatThu()

	for i=1,GetPlayerCount() do
		gmidx=PlayerIndex
		PlayerIndex=i
		
		SetTask(T_NHANNVSTHU, 0)
		SetTask(T_LOAIBOSS, 0)
		SetTask(TASK_RESET_1, MATH_SetBit(1,GetTask(TASK_RESET_1),3,0))
		Msg2Player("da reset so lan vuot ai xong")
		
		PlayerIndex=gmidx
		
		Msg2Player("da reset toan bo sv so lan vuot ai xong")
	end
end

function tbCall_BossTmer()
	local W,X,Y = GetWorldPos();
	local nMapId = W;
	local nNpcIdx = AddNpc(414,95,SubWorldID2Idx(W), X * 32, (Y +  5)* 32, 8 , "TestDame", 0,0);
			if nNpcIdx > 0 then
				SetNpcSeries(nNpcIdx, random(0,4))
				SetNpcScript(nNpcIdx, BOSTIEU_DEATH) --- duong dan boss chet
				SetNpcParam(nNpcIdx, 1, 4)
				SetNpcLiveTime(nNpcIdx,30,0,SubWorldID2Idx(mapid),1)
			end
end

function tbNhanCapTestCapOK(nSoCap,null,null)
	SetLevel(nLevel); -- §¼ng cÊp 150
end

function tbCall_BossTest(nSeri,null,null)
		local W,X,Y = GetWorldPos();
		local nMapId = W;
		local nNpcIdx = AddNpc(414,95,SubWorldID2Idx(W), X * 32, (Y +  5)* 32, 8 , "TestDame", 0,0);
				if nNpcIdx > 0 then
					SetNpcSeries(nNpcIdx, nSeri)
					SetNpcDeathScript(nNpcIdx,BOSTIEU_DEATH);
					SetNpcScript(nNpcIdx, BOSTIEU_DEATH) --- duong dan boss chet
					--LoldDropRate(nNpcIdx,BOSTIEU_DROP)---duong dan rot vat pham
					SetNpcCurlife(nNpcIdx,90000,90000)---mau boss min, max
					SetNpcItemCount(nNpcIdx,30) -----vat pham rot 30
					--SetNpcCurDefend(nNpcIdx,1,1)---khang min, max
					SetNpcResist(nNpcIdx,1)
					--SetSetNpcExper(nNpcIdx,30000,1)---kinh nghiem
					-- SetNpcParam(nNpcIdx, 0, 1); --boss truong tuyen set 1
				end
end


function Goi_NpcTest()	
	for i = 1,20 do
		local W,X,Y = GetWorldPos();
		local nMapId = W;	--	740																	--Loai boss
		local nNpcIdx = AddNpc(565,95,SubWorldID2Idx(W), (X +  random(1,20))* 32, (Y +  random(1,20))* 32, 0, "Virus corona", 0,0);
				if nNpcIdx > 0 then
					SetNpcLiveTime(nNpcIdx, 5, 0, SubWorldID2Idx(W), 1);
					SetNpcSeries(nNpcIdx, random(0,4))
					SetNpcDeathScript(nNpcIdx,BOSTIEU_DEATH);
					SetNpcScript(nNpcIdx, BOSTIEU_DEATH) --- duong dan boss chet
					--LoldDropRate(nNpcIdx,BOSTIEU_DROP)---duong dan rot vat pham
					--SetNpcCurlife(nNpcIdx,900000000,900000000)---mau boss min, max
					SetNpcItemCount(nNpcIdx,30) -----vat pham rot 30
					SetNpcCurDefend(nNpcIdx,350,350)---khang min, max
					--SetSetNpcExper(nNpcIdx,30000,1)---kinh nghiem
					--SetNpcParam(nNpcIdx, 0, 1); --boss truong tuyen set 1
				end
	end
end

function Goi_CocGo()
local tbOptions = {
		"HÖ Kim/#tbCall_BossTest(0)",
		"HÖ Méc/#tbCall_BossTest(1)",
		"HÖ Thuû/#tbCall_BossTest(2)",
		"HÖ Ho¶/#tbCall_BossTest(3)",
		"HÖ Thæ/#tbCall_BossTest(4)",
		"§ãng. /no"
	};
	Say("GM Online : <c=yellow>"..GetPlayerCount().." ng­êi! <c> Mêi b¹n ngò hµnh ", getn(tbOptions), tbOptions);
	return 1;
end

DROPRATEBOSSLB = "\\script\\tnlteam\\boss_lenhbai\\drop.lua"
DEATHFILE_BOSSLB = "\\script\\tnlteam\\boss_lenhbai\\death.lua"



BOSTIEU_DEATH = "\\script\\tnlteam\\boss_tieu\\death.lua"
BOSTIEU_DROPX = "\\script\\tnlteam\\boss_tieu\\drop.lua"

function GoiBoss_Tieu()
	--for i = 1, 100 do	
	for i = 1, 1 do	
		local W,X,Y = GetWorldPos();
		local nMapId = W;		--724
		local nNpcIdx = AddNpc(523, 95 , SubWorldID2Idx(W), X * 32, (Y +  5)* 32, 8 , "BOSS TiÓu", 0 , 0);
				
						SetNpcSeries(nNpcIdx, 1)
						SetNpcScript(nNpcIdx, BOSTIEU_DEATH) --- duong dan boss chet
						--LoldDropRate(nNpcIdx,BOSTIEU_DROPX)---duong dan rot vat pham
						--SetNpcCurlife(nNpcIdx,3000,3000)---mau boss min, max
						--SetNpclife(nNpcIdx,3000,3000)---mau boss min, max
						--SetNpcItemCount(nNpcIdx,30) -----vat pham rot 
						SetNpcCurDefend(nNpcIdx,1,1)---khang min, max
						SetNpcResist(nNpcIdx,1)
						SetSetNpcExper(nNpcIdx,1,1)---kinh nghiem
						
	end
	Msg2Player("Gäi thµnh c«ng Boss TiÓu")
	-- SetNpcParam(nNpcIdx, 0, 1); --boss truong tuyen set 1
end



function tbSetPK()
	SetFightState(1);
end


function tbLB_PLD()
	AddItem(2, 1, 3363, 10, 0, 0)
	AddItem(6,1,3363,0,0,0)
	--AddItem(4,489,0,0,0,0)
end



function mainBossDai()
	
	--dofile("script/item/ib/lbbosstruongtuyen.lua")
	local nLevel= 10
	local ForbiddenMap = {44, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 326, 327, 328, 329, 330, 331, 334, 335, 337, 338, 339, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374}
	--local GoldenBoss = {{538, "Tr­¬ng Tuyªn", 5,12},}
	local GoldenBoss = {{523, "LiÔu Thanh Thanh", 5,12},}
	local bosspro = {};
	local W,X,Y = GetWorldPos();
	local nMapId = W;
	local nn_NameMaps=Getn_NameMaps(nMapId)
	if ( GetFightState() == 0 ) then	
		Msg2Player("§ang ë trong tr¹ng th¸i phi chiÕn ®Êu kh«ng thÓ sö dông");
		return
	end

	--if %checkOnlyUseInMap() ~= 1 then
	--	Msg2Player("Kh«ng thÓ sö dông vËt phÈm nµy t¹i ®©y.")
	--	return
	--end

	--for i = 249, 318 do	--Ï´ËèµºÉ½¶´
	--	if ( i == nMapId ) then
	--		Msg2Player("N¬i ®©y kh«ng thÓ sö dông vËt phÈm nµy ");
	--		return
	--	end
	--end

	--for i = 375, 415 do	--ÐÂÔöËÎ½ðÕ½³¡µØÍ¼ ËÍÐÅÈÎÎñµØÍ¼ ±ÈÎä´ó»áµØÍ¼
	--	if ( i == nMapId ) then
	--		Msg2Player("N¬i ®©y kh«ng thÓ sö dông vËt phÈm nµy ");
	--		return
	--	end
	--end

	--for i = 1, getn( ForbiddenMap ) do		--ÌØÊâµØÍ¼½ûÓÃ
	--	if( ForbiddenMap[i] == nMapId ) then
	--		Msg2Player("N¬i ®©y kh«ng thÓ sö dông vËt phÈm nµy ");
	--		return
	--	end
	--end

	for i = 1, getn(GoldenBoss) do
		bosspro[i] = GoldenBoss[i][4];
	end

	local doubleodds = 160 - (nLevel - 1) * 10
	local j = 1;
	if( random(1,doubleodds) == 1) then
		j = 20;
	end

	for k = 1, 10 do
		local numth = randomaward(bosspro);
		local nNpcID = GoldenBoss[numth][1];
		local GoldenBossName = GoldenBoss[numth][2];
		local GoldenBossSeries = GoldenBoss[numth][3];	
		local fkBossType = 8
		if (GoldenBossSeries == 5) then --random he boss close by tuanln
			GoldenBossSeries = random( 0, 4);
		end
		local npcindex = AddNpc(nNpcID, 95 , SubWorldID2Idx(W), X * 32, (Y +  5)* 32, fkBossType , GoldenBossName, 0 , 0);
		SetNpcSeries(npcindex, GoldenBossSeries)
		--Set cac thong tin suc manh, khang, mau bosss
		local mauBosss = 3000000
		local khangbossmin = 75
		local khangbossmax = 95
		local thoigianbosss = 400
		local damageboss = 10--1000
		SetNpcCurlife(npcindex,mauBosss,mauBosss)
		SetNpcCurDefend(npcindex, khangbossmin, khangbossmax)
		-- SetNpcTime_TGPH_TD_C_CH(npcindex, 1, thoigianbosss) --thoi gian phuc hoi
		-- SetNpcTime_TGPH_TD_C_CH(npcindex, 2, thoigianbosss)--thoi gian lam cham
		-- SetNpcTime_TGPH_TD_C_CH(npcindex, 3, thoigianbosss)--thoi gian trung doc
		-- SetNpcTime_TGPH_TD_C_CH(npcindex, 4, thoigianbosss)--thoi gian lam choang
		--SetNpcDropScript(npcindex, DROPRATEBOSSLB);
		--LoldDropRate(nNpcIdx,DROPRATEBOSSLB)
		SetNpcScript(npcindex, DEATHFILE_BOSSLB);
		SetNpcParam(npcindex, 0, 1); --boss truong tuyen set 1
		local msgfk = "T¹i "..nn_NameMaps.." ng­êi ch¬i <c=pink> "..GetName().."<c> ®· gäi ra Boss : <c=green>"..GoldenBossName.. "<c>\t\n";
		--Msg2SubWorld(msgfk);
		--AddGlobalNews(msgfk);
		_w_log_Script(LOG_STATUS_SUCCESS, "createboss_truongtuyen", "T¹o boss Tr­¬ng TuyÒn", "main", WLib:Join({0, GoldenBossName, Getn_NameMaps(SubWorldID2Idx(W)), SubWorldID2Idx(W), X * 32, (Y +  5)* 32, 95, fkBossType}, "\t"));
	end
	return 0;
end

function randomaward(aryProbability)
	local nRandNum;
	local nSum = 0;
	local nArgCount = getn( aryProbability );
	local nCompareSum = 0;
	for i = 1, nArgCount do
		nSum = nSum + aryProbability[i];
	end
	nRandNum = random(1,nSum);
	for i = 1,nArgCount do
		nCompareSum = nCompareSum + aryProbability[i]
		if( nRandNum <= nCompareSum) then
			return i;
		end
	end
end

function LenhBaiBoss()
	AddItem(2, 1, 187, 10, 0, 0)
	AddItem(2, 1, 189, 10, 0, 0)
	AddItem(2, 1, 190, 10, 0, 0)
end

function SkillGM()
	AddMagic(968,1);
	AddMagic(970,1);
	AddMagic(971,1);
	AddMagic(972,1);
	AddMagic(973,1);
	AddMagic(974,1);
	AddMagic(975,1);
	AddItem(6, 1, 3701, 10, 0, 0) --lb boss truong tuyen
	--_w_log_Trade(LOG_STATUS_SUCCESS, "add_item", "Mua LB Boss", "MuaLenhBaiBossTT", 0, nItemIdx, 1);
end


function _wgm_ReloadScript()
	LocalScript("\\script\\global\\npcchucnang\\hotrotanthu.lua");
	LocalScript("\\script\\mineitem\\gmroleitem.lua");
end
function callallplayer()
	-- for i = 1, GetPlayerCount() do
	-- 	PlayerIndex = i;
	-- 	-- local a,b,c = GetWorldPos();
	-- 	-- NewWorld(53,1600,3200)
	-- end;
	AddMagic(708, 20)
	AddMagic(709, 20)
	AddMagic(710, 20)
	AddMagic(711, 20)
	AddMagic(712, 20)
	AddMagic(713, 20)
	AddMagic(714, 20)
	AddMagic(715, 20)
	AddMagic(716, 20)
	AddMagic(717, 20)
	-- print(GetMSPlayerCount(10))
end

function  ai30()
	NewWorld(957, floor(51072/32), floor(102272/32))
end

function  balanghuyengo()
	NewWorld(53,1600,3200)
end

function  vuotaigo()
	NewWorld(480, 1559, 3226)
end

function songjin()
	Include("\\script\\tnlteam\\mission\\battlesongjin\\butcher\\head.lua");
	but_battlestart()
			local fkMsg = format("Ho¹t ®éng <c=cyan><Tèng Kim><c> ®· më, mäi ng­êi cã thÓ ®Õn khu vùc B¸o Danh!")
			Msg2SubWorld(fkMsg)
			AddGlobalNews(fkMsg)
end;

function endsongjin()
	Include("\\script\\tnlteam\\mission\\battlesongjin\\butcher\\head.lua");
	but_battleclose()
end;

function OpenLienDau()
	Include("\\script\\tnlteam\\mission\\liendau\\dondau\\head.lua");
	liendau_openmission()
end;

function CloseLienDau()
	Include("\\script\\tnlteam\\mission\\liendau\\dondau\\head.lua");
	liendau_closemission()
end;

function readfile()
	print(GetTabFileInfo("\\settings\\battles\\maps\\narrow\\ºóÓª2trap.txt",1,1));
end;

function items()
	-- for i = 11, 20 do
	-- 	AddItem(2,1,i,1,0,0)
	-- end;

end;

function  reloadthp()
	-- LocalScript("\\script\\mineitem\\ib\\shenxingfu.lua");
	LocalScript("\\script\\missions\\clearskill\\clearhole.lua");
	LocalScript("\\script\\missions\\clearskill\\head.lua");
end

-- Include("\\script\\tnlteam\\mission\\challangeoftime\\head.lua")
--Include("\\script\\tnlteam\\mission\\battlesongjin\\battlehead.lua")
function points()
	LocalScript([[\script\missions\clearskill\clearhole.lua]])
	-- NewWorld(480,1559,3226)
	-- print(GetBang())
	-- print(GetLeadLevel())
	-- for i = 1, 100 do
	-- 	AddLeadExp(99999999)
	-- end;
	-- NewWorld(162,1600,3200)
	-- print(CalcItemCount(3,4,4,1,-1));

	-- print(CalcEquiproomItemCount(2,1,61,-1))

	-- 	BT_BroadView();
	-- BT_BroadAllLadder();
	-- BT_SongJin(1)
	-- BT_ViewBattleStart()
	-- BT_BroadGameData();
	-- BT_SetRestTime(1000);
	-- for i = 1, 48 do
	-- 	BT_SetView(i);
	-- 	BT_SetData(i, i);
	-- 	print(BT_GetData(i))
	-- end;

	-- 		BT_SortLadder();
	-- 		BT_BroadSelf();

	-- ClearMapNpc(SubWorld)
	-- create_all_npc(TAB_NPC_BATCH[4])
	-- create_all_npc(TAB_NPC_BATCH[8])
	-- create_all_npc(TAB_NPC_BATCH[11])
	-- create_all_npc(TAB_NPC_BATCH[13])
	-- create_all_npc(TAB_NPC_BATCH[16])
	-- create_all_npc(TAB_NPC_BATCH[18])
	-- create_all_npc(TAB_NPC_BATCH[21])
	-- create_all_npc(TAB_NPC_BATCH[25])
	-- create_all_npc(TAB_NPC_BATCH[27])
	-- create_all_npc(TAB_NPC_BATCH[28])
	-- local w,x,y = GetWorldPos();
	-- for i = 1, 20 do
	-- 	local npc = AddNpcEx(1019, 1, random(0,4), SubWorld, (x+i)*32, (y+i)*32, 1, "Trung ¨n cøc", -1);
	-- end;
	-- SetNpcDeathScript(npc, "\\script\\tnlteam\\mission\\challangeoftime\\npcdeath.lua");
	-- SetNpcIsRe(npc, -1);
	-- SetnotDeath(PIdx2NpcIdx(PlayerIndex), 1);
	-- SetBasePoint(500,500,500,500);
	-- AddMagicPoint(200);
end;


function PosPLD()
	local a,b,c = GetWorldPos();
	print(a..","..b..","..c);
end;

-- ------------------------------- PLD
function LenhBaiPLD()
	for i = 1, 1 do
		AddItem(4,6,1,0,0,0);
	end;
end;

--Include([[\script\tnlteam\mission\fenglingdu\boatman.lua]]);
function DialogPLD()
	BOATID = 1;
	boatman()
end;

function OpenPLD()
	Include("\\script\\tnlteam\\mission\\fenglingdu\\head.lua")
	fld_start_mission();
			local fkMsg = format("Ho¹t ®éng <c=cyan><Phong L¨ng §é><c> ®· më, mäi ng­êi cã thÓ ®Õn bÕn thuyÒn ®Ó b¸o danh!")
			Msg2SubWorld(fkMsg)
			AddGlobalNews(fkMsg)
end;

function ClosePLD()
	Include("\\script\\tnlteam\\mission\\fenglingdu\\head.lua")
	fld_close_mission();
end;




function ReloadPLD()
	LocalScript([[\script\tnlteam\mission\fenglingdu\timerboard.lua]])
	LocalScript([[\script\tnlteam\mission\fenglingdu\shuizeideath.lua]])
	LocalScript([[\script\tnlteam\mission\fenglingdu\playerdeath.lua]])
	LocalScript([[\script\tnlteam\mission\fenglingdu\npcdeath.lua]])
	LocalScript([[\script\tnlteam\mission\fenglingdu\mission.lua]])
	LocalScript([[\script\tnlteam\mission\fenglingdu\bossdeath.lua]])
	LocalScript([[\script\tnlteam\mission\fenglingdu\head.lua]])
	LocalScript([[\script\tnlteam\mission\fenglingdu\boatman.lua]])
end;




-- Include([[\script\tnlteam\mission\challangeoftime\npcdialog.lua]])
-- function ThamGiaVuotAiKhongChet()
-- 	SetnotDeath(PIdx2NpcIdx(PlayerIndex), 1);
-- 	test_join_mission();
-- end

-- function ReloadScriptVuotAi()
-- 	LocalScript([[\script\tnlteam\mission\challangeoftime\head.lua]])
-- 	LocalScript([[\script\tnlteam\mission\challangeoftime\playerdeath.lua]])
-- 	LocalScript([[\script\tnlteam\mission\challangeoftime\npcdeath.lua]])
-- 	LocalScript([[\script\tnlteam\mission\challangeoftime\npcdialog.lua]])
-- 	LocalScript([[\script\tnlteam\mission\challangeoftime\timerboard.lua]])
-- 	LocalScript([[\script\tnlteam\mission\challangeoftime\mission.lua]])
-- end



--Include([[\script\tnlteam\mission\challangeoftime\head.lua]])
function  OpenVA( )
Include("\\script\\tnlteam\\mission\\challangeoftime\\head.lua")
	start_mission()
	chuangguan30_start_mission()
		local msgfk = ("NhiÖm vô <c=green><V­ît ¶i><c> chÝnh thøc më b¸o danh, h·y t¹o tæ ®éi tèi thiÓu 2 ng­êi vµ ®Õn gÆp NhiÕp ThÝ TrÇn ë c¸c thµnh ®Ó b¸o danh!");
		Msg2SubWorld(format(msgfk));
		AddGlobalNews(msgfk);
end

function  CloseVA()
Include("\\script\\tnlteam\\mission\\challangeoftime\\head.lua")
	close_mission();
end


--Include([[\script\tnlteam\mission\challangeoftime\head.lua]])
function  MoCauCa( )
	start_mission()
	chuangguan30_start_mission()
end

function  TatCauCa()
	close_mission();
end


-- function  TAONPC()
-- 	local idx = PIdx2NpcIdx(PlayerIndex);
-- 	for i = 20429, 20443 do
-- 		KillNpcWithIdx(i,idx);
-- 	end;
-- 	-- create_batch_npc(1);
-- end

function GMDOSTRING()
	OpenStringUI("Command:", "GMDOSTRINGCONF", "GMERROR",5, 2);
end;

function GMERROR()
	Talk(1,"", "ERROR");
end;

function GMDOSTRINGCONF(szCMD)
	dostring(szCMD);
end;


-- function TEST2()
-- 	OpenStringUI("kaka", "TEST2_2", "TEST2_3",255, 1);
-- end;

-- function TEST2_2( str)
-- 	NewWorld(unpack(split(str)));
-- end

-- function TEST1()
-- 	print("\n\n\n\n\n\n\n\n\n\n\n")
-- 	local nStart = 8000;
-- 	for i = nStart,  nStart+2000 do
-- 		if (GetNpcKind(i) ~= 0) then
-- 			local nX,nY,nW, nID = GetNpcPos(i);
-- 			print(i.."  [ "..nID.." ]> "..GetNpcName(i).." - "..nW..","..floor(nX/32)..","..floor(nY/32));
-- 		end;
-- 	end;
-- 	print("\n\n\n")
-- end;

-- function no()
-- end;

-- function  TEST3()
-- 	OpenStringUI("kaka", "TEST3_2", "TEST3_3",99999, 1);
-- end

-- function  TEST3_3()
-- end

-- function TEST3_2(num)
-- 	local nX,nY = GetNpcPos(num);
-- 	logplayer(GetNpcName(num).."-"..SubWorldIdx2ID(SubWorld)..","..floor(nX/32)..","..floor(nY/32));
-- end

-- function logplayer(szMsg)
-- 	local zFile = "Logs/logs.log";
--   local handle = openfile(zFile,"a")
--   write(handle,format("%s\n",szMsg));
--   closefile(handle);
--  end

function tbQuanLySv()
	local tbOptions = {
		"X2 Exp Toµn SV/X2ExpSv",
		"T¾t x2 Exp Toµn SV/X2ExpSvDone",		
		"T¨ng May M¾n toµn sv 5 ®iÓm/LucKySv",
		"T¾t May M¾n toµn sv 5 ®iÓm/LucKySvDone",
		"Trë vÒ trang ®Çu/main",
		"§ãng./NO"
	};
	SayNew("<c=yellow>Hç trî GM<c>: Muèn nhËn ®iÓm nµo? ", getn(tbOptions), tbOptions);
end;

function X2ExpSv()
	SetGlbMissionV(27,1)
	local Msg = format("Server HiÖn t¹i ®ang t¨ng X2 EXP toµn server nÕu dïng Tiªn Th¶o Lé sÏ x3 !"); 
	Msg2SubWorld(Msg);
	AddGlobalNews(Msg,1);
end

function X2ExpSvDone()
	SetGlbMissionV(27,0)
	local Msg = format("Sù kiÖn x2 EXP Toµn server kÕt thóc !"); 
	Msg2SubWorld(Msg);
	AddGlobalNews(Msg,1);
end	

function LucKySv()
	SetGlbMissionV(28,5)
	local Msg = format("Server HiÖn t¹i ®ang t¨ng May M¾n toµn server lµ 5 ®iÓm !"); 
	Msg2SubWorld(Msg);
	AddGlobalNews(Msg,1);
end

function LucKySvDone()
	SetGlbMissionV(28,0)
	local Msg = format("Sù kiÖn t¨ng may m¾n 5 ®iÓm toµn sv kÕt thóc !"); 
	Msg2SubWorld(Msg);
	AddGlobalNews(Msg,1);
end

function doimauphe()
	local tbOptions = {
			"Set GM/setgm",	
			"Mµu tr¾ng      - Tr¾ng/mautrang",
			"Mµu ChÝnh Ph¸i - Vµng/mauvang",
			"Mµu Tµ ph¸i    - Hång/mautim",
			"Mµu Trung lËp  - Xanh/mauxanh",
			"Mµu S¸t Thñ    - §á/maudo",
			"Mµu Hång GM    - GM/mauhong",
			"ChuyÓn tr¹ng th¸i LuyÖn C«ng/luyencong",
			"ChuyÓn tr¹ng th¸i ChiÕn §Êu/chiendau",
			"Tho¸t/no"
			}
	Say("xin mêi chän mµu PK muèn ®æi.", getn(tbOptions), tbOptions);
end

function setgm()
	AddItem(0,12,0,14,0,5,0,0) -- phi phong gm
end
function mautrang()
n = GetCash()
	if GetCash() >= 10000 then
		Pay(10000)
	if GetCash() == n - 10000 then
		SetCurCamp(0)
		SetCamp(0)
		Msg2Player("B¹n ®æi mµu PK Tr¾ng thµnh c«ng.")
	else
	Talk(1,"","§æi mµu thÊt b¹i, b¹n kh«ng ®ñ tiÒn.")
	end
	else
	Talk(1,"","§æi mµu thÊt b¹i, b¹n kh«ng ®ñ tiÒn.")
	end
end


function mauvang()
n = GetCash()
	if GetCash() >= 10000 then
		Pay(10000)
	if GetCash() == n - 10000 then
		SetCurCamp(1)
		SetCamp(1)
		Msg2Player("B¹n ®æi mµu PK ChÝnh Ph¸i thµnh c«ng.")
	else
	Talk(1,"","§æi mµu thÊt b¹i, b¹n kh«ng ®ñ tiÒn.")
	end
	else
	Talk(1,"","§æi mµu thÊt b¹i, b¹n kh«ng ®ñ tiÒn.")
	end
end

function mautim()
n = GetCash()
	if GetCash() >= 10000 then
		Pay(10000)
	if GetCash() == n - 10000 then
		SetCurCamp(2)
		SetCamp(2)
		Msg2Player("B¹n ®æi mµu PK Tµ Ph¸i thµnh c«ng.")
	else
	Talk(1,"","§æi mµu thÊt b¹i, b¹n kh«ng ®ñ tiÒn.")
	end
	else
	Talk(1,"","§æi mµu thÊt b¹i, b¹n kh«ng ®ñ tiÒn.")
	end
end

function mauxanh()
n = GetCash()
	if GetCash() >= 10000 then
		Pay(10000)
	if GetCash() == n - 10000 then
		SetCurCamp(3)
		SetCamp(3)
		Msg2Player("B¹n ®æi mµu PK Trung LËp thµnh c«ng.")
	else
	Talk(1,"","§æi mµu thÊt b¹i, b¹n kh«ng ®ñ tiÒn.")
	end
	else
	Talk(1,"","§æi mµu thÊt b¹i, b¹n kh«ng ®ñ tiÒn.")
	end
end

function maudo()
n = GetCash()
	if GetCash() >= 10000 then
		Pay(10000)
	if GetCash() == n - 10000 then
		SetCurCamp(4)
		SetCamp(4)
		Msg2Player("B¹n ®æi mµu PK S¸t Thñ thµnh c«ng.")
	else
	Talk(1,"","§æi mµu thÊt b¹i, b¹n kh«ng ®ñ tiÒn.")
	end
	else
	Talk(1,"","§æi mµu thÊt b¹i, b¹n kh«ng ®ñ tiÒn.")
	end
end

function mauhong()
n = GetCash()
	if GetCash() >= 10000 then
		Pay(10000)
	if GetCash() == n - 10000 then
		SetCurCamp(5)
		SetCamp(5)
		Msg2Player("B¹n ®æi mµu PK Hång GM thµnh c«ng.")
	else
	Talk(1,"","§æi mµu thÊt b¹i, b¹n kh«ng ®ñ tiÒn.")
	end
	else
	Talk(1,"","§æi mµu thÊt b¹i, b¹n kh«ng ®ñ tiÒn.")
	end
end	

function tbCacLoai_Diem()
	local tbOptions = {
		"TiÒn V¹n/#POINTCONFIRM(1)",
		"TiÒn Xu/#POINTCONFIRM(2)",
		"Phóc duyªn 100/#POINTCONFIRM(3)",
		"Danh väng 100/#POINTCONFIRM(4)",
		"Tµi l·nh ®¹o/#POINTCONFIRM(5)",
		"Tèng Kim 9999/#POINTCONFIRM(6)",
		"Vinh dù 100/#POINTCONFIRM(7)",
		"Kinh nghiÖm 1->10m/#POINTCONFIRM(8)",
		"§iÓm TiÒm N¨ng/#POINTCONFIRM(9)",
		"§iÓm Kü N¨ng/#POINTCONFIRM(10)",
		"§ãng./NO"
	};
	SayNew("<c=yellow>Hç trî t©n thñ<c>: Muèn nhËn ®iÓm nµo? ", getn(tbOptions), tbOptions);
end;
function POINTCONFIRM(null, nPoint)
	if (tonumber(nPoint) == 1) then
		Earn(10000000);
	elseif (tonumber(nPoint) == 2) then
		EarnXu(10000);
	elseif (tonumber(nPoint) == 3) then
		AddFuYuan(100);
		Msg2Player("B¹n nhËn ®­îc 100 ®iÓm <c=green>phóc duyªn<c>! ");
	elseif (tonumber(nPoint) == 4) then
		AddRepute(100);
		Msg2Player("B¹n nhËn ®­îc 100 ®iÓm <c=green>danh väng<c>! ");
	elseif (tonumber(nPoint) == 5) then
		for i = 1, 99 do
			AddLeadExp(179 * 2 * 50 * 60 *  100);
		end;
		Msg2Player("B¹n nhËn ®­îc 99 ®iÓm <c=green>tµi l·nh ®¹o<c>! ")
	elseif (tonumber(nPoint) == 6) then
		AddDiemTongKim(9999)
		Msg2Player("B¹n nhËn ®­îc 9999 ®iÓm <c=green>Tèng Kim<c>! ");
	elseif (tonumber(nPoint) == 7) then
		AddDiemVinhDu(100)
		Msg2Player("B¹n nhËn ®­îc 100 ®iÓm <c=green>Vinh Dù<c>! ");
	elseif (tonumber(nPoint) == 8) then
		local nExpRand = random(1000000,10000000)
		AddOwnExp(nExpRand) --modify exp
		Msg2Player("B¹n nhËn ®­îc "..nExpRand.." ®iÓm <c=green>Exp<c>! ");
	elseif (tonumber(nPoint) == 9) then
		AddProp(1000);
		Msg2Player("B¹n nhËn ®­îc 10000 ®iÓm <c=green>Tiem nang<c>! ");
	elseif (tonumber(nPoint) == 10) then
		--print(ScriptFilePath) --API moi lay duong dan script hien hanh
		AddMagicPoint(1000);
		Msg2Player("B¹n nhËn ®­îc 1000 ®iÓm <c=green>Ky nang<c>! ");				
	end;
end;




function tb_KyNang15x()
	AddMagic(1055,20) --tl
	AddMagic(1056,20)
	AddMagic(1057,20)
	
	
	AddMagic(1058,20) --tv
	AddMagic(1059,20)
	AddMagic(1060,20)
	
	AddMagic(1069,20) --DM
	AddMagic(1070,20)	
	AddMagic(1071,20)	
	
	AddMagic(1066,20) --ND
	AddMagic(1067,20)
	
	
	AddMagic(1061,20) --nm
	AddMagic(1062,20)
	
	AddMagic(1073,20) --cb
	AddMagic(1074,20)
	
	AddMagic(1075,20) --tn
	AddMagic(1076,20)

	AddMagic(1078,20) --vd
	AddMagic(1079,20)
	
	AddMagic(1080,20) --cl
	AddMagic(1081,20)
	
	
	
	AddMagic(1369,20) --15x hoa son
	AddMagic(1384,20)--15x hoa son
	--AddMagic(1364,20) --9x
	--AddMagic(1382,20) --9x
	
	
end

