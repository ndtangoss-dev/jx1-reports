--=======================================
--Author: 横刀向天笑 QQ:25557432
--=======================================
Include("\\script\\Global\\全局任务号.lua");
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

--系统调用脚本入口
Include("\\script\\system\\qianghua.lua");  -- dam bao sysqianghua/sysError co trong script callback
function opensysui(inKind,inVala,inValb,inValc)
 
 if (inKind==2) then  --- 打开系统ui
    if (inVala==1) then  --cuong hoa: mo UI Give goc, callback sysqianghua (qianghua.lua)
	   Give("Dat <c=cyan>1 mon trang bi trong tui<c> (xanh/tim/vang) de cuong hoa. Trang bi dang mac: hay thao ra truoc. Ti le: 100-5(n-1)%, that bai chi mat nguyen lieu va bac.(:01)",1,1,"sysqianghua","sysError","Cuong hoa trang bi")
	end
   
 end
 return 1
end