p='D:/JX-build/qh9A/Classes/gameui/KuiGive_New.cpp'
c=open(p,'rb').read()
open(p+'.bak-vc39','wb').write(c)
old=b'\tPlayer[CLIENT_PLAYER_INDEX].m_ItemList.setLock(Obj.Obj.uId ,0);\r\n'
assert c.count(old)==1,c.count(old)
new=(b'\t{\t//[vc39] go mon khoi o: gui giveback nKind=0 kem m_uId de server tra mon ve tui\r\n'
b'\t\tif (g_pCoreShell)\r\n\t\t{\r\n'
b'\t\t\tPLAYER_GIVEUI pUI1; ZeroMemory(&pUI1,sizeof(pUI1));\r\n'
b'\t\t\tpUI1.uId[0] = Obj.Obj.uId;\r\n'
b'\t\t\tt_sprintf(pUI1.m_Callback,"%s",m_Callback);\r\n'
b'\t\t\tt_sprintf(pUI1.m_Error,"%s",m_Error);\r\n'
b'\t\t\tg_pCoreShell->OperationRequest(GOI_GIVE_ITEM_FAIL,(unsigned long)(&pUI1),1);\r\n'
b'\t\t}\r\n\t}\r\n')
c=c.replace(old,new+old,1)
open(p,'wb').write(c)
print('ok')
