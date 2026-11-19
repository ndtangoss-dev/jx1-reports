--=======================================
--Author: ºáµ¶ÏòÌìĞ¦ QQ:25557432
--=======================================
Include("\\script\\Global\\È«¾ÖÈÎÎñºÅ.lua");
function GetParam(strParam, index)
nLastBegin = 1
for i=1, index - 1 do
nBegin = strfind(strParam, "|", nLastBegin)
nLastBegin = nBegin + 1
end;
num = 1
strnum = strsub(strParam, nLastBegin)
nEnd = strfind(strnum, "|")
if nEnd == nil then 
return strnum
end
str1 = strsub(strnum,1,nEnd -1);
return str1
end;

--ÏµÍ³µ÷ÓÃ½Å±¾Èë¿Ú
Include("\\script\\system\\qhcuonghoa.lua");
function opensysui(inKind,inVala,inValb,inValc)
 
 if (inKind==2) then  --- ´ò¿ªÏµÍ³ui
    if (inVala>=10 and inVala<=12) then QhHandle(inVala,inValb) return 1 end
    if (inVala==1) then  --Ç¿»¯give½çÃæ
	   Give("L­u ı: ChØ cã thÓ ®Æt vµo <c=cyan>1 m¶nh trang bŞ<c> vµ <c=cyan>1 viªn ®¸ c­êng hãa<c> ®Ó c­êng hãa trang bŞ! Nh¾c nhë: <c=orange>c­êng hãa hoÆc h¹ xuèng, b¹n cÇn thËn träng <c>!(:01)(:01)(:01)",1,2,"sysqianghua","sysError","N©ng cÊp trang bŞ")
	end
   
 end
 return 1
end