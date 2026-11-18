# Bản đồ mã nguồn client (tự sinh bởi TOOLS/quet_ma_nguon.py, chỉ đọc)

Mỗi tệp: số dòng, câu chú thích đầu, hàm định nghĩa (tối đa 25), hàm của dự án mà tệp gọi tới (tối đa 15, theo tần suất). "Gọi tới" chỉ khớp theo tên, chưa phân biệt trùng tên.

## `AppDelegate.cpp`
- 229 dòng. #include "gamescene/KgameWorld.h"
- Hàm: `AppDelegate`, `AppDelegate`, `AppDelegate::initGLContextAttrs`, `register_all_packages`, `AppDelegate::applicationDidEnterBackground`, `AppDelegate::applicationWillEnterForeground`
- Gọi tới: `Size`→KFile.cpp, `scene`→KgameWorld.cpp, `create`→KHRocker.cpp, `g_SetRootPath`→KFilePath.cpp, `createScene`→HelloWorldScene.cpp, `Start`→KTimer.cpp

## `AppDelegate.h`
- 67 dòng. (không có chú thích đầu)
- Gọi tới: `AppDelegate`→AppDelegate.cpp, `initGLContextAttrs`→AppDelegate.cpp, `applicationDidEnterBackground`→AppDelegate.cpp, `applicationWillEnterForeground`→AppDelegate.cpp

## `HelloWorldScene.cpp`
- 336 dòng. (không có chú thích đầu)
- Hàm: `HelloWorld::createScene`, `problemLoading`, `drawInRect_temp`, `HelloWorld::init`, `HelloWorld::menuCloseCallback`, `HelloWorld::draw`, `HelloWorld::onTouchesBegan`
- Gọi tới: `create`→KHRocker.cpp, `ccMessageBox_new`→KCore.cpp

## `HelloWorldScene.h`
- 52 dòng. (không có chú thích đầu)
- Gọi tới: `createScene`→HelloWorldScene.cpp, `init`→HelloWorldScene.cpp, `onTouchesBegan`→HelloWorldScene.cpp, `menuCloseCallback`→HelloWorldScene.cpp, `draw`→HelloWorldScene.cpp, `create`→KHRocker.cpp

## `ImageStore/KImageStore2.cpp`
- 754 dòng. 无贴图的图形资源管理
- Hàm: `KImageStore2::ImageNameToId`, `KImageStore2::CreateImage`, `KImageStore2::Free`, `KImageStore2::FreeImage`, `KImageStore2::GetExistedCreateBitmap`, `KImageStore2::GetSprFrame`, `KImageStore2::GetImageParam`, `KImageStore2::GetImagePixelAlpha`, `KImageStore2::Init`, `KImageStore2::SaveImage`, `KImageStore2::SetBalanceParam`, `KImageStore2::CheckBalance`, `KImageStore2::ExpandSpace`, `KImageStore2::FindImage`, `KImageStore2::FreeImageObject`, `KImageStore2::LoadImage`, `KImageStore2`, `KImageStore2`, `KImageStore2::ClearAllAdjustColorPalette`
- Gọi tới: `GetSprFrame`→KPakList.cpp, `CheckBalance`→KNpcSet.cpp, `Free`→KMemClass.cpp, `SprReleaseHeader`→KPakFile.cpp, `SprGetFrame`→KPakFile.cpp, `Init`→KCache.cpp, `SprReleaseFrame`→KPakFile.cpp, `SprGetHeader`→KPakFile.cpp

## `ImageStore/KImageStore2.h`
- 290 dòng. 无贴图的图形资源管理
- Gọi tới: `KImageStore2`→KImageStore2.cpp, `Init`→KCache.cpp, `Free`→KMemClass.cpp, `SetBalanceParam`→KImageStore2.cpp, `CreateImage`→KImageStore2.cpp, `GetExistedCreateBitmap`→KImageStore2.cpp, `FreeImage`→KImageStore2.cpp, `GetImageParam`→KImageStore2.cpp, `GetImagePixelAlpha`→KImageStore2.cpp, `SaveImage`→KImageStore2.cpp, `ExpandSpace`→KImageStore2.cpp, `CheckBalance`→KNpcSet.cpp, `FindImage`→KImageStore2.cpp, `GetSprFrame`→KPakList.cpp, `FreeImageObject`→KImageStore2.cpp

## `engine/CXmlStream.cpp`
- 97 dòng. return pStr1->getCString();
- Hàm: `CXmlStream`, `CXmlStream`, `CXmlStream::GetStringByKey`, `CXmlStream::GetStringByKeyFromFile_old`, `CXmlStream::GetStringByKeyFromFile`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp

## `engine/CXmlStream.h`
- 22 dòng. (không có chú thích đầu)
- Gọi tới: `CXmlStream`→CXmlStream.cpp, `GetStringByKey`→CXmlStream.cpp, `GetStringByKeyFromFile`→CXmlStream.cpp, `GetStringByKeyFromFile_old`→CXmlStream.cpp

## `engine/KBinTreeNode.h`
- 56 dòng. 二叉树（二叉树也可用于创建普通树）结点
- Hàm: `Left`, `Right`

## `engine/KBinsTree.h`
- 401 dòng. 指向树根及当前结点的指针
- Hàm: `CopyTree`, `DeleteTree`, `FindNode`, `BinSTree`, `BinSTree`, `BinSTree`, `ClearList`, `Find`, `ListEmpty`, `ListSize`, `Insert`, `Delete`, `Update`, `GetRoot`, `BiTreeDepth`, `search`

## `engine/KCache.cpp`
- 181 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KCache`, `KCache::Release`, `KCache`, `KCache::Init`, `KCache::NewNode`, `KCache::GetNode`, `KCache::Prepare`, `KCache::ClearNode`
- Gọi tới: `FreeNode`→KScriptCache.cpp, `AddHead`→KList.h, `LoadNode`→KScriptCache.cpp, `Find`→KBinsTree.h, `GetTail`→KList.h, `Remove`→KLinkArray.cpp, `RemoveHead`→KList.h, `GetNodeCount`→KList.h, `RemoveTail`→KList.h, `g_StrCmp`→KStrBase.cpp, `GetName`→KNpcResNode.cpp, `GetPrev`→KNode.h, `GetHead`→KList.h, `GetNext`→KNode.h

## `engine/KCache.h`
- 43 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `KCache`→KCache.cpp, `Init`→KCache.cpp, `NewNode`→KCache.cpp, `GetNode`→KCache.cpp, `LoadNode`→KScriptCache.cpp, `FreeNode`→KScriptCache.cpp, `ClearNode`→KCache.cpp, `Prepare`→KCache.cpp, `Release`→KCache.cpp

## `engine/KCodec.cpp`
- 114 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KCodec::GetPackLen`, `KCodec::Encode`, `KCodec::Decode`, `g_InitCodec`, `g_FreeCodec`
- Gọi tới: `g_MemCopyMmx`→KMemBase.cpp

## `engine/KCodec.h`
- 38 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `GetPackLen`→KCodec.cpp, `Encode`→KCodec.cpp, `Decode`→KCodec.cpp, `g_InitCodec`→KCodec.cpp, `g_FreeCodec`→KCodec.cpp

## `engine/KCodecLzo.cpp`
- 440 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KCodecLzo::Encode`, `KCodecLzo::Decode`
- Gọi tới: `Encode`→KCodec.cpp, `Alloc`→KMemClass.cpp, `Decode`→KCodec.cpp

## `engine/KCodecLzo.h`
- 29 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `Encode`→KCodec.cpp, `Decode`→KCodec.cpp

## `engine/KCriticalSection.cpp`
- 67 dòng. Version     :   1.0
- Hàm: `KAutoCriticalSection`
- Gọi tới: `Lock`→KPlayerTrade.cpp

## `engine/KCriticalSection.h`
- 93 dòng. Version     :   1.0
- Gọi tới: `Lock`→KPlayerTrade.cpp, `KAutoCriticalSection`→KCriticalSection.cpp

## `engine/KDownLoadFile.cpp`
- 365 dòng. #include "..\deprecated\CCDeprecated.h"
- Hàm: `downloadFile::GetInst`, `downloadFile::Replease`, `downloadFile::getCurFileSizeInfo`, `downloadFile::DownLoadFile`, `downloadFile::createFile`, `downloadFile::getLocalFileLenth`, `downloadFile::progressFunc`, `downloadFile::downLoadPackage`, `downloadFile::save_header`, `downloadFile::writefunc`
- Gọi tới: `ccMessageBox_new`→KCore.cpp

## `engine/KDownLoadFile.h`
- 76 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `GetInst`→KDownLoadFile.cpp, `Replease`→KDownLoadFile.cpp, `DownLoadFile`→KDownLoadFile.cpp, `getLocalFileLenth`→KDownLoadFile.cpp, `progressFunc`→KDownLoadFile.cpp, `downLoadPackage`→KDownLoadFile.cpp, `save_header`→KDownLoadFile.cpp, `writefunc`→KDownLoadFile.cpp, `createFile`→KDownLoadFile.cpp, `getCurFileSizeInfo`→KDownLoadFile.cpp

## `engine/KEngine.h`
- 32 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft

## `engine/KFile.cpp`
- 337 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KFile`, `KFile`, `KFile::Open`, `KFile::Create`, `KFile::Append`, `KFile::Close`, `KFile::Read`, `KFile::Write`, `KFile::Seek`, `KFile::Tell`, `KFile::Size`
- Gọi tới: `ccMessageBox_new`→KCore.cpp, `g_GetFullPath`→KFilePath.cpp, `g_GetRootPath`→KFilePath.cpp, `CloseHandle`→KScenePlaceC.cpp

## `engine/KFile.h`
- 42 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `KFile`→KFile.cpp, `Open`→KFile.cpp, `Create`→KFile.cpp, `Append`→KFile.cpp, `Close`→KFile.cpp, `Read`→KFile.cpp, `Write`→KFile.cpp, `Seek`→KFile.cpp, `Tell`→KFile.cpp, `Size`→KFile.cpp

## `engine/KFilePath.cpp`
- 594 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `RemoveTwoPointPath`, `RemoveOnePointPath`, `RemoveAllPointPath`, `g_SetRootPath`, `g_GetRootPath`, `g_SetFilePath`, `g_GetFilePath`, `g_GetFullPath`, `g_GetHalfPath`, `g_GetPackPath`, `g_GetDiskPath`, `g_CreatePath`, `g_UnitePathAndName`, `g_FileExists`, `g_FileName2Id`, `g_ChangeFileExt`, `g_ExtractFileName`, `g_ExtractFilePath`, `g_CheckFileExist`
- Gọi tới: `g_StrCat`→KStrBase.cpp, `g_StrCpy`→KStrBase.cpp, `g_StrLen`→KStrBase.cpp, `t_sprintf`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `g_StrLower`→KStrBase.cpp, `pGetFilePath`→KPakList.cpp, `isFileExist`→KgameWorld.cpp, `g_StrCpyLen`→KStrBase.cpp

## `engine/KFilePath.h`
- 45 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `g_SetRootPath`→KFilePath.cpp, `g_GetRootPath`→KFilePath.cpp, `g_SetFilePath`→KFilePath.cpp, `g_GetFilePath`→KFilePath.cpp, `g_GetFullPath`→KFilePath.cpp, `g_GetHalfPath`→KFilePath.cpp, `g_GetPackPath`→KFilePath.cpp, `g_GetDiskPath`→KFilePath.cpp, `g_CreatePath`→KFilePath.cpp, `g_UnitePathAndName`→KFilePath.cpp, `g_FileExists`→KFilePath.cpp, `g_FileName2Id`→KFilePath.cpp, `g_ChangeFileExt`→KFilePath.cpp, `g_ExtractFileName`→KFilePath.cpp, `g_ExtractFilePath`→KFilePath.cpp

## `engine/KGbktoUtf8.h`
- 453 dòng. (không có chú thích đầu)
- Hàm: `code_convert`, `cp2u`, `tcvn2utf`, `utf2tcvn`, `utf2gbk`, `gbk2utf8`, `dl_icuuc_init`, `dl_icuuc_uninit`, `dl_icuuc_gbk2utf8`, `gbk2utf8_`, `dl_icuuc_utf82gbk`, `utf2gbk_`, `dl_icuuc_unicode2utf8`, `dl_icuuc_utf82unicode`

## `engine/KITabFile.h`
- 36 dòng. virtual void        GetInt2(int nRow, int szColumn, int *pRect)=0;
- Gọi tới: `GetString`→KTabFile.cpp, `GetInteger`→KTabFile.cpp, `GetFloat`→KTabFile.cpp, `GetInt2`→KIniFile.cpp, `GetInt3`→KIniFile.cpp, `Load`→KIniFile.cpp, `Save`→KIniFile.cpp, `CreatFile`→KTabFile.cpp, `FindRow`→KTabFile.cpp, `FindColumn`→KTabFile.cpp, `Clear`→KIniFile.cpp

## `engine/KIniFile.cpp`
- 1433 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `g_SetIniCodec`, `KIniFile`, `KIniFile`, `KIniFile::Load`, `KIniFile::LoadPack`, `KIniFile::Save`, `KIniFile::SavePack`, `KIniFile::Clear`, `KIniFile::ReadLine`, `KIniFile::IsKeyChar`, `KIniFile::CreateIniLink`, `KIniFile::ReleaseIniLink`, `KIniFile::SplitKeyValue`, `KIniFile::String2Id`, `KIniFile::IsSectionExist`, `KIniFile::EraseSection`, `KIniFile::EraseKey`, `KIniFile::GetNextSection`, `KIniFile::GetNextKey`, `KIniFile::GetSectionCount`, `KIniFile::GetRect`, `KIniFile::GetFloat3`, `KIniFile::GetFloat4`, `KIniFile::GetFloat8`, `KIniFile::GetInt5` …(+4)
- Gọi tới: `g_StrCat`→KStrBase.cpp, `Push`→KMemStack.cpp, `Free`→KMemClass.cpp, `g_StrCpy`→KStrBase.cpp, `t_sprintf`→KStrBase.cpp, `Close`→KFile.cpp, `g_StrLen`→KStrBase.cpp, `g_MemCopy`→KMemBase.cpp, `KSG_StringGetInt`→KSG_StringProcess.cpp, `Open`→KFile.cpp, `Create`→KFile.cpp, `Read`→KFile.cpp, `Write`→KFile.cpp, `g_StrCpyLen`→KStrBase.cpp, `KSG_StringSkipSymbol`→KSG_StringProcess.cpp

## `engine/KIniFile.h`
- 203 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `KIniFile`→KIniFile.cpp, `g_SetIniCodec`→KIniFile.cpp, `CreateIniLink`→KIniFile.cpp, `ReleaseIniLink`→KIniFile.cpp, `String2Id`→KIniFile.cpp, `ReadLine`→KIniFile.cpp, `IsKeyChar`→KIniFile.cpp, `SplitKeyValue`→KIniFile.cpp, `Load`→KIniFile.cpp, `Save`→KIniFile.cpp, `LoadPack`→KIniFile.cpp, `SavePack`→KIniFile.cpp, `Clear`→KIniFile.cpp, `IsSectionExist`→KIniFile.cpp, `EraseSection`→KIniFile.cpp

## `engine/KLinkArray.cpp`
- 61 dòng. if (pNodeL!=NULL)
- Hàm: `KLinkArray`, `KLinkArray::Init`, `KLinkArray::Remove`, `KLinkArray::Insert`
- Gọi tới: `Init`→KCache.cpp, `Insert`→KBinsTree.h

## `engine/KLinkArray.h`
- 35 dòng. (không có chú thích đầu)
- Gọi tới: `KLinkArray`→KLinkArray.cpp, `GetCount`→KMissleSet.cpp, `GetNode`→KCache.cpp, `Init`→KCache.cpp, `Remove`→KLinkArray.cpp, `Insert`→KBinsTree.h, `GetNext`→KNode.h, `GetPrev`→KNode.h

## `engine/KList.cpp`
- 114 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `GetNext`→KNode.h, `GetHead`→KList.h, `GetPrev`→KNode.h, `Remove`→KLinkArray.cpp, `KList`→KList.h, `IsEmpty`→KList.h, `GetTail`→KList.h, `AddHead`→KList.h, `InsertAfter`→KNode.h, `AddTail`→KList.h, `InsertBefore`→KNode.h, `RemoveHead`→KList.h, `RemoveTail`→KList.h, `GetNodeCount`→KList.h

## `engine/KList.h`
- 201 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KList::KList`, `KList::IsEmpty`, `KList::GetHead`, `KList::GetTail`, `KList::AddHead`, `KList::AddTail`, `KList::RemoveHead`, `KList::RemoveTail`, `KList::GetNodeCount`, `KList::GetStatusNode`, `KList::RemoveOneTail`
- Gọi tới: `GetNext`→KNode.h, `Remove`→KLinkArray.cpp, `GetPrev`→KNode.h, `InsertAfter`→KNode.h, `InsertBefore`→KNode.h

## `engine/KLuaScript.cpp`
- 803 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `l_alloc`, `KLuaScript`, `KLuaScript`, `KLuaScript`, `KLuaScript::LoadBuffer`, `KLuaScript::Load`, `KLuaScript::Execute`, `KLuaScript::ExecuteCode`, `KLuaScript::CallFunctionS`, `KLuaScript::CallFunction`, `KLuaScript::GetValuesFromStack`, `KLuaScript::Init`, `KLuaScript::RegisterFunction`, `KLuaScript::Compile`, `KLuaScript::RegisterFunctions`, `KLuaScript::RegisterStandardFunctions`, `KLuaScript::Exit`, `KLuaScript::ScriptError`, `KLuaScript::ScriptError`, `KLuaScript::SafeCallBegin`, `KLuaScript::SafeCallEnd`, `KLuaScript::Stop`, `KLuaScript::Resume`, `KLuaScript::CreateTable`, `KLuaScript::SetGlobalName` …(+2)
- Gọi tới: `Free`→KMemClass.cpp, `Close`→KFile.cpp, `Init`→KCache.cpp, `lua_outerrmsg`→lua.c, `t_sprintf`→KStrBase.cpp, `gTraceLogFile`→KLogFile.cpp, `Load`→KIniFile.cpp, `Open`→KFile.cpp, `Size`→KFile.cpp, `Alloc`→KMemClass.cpp, `Read`→KFile.cpp

## `engine/KLuaScript.h`
- 93 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `KLuaScript`→KLuaScript.cpp, `Execute`→KLuaScript.cpp, `ScriptError`→KLuaScript.cpp, `Activate`→KScriptList.cpp, `Init`→KCache.cpp, `Exit`→KLuaScript.cpp, `Load`→KIniFile.cpp, `Compile`→KLuaScript.cpp, `CallFunction`→KLuaScript.cpp, `RegisterFunction`→KLuaScript.cpp, `RegisterFunctions`→KLuaScript.cpp, `LoadBuffer`→KLuaScript.cpp, `SafeCallBegin`→KLuaScript.cpp, `SafeCallEnd`→KLuaScript.cpp, `GetValuesFromStack`→KLuaScript.cpp

## `engine/KLubCmpl_Blocker.cpp`
- 520 dòng. 为if语句的头
- Hàm: `KLubCmpl_Blocker::ScanIf`, `KLubCmpl_Blocker::ExchangeCurLines`, `KLubCmpl_Blocker::Load`, `KLubCmpl_Blocker::PushKey`, `KLubCmpl_Blocker::PopKey`, `KLubCmpl_Blocker::GetBuffer`, `KLubCmpl_Blocker::Write`, `KLubCmpl_Blocker::Print`
- Gọi tới: `GetNext`→KNode.h, `Alloc`→KMemClass.cpp, `GetHead`→KList.h, `AddTail`→KList.h, `RemoveHead`→KList.h, `Goto`→CoreShell.cpp, `GetPrev`→KNode.h, `Remove`→KLinkArray.cpp, `GetNodeCount`→KList.h, `AddHead`→KList.h, `InsertAfter`→KNode.h, `g_StrRep`→KStrBase.cpp, `Write`→KFile.cpp, `GetTail`→KList.h, `Free`→KMemClass.cpp

## `engine/KLubCmpl_Blocker.h`
- 53 dòng. #include "assert.h"
- Gọi tới: `g_StrLen`→KStrBase.cpp, `g_StrCpy`→KStrBase.cpp, `g_StrCpyLen`→KStrBase.cpp, `g_StrRep`→KStrBase.cpp, `main`→md5.cpp, `GetBuffer`→KLubCmpl_Blocker.cpp, `PushKey`→KLubCmpl_Blocker.cpp, `PopKey`→KLubCmpl_Blocker.cpp, `ScanIf`→KLubCmpl_Blocker.cpp, `ExchangeCurLines`→KLubCmpl_Blocker.cpp, `Load`→KIniFile.cpp, `Write`→KFile.cpp, `Print`→KLubCmpl_Blocker.cpp

## `engine/KMemBase.cpp`
- 382 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `g_MemInfo`, `g_MemAlloc`, `g_MemFreeSec`, `g_MemFreeSign`, `g_MemFree`, `g_MemCopy`, `g_MemCopyMmx`, `g_MemComp`, `g_MemFill`, `g_MemFill`, `g_MemFill`, `g_MemZero`, `g_MemXore`
- Gọi tới: `GetHead`→KList.h, `GetNext`→KNode.h, `Remove`→KLinkArray.cpp, `AddHead`→KList.h

## `engine/KMemBase.h`
- 32 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `g_MemFill`→KMemBase.cpp, `g_MemInfo`→KMemBase.cpp, `g_MemAlloc`→KMemBase.cpp, `g_MemFree`→KMemBase.cpp, `g_MemFreeSign`→KMemBase.cpp, `g_MemFreeSec`→KMemBase.cpp, `g_MemCopy`→KMemBase.cpp, `g_MemCopyMmx`→KMemBase.cpp, `g_MemComp`→KMemBase.cpp, `g_MemZero`→KMemBase.cpp, `g_MemXore`→KMemBase.cpp

## `engine/KMemClass.cpp`
- 115 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KMemClass`, `KMemClass`, `KMemClass::Alloc`, `KMemClass::Free`, `KMemClass::Zero`, `KMemClass::Fill`, `KMemClass::Fill`, `KMemClass::Fill`
- Gọi tới: `g_MemFill`→KMemBase.cpp, `g_MemAlloc`→KMemBase.cpp, `g_MemFree`→KMemBase.cpp, `g_MemZero`→KMemBase.cpp

## `engine/KMemClass.h`
- 34 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `Fill`→KMemClass.cpp, `KMemClass`→KMemClass.cpp, `Alloc`→KMemClass.cpp, `Free`→KMemClass.cpp, `Zero`→KMemClass.cpp

## `engine/KMemClass1.cpp`
- 13 dòng. (không có chú thích đầu)
- Hàm: `KMemClass1::Alloc`, `KMemClass1::Free`
- Gọi tới: `Alloc`→KMemClass.cpp, `Free`→KMemClass.cpp

## `engine/KMemClass1.h`
- 22 dòng. (không có chú thích đầu)
- Gọi tới: `Fill`→KMemClass.cpp, `Alloc`→KMemClass.cpp, `Free`→KMemClass.cpp, `Zero`→KMemClass.cpp

## `engine/KMemManager.cpp`
- 206 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KMemManager`, `KMemManager`, `KMemManager::NewChunk`, `KMemManager::FreeChunk`, `KMemManager::Malloc`, `KMemManager::Calloc`, `KMemManager::Free`
- Gọi tới: `Free`→KMemClass.cpp, `g_MemZero`→KMemBase.cpp, `GetHead`→KList.h, `g_MemAlloc`→KMemBase.cpp, `AddTail`→KList.h, `Remove`→KLinkArray.cpp, `g_MemFree`→KMemBase.cpp

## `engine/KMemManager.h`
- 59 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `KMemManager`→KMemManager.cpp, `NewChunk`→KMemManager.cpp, `FreeChunk`→KMemManager.cpp, `Malloc`→KMemManager.cpp, `Calloc`→KMemManager.cpp, `Free`→KMemClass.cpp

## `engine/KMemStack.cpp`
- 156 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KMemStack`, `KMemStack`, `KMemStack::Init`, `KMemStack::Push`, `KMemStack::Free`, `KMemStack::AllocNewChunk`, `KMemStack::FreeAllChunks`, `KMemStack::GetChunkSize`, `KMemStack::GetStackSize`
- Gọi tới: `g_MemFree`→KMemBase.cpp, `g_MemZero`→KMemBase.cpp, `Init`→KCache.cpp, `Free`→KMemClass.cpp, `g_MemAlloc`→KMemBase.cpp

## `engine/KMemStack.h`
- 38 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `KMemStack`→KMemStack.cpp, `Init`→KCache.cpp, `Push`→KMemStack.cpp, `Free`→KMemClass.cpp, `AllocNewChunk`→KMemStack.cpp, `FreeAllChunks`→KMemStack.cpp, `GetChunkSize`→KMemStack.cpp, `GetStackSize`→KMemStack.cpp

## `engine/KNode.cpp`
- 100 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `KNode`→KNode.h, `GetNext`→KNode.h, `GetPrev`→KNode.h, `InsertBefore`→KNode.h, `InsertAfter`→KNode.h, `Remove`→KLinkArray.cpp, `IsLinked`→KNode.h

## `engine/KNode.h`
- 135 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KNode::KNode`, `KNode::GetNext`, `KNode::GetPrev`, `KNode::InsertBefore`, `KNode::InsertAfter`, `KNode::Remove`, `KNode::IsLinked`
- Gọi tới: `Remove`→KLinkArray.cpp

## `engine/KPakFile.cpp`
- 675 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `g_SetPakFileMode`, `SprGetHeader`, `SprReleaseHeader`, `SprGetFrame`, `SprReleaseFrame`, `get_jpg_image`, `release_image`, `KPakFile`, `KPakFile`, `KPakFile::IsFileInPak`, `KPakFile::Open`, `KPakFile::Read`, `KPakFile::Seek`, `KPakFile::Tell`, `KPakFile::Size`, `KPakFile::Close`, `KPakFile::ReadPak`, `KPakFile::SeekPak`, `KPakFile::Save`, `KPakFile::ReadBlock`
- Gọi tới: `Read`→KFile.cpp, `Open`→KFile.cpp, `Close`→KFile.cpp, `Seek`→KFile.cpp, `Size`→KFile.cpp, `pGetFilePath`→KPakList.cpp, `Alloc`→KMemClass.cpp, `g_MemCopyMmx`→KMemBase.cpp, `Tell`→KFile.cpp, `Write`→KFile.cpp, `GetSprHeader`→KPakList.cpp, `GetSprFrame`→KPakList.cpp, `ElemFileRead`→KPakList.cpp, `Save`→KIniFile.cpp, `Create`→KFile.cpp

## `engine/KPakFile.h`
- 64 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `KPakFile`→KPakFile.cpp, `g_SetPakFileMode`→KPakFile.cpp, `Open`→KFile.cpp, `Close`→KFile.cpp, `IsFileInPak`→KPakFile.cpp, `Read`→KFile.cpp, `Seek`→KFile.cpp, `Tell`→KFile.cpp, `Size`→KFile.cpp, `Save`→KIniFile.cpp, `SprGetHeader`→KPakFile.cpp, `SprReleaseHeader`→KPakFile.cpp, `SprGetFrame`→KPakFile.cpp, `SprReleaseFrame`→KPakFile.cpp, `get_jpg_image`→KPakFile.cpp

## `engine/KPakList.cpp`
- 315 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KPakList`, `KPakList`, `KPakList::Close`, `KPakList::pFindElemFileA`, `KPakList::FileNameToId`, `KPakList::pFindElemFile`, `KPakList::Open`, `KPakList::ElemFileRead`, `KPakList::GetSprHeader`, `KPakList::GetSprFrame`, `KPakList::pGetFilePath`
- Gọi tới: `g_CheckFileExist`→KFilePath.cpp, `t_sprintf`→KStrBase.cpp, `Close`→KFile.cpp, `g_GetPackPath`→KFilePath.cpp, `Open`→KFile.cpp, `ccMessageBox_new`→KCore.cpp, `GetString`→KTabFile.cpp, `gTraceLogFile`→KLogFile.cpp, `XFindElemFile`→XPackFile.cpp, `g_FileName2Id`→KFilePath.cpp, `Load`→KIniFile.cpp, `g_GetFullPath`→KFilePath.cpp, `Clear`→KIniFile.cpp, `XElemFileRead`→XPackFile.cpp

## `engine/KPakList.h`
- 51 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `KPakList`→KPakList.cpp, `Open`→KFile.cpp, `Close`→KFile.cpp, `pFindElemFileA`→KPakList.cpp, `pFindElemFile`→KPakList.cpp, `ElemFileRead`→KPakList.cpp, `GetSprHeader`→KPakList.cpp, `GetSprFrame`→KPakList.cpp, `pGetFilePath`→KPakList.cpp, `FileNameToId`→KPakList.cpp

## `engine/KPolygon.cpp`
- 378 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KPolygon`, `KPolygon::IsPointInPolygon`, `KPolygon::IsPointInPolygon`, `KPolygon::GetNearVertex`, `KPolygon::GetIndexVertex`, `KPolygon::RemoveIndexVertex`, `KPolygon::AddPointToVertex`, `KPolygon::AddPointToVertex`, `KPolygon::LoopVertex`, `KPolygon::Clear`, `KPolygon::GetCenterPos`, `KPolygon::ShiftVertex`, `KPolygon::GetLeftVertex`, `KPolygon::GetRightVertex`
- Gọi tới: `Clear`→KIniFile.cpp

## `engine/KPolygon.h`
- 46 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `IsPointInPolygon`→KPolygon.cpp, `AddPointToVertex`→KPolygon.cpp, `KPolygon`→KPolygon.cpp, `GetNearVertex`→KPolygon.cpp, `GetIndexVertex`→KPolygon.cpp, `RemoveIndexVertex`→KPolygon.cpp, `LoopVertex`→KPolygon.cpp, `Clear`→KIniFile.cpp, `GetCenterPos`→KPolygon.cpp, `ShiftVertex`→KPolygon.cpp, `GetLeftVertex`→KPolygon.cpp, `GetRightVertex`→KPolygon.cpp

## `engine/KRandom.cpp`
- 110 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `RandomNum`, `g_RandomSeed`, `g_Random`, `g_GetRandomSeed`, `g_Random`

## `engine/KRandom.h`
- 19 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `g_Random`→KRandom.cpp, `g_GetRandomSeed`→KRandom.cpp, `g_RandomSeed`→KRandom.cpp

## `engine/KSG_MD5_String.cpp`
- 54 dòng. Version     :   1.0
- Hàm: `KSG_StringToMD5String`

## `engine/KSG_MD5_String.h`
- 19 dòng. Version     :   1.0
- Gọi tới: `KSG_StringToMD5String`→KSG_MD5_String.cpp

## `engine/KSG_StringProcess.cpp`
- 114 dòng. Version     :   1.0
- Hàm: `KSG_StringGetInt`, `KSG_StringSkipSymbol`

## `engine/KSG_StringProcess.h`
- 32 dòng. Version     :   1.0
- Hàm: `KSG_StringGetInt`, `KSG_StringSkipSymbol`
- Gọi tới: `KSG_StringGetInt`→KSG_StringProcess.cpp, `KSG_StringSkipSymbol`→KSG_StringProcess.cpp

## `engine/KScript.cpp`
- 89 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KScript`, `KScript`, `KScript::Init`, `KScript::Exit`, `KScript::Load`, `KScript::Compile`, `KScript::Execute`, `KScript::CallFunction`, `KScript::RegisterFunction`
- Gọi tới: `Init`→KCache.cpp, `Exit`→KLuaScript.cpp, `Load`→KIniFile.cpp, `Compile`→KLuaScript.cpp, `Execute`→KLuaScript.cpp, `CallFunction`→KLuaScript.cpp, `RegisterFunction`→KLuaScript.cpp

## `engine/KScript.h`
- 30 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `KScript`→KScript.cpp, `Load`→KIniFile.cpp, `Init`→KCache.cpp, `Exit`→KLuaScript.cpp, `Compile`→KLuaScript.cpp, `Execute`→KLuaScript.cpp, `CallFunction`→KLuaScript.cpp, `RegisterFunction`→KLuaScript.cpp

## `engine/KScriptCache.cpp`
- 48 dòng. Revision Count	:
- Hàm: `KScriptCache`, `KScriptCache`, `KScriptCache::LoadNode`, `KScriptCache::FreeNode`
- Gọi tới: `Release`→KCache.cpp, `Init`→KCache.cpp, `Load`→KIniFile.cpp, `GetName`→KNpcResNode.cpp, `Exit`→KLuaScript.cpp

## `engine/KScriptCache.h`
- 17 dòng. (không có chú thích đầu)
- Gọi tới: `KScriptCache`→KScriptCache.cpp, `LoadNode`→KScriptCache.cpp, `FreeNode`→KScriptCache.cpp

## `engine/KScriptList.cpp`
- 69 dòng. (không có chú thích đầu)
- Hàm: `KScriptList::GetScript`, `KScriptList::Activate`, `KScriptList::SendMessage`
- Gọi tới: `GetNext`→KNode.h, `GetHead`→KList.h, `GetNodeCount`→KList.h, `IsEmpty`→KList.h, `Active`→KStepLuaScript.cpp, `Remove`→KLinkArray.cpp, `AddMessage`→KStepLuaScript.cpp

## `engine/KScriptList.h`
- 27 dòng. (không có chú thích đầu)
- Gọi tới: `GetScript`→KScriptList.cpp, `Activate`→KScriptList.cpp, `SendMessage`→KScriptList.cpp

## `engine/KStepLuaScript.cpp`
- 433 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KStepLuaScript`, `KStepLuaScript`, `KStepLuaScript`, `KStepLuaScript::GetNextLine`, `KStepLuaScript::Load`, `KStepLuaScript::ExeLine`, `KStepLuaScript::Active`, `KStepLuaScript::PosUp`, `KStepLuaScript::GotoLabel`, `KStepLuaScript::AddMessage`, `KStepLuaScript::SendMessage`
- Gọi tới: `Alloc`→KMemClass.cpp, `Close`→KFile.cpp, `Load`→KIniFile.cpp, `LoadBuffer`→KLuaScript.cpp, `ExecuteCode`→KLuaScript.cpp, `t_sprintf`→KStrBase.cpp, `Free`→KMemClass.cpp, `Exit`→KLuaScript.cpp, `AddTail`→KList.h, `ScanIf`→KLubCmpl_Blocker.cpp, `GetBuffer`→KLubCmpl_Blocker.cpp, `Open`→KFile.cpp, `Size`→KFile.cpp, `Read`→KFile.cpp, `g_MemCopy`→KMemBase.cpp

## `engine/KStepLuaScript.h`
- 94 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `KStepLuaScript`→KStepLuaScript.cpp, `main`→md5.cpp, `Active`→KStepLuaScript.cpp, `GetNextLine`→KStepLuaScript.cpp, `ExeLine`→KStepLuaScript.cpp, `Load`→KIniFile.cpp, `SendMessage`→KScriptList.cpp, `AddMessage`→KStepLuaScript.cpp, `PosUp`→KStepLuaScript.cpp, `GotoLabel`→KStepLuaScript.cpp

## `engine/KStrBase.cpp`
- 1004 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `GetBig5Count`, `g_Atoui`, `g_ExtractChar`, `g_StrLen`, `g_StrEnd`, `g_StrCpy`, `g_StrCpyLen`, `g_StrCat`, `g_StrCatLen`, `g_StrCmp`, `g_StrCmpLen`, `g_StrUpper`, `g_StrLower`, `g_StrRep`, `t_printchar`, `t_prints`, `t_printi`, `t_print`, `t_printf`, `t_sprintf`, `t_snprintf`, `_mysprintf`, `__replaceNmae`, `__CreateFolder`, `g_isFileExist` …(+8)
- Gọi tới: `ccMessageBox_new`→KCore.cpp, `g_MemComp`→KMemBase.cpp, `pGetFilePath`→KPakList.cpp, `ElemFileRead`→KPakList.cpp

## `engine/KStrBase.h`
- 59 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `_utf_length`→KStrBase.cpp, `g_StrLen`→KStrBase.cpp, `g_StrEnd`→KStrBase.cpp, `g_StrCpy`→KStrBase.cpp, `g_StrCpyLen`→KStrBase.cpp, `g_StrCat`→KStrBase.cpp, `g_StrCatLen`→KStrBase.cpp, `g_StrCmp`→KStrBase.cpp, `g_StrCmpLen`→KStrBase.cpp, `g_StrUpper`→KStrBase.cpp, `g_StrLower`→KStrBase.cpp, `g_StrRep`→KStrBase.cpp, `g_Atoui`→KStrBase.cpp, `g_StrCopy`→KStrBase.cpp, `g_isFileExist`→KStrBase.cpp

## `engine/KStrList.cpp`
- 28 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KStrList::Find`
- Gọi tới: `Find`→KBinsTree.h, `GetHead`→KList.h, `g_StrCmp`→KStrBase.cpp, `GetName`→KNpcResNode.cpp, `GetNext`→KNode.h

## `engine/KStrList.h`
- 21 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `Find`→KBinsTree.h

## `engine/KStrNode.cpp`
- 21 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KStrNode`
- Gọi tới: `g_MemZero`→KMemBase.cpp

## `engine/KStrNode.h`
- 27 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `KStrNode`→KStrNode.cpp, `GetName`→KNpcResNode.cpp, `g_StrCpyLen`→KStrBase.cpp

## `engine/KTabFile.cpp`
- 901 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KTabFile`, `KTabFile`, `KTabFile::CreatFile`, `KTabFile::Load`, `KTabFile::CreateTabOffset`, `KTabFile::Str2Col`, `KTabFile::GetString`, `KTabFile::GetString`, `KTabFile::GetString`, `KTabFile::GetString`, `KTabFile::GetInteger`, `KTabFile::GetInteger6`, `KTabFile::GetInteger3`, `KTabFile::GetInt2`, `KTabFile::GetInt15`, `KTabFile::GetInt15s`, `KTabFile::GetInt3`, `KTabFile::GetInt2s`, `KTabFile::GetInt3s`, `KTabFile::GetInteger`, `KTabFile::GetInteger`, `KTabFile::GetIntegerDW`, `KTabFile::GetDword`, `KTabFile::GetDouble`, `KTabFile::GetFloat` …(+7)
- Gọi tới: `g_StrCpyLen`→KStrBase.cpp, `Close`→KFile.cpp, `Alloc`→KMemClass.cpp, `g_StrLen`→KStrBase.cpp, `Clear`→KIniFile.cpp, `g_FileName2Id`→KFilePath.cpp, `GetInt2`→KIniFile.cpp, `Free`→KMemClass.cpp, `g_StrCmp`→KStrBase.cpp, `Create`→KFile.cpp, `Load`→KIniFile.cpp, `Open`→KFile.cpp, `Size`→KFile.cpp, `g_StrLower`→KStrBase.cpp, `Read`→KFile.cpp

## `engine/KTabFile.h`
- 78 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `GetString`→KTabFile.cpp, `GetFloat`→KTabFile.cpp, `GetInteger`→KTabFile.cpp, `KTabFile`→KTabFile.cpp, `CreateTabOffset`→KTabFile.cpp, `GetValue`→KTabFile.cpp, `Str2Col`→KTabFile.cpp, `Load`→KIniFile.cpp, `CreatFile`→KTabFile.cpp, `Save`→KIniFile.cpp, `LoadPack`→KIniFile.cpp, `FindRow`→KTabFile.cpp, `FindColumn`→KTabFile.cpp, `Col2Str`→KTabFile.cpp, `GetInteger6`→KTabFile.cpp

## `engine/KTabFileCtrl.cpp`
- 610 dòng. check file name
- Hàm: `KTabFileCtrl`, `KTabFileCtrl`, `KTabFileCtrl::Load`, `KTabFileCtrl::openfile`, `KTabFileCtrl::LoadPack`, `KTabFileCtrl::Save`, `KTabFileCtrl::GetRowName`, `KTabFileCtrl::GetColName`, `KTabFileCtrl::FindRow`, `KTabFileCtrl::FindColumn`, `KTabFileCtrl::GetValue`, `KTabFileCtrl::SetValue`, `KTabFileCtrl::GetString`, `KTabFileCtrl::GetInteger`, `KTabFileCtrl::GetFloat`, `KTabFileCtrl::Clear`, `KTabFileCtrl::WriteString`, `KTabFileCtrl::WriteInteger`, `KTabFileCtrl::WriteFloat`, `KTabFileCtrl::Str2Col`, `KTabFileCtrl::Remove`, `KTabFileCtrl::InsertAfter`, `KTabFileCtrl::InsertBefore`, `KTabFileCtrl::InsertNewCol`
- Gọi tới: `GetHead`→KList.h, `GetNext`→KNode.h, `AddTail`→KList.h, `Close`→KFile.cpp, `g_StrCpyLen`→KStrBase.cpp, `g_StrLen`→KStrBase.cpp, `Open`→KFile.cpp, `Create`→KFile.cpp, `GetValue`→KTabFile.cpp, `t_sprintf`→KStrBase.cpp, `Write`→KFile.cpp, `GetTail`→KList.h, `Remove`→KLinkArray.cpp, `Clear`→KIniFile.cpp, `Size`→KFile.cpp

## `engine/KTabFileCtrl.h`
- 193 dòng. delete pList;pList=NULL;
- Gọi tới: `FindColumn`→KTabFile.cpp, `FindRow`→KTabFile.cpp, `Str2Col`→KTabFile.cpp, `GetString`→KTabFile.cpp, `GetInteger`→KTabFile.cpp, `GetFloat`→KTabFile.cpp, `WriteString`→KTabFileCtrl.cpp, `WriteInteger`→KTabFileCtrl.cpp, `WriteFloat`→KTabFileCtrl.cpp, `InsertAfter`→KNode.h, `InsertBefore`→KNode.h, `Remove`→KLinkArray.cpp, `GetHead`→KList.h, `GetValue`→KTabFile.cpp, `KTabFileCtrl`→KTabFileCtrl.cpp

## `engine/KTimer.cpp`
- 158 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KTimer`, `KTimer::Start`, `KTimer::Reset`, `KTimer::Stop`, `KTimer::GetElapse`, `KTimer::GetElapseFrequency`, `KTimer::GetInterval`, `KTimer::Passed`, `KTimer::GetFPS`
- Gọi tới: `Stop`→KLuaScript.cpp

## `engine/KTimer.h`
- 49 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `KTimer`→KTimer.cpp, `Start`→KTimer.cpp, `Stop`→KLuaScript.cpp, `GetElapse`→KTimer.cpp, `GetElapseFrequency`→KTimer.cpp, `GetInterval`→KTimer.cpp, `Passed`→KTimer.cpp, `GetFPS`→KTimer.cpp, `Reset`→KTimer.cpp

## `engine/KbugInfo.h`
- 391 dòng. #include "tchar.h"
- Gọi tới: `Release`→KCache.cpp

## `engine/Kgetinidata.cpp`
- 740 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `Kgetinidata`, `Kgetinidata::GetLen`, `Kgetinidata::getpicPath`, `Kgetinidata::findinidata_one`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `isFileExist`→KgameWorld.cpp, `g_FileName2Id`→KFilePath.cpp, `Init`→KCache.cpp, `g_StrLower`→KStrBase.cpp, `pGetFilePath`→KPakList.cpp, `ElemFileRead`→KPakList.cpp, `ccMessageBox_new`→KCore.cpp

## `engine/Kgetinidata.h`
- 86 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `Kgetinidata`→Kgetinidata.cpp, `GetLen`→Kgetinidata.cpp, `findinidata_one`→Kgetinidata.cpp, `getpicPath`→Kgetinidata.cpp, `g_InitCodec`→KCodec.cpp, `g_FreeCodec`→KCodec.cpp

## `engine/LinkStruct.h`
- 274 dòng. By Fyt(Fan Zhanpeng)
- Gọi tới: `Reset`→KTimer.cpp, `Clear`→KIniFile.cpp, `GetCount`→KMissleSet.cpp

## `engine/Text.cpp`
- 1652 dòng. Author	:   Wooy(Wu yue)
- Hàm: `TReplaceText`, `getColorIndex`, `EGetBit`, `ESetBit`, `FilterTextColor`, `ESetByte`, `EGetByte`, `TGetColorStr`, `TGetColor`, `TIsCharacterNotAlowAtLineHead`, `TGetSecondVisibleCharacterThisLine`, `TSplitString`, `TSplitEncodedString`, `TEncodeText_`, `TEncodeText`, `TFilterEncodedText`, `TEncodeCtrl`, `TEncodeCtrlc`, `TRemoveCtrlInEncodedText`, `TGetEncodeStringLineHeadPos`, `TGetLimitLenString`, `TFindSpecialCtrlInEncodedText`, `TClearSpecialCtrlInEncodedText`, `TGetEncodedTextOutputLenPos`, `TGetEncodedTextEffectCtrls`
- Gọi tới: `ccMessageBox_new`→KCore.cpp, `t_sprintf`→KStrBase.cpp

## `engine/Text.h`
- 183 dòng. Author	:   Wooy(Wu yue)
- Gọi tới: `getColorIndex`→Text.cpp, `EGetBit`→Text.cpp, `ESetBit`→Text.cpp, `EGetByte`→Text.cpp, `ESetByte`→Text.cpp, `FilterTextColor`→Text.cpp, `TGetColor`→Text.cpp, `TGetColorStr`→Text.cpp, `TReplaceText`→Text.cpp, `TGetSecondVisibleCharacterThisLine`→Text.cpp, `TIsCharacterNotAlowAtLineHead`→Text.cpp, `TGetLimitLenString`→Text.cpp, `TSplitString`→Text.cpp, `TSplitEncodedString`→Text.cpp, `TGetEncodeStringLineHeadPos`→Text.cpp

## `engine/XPackFile.cpp`
- 741 dòng. Author	:   Wooy(Wu yue)
- Hàm: `XPackFile`, `XPackFile`, `XPackFile::Open`, `XPackFile::Close`, `XPackFile::FreeElemCache`, `XPackFile::DirectRead`, `XPackFile::ExtractRead`, `XPackFile::XFindElemFileA`, `XPackFile::XFindElemFile`, `XPackFile::ReadElemFile`, `XPackFile::FindElemFileInCache`, `XPackFile::AddElemFileToCache`, `XPackFile::XElemFileRead`, `XPackFile::GetSprHeader`, `XPackFile::GetSprFrame`
- Gọi tới: `Close`→KFile.cpp, `ccMessageBox_new`→KCore.cpp, `Open`→KFile.cpp, `GetSprHeader`→KPakList.cpp, `GetSprFrame`→KPakList.cpp

## `engine/XPackFile.h`
- 93 dòng. Author	:   Wooy(Wu yue)
- Gọi tới: `XPackFile`→XPackFile.cpp, `Open`→KFile.cpp, `Close`→KFile.cpp, `XFindElemFile`→XPackFile.cpp, `XElemFileRead`→XPackFile.cpp, `GetSprHeader`→KPakList.cpp, `GetSprFrame`→KPakList.cpp, `DirectRead`→XPackFile.cpp, `ExtractRead`→XPackFile.cpp, `XFindElemFileA`→XPackFile.cpp, `FindElemFileInCache`→XPackFile.cpp, `AddElemFileToCache`→XPackFile.cpp, `ReadElemFile`→XPackFile.cpp, `FreeElemCache`→XPackFile.cpp

## `engine/acc/acc.h`
- 94 dòng. ACC -- Automatic Compiler Configuration

## `engine/acc/acc_arch.h`
- 124 dòng. ACC -- Automatic Compiler Configuration

## `engine/acc/acc_auto.h`
- 662 dòng. ACC -- Automatic Compiler Configuration

## `engine/acc/acc_cc.h`
- 143 dòng. ACC -- Automatic Compiler Configuration

## `engine/acc/acc_cxx.h`
- 157 dòng. ACC -- Automatic Compiler Configuration

## `engine/acc/acc_defs.h`
- 191 dòng. ACC -- Automatic Compiler Configuration

## `engine/acc/acc_incd.h`
- 67 dòng. ACC -- Automatic Compiler Configuration

## `engine/acc/acc_ince.h`
- 87 dòng. ACC -- Automatic Compiler Configuration

## `engine/acc/acc_inci.h`
- 103 dòng. ACC -- Automatic Compiler Configuration

## `engine/acc/acc_init.h`
- 237 dòng. ACC -- Automatic Compiler Configuration

## `engine/acc/acc_lib.h`
- 526 dòng. ACC -- Automatic Compiler Configuration

## `engine/acc/acc_mm.h`
- 199 dòng. ACC -- Automatic Compiler Configuration

## `engine/acc/acc_os.h`
- 203 dòng. ACC -- Automatic Compiler Configuration

## `engine/acc/acc_type.h`
- 321 dòng. ACC -- Automatic Compiler Configuration

## `engine/dataChecksum.cpp`
- 273 dòng. MD5Checksum.cpp: implementation of the MD5Checksum class.
- Hàm: `dataChecksum::__rol`, `dataChecksum::pgChar2Int`, `dataChecksum::pgInt2Char`, `dataChecksum::pgStrLen`, `dataChecksum::pgSwapChars`, `dataChecksum::pgEncrypt`, `dataChecksum::pgDecrypt`, `dataChecksum::pgSameString`, `dataChecksum::SimplyDecrypt`

## `engine/dataChecksum.h`
- 53 dòng. public use
- Gọi tới: `SimplyDecrypt`→dataChecksum.cpp, `pgChar2Int`→dataChecksum.cpp, `__rol`→dataChecksum.cpp, `pgStrLen`→dataChecksum.cpp, `pgSwapChars`→dataChecksum.cpp, `pgDecrypt`→dataChecksum.cpp, `pgInt2Char`→dataChecksum.cpp, `pgSameString`→dataChecksum.cpp, `pgEncrypt`→dataChecksum.cpp

## `engine/kobjallocator.h`
- 84 dòng. 文件名		：	KObjAllocator.h
- Gọi tới: `Init`→KCache.cpp, `Insert`→KBinsTree.h, `Remove`→KLinkArray.cpp, `Malloc`→KMemManager.cpp, `GetNext`→KNode.h, `Free`→KMemClass.cpp

## `engine/lualib/LuaDef.h`
- 153 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `lua_compilebuffer`→ldo.c, `lua_execute`→ldo.c, `Lua_SetTable_StringFromId`→LuaExtend.c, `Lua_SetTable_DoubleFromId`→LuaExtend.c, `Lua_SetTable_IntFromId`→LuaExtend.c, `Lua_SetTable_CFunFromName`→LuaExtend.c, `Lua_SetTable_CFunFromId`→LuaExtend.c, `Lua_SetTable_StringFromName`→LuaExtend.c, `Lua_SetTable_IntFromName`→LuaExtend.c, `Lua_SetTable_DoubleFromName`→LuaExtend.c, `Lua_GetValuesFromStack`→LuaExtend.c

## `engine/lualib/LuaExtend.c`
- 282 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `Lua_SetTable_DoubleFromName`, `Lua_SetTable_IntFromName`, `Lua_SetTable_StringFromName`, `Lua_SetTable_StringFromId`, `Lua_SetTable_DoubleFromId`, `Lua_SetTable_IntFromId`, `Lua_SetTable_CFunFromName`, `Lua_SetTable_CFunFromId`, `Lua_GetValuesFromStack`
- Gọi tới: `ScriptError`→KLuaScript.cpp

## `engine/lualib/LuaLib.h`
- 54 dòng. Lua standard libraries

## `engine/lualib/baselib/lauxlib.c`
- 216 dòng. Auxiliary functions for building Lua libraries

## `engine/lualib/baselib/lbaselib.c`
- 651 dòng. Basic library

## `engine/lualib/baselib/ldblib.c`
- 188 dòng. Interface from Lua to its debug API

## `engine/lualib/baselib/liolib.c`
- 718 dòng. Standard I/O (and system) library

## `engine/lualib/baselib/lmathlib.c`
- 238 dòng. Standard mathematical library

## `engine/lualib/baselib/lstrlib.c`
- 621 dòng. Standard library for string operations and pattern-matching

## `engine/lualib/dump.c`
- 121 dòng. save bytecodes to file
- Hàm: `DumpInt`, `DumpSize`, `DumpNumber`, `DumpString`, `DumpCode`, `DumpLocals`, `DumpLines`, `DumpConstants`, `DumpFunction`, `DumpHeader`, `luaU_dumpchunk`
- Gọi tới: `luaU_endianess`→lundump.c

## `engine/lualib/lapi.c`
- 494 dòng. Lua API

## `engine/lualib/lapi.h`
- 17 dòng. Auxiliary functions from Lua API

## `engine/lualib/lauxlib.h`
- 100 dòng. Auxiliary functions for building Lua libraries

## `engine/lualib/lcode.c`
- 701 dòng. Code generator for Lua

## `engine/lualib/lcode.h`
- 70 dòng. Code generator for Lua

## `engine/lualib/ldebug.c`
- 466 dòng. Debug Interface

## `engine/lualib/ldebug.h`
- 21 dòng. Auxiliary functions from Debug Interface module

## `engine/lualib/ldo.c`
- 421 dòng. Stack and Call structure of Lua
- Hàm: `lua_compilebuffer`, `lua_execute`
- Gọi tới: `luaU_undump`→lundump.c

## `engine/lualib/ldo.h`
- 33 dòng. Stack and Call structure of Lua

## `engine/lualib/lfunc.c`
- 109 dòng. Auxiliary functions to manipulate prototypes and closures

## `engine/lualib/lfunc.h`
- 24 dòng. Auxiliary functions to manipulate prototypes and closures

## `engine/lualib/lgc.c`
- 353 dòng. Garbage Collector

## `engine/lualib/lgc.h`
- 19 dòng. Garbage Collector

## `engine/lualib/llex.c`
- 380 dòng. Lexical Analyzer

## `engine/lualib/llex.h`
- 81 dòng. Lexical Analyzer

## `engine/lualib/llimits.h`
- 204 dòng. Limits, basic types, and some other "installation-dependent" definitions

## `engine/lualib/lmem.c`
- 150 dòng. Interface to Memory Manager

## `engine/lualib/lmem.h`
- 42 dòng. Interface to Memory Manager

## `engine/lualib/lobject.c`
- 125 dòng. Some generic functions over Lua objects

## `engine/lualib/lobject.h`
- 204 dòng. Type definitions for Lua objects

## `engine/lualib/lopcodes.h`
- 168 dòng. Opcodes for Lua virtual machine

## `engine/lualib/lparser.c`
- 1124 dòng. LL(1) Parser and code generator for Lua

## `engine/lualib/lparser.h`
- 60 dòng. LL(1) Parser and code generator for Lua

## `engine/lualib/lstate.c`
- 120 dòng. Global State

## `engine/lualib/lstate.h`
- 77 dòng. Global State

## `engine/lualib/lstring.c`
- 155 dòng. String table (keeps all strings handled by Lua)

## `engine/lualib/lstring.h`
- 37 dòng. String table (keep all strings handled by Lua)

## `engine/lualib/ltable.c`
- 303 dòng. Lua tables (hash)

## `engine/lualib/ltable.h`
- 34 dòng. Lua tables (hash)

## `engine/lualib/ltests.c`
- 543 dòng. Internal Module for Debugging of the Lua Implementation

## `engine/lualib/ltm.c`
- 163 dòng. Tag methods

## `engine/lualib/ltm.h`
- 59 dòng. Tag methods

## `engine/lualib/lua.c`
- 361 dòng. Lua stand-alone interpreter
- Hàm: `lua_setdebugout`, `lua_outerrmsg`, `lua_outoutmsg`
- Gọi tới: `main`→md5.cpp

## `engine/lualib/lua.h`
- 429 dòng. Lua - An Extensible Extension Language
- Gọi tới: `lua_compilebuffer`→ldo.c, `lua_execute`→ldo.c, `lua_setdebugout`→lua.c, `lua_outoutmsg`→lua.c, `lua_outerrmsg`→lua.c, `Lua_SetTable_StringFromId`→LuaExtend.c, `Lua_SetTable_DoubleFromId`→LuaExtend.c, `Lua_SetTable_IntFromId`→LuaExtend.c, `Lua_SetTable_CFunFromName`→LuaExtend.c, `Lua_SetTable_CFunFromId`→LuaExtend.c, `Lua_SetTable_StringFromName`→LuaExtend.c, `Lua_SetTable_IntFromName`→LuaExtend.c, `Lua_SetTable_DoubleFromName`→LuaExtend.c, `Lua_GetValuesFromStack`→LuaExtend.c

## `engine/lualib/luac.c`
- 203 dòng. lua compiler (saves bytecodes to files; also list binary files)
- Hàm: `main`, `usage`, `doargs`, `load`, `combine`, `strip`, `efopen`, `luaU_testchunk`
- Gọi tới: `main`→md5.cpp, `luaU_dumpchunk`→dump.c, `luaU_undump`→lundump.c

## `engine/lualib/luac.h`
- 31 dòng. definitions for luac
- Gọi tới: `luaU_dumpchunk`→dump.c, `luaU_testchunk`→luac.c

## `engine/lualib/luadebug.h`
- 46 dòng. Debugging API

## `engine/lualib/lundump.c`
- 244 dòng. load bytecodes from files
- Hàm: `ZNAME`, `unexpectedEOZ`, `ezgetc`, `ezread`, `LoadBlock`, `LoadVector`, `LoadInt`, `LoadSize`, `LoadNumber`, `LoadString`, `LoadCode`, `LoadLocals`, `LoadLines`, `LoadConstants`, `LoadFunction`, `LoadSignature`, `TestSize`, `LoadHeader`, `LoadChunk`, `luaU_undump`, `luaU_endianess`

## `engine/lualib/lundump.h`
- 35 dòng. load pre-compiled Lua chunks
- Gọi tới: `luaU_undump`→lundump.c, `luaU_endianess`→lundump.c

## `engine/lualib/lvm.c`
- 710 dòng. Lua virtual machine

## `engine/lualib/lvm.h`
- 32 dòng. Lua virtual machine

## `engine/lualib/lzio.c`
- 84 dòng. a generic input stream interface

## `engine/lualib/lzio.h`
- 53 dòng. Buffered streams

## `engine/lualib/opt.c`
- 127 dòng. optimize bytecodes
- Hàm: `MapConstant`, `MapConstants`, `PackConstants`, `OptConstants`, `OptFunction`

## `engine/lualib/print.c`
- 99 dòng. print bytecodes
- Hàm: `PrintString`, `PrintLocal`, `PrintCode`, `PrintHeader`, `PrintFunction`

## `engine/lualib/print.h`
- 55 dòng. extracted automatically from lopcodes.h by mkprint.lua -- DO NOT EDIT

## `engine/lualib/stubs.c`
- 127 dòng. avoid runtime modules in luac

## `engine/md5.cpp`
- 455 dòng. (không có chú thích đầu)
- Hàm: `main`

## `engine/md5.h`
- 85 dòng. (không có chú thích đầu)

## `engine/ucl/alloc.c`
- 125 dòng. alloc.c -- memory allocation

## `engine/ucl/getbit.h`
- 64 dòng. getbit.h -- bit-buffer access

## `engine/ucl/io.c`
- 105 dòng. io.c -- io functions

## `engine/ucl/n2b_99.c`
- 38 dòng. n2b_99.c -- implementation of the NRV2B-99 compression algorithm

## `engine/ucl/n2b_d.c`
- 178 dòng. n2b_d.c -- implementation of the NRV2B decompression algorithm

## `engine/ucl/n2b_ds.c`
- 40 dòng. n2b_ds.c -- implementation of the NRV2B decompression algorithm

## `engine/ucl/n2b_to.c`
- 79 dòng. n2b_to.c -- implementation of the NRV2B test overlap algorithm

## `engine/ucl/n2d_99.c`
- 38 dòng. n2d_99.c -- implementation of the NRV2D-99 compression algorithm

## `engine/ucl/n2d_d.c`
- 183 dòng. n2d_d.c -- implementation of the NRV2D decompression algorithm

## `engine/ucl/n2d_ds.c`
- 40 dòng. n2d_ds.c -- implementation of the NRV2D decompression algorithm

## `engine/ucl/n2d_to.c`
- 79 dòng. n2d_to.c -- implementation of the NRV2D test overlap algorithm

## `engine/ucl/n2e_99.c`
- 38 dòng. n2e_99.c -- implementation of the NRV2E-99 compression algorithm

## `engine/ucl/n2e_d.c`
- 186 dòng. n2e_d.c -- implementation of the NRV2E decompression algorithm

## `engine/ucl/n2e_ds.c`
- 40 dòng. n2e_ds.c -- implementation of the NRV2E decompression algorithm

## `engine/ucl/n2e_to.c`
- 79 dòng. n2e_to.c -- implementation of the NRV2E test overlap algorithm

## `engine/ucl/ucl.h`
- 249 dòng. ucl.h -- prototypes for the UCL data compression library

## `engine/ucl/ucl_asm.h`
- 320 dòng. ucl_asm.h -- assembler prototypes for the UCL data compression library

## `engine/ucl/ucl_conf.h`
- 218 dòng. ucl_conf.h -- main internal configuration file for the the UCL library

## `engine/ucl/ucl_crc.c`
- 149 dòng. ucl_crc.c -- crc checksum for the the UCL library

## `engine/ucl/ucl_dll.c`
- 61 dòng. ucl_dll.c -- DLL initialization of the UCL library

## `engine/ucl/ucl_init.c`
- 367 dòng. ucl_init.c -- initialization of the UCL library
- Hàm: `__ucl_assert_fail`, `ptr_check`, `schedule_insns_bug`, `strength_reduce_bug`

## `engine/ucl/ucl_ptr.c`
- 81 dòng. ucl_ptr.c -- low-level pointer constructs

## `engine/ucl/ucl_ptr.h`
- 129 dòng. ucl_ptr.h -- low-level pointer constructs

## `engine/ucl/ucl_str.c`
- 58 dòng. ucl_str.c -- string functions for the the UCL library

## `engine/ucl/ucl_util.c`
- 165 dòng. ucl_util.c -- utilities for the UCL library

## `engine/ucl/uclconf.h`
- 439 dòng. uclconf.h -- configuration for the UCL data compression library

## `gamecore/CoreDrawGameObj.cpp`
- 257 dòng. #include "../../Represent/iRepresent/iRepresentshell.h"
- Hàm: `CoreGetGameObjLightInfo`, `CoreDrawGameObj`
- Gọi tới: `Draw`→KLittleMap.cpp, `Paint`→KMissle.cpp, `GetMpsPos`→KMissle.cpp, `GetLocalPositionByMps`→KSubWorld.cpp, `PaintOther`→KNpc.cpp, `FindMemberID`→KPlayerTeam.cpp, `NewMap2Mps`→KSubWorld.cpp, `GetLightInfo`→KMissle.cpp, `ClearOtherNode`→KgameWorld.cpp, `GetNpcPate`→KNpc.cpp, `PaintBlood`→KNpc.cpp, `SetClientSpr`→KNpc.cpp, `DrawBorder`→KNpc.cpp, `ClearObjNode`→KgameWorld.cpp, `DrawInfo`→KObj.cpp

## `gamecore/CoreDrawGameObj.h`
- 12 dòng. 查询对象的光源属性
- Gọi tới: `CoreDrawGameObj`→CoreDrawGameObj.cpp, `CoreGetGameObjLightInfo`→CoreDrawGameObj.cpp

## `gamecore/CoreObjGenreDef.h`
- 63 dòng. Core需要被外引用的物品的类属定义

## `gamecore/CoreShell.cpp`
- 5169 dòng. Íâ½ç·ÃÎÊCore½Ó¿Ú·½·¨
- Hàm: `CoreGetShell`, `KCoreShell::SendNewDataToServer`, `KCoreShell::SetCallDataChangedNofify`, `KCoreShell::setPadCanMove`, `KCoreShell::GetDataDynamicShop`, `KCoreShell::resetPeopledx`, `KCoreShell::getTradeState`, `KCoreShell::TradeApplyStart`, `KCoreShell::__opensysui`, `KCoreShell::ClearClientRoom`, `KCoreShell::__ApplyAddTeam`, `KCoreShell::GetSkillLiveTime`, `KCoreShell::AutoUseSkill`, `KCoreShell::YaBiao`, `KCoreShell::Activate_Ai`, `KCoreShell::Guaji`, `KCoreShell::SetNpcCurPos`, `KCoreShell::GetNpcCurPos`, `KCoreShell::Setpos`, `KCoreShell::GetAutoplayid`, `KCoreShell::AutoChangeItem`, `KCoreShell::clientPickItem`, `KCoreShell::MainAttack`, `KCoreShell::SetRepresentAreaSize`, `KCoreShell::TongOperation` …(+22)
- Gọi tới: `t_sprintf`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `GetInteger`→KTabFile.cpp, `GetSaveVal`→KPlayerTask.cpp, `ClientShowMsg`→KNpc.cpp, `SendSerCommand`→KNpc.cpp, `EGetByte`→Text.cpp, `GetString`→KTabFile.cpp, `GetNextItem`→KInventory.cpp, `GetStringByKeyFromFile`→CXmlStream.cpp, `TEncodeText`→Text.cpp, `CheckTrading`→KPlayer.cpp, `GetID`→KFaction.cpp, `Clear`→KIniFile.cpp, `ApplyUseItem`→KPlayer.cpp

## `gamecore/CoreShell.h`
- 1124 dòng. 外界访问Core接口方法定义
- Gọi tới: `CoreDataChanged`→CoreShell.cpp, `ChannelMessageArrival`→CoreShell.cpp, `MSNMessageArrival`→CoreShell.cpp, `NotifyChannelID`→KgameWorld.cpp, `AddFriend`→KuiFriendListVN.cpp, `Breathe`→CoreShell.cpp, `GetSubGameTime`→CoreShell.cpp, `GetProtocolSize`→CoreShell.cpp, `NetMsgCallbackFunc`→CoreShell.cpp, `OperationRequest`→CoreShell.cpp, `GetGameData`→CoreShell.cpp, `SceneMapOperation`→CoreShell.cpp, `TeamOperation`→CoreShell.cpp, `TongOperation`→CoreShell.cpp, `Goto`→CoreShell.cpp

## `gamecore/CoreUseNameDef.h`
- 459 dòng. Npc部件顺序枚举（必须跟部件配置文件对应）

## `gamecore/GameDataDef.h`
- 2219 dòng. 外界访问Core用到数据结构等的定义
- Gọi tới: `Clear`→KIniFile.cpp, `Init`→KCache.cpp

## `gamecore/ImgRef.cpp`
- 59 dòng. #include "../../Represent/iRepresent/iRepresentShell.h"
- Hàm: `IR_GetCurrentTime`, `IR_UpdateTime`, `IR_IsTimePassed`, `IR_GetRemainTime`, `IR_NextFrame`

## `gamecore/ImgRef.h`
- 8 dòng. extern struct iRepresentShell*	g_pRepresent;
- Gọi tới: `IR_UpdateTime`→ImgRef.cpp, `IR_GetCurrentTime`→ImgRef.cpp, `IR_NextFrame`→ImgRef.cpp

## `gamecore/KBasPropTbl.CPP`
- 2317 dòng. Sword3 Core (c) 2002 by Kingsoft
- Hàm: `KLibOfBPT`, `KLibOfBPT`, `KLibOfBPT::Init`, `KLibOfBPT::InitMAIT`, `KLibOfBPT::InitMALib`, `KLibOfBPT::GetPlatinaRecord`, `KLibOfBPT::GetPlatinaNumber`, `KLibOfBPT::GetGoldItemRecord`, `KLibOfBPT::GetGoldItemNumber`, `KLibOfBPT::GetCMAT`, `KLibOfBPT::GetCMIT`, `KLibOfBPT::GetMARecord`, `KLibOfBPT::GetMARecordNumber`, `KLibOfBPT::GetMeleeWeaponRecord`, `KLibOfBPT::GetMeleeWeaponRecordNumber`, `KLibOfBPT::GetRangeWeaponRecord`, `KLibOfBPT::GetRangeWeaponRecordNumber`, `KLibOfBPT::GetArmorRecord`, `KLibOfBPT::GetArmorRecordNumber`, `KLibOfBPT::GetHelmRecord`, `KLibOfBPT::GetHelmRecordNumber`, `KLibOfBPT::GetBootRecord`, `KLibOfBPT::GetBootRecordNumber`, `KLibOfBPT::GetBeltRecord`, `KLibOfBPT::GetBeltRecordNumber` …(+100)
- Gọi tới: `Init`→KCache.cpp, `Clear`→KIniFile.cpp, `Load`→KIniFile.cpp, `GetInteger`→KTabFile.cpp, `t_sprintf`→KStrBase.cpp, `Insert`→KBinsTree.h, `GetCount`→KMissleSet.cpp, `GetString`→KTabFile.cpp, `g_SetRootPath`→KFilePath.cpp, `g_SetFilePath`→KFilePath.cpp, `g_UnitePathAndName`→KFilePath.cpp

## `gamecore/KBasPropTbl.h`
- 770 dòng. Sword3 Core (c) 2002 by Kingsoft
- Gọi tới: `LoadRecord`→KBasPropTbl.CPP, `GetRecord`→KBasPropTbl.CPP, `FindRecord`→KBasPropTbl.CPP, `Init`→KCache.cpp, `KBasicPropertyTable`→KBasPropTbl.CPP, `GetMemory`→KBasPropTbl.CPP, `ReleaseMemory`→KBasPropTbl.CPP, `KBPT_Mine`→KBasPropTbl.CPP, `KBPT_Medicine`→KBasPropTbl.CPP, `KBPT_Quest`→KBasPropTbl.CPP, `KBPT_Fusion`→KBasPropTbl.CPP, `KBPT_TownPortal`→KBasPropTbl.CPP, `KBPT_MedMaterial`→KBasPropTbl.CPP, `KBPT_Equipment`→KBasPropTbl.CPP, `KBPT_Equipment_Unique`→KBasPropTbl.CPP

## `gamecore/KBuySell.cpp`
- 490 dòng. #include "crtdbg.h"
- Hàm: `KBuySell`, `KBuySell`, `KBuySell::Init`, `KBuySell::GetItemDataByidx`, `KBuySell::GetItemidx`, `KBuySell::GetItemIndex`, `KBuySell::PaintItem`, `KBuySell::PaintItemPai`, `KBuySell::OpenCSuPerShop`, `KBuySell::SetShopItemdata`, `KBuySell::SetShopItemInfo`
- Gọi tới: `GetInteger`→KTabFile.cpp, `Clear`→KIniFile.cpp, `ClientShowMsg`→KNpc.cpp, `Init`→KCache.cpp, `CoreDataChanged`→CoreShell.cpp, `Load`→KIniFile.cpp, `Gen_MineShop`→KItemGenerator.CPP, `Paint`→KMissle.cpp, `SetIndex`→KObj.cpp, `g_SetFilePath`→KFilePath.cpp, `GetName`→KNpcResNode.cpp

## `gamecore/KBuySell.h`
- 58 dòng. 商店商品产生结构
- Gọi tới: `KBuySell`→KBuySell.cpp, `Init`→KCache.cpp, `GetItemidx`→KBuySell.cpp, `GetItemIndex`→KBuySell.cpp, `PaintItem`→KBuySell.cpp, `PaintItemPai`→KBuySell.cpp, `OpenCSuPerShop`→KBuySell.cpp, `SetShopItemInfo`→KBuySell.cpp, `SetShopItemdata`→KBuySell.cpp, `GetItemDataByidx`→KBuySell.cpp

## `gamecore/KCore.cpp`
- 486 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `InitSkillSetting`, `InitMissleSetting`, `InitTaskSetting`, `InitNpcSetting`, `ccMessageBox_new`, `g_ReleaseCore`, `g_InitCore`, `KCore`
- Gọi tới: `Load`→KIniFile.cpp, `Init`→KCache.cpp, `GetInteger`→KTabFile.cpp, `t_sprintf`→KStrBase.cpp, `GetString`→KTabFile.cpp, `Clear`→KIniFile.cpp, `g_InitProtocol`→KProtocol.cpp, `KPIGetExePath`→KCore.h, `CGameClient`→ClientStage.cpp, `Initialize`→KLogFile.cpp, `GetInfoFromTabFile`→KMissle.cpp, `g_SetFilePath`→KFilePath.cpp, `Close`→KFile.cpp, `ClosePlace`→KScenePlaceC.cpp, `Start`→KTimer.cpp

## `gamecore/KCore.h`
- 465 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KPIGetExePath`, `_Rand`, `RandMemSet`
- Gọi tới: `g_Random`→KRandom.cpp, `KCore`→KCore.cpp, `InitSkillSetting`→KCore.cpp, `InitMissleSetting`→KCore.cpp, `InitNpcSetting`→KCore.cpp, `g_ReleaseCore`→KCore.cpp, `ccMessageBox_new`→KCore.cpp, `g_GetStringRes`→KTaskFuns.cpp, `g_InitCodec`→KCodec.cpp, `g_FreeCodec`→KCodec.cpp

## `gamecore/KDropScript.cpp`
- 15 dòng. #include "KDebug.h"

## `gamecore/KDropScript.h`
- 11 dòng. 排序二叉树，保存经过文件名转数字的脚本的id,并实现快速查找对应脚本

## `gamecore/KFaction.cpp`
- 134 dòng. Sword3 Engine (c) 2002 by Kingsoft
- Hàm: `KFaction`, `KFaction`, `KFaction::Init`, `KFaction::GetID`, `KFaction::GetID`, `KFaction::GetCamp`
- Gọi tới: `GetString`→KTabFile.cpp, `g_StrCmp`→KStrBase.cpp, `Init`→KCache.cpp, `Load`→KIniFile.cpp, `t_sprintf`→KStrBase.cpp, `Clear`→KIniFile.cpp

## `gamecore/KFaction.h`
- 41 dòng. Sword3 Engine (c) 2002 by Kingsoft
- Gọi tới: `KFaction`→KFaction.cpp, `GetID`→KFaction.cpp, `Init`→KCache.cpp, `GetCamp`→KFaction.cpp

## `gamecore/KGameglobalSet.cpp`
- 139 dòng. #include "KGameglobalSet.h"
- Hàm: `KGameglobalSet`, `KGameglobalSet::Release`, `KGameglobalSet::Init`
- Gọi tới: `GetInteger`→KTabFile.cpp, `GetInt3`→KIniFile.cpp, `GetInt5`→KIniFile.cpp, `Release`→KCache.cpp, `Init`→KCache.cpp, `GetString`→KTabFile.cpp

## `gamecore/KGameglobalSet.h`
- 107 dòng. (không có chú thích đầu)
- Gọi tới: `KGameglobalSet`→KGameglobalSet.cpp, `Init`→KCache.cpp, `Release`→KCache.cpp

## `gamecore/KGlobalNpcRes.cpp`
- 5 dòng. (không có chú thích đầu)

## `gamecore/KGlobalNpcRes.h`
- 9 dòng. (không có chú thích đầu)

## `gamecore/KIndexNode.h`
- 15 dòng. (không có chú thích đầu)
- Gọi tới: `AddRef`→KRegion.cpp, `Release`→KCache.cpp

## `gamecore/KInventory.cpp`
- 594 dòng. ZeroMemory(m_pArray, sizeof(int) * nWidth * nHeight);
- Hàm: `KInventory`, `KInventory`, `KInventory::Init`, `KInventory::Release`, `KInventory::Clear`, `KInventory::PlaceItem`, `KInventory::DirectSetPosition`, `KInventory::SetEmptyPlaceItemIdx`, `KInventory::HoldItem`, `KInventory::PickUpItem`, `KInventory::SetRoomNull`, `KInventory::FindItem`, `KInventory::GetFreeRoomCount`, `KInventory::FindRoom`, `KInventory::CheckRoom`, `KInventory::AddmClient`, `KInventory::AddxCliet`, `KInventory::GetNextItem`, `KInventory::GetCurIndexItem`, `KInventory::CalcSameDetailType`, `KInventory::FindEmptyPlace`, `KInventory::FindSameDetailType`, `KInventory::CheckSameDetailType`, `KInventory::FindSameGenreItem`
- Gọi tới: `Release`→KCache.cpp, `Init`→KCache.cpp, `Clear`→KIniFile.cpp

## `gamecore/KInventory.h`
- 56 dòng. (không có chú thích đầu)
- Gọi tới: `KInventory`→KInventory.cpp, `Init`→KCache.cpp, `Release`→KCache.cpp, `Clear`→KIniFile.cpp, `PickUpItem`→KInventory.cpp, `SetRoomNull`→KInventory.cpp, `SetEmptyPlaceItemIdx`→KInventory.cpp, `FindItem`→KInventory.cpp, `PlaceItem`→KInventory.cpp, `DirectSetPosition`→KInventory.cpp, `HoldItem`→KInventory.cpp, `FindRoom`→KInventory.cpp, `CheckRoom`→KInventory.cpp, `GetFreeRoomCount`→KInventory.cpp, `AddmClient`→KInventory.cpp

## `gamecore/KItem.cpp`
- 4116 dòng. #include "MyAssert.H"
- Hàm: `KItem::GetTimeItem`, `KItem::CheckItemTime`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `GetInteger`→KTabFile.cpp, `Clear`→KIniFile.cpp, `ModifyAttrib`→KNpc.cpp, `Load`→KIniFile.cpp, `GetString`→KTabFile.cpp, `GetImageParam`→KImageStore2.cpp, `GetDesc`→KMagicDesc.cpp, `TakeRemainder`→KNpc.cpp, `SafeCallBegin`→KLuaScript.cpp, `GetName`→KNpcResNode.cpp, `ccMessageBox_new`→KCore.cpp, `g_GetScript`→KSortScript.cpp, `Remove`→KLinkArray.cpp, `SetIndex`→KObj.cpp

## `gamecore/KItem.h`
- 533 dòng. Sword3 Core (c) 2002 by Kingsoft
- Gọi tới: `t_sprintf`→KStrBase.cpp, `SetID`→KItemSet.cpp, `GetID`→KFaction.cpp, `ExtractChars`→ScriptFuns.cpp, `GetChiBangRes`→KItemChangeRes.cpp, `GetLevel`→KPlayerSet.cpp, `SetSeries`→KNpc.cpp, `GetName`→KNpcResNode.cpp, `Remove`→KLinkArray.cpp, `SetIndex`→KObj.cpp, `GetColor`→KScenePlaceRegionC.cpp, `HoldItem`→KInventory.cpp, `GetScript`→KScriptList.cpp, `SetLevel`→KSkillList.cpp, `GetTimeItem`→KItem.cpp

## `gamecore/KItemChangeRes.cpp`
- 170 dòng. Sword3 Core (c) 2002 by Kingsoft
- Hàm: `KItemChangeRes::GetWeaponRes`, `KItemChangeRes::GetArmorRes`, `KItemChangeRes::GetHelmRes`, `KItemChangeRes::GetPifengRes`, `KItemChangeRes::GetChiBangRes`, `KItemChangeRes::GetHorseRes`
- Gọi tới: `GetInteger`→KTabFile.cpp, `Load`→KIniFile.cpp, `Init`→KCache.cpp

## `gamecore/KItemChangeRes.h`
- 40 dòng. Sword3 Core (c) 2002 by Kingsoft
- Gọi tới: `Init`→KCache.cpp, `GetWeaponRes`→KItemChangeRes.cpp, `GetArmorRes`→KItemChangeRes.cpp, `GetHelmRes`→KItemChangeRes.cpp, `GetPifengRes`→KItemChangeRes.cpp, `GetChiBangRes`→KItemChangeRes.cpp, `GetHorseRes`→KItemChangeRes.cpp

## `gamecore/KItemGenerator.CPP`
- 4155 dòng. Sword3 Core (c) 2002 by Kingsoft
- Hàm: `KItemGenerator`, `KItemGenerator`, `KItemGenerator::Init`, `KItemGenerator::GetMARecord`, `KItemGenerator::GetMedicineCommonAttrib`, `KItemGenerator::GetPlatinaByIndex`, `KItemGenerator::GetGoldItemByIndex`, `KItemGenerator::GetEquipmentCommonAttrib`, `KItemGenerator::Gen_Quest`, `KItemGenerator::Gen_MineShop`
- Gọi tới: `GetInteger`→KTabFile.cpp, `Clear`→KIniFile.cpp, `Load`→KIniFile.cpp, `g_RandomSeed`→KRandom.cpp, `SetSeries`→KNpc.cpp, `g_GetRandomSeed`→KRandom.cpp, `SetLevel`→KSkillList.cpp, `GetMeleeWeaponRecord`→KBasPropTbl.CPP, `GetRangeWeaponRecord`→KBasPropTbl.CPP, `GetArmorRecord`→KBasPropTbl.CPP, `GetHelmRecord`→KBasPropTbl.CPP, `GetBootRecord`→KBasPropTbl.CPP, `GetBeltRecord`→KBasPropTbl.CPP, `GetAmuletRecord`→KBasPropTbl.CPP, `GetRingRecord`→KBasPropTbl.CPP

## `gamecore/KItemGenerator.h`
- 93 dòng. Sword3 Core (c) 2002 by Kingsoft
- Gọi tới: `KItemGenerator`→KItemGenerator.CPP, `Init`→KCache.cpp, `Gen_Quest`→KItemGenerator.CPP, `Gen_MineShop`→KItemGenerator.CPP, `GetEquipmentCommonAttrib`→KItemGenerator.CPP, `GetMedicineCommonAttrib`→KItemGenerator.CPP, `GetGoldItemByIndex`→KItemGenerator.CPP, `GetPlatinaByIndex`→KItemGenerator.CPP, `GetMARecord`→KBasPropTbl.CPP

## `gamecore/KItemList.cpp`
- 5036 dòng. #include	"MyAssert.H"
- Hàm: `KItemList::GetWeaponType`, `KItemList::GetWeaponPhysicDamagePoint`, `KItemList::InAllNextEquip`, `KItemList::DecXu`
- Gọi tới: `FindSame`→KPlayerSet.cpp, `PlaceItem`→KInventory.cpp, `PickUpItem`→KInventory.cpp, `t_sprintf`→KStrBase.cpp, `Remove`→KLinkArray.cpp, `ClientShowMsg`→KNpc.cpp, `CoreDataChanged`→CoreShell.cpp, `Init`→KCache.cpp, `FindItem`→KInventory.cpp, `ccMessageBox_new`→KCore.cpp, `GetLevel`→KPlayerSet.cpp, `Clear`→KIniFile.cpp, `GetNext`→KNode.h, `CheckTrading`→KPlayer.cpp, `GetID`→KFaction.cpp

## `gamecore/KItemList.h`
- 200 dòng. (không có chú thích đầu)
- Gọi tới: `FindFree`→KMissleSet.cpp, `FindSame`→KPlayerSet.cpp, `Init`→KCache.cpp, `GetWeaponType`→KItemList.cpp, `GetWeaponPhysicDamagePoint`→KItemList.cpp, `Remove`→KLinkArray.cpp, `RemoveAll`→KNpcSet.cpp, `ReSkillEnhance`→KNpc.cpp, `GetNextItem`→KInventory.cpp, `SearchID`→KItemSet.cpp, `GetCurIndexItem`→KInventory.cpp, `AddxCliet`→KInventory.cpp, `DecXu`→KItemList.cpp, `SetPlayerIdx`→KNpc.cpp, `StartTrade`→KPlayerTrade.cpp

## `gamecore/KItemSet.cpp`
- 536 dòng. #include "MyAssert.h"
- Hàm: `KItemSet`, `KItemSet`, `KItemSet::Init`, `KItemSet::SearchID`, `KItemSet::Add`, `KItemSet::ReSetItem`, `KItemSet::FindFreeItemSet`, `KItemSet::Remove`, `KItemSet::SetID`, `KItemSet::BackItemInfo`, `KItemSet::GetAbradeRange`
- Gọi tới: `GetInteger`→KTabFile.cpp, `Remove`→KLinkArray.cpp, `Insert`→KBinsTree.h, `Init`→KCache.cpp, `GetNext`→KNode.h, `GetGoldItemByIndex`→KItemGenerator.CPP, `GetPlatinaByIndex`→KItemGenerator.CPP, `Gen_Quest`→KItemGenerator.CPP, `Load`→KIniFile.cpp, `Clear`→KIniFile.cpp, `GetID`→KFaction.cpp

## `gamecore/KItemSet.h`
- 91 dòng. 玩家之间交易进行时，用于判断玩家物品栏能否放下买进的物品
- Gọi tới: `KItemSet`→KItemSet.cpp, `Init`→KCache.cpp, `ReSetItem`→KItemSet.cpp, `SearchID`→KItemSet.cpp, `Remove`→KLinkArray.cpp, `GetAbradeRange`→KItemSet.cpp, `SetID`→KItemSet.cpp, `FindFreeItemSet`→KItemSet.cpp

## `gamecore/KLadder.cpp`
- 120 dòng. 获取排名数据包
- Hàm: `KLadder`, `KLadder`, `KLadder::Init`, `KLadder::TopTenFacMasterHand`, `KLadder::TopTenFacRich`, `KLadder::TopTenFacXu`, `KLadder::TopTenKiller`, `KLadder::TopTenMasterHand`, `KLadder::TopTenRich`, `KLadder::TopTenXu`, `KLadder::GetFacMasterHandPercent`, `KLadder::GetFacMoneyPercent`, `KLadder::GetFacMemberCount`
- Gọi tới: `Init`→KCache.cpp

## `gamecore/KLadder.h`
- 43 dòng. (không có chú thích đầu)
- Gọi tới: `KLadder`→KLadder.cpp, `TopTenRich`→KLadder.cpp, `TopTenXu`→KLadder.cpp, `TopTenMasterHand`→KLadder.cpp, `TopTenKiller`→KLadder.cpp, `TopTenFacRich`→KLadder.cpp, `TopTenFacXu`→KLadder.cpp, `TopTenFacMasterHand`→KLadder.cpp, `GetFacMemberCount`→KLadder.cpp, `GetFacMasterHandPercent`→KLadder.cpp, `GetFacMoneyPercent`→KLadder.cpp, `Init`→KCache.cpp

## `gamecore/KLittleMap.cpp`
- 628 dòng. Sword3 Engine (c) 2003 by Kingsoft
- Hàm: `KLittleMap`, `KLittleMap`, `KLittleMap::Release`, `KLittleMap::Init`, `KLittleMap::GetBarrierBuf`, `KLittleMap::SetHaveLoad`, `KLittleMap::Draw`, `KLittleMap::SetTeammateShow`, `KLittleMap::SetPlayerShow`, `KLittleMap::SetFightNpcShow`, `KLittleMap::SetNormalNpcShow`, `KLittleMap::SetScreenPos`, `KLittleMap::Show`, `KLittleMap::SetShowSize`
- Gọi tới: `KSG_StringGetInt`→KSG_StringProcess.cpp, `KSG_StringSkipSymbol`→KSG_StringProcess.cpp, `DrawPrimitives`→KgameWorld.cpp, `GetString`→KTabFile.cpp, `t_sprintf`→KStrBase.cpp, `GetInteger`→KTabFile.cpp, `Release`→KCache.cpp, `SearchID`→KItemSet.cpp, `Open`→KFile.cpp, `gTraceLogFile`→KLogFile.cpp, `Close`→KFile.cpp, `LoadLittleMapData`→KRegion.cpp, `Init`→KCache.cpp, `g_SetFilePath`→KFilePath.cpp, `Load`→KIniFile.cpp

## `gamecore/KLittleMap.h`
- 71 dòng. Sword3 Engine (c) 2003 by Kingsoft
- Gọi tới: `KLittleMap`→KLittleMap.cpp, `Release`→KCache.cpp, `Init`→KCache.cpp, `GetBarrierBuf`→KLittleMap.cpp, `SetHaveLoad`→KLittleMap.cpp, `Draw`→KLittleMap.cpp, `SetTeammateShow`→KLittleMap.cpp, `SetPlayerShow`→KLittleMap.cpp, `SetFightNpcShow`→KLittleMap.cpp, `SetNormalNpcShow`→KLittleMap.cpp, `SetScreenPos`→KLittleMap.cpp, `Show`→KLittleMap.cpp, `SetShowSize`→KLittleMap.cpp

## `gamecore/KLogFile.cpp`
- 362 dòng. #ifdef _DEBUG
- Hàm: `CLogFile`, `CLogFile::Initialize`, `CLogFile::Uninitialize`, `CLogFile::TraceLog`, `CLogFile::PrepareFile`, `CLogFile::BeginBatch`, `CLogFile::EndBatch`, `CLogFile::IsBatched`, `CLogFile::OpenUniDirectory`, `CLogFile::CreateUniFile`, `CLogFile::sLogProgram`, `CLogFile::gTimeStamp`, `CLogFile::gTraceLogFile`
- Gọi tới: `CloseHandle`→KScenePlaceC.cpp, `t_sprintf`→KStrBase.cpp, `_ccHash`→KStrBase.cpp, `Start`→KTimer.cpp, `Stop`→KLuaScript.cpp

## `gamecore/KLogFile.h`
- 56 dòng. LogFile.h: interface for the CLogFile class.
- Gọi tới: `CLogFile`→KLogFile.cpp, `Initialize`→KLogFile.cpp, `Uninitialize`→KLogFile.cpp, `BeginBatch`→KLogFile.cpp, `EndBatch`→KLogFile.cpp, `IsBatched`→KLogFile.cpp, `sLogProgram`→KLogFile.cpp, `gTraceLogFile`→KLogFile.cpp, `PrepareFile`→KLogFile.cpp, `OpenUniDirectory`→KLogFile.cpp, `CreateUniFile`→KLogFile.cpp, `gTimeStamp`→KLogFile.cpp, `TraceLog`→KLogFile.cpp

## `gamecore/KMagicAttrib.h`
- 375 dòng. 枚举类型最后一个字母表示该数值的类型，v为整型，直接加的点数，p为百分比，b为布尔型

## `gamecore/KMagicDesc.cpp`
- 1010 dòng. 改变技能的属性
- Hàm: `KMagicDesc`, `KMagicDesc`, `KMagicDesc::Init`, `KMagicDesc::scat`, `KMagicDesc::GetDesc_New`, `KMagicDesc::GetDesc`, `g_String2MagicID`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `GetStringByKeyFromFile`→CXmlStream.cpp, `GetSkillName`→KThiefSkill.cpp, `Load`→KIniFile.cpp, `GetString`→KTabFile.cpp, `GetSkill`→KSkillManager.h, `Init`→KCache.cpp, `g_SetFilePath`→KFilePath.cpp, `g_StrCmp`→KStrBase.cpp

## `gamecore/KMagicDesc.h`
- 21 dòng. (không có chú thích đầu)
- Gọi tới: `KMagicDesc`→KMagicDesc.cpp, `Init`→KCache.cpp, `scat`→KMagicDesc.cpp, `GetDesc`→KMagicDesc.cpp, `GetDesc_New`→KMagicDesc.cpp

## `gamecore/KMapMusic.cpp`
- 610 dòng. Sword3 Engine (c) 2003 by Kingsoft
- Hàm: `KMapMusic`, `KMapMusic`, `KMapMusic::Release`, `KMapMusic::LoadSetFile`, `KMapMusic::Init`, `KMapMusic::Play`, `KMapMusic::Stop`, `KMapMusic::SetGameVolume`, `KMapMusic::SetWeatherVolume`, `KMapMusic::Start`, `KMapMusic::ScriptPlay`, `KMapMusic::CreateFolder`, `KMapMusic::downLoadAllMapmusic`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `GetInteger`→KTabFile.cpp, `__replaceNmae`→KStrBase.cpp, `Release`→KCache.cpp, `Start`→KTimer.cpp, `g_SetFilePath`→KFilePath.cpp, `Load`→KIniFile.cpp, `GetString`→KTabFile.cpp, `Clear`→KIniFile.cpp, `g_Random`→KRandom.cpp, `ccMessageBox_new`→KCore.cpp, `Init`→KCache.cpp, `Stop`→KLuaScript.cpp, `pGetFilePath`→KPakList.cpp, `ElemFileRead`→KPakList.cpp

## `gamecore/KMapMusic.h`
- 104 dòng. Sword3 Engine (c) 2003 by Kingsoft
- Gọi tới: `KMapMusic`→KMapMusic.cpp, `LoadSetFile`→KMapMusic.cpp, `Init`→KCache.cpp, `Play`→KMapMusic.cpp, `Stop`→KLuaScript.cpp, `Start`→KTimer.cpp, `SetGameVolume`→KMapMusic.cpp, `SetWeatherVolume`→KMapMusic.cpp, `ScriptPlay`→KMapMusic.cpp, `downLoadAllMapmusic`→KMapMusic.cpp, `Release`→KCache.cpp, `CreateFolder`→KMapMusic.cpp

## `gamecore/KMath.cpp`
- 163 dòng. 正弦表 (将浮点数 *1024 整型化)
- Hàm: `g_InitSeries`, `g_InitSeries`

## `gamecore/KMath.h`
- 376 dòng. 正弦表 (将浮点数 *1024 整型化)
- Hàm: `g_DirSin`, `g_DirCos`, `g_IsConquer`, `qsqrt`, `g_GetNewDistance`, `g_GetDistance`, `g_GetLength`, `g_Square`, `g_GetDisSquare`, `g_GetNewDirIndex`, `g_GetOldDirIndex`, `g_GetDirIdxForFindPath`, `g_GetDirIndex`, `g_Dir2DirIndex`, `g_DirIndex2Dir`, `g_RandPercent`
- Gọi tới: `g_Random`→KRandom.cpp, `g_InitSeries`→KMath.cpp

## `gamecore/KMissle.cpp`
- 2229 dòng. Revision Count	:
- Hàm: `KMissle`, `KMissle::Release`, `KMissle`, `KMissle::GetInfoFromTabFile`, `KMissle::GetInfoFromTabFile`, `KMissle::Init`, `KMissle::drawSpecial`, `KMissle::Activate`, `KMissle::OnWait`, `KMissle::OnCollision`, `KMissle::FsCheckCollision`, `KMissle::GetCurrentSubWorldTime`, `KMissle::OnFly`, `KMissle::OnVanish`, `KMissle::Paint`, `KMissle::CheckBeyondRegion`, `KMissle::ProcessDamage`, `KMissle::DoVanish`, `KMissle::DoCollision`, `KMissle::DoFly`, `KMissle::ProcessCollision`, `KMissle::ProcessCollision`, `KMissle::CreateSpecialEffect`, `KMissle::CreateMissleForShow`, `KMissle::GetLightInfo` …(+5)
- Gọi tới: `GetInteger`→KTabFile.cpp, `NewMap2Mps`→KSubWorld.cpp, `g_DirCos`→KMath.h, `g_DirSin`→KMath.h, `t_sprintf`→KStrBase.cpp, `KSG_StringGetInt`→KSG_StringProcess.cpp, `NewSend`→KWorldMsg.h, `GetString`→KTabFile.cpp, `Remove`→KLinkArray.cpp, `KSG_StringSkipSymbol`→KSG_StringProcess.cpp, `g_DirIndex2Dir`→KMath.h, `DecRef`→KRegion.cpp, `MissleChangeRegion`→KSubWorld.cpp, `MoveObject`→KgameWorld.cpp, `GetDistance`→KSubWorld.cpp

## `gamecore/KMissle.h`
- 237 dòng. KMissle.h: interface for the KMissle class.
- Gọi tới: `ProcessCollision`→KMissle.cpp, `TestBarrier`→KSubWorld.cpp, `KMissle`→KMissle.cpp, `GetInfoFromTabFile`→KMissle.cpp, `Init`→KCache.cpp, `OnVanish`→KMissle.cpp, `OnCollision`→KMissle.cpp, `OnFly`→KMissle.cpp, `OnWait`→KMissle.cpp, `DoWait`→KMissle.cpp, `DoFly`→KMissle.cpp, `PrePareFly`→KMissle.cpp, `DoVanish`→KMissle.cpp, `DoCollision`→KMissle.cpp, `CheckNearestCollision`→KMissle.cpp

## `gamecore/KMissleMagicAttribsData.cpp`
- 7 dòng. Revision Count	:

## `gamecore/KMissleMagicAttribsData.h`
- 81 dòng. if (m_pStateMagicAttribs != NULL)		delete m_pStateMagicAttribs;
- Gọi tới: `Remove`→KLinkArray.cpp, `AddRef`→KRegion.cpp, `GetRef`→KRegion.cpp

## `gamecore/KMissleRes.cpp`
- 331 dòng. Revision Count	:	子弹绘画
- Hàm: `KMissleRes`, `KMissleRes`, `KMissleRes::LoadResource`, `KMissleRes::Init`, `KMissleRes::Remove`, `KMissleRes::Clear`, `KMissleRes::Draw`, `KMissleRes::PlaySound`, `KMissleRes::GetSndVolume`, `KMissleRes::StopSound`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `Remove`→KLinkArray.cpp, `GetHead`→KList.h, `GetTail`→KList.h, `Clear`→KIniFile.cpp, `GetNext`→KNode.h, `RemoveTail`→KList.h, `Init`→KCache.cpp, `RemoveHead`→KList.h, `Draw`→KLittleMap.cpp, `g_SetFilePath`→KFilePath.cpp, `g_GetFullPath`→KFilePath.cpp, `g_StrCpy`→KStrBase.cpp, `getIniDataForGame`→KgameWorld.cpp, `DrawPrimitives_miss`→KgameWorld.cpp

## `gamecore/KMissleRes.h`
- 87 dòng. Revision Count	:
- Gọi tới: `KMissleRes`→KMissleRes.cpp, `Init`→KCache.cpp, `Remove`→KLinkArray.cpp, `Clear`→KIniFile.cpp, `LoadResource`→KMissleRes.cpp, `Draw`→KLittleMap.cpp, `PlaySound`→KMissleRes.cpp, `GetSndVolume`→KMissleRes.cpp, `StopSound`→KMissleRes.cpp, `GetHead`→KList.h

## `gamecore/KMissleSet.cpp`
- 156 dòng. 开始时所有的数组元素都为空
- Hàm: `KMissleSet::Init`, `KMissleSet::FindFree`, `KMissleSet::Add`, `KMissleSet::Add`, `KMissleSet::CreateMissile`, `KMissleSet::Activate`, `KMissleSet::Remove`, `KMissleSet::Draw`, `KMissleSet::GetCount`, `KMissleSet::ClearMissles`
- Gọi tới: `Remove`→KLinkArray.cpp, `Init`→KCache.cpp, `Insert`→KBinsTree.h, `GetNext`→KNode.h, `AddMissle`→KRegion.cpp, `Activate`→KScriptList.cpp, `Mps2Map`→KSubWorld.cpp, `Send`→KWorldMsg.h, `AddRef`→KRegion.cpp, `Release`→KCache.cpp, `Draw`→KLittleMap.cpp, `Paint`→KMissle.cpp

## `gamecore/KMissleSet.h`
- 23 dòng. (không có chú thích đầu)
- Gọi tới: `Init`→KCache.cpp, `Activate`→KScriptList.cpp, `FindFree`→KMissleSet.cpp, `CreateMissile`→KMissleSet.cpp, `Remove`→KLinkArray.cpp, `ClearMissles`→KMissleSet.cpp, `GetCount`→KMissleSet.cpp, `Draw`→KLittleMap.cpp

## `gamecore/KNpc.cpp`
- 11386 dòng. Sword3 KNpc.cpp
- Hàm: `KNpc`, `KNpc`, `KNpc::GetActiveSkillByIndex`, `KNpc::GetActiveSkill`, `KNpc::SetCurrentCamp`, `KNpc::SetCamp`, `KNpc::RestoreCurrentCamp`, `KNpc::TakeRemainder`, `KNpc::Activate`, `KNpc::ProcStatus`, `KNpc::ProcessState`, `KNpc::GetSkillLeftTime`, `KNpc::SetSkillLeftTime`, `KNpc::ClearOneSkillState`, `KNpc::DoDeath`, `KNpc::OnDeath`, `KNpc::DoIdle`, `KNpc::OnIdle`, `KNpc::DoDrag`, `KNpc::OnDrag`, `KNpc::MovePos`, `KNpc::DoHurt`, `KNpc::SetPos`, `KNpc::OnHurt`, `KNpc::DoSpecial1` …(+168)
- Gọi tới: `GetInteger`→KTabFile.cpp, `t_sprintf`→KStrBase.cpp, `TGetColor`→Text.cpp, `g_Random`→KRandom.cpp, `GetMpsPos`→KMissle.cpp, `g_StrLen`→KStrBase.cpp, `GetSaveVal`→KPlayerTask.cpp, `GetSkill`→KSkillManager.h, `SetBlur`→KNpcRes.cpp, `FindSame`→KPlayerSet.cpp, `NewMap2Mps`→KSubWorld.cpp, `DirectAddExp`→KPlayer.cpp, `Remove`→KLinkArray.cpp, `EGetByte`→Text.cpp, `DecRef`→KRegion.cpp

## `gamecore/KNpc.h`
- 1113 dòng. #include <hash_map>
- Gọi tới: `t_sprintf`→KStrBase.cpp, `KNpc`→KNpc.cpp, `SetNpcState`→KNpc.cpp, `UseSkills`→KNpc.cpp, `PaintHonor`→KNpc.cpp, `WaitForFrame`→KNpc.cpp, `IsReachFrame`→KNpc.cpp, `DoStand`→KNpc.cpp, `OnStand`→KNpc.cpp, `DoWait`→KMissle.cpp, `OnWait`→KMissle.cpp, `DoWalk`→KNpc.cpp, `OnWalk`→KNpc.cpp, `DoRun`→KNpc.cpp, `OnRun`→KNpc.cpp

## `gamecore/KNpcAI.cpp`
- 5811 dòng. #include "KCore.h"
- Hàm: `KNpcAI`, `KNpcAI`, `KNpcAI::Activate_New`, `KNpcAI::Activate`, `KNpcAI::ProcessShowNpc`, `KNpcAI::ShowNpcType11`, `KNpcAI::ShowNpcType12`, `KNpcAI::ShowNpcType13`, `KNpcAI::ShowNpcType14`, `KNpcAI::ShowNpcType15`, `KNpcAI::ShowNpcType16`, `KNpcAI::ShowNpcType17`, `KNpcAI::ProcessPlayer`, `KNpcAI::FollowObject`, `KNpcAI::FollowPeople`, `KNpcAI::Setscpos`, `KNpcAI::SetCurpos`, `KNpcAI::MoveJiaoBen`, `KNpcAI::MoveYaBiao`, `KNpcAI::FollowCharacter`, `KNpcAI::AutoMovePickUp`, `KNpcAI::FollowAttackCharacter`, `KNpcAI::AiCheckDistance`, `KNpcAI::GetNearestCharacter`, `KNpcAI::GetNearestObject` …(+36)
- Gọi tới: `SetActiveSkill`→KNpc.cpp, `g_RandPercent`→KMath.h, `SendSerCommand`→KNpc.cpp, `GetMpsPos`→KMissle.cpp, `GetInteger`→KTabFile.cpp, `g_Random`→KRandom.cpp, `ClientShowMsg`→KNpc.cpp, `GetDistance`→KSubWorld.cpp, `t_sprintf`→KStrBase.cpp, `SendClientCmdRun`→KProtocol.cpp, `GetGoldType`→KNpcGold.cpp, `SendClientCmdWalk`→KProtocol.cpp, `SendClientCmdRide`→KProtocol.cpp, `GetNpcMoveOffset`→KNpcAI.h, `FindNameID`→KPlayerSet.cpp

## `gamecore/KNpcAI.h`
- 151 dòng. #include "KBasPropTbl.h"
- Hàm: `KNpcAI::GetNpcMoveOffset`, `KNpcAI::CanShowNpc`
- Gọi tới: `KNpcAI`→KNpcAI.cpp, `CommonActionWithPlayer`→KNpcAI.cpp, `Activate_New`→KNpcAI.cpp, `Activate`→KScriptList.cpp, `FollowCharacter`→KNpcAI.cpp, `Setscpos`→KNpcAI.cpp, `MoveYaBiao`→KNpcAI.cpp, `AiCheckDistance`→KNpcAI.cpp, `GetNearestObject`→KNpcAI.cpp, `GetNearestCharacter`→KNpcAI.cpp, `GetNearestNpc`→KNpcAI.cpp, `GetNearestObj`→KNpcAI.cpp, `ReMoveCommonAction`→KNpcAI.cpp, `MoveJiaoBen`→KNpcAI.cpp, `SetCurpos`→KNpcAI.cpp

## `gamecore/KNpcAttribModify.cpp`
- 3809 dòng. (không có chú thích đầu)
- Hàm: `KNpcAttribModify`, `KNpcAttribModify`, `KNpcAttribModify::ModifyAttrib`, `KNpcAttribModify::AllresP`, `KNpcAttribModify::AllSkillV`, `KNpcAttribModify::Ignoredefense_p`, `KNpcAttribModify::AttackRatingP`, `KNpcAttribModify::AttackRatingV`, `KNpcAttribModify::AddAttackRatingV`, `KNpcAttribModify::AddAttackRatingP`, `KNpcAttribModify::lightingres_yan_p`, `KNpcAttribModify::fireres_yan_p`, `KNpcAttribModify::physicsres_yan_p`, `KNpcAttribModify::poisonres_yan_p`, `KNpcAttribModify::lifemax_yan_p`, `KNpcAttribModify::lifemax_yan_v`, `KNpcAttribModify::coldres_yan_p`, `KNpcAttribModify::manamax_yan_v`, `KNpcAttribModify::manamax_yan_p`, `KNpcAttribModify::sorbdamage_yan_p`, `KNpcAttribModify::fastwalkrun_yan_p`, `KNpcAttribModify::attackspeed_yan_v`, `KNpcAttribModify::castspeed_yan_v`, `KNpcAttribModify::allres_yan_p`, `KNpcAttribModify::fasthitrecover_yan_v` …(+186)
- Gọi tới: `GetCurrentLevelByIdx`→KSkillList.cpp, `TakeRemainder`→KNpc.cpp, `FindSame`→KPlayerSet.cpp, `IsPlayer`→KNpc.cpp, `CheckNoSkill`→KSkillList.cpp, `ClientShowMsg`→KNpc.cpp, `GetCurrentLevel`→KSkillList.cpp, `GetInteger`→KTabFile.cpp, `ModifyAttrib`→KNpc.cpp, `IncreaseLevel`→KSkillList.cpp, `Load`→KIniFile.cpp, `Clear`→KIniFile.cpp, `ChangeCurDexterity`→KPlayer.cpp, `ChangeCurEngergy`→KPlayer.cpp, `ChangeCurStrength`→KPlayer.cpp

## `gamecore/KNpcAttribModify.h`
- 257 dòng. (không có chú thích đầu)
- Gọi tới: `KNpcAttribModify`→KNpcAttribModify.cpp, `ModifyAttrib`→KNpc.cpp, `MixPoisonDamage`→KNpcAttribModify.cpp, `AllResMaxP`→KNpcAttribModify.cpp, `PhysicsResMaxP`→KNpcAttribModify.cpp, `ColdResMaxP`→KNpcAttribModify.cpp, `FireResMaxP`→KNpcAttribModify.cpp, `LightingResMaxP`→KNpcAttribModify.cpp, `PoisonResMaxP`→KNpcAttribModify.cpp, `LifePotionV`→KNpcAttribModify.cpp, `ManaPotionV`→KNpcAttribModify.cpp, `PoisonEnhanceP`→KNpcAttribModify.cpp, `LightingEnhanceP`→KNpcAttribModify.cpp, `FireEnhanceP`→KNpcAttribModify.cpp, `ColdEnhanceP`→KNpcAttribModify.cpp

## `gamecore/KNpcDeathCalcExp.cpp`
- 61 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KNpcDeathCalcExp::Init`, `KNpcDeathCalcExp::Active`, `KNpcDeathCalcExp::Clear`
- Gọi tới: `Init`→KCache.cpp, `Active`→KStepLuaScript.cpp, `GetDistanceSquare`→KNpcSet.cpp, `GetInteger`→KTabFile.cpp, `Clear`→KIniFile.cpp

## `gamecore/KNpcDeathCalcExp.h`
- 35 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `Init`→KCache.cpp, `Active`→KStepLuaScript.cpp, `Clear`→KIniFile.cpp

## `gamecore/KNpcFindPath.cpp`
- 390 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KNpcFindPath`, `KNpcFindPath::Init`, `KNpcFindPath::GetDir`, `KNpcFindPath::Dir64To8`, `KNpcFindPath::Dir8To64`, `KNpcFindPath::CheckDistance`, `KNpcFindPath::CheckBarrier`, `KNpcFindPath::CheckBarrierMin`, `KNpcFindPath::CheckBarrier`
- Gọi tới: `g_DirCos`→KMath.h, `g_DirSin`→KMath.h, `IsPlayer`→KNpc.cpp, `TestBarrier`→KSubWorld.cpp, `TestBarrierMin`→KSubWorld.cpp, `GetBarrierMin`→KRegion.cpp, `ClientShowMsg`→KNpc.cpp, `Init`→KCache.cpp, `g_GetDirIndex`→KMath.h

## `gamecore/KNpcFindPath.h`
- 42 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `KNpcFindPath`→KNpcFindPath.cpp, `Init`→KCache.cpp, `GetDir`→KNpcFindPath.cpp, `Dir64To8`→KNpcFindPath.cpp, `Dir8To64`→KNpcFindPath.cpp, `CheckDistance`→KNpcFindPath.cpp, `CheckBarrierMin`→KNpcFindPath.cpp, `CheckBarrier`→KNpcFindPath.cpp

## `gamecore/KNpcGold.cpp`
- 450 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KNpcGold::Init`, `KNpcGold::SetGoldType`, `KNpcGold::SetGoldTypeAndBackData`, `KNpcGold::SetBossTypeAndBackData`, `KNpcGold::RecoverBackData`, `KNpcGold::GetGoldNpcLevelDataFromScript`, `KNpcGold::GetGoldType`, `KNpcGold::SetGoldCurrentType`, `KNpcGold::ClientClearState`, `KNpcGoldTemplate`, `KNpcGoldTemplate::Init`
- Gọi tới: `GetInteger`→KTabFile.cpp, `g_Random`→KRandom.cpp, `Init`→KCache.cpp, `GetString`→KTabFile.cpp, `t_sprintf`→KStrBase.cpp, `SafeCallBegin`→KLuaScript.cpp, `CallFunction`→KLuaScript.cpp, `SafeCallEnd`→KLuaScript.cpp, `g_SetFilePath`→KFilePath.cpp, `Load`→KIniFile.cpp, `SkillString2Id`→KNpcTemplate.cpp, `Clear`→KIniFile.cpp

## `gamecore/KNpcGold.h`
- 152 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `SkillString2Id`→KNpcTemplate.cpp, `Init`→KCache.cpp, `GetGoldNpcLevelDataFromScript`→KNpcGold.cpp, `SetGoldType`→KNpcGold.cpp, `SetGoldTypeAndBackData`→KNpcGold.cpp, `SetBossTypeAndBackData`→KNpcGold.cpp, `RecoverBackData`→KNpcGold.cpp, `GetGoldType`→KNpcGold.cpp, `SetGoldCurrentType`→KNpcGold.cpp, `ClientClearState`→KNpcGold.cpp, `KNpcGoldTemplate`→KNpcGold.cpp

## `gamecore/KNpcRes.cpp`
- 2993 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KNpcRes`, `KNpcRes::Init`, `KNpcRes::SetPos`, `KNpcRes::Remove`, `KNpcRes::Draw`, `KNpcRes::GetShadowName`, `KNpcRes`, `KNpcRes::SetPifeng`, `KNpcRes::SetChiBang`, `KNpcRes::SetHelm`, `KNpcRes::SetArmor`, `KNpcRes::SetWeapon`, `KNpcRes::SetHorse`, `KNpcRes::SetAction`, `KNpcRes::SetDoing`, `KNpcRes::UpdateAction`, `KNpcRes::UpdateActionNormal`, `KNpcRes::ChangeFeature`, `KNpcRes::SetPartInfo`, `KNpcRes::SetRideHorse`, `KNpcRes::SetSprState`, `KNpcRes::SetState`, `KNpcRes::SetState`, `KNpcRes::SetClientState`, `KNpcRes::SetClientSpr` …(+33)
- Gọi tới: `Release`→KCache.cpp, `SetSprFile`→KSprControl.cpp, `GetTotalFrames`→KNpcResNode.cpp, `CheckPartExist`→KNpcResNode.cpp, `GetFileName`→KNpcResNode.cpp, `GetTotalDirs`→KNpcResNode.cpp, `GetInterval`→KTimer.cpp, `getIniDataForGame`→KgameWorld.cpp, `GetNextFrame`→KSprControl.cpp, `Remove`→KLinkArray.cpp, `DrawPrimitives`→KgameWorld.cpp, `SetCurFrame`→KSprControl.cpp, `t_sprintf`→KStrBase.cpp, `GetFile`→KNpcResNode.cpp, `SetCenterPos`→KSprControl.cpp

## `gamecore/KNpcRes.h`
- 193 dòng. using namespace cocos2d::experimental;
- Gọi tới: `KNpcBlur`→KNpcRes.cpp, `Init`→KCache.cpp, `Remove`→KLinkArray.cpp, `clearBlur`→KNpcRes.cpp, `Draw`→KLittleMap.cpp, `KNpcRes`→KNpcRes.cpp, `SetState`→KNpcRes.cpp, `KStateSpr`→KNpcRes.cpp, `Release`→KCache.cpp, `SetNextNo`→KNpcRes.cpp, `SetMapPos`→KNpcRes.cpp, `ChangeAlpha`→KNpcRes.cpp, `ClearCurNo`→KNpcRes.cpp, `SetFile`→KNpcRes.cpp, `NowGetBlur`→KNpcRes.cpp

## `gamecore/KNpcResList.cpp`
- 156 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KNpcResList`, `KNpcResList`, `KNpcResList::Init`, `KNpcResList::FindNpcRes`, `KNpcResList::AddNpcRes`, `KNpcResList::ClearOneNpcRes`, `KNpcResList::ClearAllNpcRes`
- Gọi tới: `Init`→KCache.cpp, `GetHead`→KList.h, `GetNext`→KNode.h, `g_StrCmp`→KStrBase.cpp, `AddTail`→KList.h

## `gamecore/KNpcResList.h`
- 41 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `KNpcResList`→KNpcResList.cpp, `FindNpcRes`→KNpcResList.cpp, `Init`→KCache.cpp, `AddNpcRes`→KNpcResList.cpp, `ClearAllNpcRes`→KNpcResList.cpp, `ClearOneNpcRes`→KNpcResList.cpp

## `gamecore/KNpcResNode.cpp`
- 1483 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KNpcResNode`, `KNpcResNode`, `KNpcResNode::Init`, `KNpcResNode::ComposePathAndName`, `KNpcResNode::CheckPartExist`, `KNpcResNode::GetFileName`, `KNpcResNode::GetInterval`, `KNpcResNode::GetTotalFrames`, `KNpcResNode::GetTotalDirs`, `KNpcResNode::GetActNo`, `KNpcResNode::GetnSort`, `KNpcResNode::GetActionSoundName`, `KNpcResNode::GetShadowName`, `CActionName`, `CActionName::Init`, `CActionName::GetActionNo`, `CActionName::GetActionCount`, `CActionName::GetActionName`, `CShadowFileName`, `CShadowFileName`, `CShadowFileName::Init`, `CShadowFileName::GetFile`, `CStateMagicTable`, `CStateMagicTable::Init`, `CStateMagicTable::GetInfo` …(+21)
- Gọi tới: `GetString`→KTabFile.cpp, `Clear`→KIniFile.cpp, `Load`→KIniFile.cpp, `ccMessageBox_new`→KCore.cpp, `g_SetFilePath`→KFilePath.cpp, `t_sprintf`→KStrBase.cpp, `KSG_StringGetInt`→KSG_StringProcess.cpp, `g_UnitePathAndName`→KFilePath.cpp, `GetInteger`→KTabFile.cpp, `KSG_StringSkipSymbol`→KSG_StringProcess.cpp, `Init`→KCache.cpp, `g_StrCmp`→KStrBase.cpp, `Release`→KCache.cpp, `FindRow`→KTabFile.cpp, `g_StrCpyLen`→KStrBase.cpp

## `gamecore/KNpcResNode.h`
- 253 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `Init`→KCache.cpp, `Clear`→KIniFile.cpp, `CShadowFileName`→KNpcResNode.cpp, `CRESINFO`→KNpcResNode.cpp, `AutoDelete`→KNpcResNode.cpp, `AutoNew`→KNpcResNode.cpp, `GetInterval`→KTimer.cpp, `GetTotalFrames`→KNpcResNode.cpp, `GetTotalDirs`→KNpcResNode.cpp, `CEquipStyleTable`→KNpcResNode.cpp, `CSortTable`→KNpcResNode.cpp, `KNpcResNode`→KNpcResNode.cpp, `CActionName`→KNpcResNode.cpp, `GetActionNo`→KNpcResNode.cpp, `GetActionCount`→KNpcResNode.cpp

## `gamecore/KNpcSet.cpp`
- 1899 dòng. #include "Scene/KScenePlaceC.h"
- Hàm: `KNpcSet`, `KNpcSet::Release`, `KNpcSet::Init`, `KNpcSet::LoadPlayerBaseValue`, `KNpcSet::IsNpcExist`, `KNpcSet::GenOneRelation`, `KNpcSet::GenRelationTable`, `KNpcSet::SearchByTongName`, `KNpcSet::SearchID`, `KNpcSet::SearchClientID`, `KNpcSet::SearchName`, `KNpcSet::SearchGSNameInMap`, `KNpcSet::SearchNameInMap`, `KNpcSet::SearchNpcSettingID`, `KNpcSet::DelNpcInNpcSet`, `KNpcSet::SearchGSName`, `KNpcSet::SearchNameID`, `KNpcSet::FindFreeNpcSet`, `KNpcSet::AddClientNpc`, `KNpcSet::AddMapNpc`, `KNpcSet::AddServerNpcA`, `KNpcSet::Addyabiao`, `KNpcSet::AddTongBan`, `KNpcSet::AddServerNpcB`, `KNpcSet::Remove` …(+35)
- Gọi tới: `GetNext`→KNode.h, `GetInteger`→KTabFile.cpp, `Remove`→KLinkArray.cpp, `Init`→KCache.cpp, `Insert`→KBinsTree.h, `t_sprintf`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `Load`→KIniFile.cpp, `Mps2Map`→KSubWorld.cpp, `g_StrCpyLen`→KStrBase.cpp, `NewMap2Mps`→KSubWorld.cpp, `GetNormalPKState`→KPlayerPK.cpp, `Clear`→KIniFile.cpp, `g_StrCmp`→KStrBase.cpp, `g_FileName2Id`→KFilePath.cpp

## `gamecore/KNpcSet.h`
- 197 dòng. KWavSound	*m_pWave;		// 声效wav指针
- Gọi tới: `LoadSprName`→KNpcSet.cpp, `LoadSoundName`→KNpcSet.cpp, `KInstantSpecial`→KNpcSet.cpp, `GetSprName`→KNpcSet.cpp, `PlaySound`→KMissleRes.cpp, `KNpcSet`→KNpcSet.cpp, `Init`→KCache.cpp, `Release`→KCache.cpp, `SearchName`→KNpcSet.cpp, `SearchNameInMap`→KNpcSet.cpp, `SearchGSNameInMap`→KNpcSet.cpp, `SearchNpcSettingID`→KNpcSet.cpp, `SearchByTongName`→KNpcSet.cpp, `SearchID`→KItemSet.cpp, `DelNpcInNpcSet`→KNpcSet.cpp

## `gamecore/KNpcTemplate.cpp`
- 155 dòng. #include "KDropScript.h"
- Hàm: `KNpcTemplate::InitNpcBaseData`, `KNpcTemplate::InitNpcLevelData`, `KNpcTemplate::GetNpcLevelDataFromScript`, `KNpcTemplate::GetNpcKeyDataFromScript`, `KNpcTemplate::SkillString2Id`
- Gọi tới: `GetInteger`→KTabFile.cpp, `SafeCallBegin`→KLuaScript.cpp, `GetString`→KTabFile.cpp, `GetDouble`→KTabFile.cpp, `SafeCallEnd`→KLuaScript.cpp, `t_sprintf`→KStrBase.cpp, `CallFunction`→KLuaScript.cpp, `g_StrCmp`→KStrBase.cpp

## `gamecore/KNpcTemplate.h`
- 69 dòng. #include "KBinTreeNode.h"
- Gọi tới: `InitNpcBaseData`→KNpcTemplate.cpp, `InitNpcLevelData`→KNpcTemplate.cpp, `GetNpcLevelDataFromScript`→KNpcTemplate.cpp, `GetNpcKeyDataFromScript`→KNpcTemplate.cpp, `SkillString2Id`→KNpcTemplate.cpp

## `gamecore/KObj.cpp`
- 1171 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KObj`, `KObj::Release`, `KObj::Save`, `KObj::Load`, `KObj::SetIndex`, `KObj::SetWorldID`, `KObj::SetLifeTime`, `KObj::SetState`, `KObj::BoxOpen`, `KObj::BoxClose`, `KObj::DoorOpen`, `KObj::DoorClose`, `KObj::SetDir`, `KObj::SetScriptFile`, `KObj::SetImageDir`, `KObj::DrawInfo`, `KObj::Draw`, `KObj::Activate`, `KObj::PlayLoopSound`, `KObj::PlayRandSound`, `KObj::GetSoundPan`, `KObj::GetSoundVolume`, `KObj::PlaySound`, `KObj::ExecScript`, `KObj::ExecScriptFiled` …(+6)
- Gọi tới: `WriteInteger`→KTabFileCtrl.cpp, `GetInteger`→KTabFile.cpp, `GetNextFrame`→KSprControl.cpp, `NewMap2Mps`→KSubWorld.cpp, `PlaySound`→KMissleRes.cpp, `DrawPrimitives_obj`→KgameWorld.cpp, `Release`→KCache.cpp, `getIniDataForGame`→KgameWorld.cpp, `SetGlobalName`→KLuaScript.cpp, `SafeCallBegin`→KLuaScript.cpp, `Remove`→KLinkArray.cpp, `WriteString`→KTabFileCtrl.cpp, `GetString`→KTabFile.cpp, `SafeCallEnd`→KLuaScript.cpp, `IsPointInPolygon`→KPolygon.cpp

## `gamecore/KObj.h`
- 236 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `Release`→KCache.cpp, `CastSkill`→KObj.cpp, `KObj`→KObj.cpp, `GetMpsPos`→KMissle.cpp, `Activate`→KScriptList.cpp, `Save`→KIniFile.cpp, `Load`→KIniFile.cpp, `ExecScript`→KObj.cpp, `ExecScriptFiled`→KObj.cpp, `SetIndex`→KObj.cpp, `SetWorldID`→KObj.cpp, `SetLifeTime`→KObj.cpp, `SetDir`→KObj.cpp, `SetState`→KNpcRes.cpp, `SetImageDir`→KObj.cpp

## `gamecore/KObjSet.cpp`
- 766 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Hàm: `KObjSet`, `KObjSet`, `KObjSet::Init`, `KObjSet::ClientAdd`, `KObjSet::ClientLoadRegionObj`, `KObjSet::ClientAddRegionObj`, `KObjSet::AddData`, `KObjSet::FindFree`, `KObjSet::CheckClientKind`, `KObjSet::FindID`, `KObjSet::FindName`, `KObjSet::GetID`, `KObjSet::Remove`, `KObjSet::RemoveIfClientOnly`, `KObjSet::GetDataIDKind`, `KObjSet::SearchObjAt`, `KObjSet::GetNameColor`, `KObjSet::SetShowNameFlag`, `KObjSet::CheckShowName`
- Gọi tới: `GetInteger`→KTabFile.cpp, `GetString`→KTabFile.cpp, `t_sprintf`→KStrBase.cpp, `Read`→KFile.cpp, `GetNext`→KNode.h, `Remove`→KLinkArray.cpp, `Insert`→KBinsTree.h, `g_SetFilePath`→KFilePath.cpp, `SetCurFrame`→KSprControl.cpp, `Init`→KCache.cpp, `Load`→KIniFile.cpp, `SetDir`→KObj.cpp, `Release`→KCache.cpp, `Close`→KFile.cpp, `FindFree`→KMissleSet.cpp

## `gamecore/KObjSet.h`
- 152 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `KObjSet`→KObjSet.cpp, `AddData`→KObjSet.cpp, `ClientAdd`→KObjSet.cpp, `Init`→KCache.cpp, `GetID`→KFaction.cpp, `Remove`→KLinkArray.cpp, `ClientLoadRegionObj`→KObjSet.cpp, `ClientAddRegionObj`→KObjSet.cpp, `RemoveIfClientOnly`→KObjSet.cpp, `SearchObjAt`→KObjSet.cpp, `GetNameColor`→KObjSet.cpp, `SetShowNameFlag`→KNpcSet.cpp, `CheckShowName`→KNpcSet.cpp, `FindID`→KObjSet.cpp, `FindName`→KObjSet.cpp

## `gamecore/KPlayer.cpp`
- 5804 dòng. #include "../engine/KGbktoUtf8.h"
- Hàm: `KPlayer`, `KPlayer`, `KPlayer::Release`, `KPlayer::SetPlayerIndex`, `KPlayer::GetPlayerIndex`, `KPlayer::Active`, `KPlayer::ProcessMsg`, `KPlayer::ProcessInputMsg`, `KPlayer::OnButtonDown`, `KPlayer::OnButtonMove`, `KPlayer::OnButtonUp`, `KPlayer::OnMouseMove`, `KPlayer::ProcessMouse`, `KPlayer::Walk`, `KPlayer::Walk`, `KPlayer::TurnLeft`, `KPlayer::TurnRight`, `KPlayer::TurnBack`, `KPlayer::FindSelectNpc`, `KPlayer::FindSelectObject`, `KPlayer::NetCommandPlayerTalk`, `KPlayer::ConformIdx`, `KPlayer::NewPlayerGetBaseAttribute`, `KPlayer::CalcCurLucky`, `KPlayer::ChangeCurStrength` …(+107)
- Gọi tới: `t_sprintf`→KStrBase.cpp, `CoreDataChanged`→CoreShell.cpp, `ClientShowMsg`→KNpc.cpp, `TEncodeText_`→Text.cpp, `ccMessageBox_new`→KCore.cpp, `GetInteger`→KTabFile.cpp, `SetGlobalName`→KLuaScript.cpp, `SafeCallBegin`→KLuaScript.cpp, `g_StrCpyLen`→KStrBase.cpp, `SendSerCommand`→KNpc.cpp, `SearchID`→KItemSet.cpp, `SafeCallEnd`→KLuaScript.cpp, `GetSkill`→KSkillManager.h, `GetWeaponType`→KItemList.cpp, `TEncodeText`→Text.cpp

## `gamecore/KPlayer.h`
- 563 dòng. #include "KWorldMsg.h"
- Gọi tới: `KPlayer`→KPlayer.cpp, `ExecuteScriptC`→KPlayer.cpp, `GetEchoDamage`→KPlayer.cpp, `SetPlayerIndex`→KPlayer.cpp, `GetPlayerIndex`→KPlayer.cpp, `GetFactionName`→KPlayer.cpp, `ChatFriendOnLine`→KPlayer.cpp, `ExecuteScriptA`→KPlayer.cpp, `ExeNoBackScript`→KPlayer.cpp, `ExecuteScriptD`→KPlayer.cpp, `ExecuteScriptB`→KPlayer.cpp, `DoScript`→KPlayer.cpp, `ExeItemScriptA`→KPlayer.cpp, `ExeItemScript`→KPlayer.cpp, `myPrintLuaStackA`→KPlayer.cpp

## `gamecore/KPlayerDef.h`
- 78 dòng. 数据库加载列表数据时每帧加载数量

## `gamecore/KPlayerFaction.cpp`
- 198 dòng. Sword3 Engine (c) 2002 by Kingsoft
- Hàm: `KPlayerFaction`, `KPlayerFaction::Release`, `KPlayerFaction::SetSeries`, `KPlayerFaction::AddFaction`, `KPlayerFaction::AddFaction`, `KPlayerFaction::LeaveFaction`, `KPlayerFaction::OpenCurSkillLevel`, `KPlayerFaction::GetGurFactionCamp`, `KPlayerFaction::GetCurFactionNo`, `KPlayerFaction::GetCurFactionName`
- Gọi tới: `Release`→KCache.cpp, `SetSeries`→KNpc.cpp, `GetID`→KFaction.cpp, `GetCamp`→KFaction.cpp

## `gamecore/KPlayerFaction.h`
- 49 dòng. Sword3 Engine (c) 2002 by Kingsoft
- Gọi tới: `AddFaction`→KPlayerFaction.cpp, `KPlayerFaction`→KPlayerFaction.cpp, `Release`→KCache.cpp, `SetSeries`→KNpc.cpp, `LeaveFaction`→KPlayerFaction.cpp, `OpenCurSkillLevel`→KPlayerFaction.cpp, `GetGurFactionCamp`→KPlayerFaction.cpp, `GetCurFactionNo`→KPlayerFaction.cpp, `GetCurFactionName`→KPlayerFaction.cpp

## `gamecore/KPlayerFuYuan.cpp`
- 50 dòng. Sword3 Engine (c) 2003 by Kingsoft
- Hàm: `KPlayerFuYuan::SetFuYuanValue`, `KPlayerFuYuan::AddFuYuanValue`

## `gamecore/KPlayerFuYuan.h`
- 25 dòng. Sword3 Engine (c) 2003 by Kingsoft
- Gọi tới: `SetFuYuanValue`→KPlayerFuYuan.cpp, `AddFuYuanValue`→KPlayerFuYuan.cpp

## `gamecore/KPlayerMenuState.cpp`
- 68 dòng. Sword3 Engine (c) 2002 by Kingsoft
- Hàm: `KPlayerMenuState`, `KPlayerMenuState::Release`, `KPlayerMenuState::SetState`, `KPlayerMenuStateGraph::Init`, `KPlayerMenuStateGraph::GetStateSpr`
- Gọi tới: `Release`→KCache.cpp, `SetState`→KNpcRes.cpp, `Init`→KCache.cpp, `g_SetFilePath`→KFilePath.cpp, `Load`→KIniFile.cpp, `GetString`→KTabFile.cpp, `Clear`→KIniFile.cpp, `g_StrCpy`→KStrBase.cpp

## `gamecore/KPlayerMenuState.h`
- 50 dòng. Sword3 Engine (c) 2002 by Kingsoft
- Gọi tới: `KPlayerMenuState`→KPlayerMenuState.cpp, `Release`→KCache.cpp, `SetState`→KNpcRes.cpp, `Init`→KCache.cpp, `GetStateSpr`→KPlayerMenuState.cpp

## `gamecore/KPlayerPK.cpp`
- 292 dòng. Sword3 Engine (c) 2003 by Kingsoft
- Hàm: `KPlayerPK::Init`, `KPlayerPK::Active`, `KPlayerPK::SetNormalPKState`, `KPlayerPK::ApplySetNormalPKState`, `KPlayerPK::GetNormalPKState`, `KPlayerPK::ApplyEnmityPK`, `KPlayerPK::ApplyEnmityPK`, `KPlayerPK::SetEnmityPKState`, `KPlayerPK::EnmityPKCountDown`, `KPlayerPK::SetExercisePKState`, `KPlayerPK::SetPKValue`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `CoreDataChanged`→CoreShell.cpp, `TEncodeText_`→Text.cpp, `Init`→KCache.cpp, `Active`→KStepLuaScript.cpp, `SearchName`→KNpcSet.cpp, `SearchID`→KItemSet.cpp

## `gamecore/KPlayerPK.h`
- 59 dòng. Sword3 Engine (c) 2003 by Kingsoft
- Gọi tới: `ApplyEnmityPK`→KPlayerPK.cpp, `Init`→KCache.cpp, `ApplySetNormalPKState`→KPlayerPK.cpp, `SetNormalPKState`→KPlayerPK.cpp, `GetNormalPKState`→KPlayerPK.cpp, `SetEnmityPKState`→KPlayerPK.cpp, `EnmityPKCountDown`→KPlayerPK.cpp, `SetExercisePKState`→KPlayerPK.cpp, `SetPKValue`→KPlayerPK.cpp, `Active`→KStepLuaScript.cpp

## `gamecore/KPlayerReBorn.cpp`
- 98 dòng. Sword3 Engine (c) 2003 by Kingsoft
- Hàm: `KPlayerReBorn::SetReBornValue`, `KPlayerReBorn::SetReBornByte`, `KPlayerReBorn::GetReBornByte`, `KPlayerReBorn::AddReBornValue`

## `gamecore/KPlayerReBorn.h`
- 47 dòng. Sword3 Engine (c) 2003 by Kingsoft
- Gọi tới: `SetReBornValue`→KPlayerReBorn.cpp, `AddReBornValue`→KPlayerReBorn.cpp, `SetReBornByte`→KPlayerReBorn.cpp, `GetReBornByte`→KPlayerReBorn.cpp

## `gamecore/KPlayerRepute.cpp`
- 44 dòng. Sword3 Engine (c) 2003 by Kingsoft
- Hàm: `KPlayerRepute::SetReputeValue`, `KPlayerRepute::AddReputeValue`

## `gamecore/KPlayerRepute.h`
- 26 dòng. Sword3 Engine (c) 2003 by Kingsoft
- Gọi tới: `SetReputeValue`→KPlayerRepute.cpp, `AddReputeValue`→KPlayerRepute.cpp

## `gamecore/KPlayerSet.cpp`
- 568 dòng. #include <objbase.h>
- Hàm: `KPlayerSet`, `KPlayerSet::Init`, `KPlayerSet::FindFree`, `KPlayerSet::FindSame`, `KPlayerSet::CheckLiXian`, `KPlayerSet::FindByTongName`, `KPlayerSet::FindNameID`, `KPlayerSet::FindPlayerID`, `KPlayerSet::GetFirstPlayer`, `KPlayerSet::GetNextPlayer`, `KPlayerSet::TakeRemainder`, `KPlayerSet::FindClient`, `KLevelAdd`, `KLevelAdd::Init`, `KLevelAdd::GetLevelExp`, `KLevelAdd::GetLifePerLevel`, `KLevelAdd::GetStaminaPerLevel`, `KLevelAdd::GetManaPerLevel`, `KLevelAdd::GetLifePerVitality`, `KLevelAdd::GetStaminaPerVitality`, `KLevelAdd::GetManaPerEnergy`, `KLevelAdd::GetLeadExpShare`, `KLevelAdd::GetFireResist`, `KLevelAdd::GetColdResist`, `KLevelAdd::GetPoisonResist` …(+11)
- Gọi tới: `GetInteger`→KTabFile.cpp, `GetNext`→KNode.h, `Init`→KCache.cpp, `Load`→KIniFile.cpp, `Clear`→KIniFile.cpp, `g_StrCmp`→KStrBase.cpp, `Insert`→KBinsTree.h, `Release`→KCache.cpp, `SetPlayerIndex`→KPlayer.cpp, `FindFree`→KMissleSet.cpp, `RestoreCurrentCamp`→KNpc.cpp, `TakeRemainder`→KNpc.cpp, `Save`→KIniFile.cpp

## `gamecore/KPlayerSet.h`
- 131 dòng. (không có chú thích đầu)
- Gọi tới: `Init`→KCache.cpp, `GetLevelExp`→KPlayerSet.cpp, `FindClient`→KPlayerSet.cpp, `KLevelAdd`→KPlayerSet.cpp, `GetLifePerLevel`→KPlayerSet.cpp, `GetStaminaPerLevel`→KPlayerSet.cpp, `GetManaPerLevel`→KPlayerSet.cpp, `GetLifePerVitality`→KPlayerSet.cpp, `GetStaminaPerVitality`→KPlayerSet.cpp, `GetManaPerEnergy`→KPlayerSet.cpp, `GetLeadExpShare`→KPlayerSet.cpp, `GetFireResist`→KPlayerSet.cpp, `GetColdResist`→KPlayerSet.cpp, `GetPoisonResist`→KPlayerSet.cpp, `GetLightResist`→KPlayerSet.cpp

## `gamecore/KPlayerTask.cpp`
- 157 dòng. Sword3 Engine (c) 2002 by Kingsoft
- Hàm: `KPlayerTask`, `KPlayerTask::Release`, `KPlayerTask::ClearTempVar`, `KPlayerTask::GetSaveVal`, `KPlayerTask::SetSaveVal`, `KPlayerTask::GetClearVal`, `KPlayerTask::SetClearVal`, `KPlayerTask::SetTaskByte`, `KPlayerTask::GetTaskByte`
- Gọi tới: `Release`→KCache.cpp, `upTaskdata`→Kuitasktrace.cpp

## `gamecore/KPlayerTask.h`
- 51 dòng. Sword3 Engine (c) 2002 by Kingsoft
- Gọi tới: `KPlayerTask`→KPlayerTask.cpp, `Release`→KCache.cpp, `ClearTempVar`→KPlayerTask.cpp, `GetSaveVal`→KPlayerTask.cpp, `SetSaveVal`→KPlayerTask.cpp, `GetClearVal`→KPlayerTask.cpp, `SetClearVal`→KPlayerTask.cpp, `SetTaskByte`→KPlayerTask.cpp, `GetTaskByte`→KPlayerTask.cpp

## `gamecore/KPlayerTeam.cpp`
- 463 dòng. Sword3 Engine (c) 2002 by Kingsoft
- Hàm: `KPlayerTeam`, `KPlayerTeam::Release`, `KPlayerTeam::ReleaseList`, `KPlayerTeam::ApplyCreate`, `KPlayerTeam::InviteAdd`, `KPlayerTeam::ReceiveInvite`, `KPlayerTeam::ReplyInvite`, `KPlayerTeam::SetAutoRefuseInvite`, `KPlayerTeam::GetAutoRefuseState`, `KPlayerTeam::GetInfo`, `KPlayerTeam::UpdateInterface`, `KPlayerTeam::UpdateamUI`, `KPlayerTeam::DeleteOneFromApplyList`, `KTeam`, `KTeam::Release`, `KTeam::SetIndex`, `KTeam::FindFree`, `KTeam::FindMemberID`, `KTeam::SetTeamOpen`, `KTeam::SetTeamClose`, `KTeam::CalcCaptainPower`, `KTeam::CreateTeam`, `KTeam::AddMember`, `KTeam::DeleteMember`, `KTeam::GetMemberInfo` …(+1)
- Gọi tới: `Release`→KCache.cpp, `CoreDataChanged`→CoreShell.cpp, `t_sprintf`→KStrBase.cpp, `GetInfo`→KNpcResNode.cpp, `FindFree`→KMissleSet.cpp, `TEncodeText_`→Text.cpp, `TEncodeText`→Text.cpp, `SetIndex`→KObj.cpp, `GetMemNumFromLevel`→KPlayerSet.cpp

## `gamecore/KPlayerTeam.h`
- 86 dòng. Sword3 Engine (c) 2002 by Kingsoft
- Gọi tới: `Release`→KCache.cpp, `KPlayerTeam`→KPlayerTeam.cpp, `ReleaseList`→KPlayerTeam.cpp, `ApplyCreate`→KPlayerTeam.cpp, `InviteAdd`→KPlayerTeam.cpp, `ReceiveInvite`→KPlayerTeam.cpp, `ReplyInvite`→KPlayerTeam.cpp, `SetAutoRefuseInvite`→KPlayerTeam.cpp, `GetAutoRefuseState`→KPlayerTeam.cpp, `GetInfo`→KNpcResNode.cpp, `UpdateInterface`→KPlayerTeam.cpp, `UpdateamUI`→KPlayerTeam.cpp, `DeleteOneFromApplyList`→KPlayerTeam.cpp, `KTeam`→KPlayerTeam.cpp, `SetIndex`→KObj.cpp

## `gamecore/KPlayerTong.cpp`
- 1220 dòng. Sword3 Engine (c) 2003 by Kingsoft
- Hàm: `KPlayerTong::Init`, `KPlayerTong::Clear`, `KPlayerTong::ApplyCreateTong`, `KPlayerTong::ApplyAddTong`, `KPlayerTong::Create`, `KPlayerTong::Active`, `KPlayerTong::SendAttack`, `KPlayerTong::SetTongLevel`, `KPlayerTong::SetTongMap`, `KPlayerTong::SetTongCamp`, `KPlayerTong::AcceptMember`, `KPlayerTong::GetTongName`, `KPlayerTong::AddTong`, `KPlayerTong::ApplyInstate`, `KPlayerTong::ApplyKick`, `KPlayerTong::ApplyChangeMaster`, `KPlayerTong::ApplyLeave`, `KPlayerTong::ApplyInfo`, `KPlayerTong::GetTongNameID`, `KPlayerTong::CanGetManagerInfo`, `KPlayerTong::CanGetMemberInfo`, `KPlayerTong::SetSelfInfo`, `KPlayerTong::OpenCreateInterface`, `KPlayerTong::ApplySaveMoney`, `KPlayerTong::ApplyGetMoney` …(+7)
- Gọi tới: `g_FileName2Id`→KFilePath.cpp, `t_sprintf`→KStrBase.cpp, `CoreDataChanged`→CoreShell.cpp, `ClientShowMsg`→KNpc.cpp, `g_CheckFileExist`→KFilePath.cpp, `TEncodeText`→Text.cpp, `Clear`→KIniFile.cpp, `CheckTrading`→KPlayer.cpp, `ccMessageBox_new`→KCore.cpp, `TEncodeText_`→Text.cpp, `Init`→KCache.cpp, `Create`→KFile.cpp, `Active`→KStepLuaScript.cpp, `SearchID`→KItemSet.cpp

## `gamecore/KPlayerTong.h`
- 155 dòng. Sword3 Engine (c) 2003 by Kingsoft
- Gọi tới: `Init`→KCache.cpp, `Clear`→KIniFile.cpp, `GetTongName`→KPlayerTong.cpp, `GetTongNameID`→KPlayerTong.cpp, `GetCamp`→KFaction.cpp, `Active`→KStepLuaScript.cpp, `CanGetManagerInfo`→KPlayerTong.cpp, `CanGetMemberInfo`→KPlayerTong.cpp, `SetTongLevel`→KPlayerTong.cpp, `SetTongMap`→KPlayerTong.cpp, `SetTongCamp`→KPlayerTong.cpp, `ApplyChangeAnnounce`→KPlayerTong.cpp, `ApplyPower`→KPlayerTong.cpp, `SendAttack`→KPlayerTong.cpp, `ApplyCreateTong`→KPlayerTong.cpp

## `gamecore/KPlayerTrade.cpp`
- 165 dòng. Sword3 Engine (c) 2003 by Kingsoft
- Hàm: `KTrade`, `KTrade::Release`, `KTrade::StartTrade`, `KTrade::Lock`, `KTrade::SetTradeState`, `KTrade::ReplyInvite`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `CoreDataChanged`→CoreShell.cpp, `TEncodeText_`→Text.cpp, `Release`→KCache.cpp, `SearchID`→KItemSet.cpp, `ReplyInvite`→KPlayerTeam.cpp, `ccMessageBox_new`→KCore.cpp

## `gamecore/KPlayerTrade.h`
- 39 dòng. Sword3 Engine (c) 2003 by Kingsoft
- Gọi tới: `KTrade`→KPlayerTrade.cpp, `Release`→KCache.cpp, `StartTrade`→KPlayerTrade.cpp, `Lock`→KPlayerTrade.cpp, `SetTradeState`→KPlayerTrade.cpp, `ReplyInvite`→KPlayerTeam.cpp

## `gamecore/KPlayerVip.cpp`
- 95 dòng. Date:	2019.08.23
- Hàm: `KPlayerVip::SetRoleVipValue`, `KPlayerVip::SetRoleVipByte`, `KPlayerVip::GetRoleVipByte`, `KPlayerVip::AddRoleVipValue`

## `gamecore/KPlayerVip.h`
- 44 dòng. Sword3 Engine (c) 2003 by Kingsoft
- Gọi tới: `SetRoleVipValue`→KPlayerVip.cpp, `AddRoleVipValue`→KPlayerVip.cpp, `SetRoleVipByte`→KPlayerVip.cpp, `GetRoleVipByte`→KPlayerVip.cpp

## `gamecore/KProtocol.cpp`
- 1221 dòng. 客户端接收到的服务器到客户端的协议长度
- Hàm: `g_InitProtocol`, `SendClientCmdRun`, `SendClientCmdWalk`, `SendClientRunScript`, `SendClientCmdSkill`, `SendClientCmdRequestNpc`, `SendClientCmdSell`, `SendClientCmdBuy`, `SendClientCPUnlockCmd`, `SendClientCPLockCmd`, `SendClientCPResetCmd`, `SendClientCPChangeCmd`, `SendClientOpenMarket`, `SendClientCmdJinMai`, `SendClientDaTau`, `SendClientCmdSit`, `SendClientCmdRide`, `SendClientCmdJump`, `SendObjMouseClick`, `SendClientCmdStoreMoney`, `SendClientCmdRevive`, `SendClientCmdGua`, `SendClientCmdRevive`, `SendClientCmdMoveItem`, `SendClientCmdQueryLadder` …(+27)
- Gọi tới: `t_sprintf`→KStrBase.cpp, `ClientShowMsg`→KNpc.cpp, `Clear`→KIniFile.cpp, `Load`→KIniFile.cpp, `ESetByte`→Text.cpp, `GetID`→KFaction.cpp, `ApplyRoomInfo`→KPlayer.cpp, `CoreDataChanged`→CoreShell.cpp, `g_FileName2Id`→KFilePath.cpp, `SetTaskByte`→KPlayerTask.cpp, `TEncodeText`→Text.cpp

## `gamecore/KProtocol.h`
- 3609 dòng. (không có chú thích đầu)
- Gọi tới: `Release`→KCache.cpp, `SendClientCmdSell`→KProtocol.cpp, `SendClientCmdBuy`→KProtocol.cpp, `SendClientCmdRun`→KProtocol.cpp, `SendClientCmdWalk`→KProtocol.cpp, `SendClientCmdSkill`→KProtocol.cpp, `SendClientCmdSit`→KProtocol.cpp, `SendClientCPUnlockCmd`→KProtocol.cpp, `SendClientCPLockCmd`→KProtocol.cpp, `SendClientCPChangeCmd`→KProtocol.cpp, `SendClientCPResetCmd`→KProtocol.cpp, `SendClientOpenMarket`→KProtocol.cpp, `SendClientString`→KProtocol.cpp, `SendClientDaTau`→KProtocol.cpp, `SendClientCmdMoveItem`→KProtocol.cpp

## `gamecore/KProtocolDef.h`
- 533 dòng. Add by Freeway chen in 2003.7.1

## `gamecore/KProtocolProcess.cpp`
- 5355 dòng. #include "KProtocolProcess.h"
- Hàm: `KProtocolProcess::s2cLianUpdateItem`, `KProtocolProcess::NetCommandSit`, `KProtocolProcess::NetCommandStand`, `KProtocolProcess::s2csyncrankdata`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `CoreDataChanged`→CoreShell.cpp, `TEncodeText_`→Text.cpp, `SearchID`→KItemSet.cpp, `TEncodeText`→Text.cpp, `ClientShowMsg`→KNpc.cpp, `GetInteger`→KTabFile.cpp, `ccMessageBox_new`→KCore.cpp, `SendSerCommand`→KNpc.cpp, `ConformIdx`→KPlayer.cpp, `AddRef`→KRegion.cpp, `ApplySelfTeamInfo`→KPlayer.cpp, `SetSaveVal`→KPlayerTask.cpp, `DecRef`→KRegion.cpp, `ProcNetCommand`→KNpc.cpp

## `gamecore/KProtocolProcess.h`
- 177 dòng. (không có chú thích đầu)
- Gọi tới: `SyncCurPlayer`→KPlayer.cpp, `NetCommandSit`→KProtocolProcess.cpp, `NetCommandStand`→KProtocolProcess.cpp, `s2cApplyAddTeam`→KPlayer.cpp, `s2cLevelUp`→KPlayer.cpp, `s2cGetCurAttribute`→KPlayer.cpp, `s2cSyncMoney`→KPlayer.cpp, `s2cSyncXu`→KPlayer.cpp, `s2cTradeChangeState`→KPlayer.cpp, `s2cTradeMoneySync`→KPlayer.cpp, `s2cTradeDecision`→KPlayer.cpp, `s2cTradeApplyStart`→KPlayer.cpp, `s2cLianUpdateItem`→KProtocolProcess.cpp, `s2csyncrankdata`→KProtocolProcess.cpp

## `gamecore/KRUImage.h`
- 333 dòng. iRepresentShell绘制的图元对象表述定义

## `gamecore/KRegion.cpp`
- 1238 dòng. #include "KObj.h"
- Hàm: `KRegion`, `KRegion`, `KRegion::Init`, `KRegion::Load`, `KRegion::LoadObjectC`, `KRegion::LoadClientNpc`, `KRegion::LoadClientObj`, `KRegion::LoadLittleMapData`, `KRegion::NewRegActivate`, `KRegion::AddNpc`, `KRegion::RemoveNpc`, `KRegion::AddMissle`, `KRegion::RemoveMissle`, `KRegion::AddObj`, `KRegion::RemoveObj`, `KRegion::SetTrap`, `KRegion::GetTrap`, `KRegion::GetBarrier`, `KRegion::GetNewBarrier`, `KRegion::GetBarrierNewMin`, `KRegion::GetBarrierMin`, `KRegion::GetRef`, `KRegion::AddRef`, `KRegion::DecRef`, `KRegion::AddPlayer` …(+7)
- Gọi tới: `Remove`→KLinkArray.cpp, `GetHead`→KList.h, `GetNext`→KNode.h, `Read`→KFile.cpp, `Clear`→KIniFile.cpp, `t_sprintf`→KStrBase.cpp, `Release`→KCache.cpp, `Close`→KFile.cpp, `Seek`→KFile.cpp, `AddTail`→KList.h, `gTraceLogFile`→KLogFile.cpp, `Activate`→KScriptList.cpp, `Paint`→KMissle.cpp, `g_SetFilePath`→KFilePath.cpp, `Open`→KFile.cpp

## `gamecore/KRegion.h`
- 631 dòng. #include "KWorldMsg.h"
- Hàm: `KRegion::CheckNpcInDisten`, `KRegion::FindNpc`, `KRegion::FindNpcAuto`, `KRegion::FindObject`, `KRegion::FindObjectAuto`, `KRegion::FindObjectAuto`
- Gọi tới: `GetNext`→KNode.h, `t_sprintf`→KStrBase.cpp, `GetRef`→KRegion.cpp, `GetHead`→KList.h, `FindObject`→KRegion.cpp, `GetRelation`→KNpcSet.cpp, `KRegion`→KRegion.cpp, `GetObjNode`→KRegion.cpp, `SearchNpc`→KRegion.cpp, `GetMpsPos`→KMissle.cpp, `GetData`→KSellItem.cpp, `Clear`→KIniFile.cpp, `Init`→KCache.cpp, `Load`→KIniFile.cpp, `LoadObjectC`→KRegion.cpp

## `gamecore/KRelayProtocol.h`
- 172 dòng. Sword3 Engine (c) 2003 by Kingsoft

## `gamecore/KScriptValueSet.cpp`
- 167 dòng. KScriptValueSet.cpp: implementation of the KScriptValueSet class.
- Hàm: `KScriptValueSet`, `KScriptValueSet`, `KScriptValueSet::Load`, `KScriptValueSet::Save`, `KScriptValueSet::SetValue`, `KScriptValueSet::SetValue`, `KScriptValueSet::GetValue`, `KScriptValueSet::GetValue`, `KScriptValueSet::AddValue`, `KScriptValueSet::AddValue`, `KScriptValueSet::SearchValue`
- Gọi tới: `AddTail`→KList.h, `GetHead`→KList.h, `GetNext`→KNode.h, `Load`→KIniFile.cpp, `GetNextKey`→KIniFile.cpp, `Clear`→KIniFile.cpp, `Save`→KIniFile.cpp, `SetValue`→KTabFileCtrl.cpp, `GetValue`→KTabFile.cpp, `GetString`→KTabFile.cpp, `GetInteger`→KTabFile.cpp, `WriteString`→KTabFileCtrl.cpp, `WriteInteger`→KTabFileCtrl.cpp

## `gamecore/KScriptValueSet.h`
- 57 dòng. KScriptValueSet.h: interface for the KScriptValueSet class.
- Gọi tới: `KScriptValueSet`→KScriptValueSet.cpp, `SetValue`→KTabFileCtrl.cpp, `GetValue`→KTabFile.cpp, `AddValue`→KScriptValueSet.cpp, `Load`→KIniFile.cpp, `Save`→KIniFile.cpp, `SearchValue`→KScriptValueSet.cpp

## `gamecore/KSellItem.cpp`
- 794 dòng. Sword3 Engine (c) 2003 by Kingsoft
- Hàm: `KSellItem`, `KSellItem::Init`, `KSellItem::DeleteAll`, `KSellItem::DeleteLAll`, `KSellItem::FindIdx_lian`, `KSellItem::FindIdx`, `KSellItem::GetDataL`, `KSellItem::GetData`, `KSellItem::GetData`, `KSellItem::UpdateItem`, `KSellItem::UpdateLianItem`, `KSellItem::GetCount`, `KSellItem::GetLCount`, `KSellItem::Check`, `KSellItem::CheckLian`
- Gọi tới: `CoreDataChanged`→CoreShell.cpp, `Remove`→KLinkArray.cpp, `t_sprintf`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `SetID`→KItemSet.cpp, `Init`→KCache.cpp, `SearchID`→KItemSet.cpp, `GetMenuState`→KNpc.cpp, `TEncodeText`→Text.cpp, `GetName`→KNpcResNode.cpp, `GetCount`→KMissleSet.cpp

## `gamecore/KSellItem.h`
- 53 dòng. Sword3 Engine (c) 2003 by Kingsoft
- Gọi tới: `KSellItem`→KSellItem.cpp, `Init`→KCache.cpp, `UpdateItem`→KSellItem.cpp, `UpdateLianItem`→KSellItem.cpp, `GetLCount`→KSellItem.cpp, `Check`→KSellItem.cpp, `GetCount`→KMissleSet.cpp, `CheckLian`→KSellItem.cpp, `DeleteAll`→KSellItem.cpp, `DeleteLAll`→KSellItem.cpp, `GetData`→KSellItem.cpp, `GetDataL`→KSellItem.cpp, `FindIdx`→KSellItem.cpp, `FindIdx_lian`→KSellItem.cpp

## `gamecore/KSkillList.cpp`
- 1379 dòng. #include "crtdbg.h"
- Hàm: `KSkillList`, `KSkillList`, `KSkillList::FindSame`, `KSkillList::FindFree`, `KSkillList::GetCount`, `KSkillList::SetSkillLevel`, `KSkillList::SetLevel`, `KSkillList::IncreaseLevel`, `KSkillList::Remove`, `KSkillList::RemoveAllSkill`, `KSkillList::Add`, `KSkillList::AddSkillExpByListidx`, `KSkillList::GetCurSkillExpByListidx`, `KSkillList::GetSkillExpByListidx`, `KSkillList::SetSkillExpByListidx`, `KSkillList::IsSkillExpByListidx`, `KSkillList::GetSkillExp`, `KSkillList::SetSkillExp`, `KSkillList::SetCurSkillExp`, `KSkillList::GetCurSkillExp`, `KSkillList::IsSkillExp`, `KSkillList::GetLevelByListidx`, `KSkillList::AddSkillExp`, `KSkillList::GetLevel`, `KSkillList::SetSLevelByListidx` …(+26)
- Gọi tới: `GetSkillStyle`→KSkillManager.h, `FindSame`→KPlayerSet.cpp, `GetSkill`→KSkillManager.h, `Cast`→KSkills.cpp, `ccMessageBox_new`→KCore.cpp, `GetSkillName`→KThiefSkill.cpp, `NewCanCastSkill`→KSkills.cpp, `FindFree`→KMissleSet.cpp, `GetCurActiveWeaponSkill`→KNpc.cpp, `GetCount`→KMissleSet.cpp, `SetSkillLeftTime`→KNpc.cpp, `Remove`→KLinkArray.cpp, `GetLevel`→KPlayerSet.cpp, `EnChanceSkill`→KSkills.cpp, `GetInteger`→KTabFile.cpp

## `gamecore/KSkillList.h`
- 215 dòng. #include "Windows.h"
- Gọi tới: `KSkillList`→KSkillList.cpp, `CanCast`→KSkillList.cpp, `SetNextCastTime`→KSkillList.cpp, `SetHorseNextCastTime`→KSkillList.cpp, `GetHorseNextCastTime`→KSkillList.cpp, `GetNextCastTime`→KSkillList.cpp, `ReEnChance`→KSkillList.cpp, `CheckNoSkill`→KSkillList.cpp, `Remove`→KLinkArray.cpp, `RemoveAllSkill`→KSkillList.cpp, `GetSkillId`→KThiefSkill.cpp, `SetSkillLeftTime`→KNpc.cpp, `Clear`→KIniFile.cpp, `SetAddPointByIndex`→KSkillList.cpp, `SetAddPoint`→KSkillList.cpp

## `gamecore/KSkillManager.cpp`
- 181 dòng. #include "MyAssert.H"
- Hàm: `KSkillManager`, `KSkillManager`, `KSkillManager::Init`, `KSkillManager::InstanceSkill`
- Gọi tới: `GetInteger`→KTabFile.cpp, `Init`→KCache.cpp, `LoadSkillLevelData`→KSkills.cpp, `Load`→KIniFile.cpp, `Clear`→KIniFile.cpp, `GetSkillStyle`→KSkillManager.h, `GetInfoFromTabFile`→KMissle.cpp, `SetSkillLevel`→KSkillList.cpp, `LoadSetting`→KThiefSkill.cpp

## `gamecore/KSkillManager.h`
- 108 dòng. #ifndef _STANDALONE
- Hàm: `KSkillManager::GetSkillStyle`, `KSkillManager::GetSkillB`, `KSkillManager::GetSkill`
- Gọi tới: `InstanceSkill`→KSkillManager.cpp, `KSkillManager`→KSkillManager.cpp, `Init`→KCache.cpp

## `gamecore/KSkillSpecial.cpp`
- 173 dòng. Revision Count	:
- Hàm: `KSkillSpecial`, `KSkillSpecial::Init`, `KSkillSpecial::SetFrameSpr`, `KSkillSpecial::DrawC`, `KSkillSpecial::SetAnimation`, `KSkillSpecial::Remove`
- Gọi tới: `Release`→KCache.cpp, `NewMap2Mps`→KSubWorld.cpp, `getIniDataForGame`→KgameWorld.cpp, `t_sprintf`→KStrBase.cpp, `DrawSpecial_miss`→KgameWorld.cpp, `Init`→KCache.cpp, `SetFrameSpr`→KNpcRes.cpp, `GetImageParam`→KImageStore2.cpp, `SetSprFile`→KSprControl.cpp, `GetNextFrame`→KSprControl.cpp, `CheckEnd`→KSprControl.cpp, `Remove`→KLinkArray.cpp, `RemoveMissle`→KRegion.cpp

## `gamecore/KSkillSpecial.h`
- 61 dòng. Revision Count	:
- Gọi tới: `KSkillSpecial`→KSkillSpecial.cpp, `Init`→KCache.cpp, `Remove`→KLinkArray.cpp, `DrawC`→KSkillSpecial.cpp, `Draw`→KLittleMap.cpp, `SetAnimation`→KSkillSpecial.cpp, `SetFrameSpr`→KNpcRes.cpp

## `gamecore/KSkills.cpp`
- 4212 dòng. KSkills.cpp: implementation of the KSkills class.
- Hàm: `KSkill`, `KSkill`, `KSkill::Param2PCoordinate`, `KSkill::CanCastSkill`, `KSkill::NewCanCastSkill`, `KSkill::Cast`, `KSkill::Vanish`, `KSkill::OnMissleEvent`, `KSkill::FlyEvent`, `KSkill::Collidsion`, `KSkill::__CastWall`, `KSkill::__CastLine`, `KSkill::__CastSpread`, `KSkill::__CastCircle`, `KSkill::__CastZone`, `KSkill::__CastFixed`, `KSkill::__CastRound`, `KSkill::CastMissles`, `KSkill::CastZone`, `KSkill::CastLine`, `KSkill::CastExtractiveLineMissle`, `KSkill::CastWall`, `KSkill::CastNotWall`, `KSkill::CastCircle`, `KSkill::CastSpread` …(+19)
- Gọi tới: `GetInteger`→KTabFile.cpp, `t_sprintf`→KStrBase.cpp, `NewMap2Mps`→KSubWorld.cpp, `GetSkillName`→KThiefSkill.cpp, `GetSkill`→KSkillManager.h, `GetStringByKeyFromFile`→CXmlStream.cpp, `g_DirCos`→KMath.h, `g_DirSin`→KMath.h, `GetString`→KTabFile.cpp, `ClientShowMsg`→KNpc.cpp, `g_Dir2DirIndex`→KMath.h, `g_GetDistance`→KMath.h, `g_GetDirIndex`→KMath.h, `g_DirIndex2Dir`→KMath.h, `IsPlayer`→KNpc.cpp

## `gamecore/KSkills.h`
- 297 dòng. KSkills.h: interface for the KSkills class.
- Gọi tới: `KSkill`→KSkills.cpp, `GetInfoFromTabFile`→KMissle.cpp, `GetChildSkillNum`→KSkills.cpp, `OnVanish`→KMissle.cpp, `OnMissleEvent`→KSkills.cpp, `GetSkillIdFromName`→KSkills.cpp, `GetSkillName`→KThiefSkill.cpp, `GetSkillStyle`→KSkillManager.h, `Load`→KIniFile.cpp, `Cast`→KSkills.cpp, `LoadSkillLevelData`→KSkills.cpp, `GetSkillCost`→KThiefSkill.cpp, `GetMissleGenerateTime`→KSkills.cpp, `GetSkillId`→KThiefSkill.cpp, `SetSkillLevel`→KSkillList.cpp

## `gamecore/KSortScript.cpp`
- 431 dòng. KScriptBinTree g_ScriptBinTree;
- Hàm: `g_GetScript`, `g_GetScript`, `KSceGetFliePath`, `LoadScriptToSortListA`, `LoadAllScript`, `g_IniScriptEngine`, `LoadScriptToSortList`, `LoadScriptInDirectory`, `UnLoadScript`, `ReLoadScript`, `ReLoadAllScript`, `ClearAllScript`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `g_CheckFileExist`→KFilePath.cpp, `Save`→KIniFile.cpp, `Load`→KIniFile.cpp, `Clear`→KIniFile.cpp, `g_StrUpper`→KStrBase.cpp, `g_StrLower`→KStrBase.cpp, `Write`→KFile.cpp, `WriteString`→KTabFileCtrl.cpp, `g_FileName2Id`→KFilePath.cpp, `ClearList`→KBinsTree.h, `Find`→KBinsTree.h, `GetScript`→KScriptList.cpp, `LuaIncludeFile`→ScriptFuns.cpp, `LuaIncludeLib`→ScriptFuns.cpp

## `gamecore/KSortScript.h`
- 48 dòng. 排序二叉树，保存经过文件名转数字的脚本的id,并实现快速查找对应脚本
- Gọi tới: `g_GetScript`→KSortScript.cpp, `GetScript`→KScriptList.cpp, `g_IniScriptEngine`→KSortScript.cpp, `ReLoadScript`→KSortScript.cpp, `ReLoadAllScript`→KSortScript.cpp, `ClearAllScript`→KSortScript.cpp

## `gamecore/KSprControl.cpp`
- 501 dòng. #include "MyAssert.h"
- Hàm: `KSprControl`, `KSprControl::Release`, `KSprControl::SetSprFile`, `KSprControl::SetCurFrame`, `KSprControl::SetDirFrame`, `KSprControl::Set64DirFrame`, `KSprControl::SetCurDir`, `KSprControl::SetCurDir64`, `KSprControl::SetCenterPos`, `KSprControl::GetOneDirFrames`, `KSprControl::SetPos`, `KSprControl::CheckEnd`, `KSprControl::SetDirStart`, `KSprControl::SetDirEnd`, `KSprControl::GetCurDirFrameNo`, `KSprControl::ChangeNextFrame`, `KSprControl::ChangePrevFrame`, `KSprControl::ChangeCurFrame`, `KSprControl::GetNextFrame`, `KSprControl::GetPrevFrame`, `KSprControl::SetFileName`, `KSprControl::SetTotalFrame`, `KSprControl::SetTotalDir`, `KSprControl::SetInterVal`
- Gọi tới: `Release`→KCache.cpp, `GetNode`→KCache.cpp, `DrawBorder`→KNpc.cpp, `g_StrCmp`→KStrBase.cpp, `g_FileName2Id`→KFilePath.cpp, `SetPos`→KNpc.cpp

## `gamecore/KSprControl.h`
- 78 dòng. (không có chú thích đầu)
- Hàm: `KSprControl::CheckExist`
- Gọi tới: `KSprControl`→KSprControl.cpp, `Release`→KCache.cpp, `SetFileName`→KSprControl.cpp, `SetTotalFrame`→KSprControl.cpp, `SetCurFrame`→KSprControl.cpp, `SetTotalDir`→KSprControl.cpp, `SetCurDir`→KSprControl.cpp, `SetInterVal`→KSprControl.cpp, `SetPos`→KNpc.cpp, `SetCenterPos`→KSprControl.cpp, `SetDirFrame`→KSprControl.cpp, `Set64DirFrame`→KSprControl.cpp, `SetCurDir64`→KSprControl.cpp, `GetOneDirFrames`→KSprControl.cpp, `SetSprFile`→KSprControl.cpp

## `gamecore/KSubWorld.cpp`
- 1648 dòng. #include <ppl.h>
- Hàm: `KSubWorld`, `KSubWorld`, `KSubWorld::FindRegion`, `KSubWorld::FindFreeRegion`, `KSubWorld::Activate`, `KSubWorld::GetDistance`, `KSubWorld::SetFocusPosition`, `KSubWorld::LookAt`, `KSubWorld::GetMpsByLocalPosition`, `KSubWorld::GetLocalPositionByMps`, `KSubWorld::NewMap2Mps`, `KSubWorld::Mps2Map`, `KSubWorld::NewMap2Mps`, `KSubWorld::Mps2Map`, `KSubWorld::IsHave`, `KSubWorld::Mps2MapClient`, `KSubWorld::Mps2MapnRodom`, `KSubWorld::getCellPos`, `KSubWorld::TestBarrier`, `KSubWorld::TestBarrier`, `KSubWorld::TestBarrierMin`, `KSubWorld::SetTrap`, `KSubWorld::GetTrap`, `KSubWorld::GetBarrier`, `KSubWorld::LoadMapC` …(+16)
- Gọi tới: `Remove`→KLinkArray.cpp, `ccMessageBox_new`→KCore.cpp, `GetBarrier`→KRegion.cpp, `Load`→KIniFile.cpp, `t_sprintf`→KStrBase.cpp, `setIsPaint`→KgameWorld.cpp, `GetObstacleInfo`→KScenePlaceC.cpp, `Close`→KFile.cpp, `Clear`→KIniFile.cpp, `AddNpc`→KRegion.cpp, `checkPos`→KScenePlaceC.cpp, `SetTrap`→KRegion.cpp, `GetTrap`→KRegion.cpp, `Init`→KCache.cpp, `LoadObjectC`→KRegion.cpp

## `gamecore/KSubWorld.h`
- 142 dòng. #include "KWeatherMgr.h"
- Gọi tới: `KSubWorld`→KSubWorld.cpp, `TestBarrier`→KSubWorld.cpp, `SetCurrentCamp`→KNpc.cpp, `Activate`→KScriptList.cpp, `GetFreeObjPos`→KSubWorld.cpp, `GetFreePos`→KSubWorld.cpp, `GetFreeNewObjPos`→KSubWorld.cpp, `CanPutObj`→KSubWorld.cpp, `ObjChangeRegion`→KSubWorld.cpp, `MissleChangeRegion`→KSubWorld.cpp, `AddPlayer`→KRegion.cpp, `RemovePlayer`→KRegion.cpp, `Close`→KFile.cpp, `GetDistance`→KSubWorld.cpp, `LookAt`→KSubWorld.cpp

## `gamecore/KSubWorldSet.cpp`
- 309 dòng. #include "KScriptValueSet.h"
- Hàm: `KSubWorldSet`, `KSubWorldSet::SubExecuteScriptA`, `KSubWorldSet::SubExecuteScriptB`, `KSubWorldSet::SubExecuteScript`, `KSubWorldSet::SubExecuteScript`, `KSubWorldSet::SearchWorld`, `KSubWorldSet::SearchWorldRows`, `KSubWorldSet::LoadSerMaps`, `KSubWorldSet::MainLoop`, `KSubWorldSet::getCilentRunTime`, `KSubWorldSet::Close`, `KSubWorldSet::Paint`
- Gọi tới: `SafeCallBegin`→KLuaScript.cpp, `SafeCallEnd`→KLuaScript.cpp, `g_GetScript`→KSortScript.cpp, `CallFunction`→KLuaScript.cpp, `Clear`→KIniFile.cpp, `Release`→KCache.cpp, `t_sprintf`→KStrBase.cpp, `GetInteger`→KTabFile.cpp, `Stop`→KLuaScript.cpp, `Close`→KFile.cpp, `RemoveAll`→KNpcSet.cpp, `Paint`→KMissle.cpp, `Start`→KTimer.cpp, `ccMessageBox_new`→KCore.cpp, `g_FileName2Id`→KFilePath.cpp

## `gamecore/KSubWorldSet.h`
- 56 dòng. void	MessageLoop();
- Gọi tới: `SubExecuteScript`→KSubWorldSet.cpp, `KSubWorldSet`→KSubWorldSet.cpp, `LoadSerMaps`→KSubWorldSet.cpp, `SearchWorld`→KSubWorldSet.cpp, `SearchWorldRows`→KSubWorldSet.cpp, `MainLoop`→KSubWorldSet.cpp, `SendMessage`→KScriptList.cpp, `Close`→KFile.cpp, `SubExecuteScriptA`→KSubWorldSet.cpp, `SubExecuteScriptB`→KSubWorldSet.cpp, `getCilentRunTime`→KSubWorldSet.cpp, `Paint`→KMissle.cpp

## `gamecore/KTaskFuns.cpp`
- 15 dòng. #include "MyAssert.H"
- Hàm: `g_GetStringRes`
- Gọi tới: `GetString`→KTabFile.cpp

## `gamecore/KTaskFuns.h`
- 42 dòng. m_pTimerOwner = pOwner;

## `gamecore/KThiefSkill.cpp`
- 277 dòng. #include "../../Represent/iRepresent/iRepresentshell.h"
- Hàm: `KThiefSkill`, `KThiefSkill`, `KThiefSkill::GetSkillId`, `KThiefSkill::GetSkillName`, `KThiefSkill::GetSkillStyle`, `KThiefSkill::LoadSkillLevelData`, `KThiefSkill::DoSkill`, `KThiefSkill::Cast`, `KThiefSkill::OnSkill`, `KThiefSkill::CanCastSkill`, `KThiefSkill::NewCanCastSkill`, `KThiefSkill::GetDesc`, `KThiefSkill::LoadSetting`, `KThiefSkill::GetSkillCost`, `KThiefSkill::DrawSkillIcon`
- Gọi tới: `GetInteger`→KTabFile.cpp, `GetString`→KTabFile.cpp, `CreateMissleForShow`→KMissle.cpp, `Cast`→KSkills.cpp, `GetSkillStyle`→KSkillManager.h, `LoadSkillLevelData`→KSkills.cpp, `DoSkill`→KNpc.cpp, `SetSpecialSpr`→KNpc.cpp, `OnSkill`→KNpc.cpp, `SetBlur`→KNpcRes.cpp, `SetNextCastTimeByIndex`→KSkillList.cpp, `CanCastSkill`→KSkills.cpp, `GetRelation`→KNpcSet.cpp, `GetDistance`→KSubWorld.cpp, `NewCanCastSkill`→KSkills.cpp

## `gamecore/KThiefSkill.h`
- 90 dòng. (không có chú thích đầu)
- Gọi tới: `KThiefSkill`→KThiefSkill.cpp, `GetSkillId`→KThiefSkill.cpp, `GetSkillName`→KThiefSkill.cpp, `GetSkillStyle`→KSkillManager.h, `LoadSkillLevelData`→KSkills.cpp, `DoSkill`→KNpc.cpp, `OnSkill`→KNpc.cpp, `CanCastSkill`→KSkills.cpp, `NewCanCastSkill`→KSkills.cpp, `Cast`→KSkills.cpp, `GetSkillCost`→KThiefSkill.cpp, `LoadSetting`→KThiefSkill.cpp, `DrawSkillIcon`→KSkills.cpp, `GetDesc`→KMagicDesc.cpp

## `gamecore/KTongProtocol.h`
- 778 dòng. 文件名		：	KTongProtocol.h

## `gamecore/KViewItem.cpp`
- 398 dòng. Sword3 Engine (c) 2003 by Kingsoft
- Hàm: `KViewItem`, `KViewItem::Init`, `KViewItem::ApplyViewEquip`, `KViewItem::DeleteAll`, `KViewItem::DeleteNewAll`, `KViewItem::FindIdx`, `KViewItem::GetData`, `KViewItem::UpdateItem`, `KViewItem::GetCount`, `KViewItem::Check`
- Gọi tới: `Remove`→KLinkArray.cpp, `Init`→KCache.cpp, `DeleteAll`→KSellItem.cpp, `CoreDataChanged`→CoreShell.cpp, `UpdateItem`→KSellItem.cpp, `FindIdx`→KSellItem.cpp, `GetData`→KSellItem.cpp, `SearchID`→KItemSet.cpp, `GetMenuState`→KNpc.cpp, `SetID`→KItemSet.cpp, `GetCount`→KMissleSet.cpp, `Check`→KSellItem.cpp

## `gamecore/KViewItem.h`
- 42 dòng. Sword3 Engine (c) 2003 by Kingsoft
- Gọi tới: `KViewItem`→KViewItem.cpp, `Init`→KCache.cpp, `ApplyViewEquip`→KViewItem.cpp, `UpdateItem`→KSellItem.cpp, `DeleteAll`→KSellItem.cpp, `DeleteNewAll`→KViewItem.cpp, `GetData`→KSellItem.cpp, `Check`→KSellItem.cpp, `GetCount`→KMissleSet.cpp, `FindIdx`→KSellItem.cpp

## `gamecore/KWorldMsg.cpp`
- 68 dòng. KWorldMsg g_WorldMsg;
- Hàm: `KWorldMsg::Get`, `KWorldMsg::Peek`, `KWorldMsg::Clear`
- Gọi tới: `GetHead`→KList.h, `GetNext`→KNode.h, `Remove`→KLinkArray.cpp, `Clear`→KIniFile.cpp, `RemoveHead`→KList.h

## `gamecore/KWorldMsg.h`
- 106 dòng. zroc 说明：src dest 在 server 上用 idx，在客户端用 ID
- Hàm: `KWorldMsg::NewSend`, `KWorldMsg::Send`
- Gọi tới: `AddTail`→KList.h, `Peek`→KWorldMsg.cpp, `Clear`→KIniFile.cpp

## `gamecore/LuaFuns.cpp`
- 316 dòng. #include "KNetClient.h"
- Hàm: `g_GetLuaFunsCount`, `LuaLabel`, `LuaGotoLabel`, `LuaGetScript`, `LuaNewScript`, `LuaResume`, `LuaWait`, `LuaEndWait`, `LuaGetScriptState`, `LuaSendScriptMessage`, `LuaSendMessage`, `LuaWaitForEvent`, `LuaGetValue`, `LuaSetValue`, `LuaReturn`
- Gọi tới: `GetScript`→KScriptList.cpp, `GetValue`→KTabFile.cpp, `SendMessage`→KScriptList.cpp, `SetValue`→KTabFileCtrl.cpp, `LuaGetTempTaskValue`→ScriptFuns.cpp, `LuaSetTempTaskValue`→ScriptFuns.cpp, `GotoLabel`→KStepLuaScript.cpp, `KStepLuaScript`→KStepLuaScript.cpp, `Init`→KCache.cpp, `g_SetFilePath`→KFilePath.cpp, `g_GetFullPath`→KFilePath.cpp, `Load`→KIniFile.cpp, `RegisterFunctions`→KLuaScript.cpp, `AddTail`→KList.h, `PosUp`→KStepLuaScript.cpp

## `gamecore/LuaFuns.h`
- 17 dòng. Questions:单机版剧情脚本列表在网络版暂用.
- Gọi tới: `g_GetGameScriptFunNum`→ScriptFuns.cpp, `g_GetWorldScriptFunNum`→ScriptFuns.cpp

## `gamecore/MsgGenreDef.h`
- 17 dòng. 发送消息的类型

## `gamecore/ScriptFuns.cpp`
- 3235 dòng. Revision Count	:
- Hàm: `KSceGetFliePathc`, `GetPlayerIndex`, `GetObjIndex`, `LuaGetBit`, `LuaSetBit`, `LuaSetByte`, `LuaGetByte`, `GetSubWorldIndex`, `LuaSubWorldIDToIndex`, `LuaIndexToSubWorldID`, `LuaSetOrAddTrap`, `LuaSubWorldName`, `ExtractChars`, `LuaSayUI`, `LuaCreateSprSay`, `LuaCreateTaskSay`, `LuaCreateNewSayEx`, `LuaSayNew`, `LuaSendMessageInfo`, `LuaAddGlobalNews`, `LuaAddLocalNews`, `LuaAddSysNews`, `LuaAddGlobalCountNews`, `LuaAddLocalCountNews`, `LuaAddGlobalTimeNews` …(+61)
- Gọi tới: `t_sprintf`→KStrBase.cpp, `g_StrCpyLen`→KStrBase.cpp, `GetPlayerIndex`→KPlayer.cpp, `GetString`→KTabFile.cpp, `Clear`→KIniFile.cpp, `Load`→KIniFile.cpp, `g_StrCat`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `CoreDataChanged`→CoreShell.cpp, `Save`→KIniFile.cpp, `gTraceLogFile`→KLogFile.cpp, `Close`→KFile.cpp, `checkPos`→KScenePlaceC.cpp, `WriteString`→KTabFileCtrl.cpp, `SetTrap`→KRegion.cpp

## `gamecore/Skill.cpp`
- 1 dòng. (không có chú thích đầu)

## `gamecore/Skill.h`
- 38 dòng. (không có chú thích đầu)
- Gọi tới: `GetSkillId`→KThiefSkill.cpp, `GetSkillName`→KThiefSkill.cpp, `GetSkillStyle`→KSkillManager.h, `LoadSkillLevelData`→KSkills.cpp, `CanCastSkill`→KSkills.cpp, `NewCanCastSkill`→KSkills.cpp, `GetSkillCost`→KThiefSkill.cpp, `DrawSkillIcon`→KSkills.cpp

## `gamecore/SkillDef.h`
- 201 dòng. MoveKind 运动类型

## `gamecore/TaskDef.h`
- 6 dòng. (không có chú thích đầu)

## `gamescene/AutoPathFinder.cpp`
- 467 dòng. (không có chú thích đầu)
- Hàm: `FaceBook_link`, `FaceBook_link`, `FaceBook_link`, `FaceBook_link::InitFaceBook`, `FaceBook_link::setLink`, `FaceBook_link::reSet`, `FaceBook_link::getFaceBook`, `FaceBook_link::genFaceBook`, `FaceBook_link::Activate`, `FaceBook_link::setFaceBookInfo`, `FaceBook_link::setFaceBookState`
- Gọi tới: `GetMpsPos`→KMissle.cpp, `Activate`→KScriptList.cpp, `AiCheckDistance`→KNpcAI.cpp, `SendClientCmdRun`→KProtocol.cpp, `SendClientCmdWalk`→KProtocol.cpp, `t_sprintf`→KStrBase.cpp

## `gamescene/AutoPathFinder.h`
- 118 dòng. #pragma once
- Gọi tới: `FaceBook_link`→AutoPathFinder.cpp, `InitFaceBook`→AutoPathFinder.cpp, `setLink`→AutoPathFinder.cpp, `reSet`→AutoPathFinder.cpp, `getFaceBook`→AutoPathFinder.cpp, `Activate`→KScriptList.cpp, `setFaceBookState`→AutoPathFinder.cpp, `genFaceBook`→AutoPathFinder.cpp, `setFaceBookInfo`→AutoPathFinder.cpp

## `gamescene/KHRocker - Copy.cpp`
- 397 dòng. #include "../gamecore/KCore.h"
- Hàm: `HRocker::Active`, `HRocker::Inactive`, `HRocker::getAngleSigned`, `HRocker::getRad`, `HRocker::getDirection`, `HRocker::getVelocity`, `HRocker::onTouchBegan`, `HRocker::onTouchMoved`, `HRocker::onTouchEnded`, `HRocker::setTouchEnabled`, `HRocker::updateMovement`, `HRocker::isTouchInSpecificArea`
- Gọi tới: `create`→KHRocker.cpp, `setPadCanMove`→CoreShell.cpp, `getTradeState`→CoreShell.cpp, `Active`→KStepLuaScript.cpp, `SetNpcCurPos`→CoreShell.cpp, `setSand`→CoreShell.cpp, `setContentSize`→ComboBox.cpp, `reSet`→AutoPathFinder.cpp, `resetPeopledx`→CoreShell.cpp, `LockSomeoneAction`→CoreShell.cpp, `LockObjectAction`→CoreShell.cpp

## `gamescene/KHRocker - Copy.h`
- 55 dòng. #include "KgameWorld.h"
- Gọi tới: `Active`→KStepLuaScript.cpp, `Inactive`→KHRocker - Copy.cpp, `getDirection`→KHRocker - Copy.cpp, `getAngleSigned`→KHRocker - Copy.cpp, `getRad`→KHRocker - Copy.cpp, `getVelocity`→KHRocker - Copy.cpp, `updateMovement`→KHRocker - Copy.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `isTouchInSpecificArea`→KHRocker - Copy.cpp, `setTouchEnabled`→KHRocker - Copy.cpp

## `gamescene/KHRocker.cpp`
- 930 dòng. #include "../gamecore/KCore.h"
- Hàm: `HRocker::Active`, `HRocker::Inactive`, `HRocker::getAngleSigned`, `HRocker::getRad`, `HRocker::getDirection`, `HRocker::getVelocity`, `HRocker::onTouchBegan`, `HRocker::onTouchMoved`, `HRocker::onTouchMoved`, `HRocker::onTouchEnded`, `HRocker::onTouchCancelled`, `HRocker::setTouchEnabled`, `HRocker::updateMovement`, `HRocker::isTouchInSpecificArea`, `Joystick::create`, `Joystick::init`, `Joystick::onTouchesBegan`, `Joystick::onTouchesMoved`, `Joystick::onTouchesEnded`, `Joystick::setIsActive`, `Joystick::setOnActiveChange`, `Joystick::joystickBoundaryUpdate`, `Joystick::getDirection`, `Joystick::setJoystickRadius`, `Joystick::getIsActive` …(+1)
- Gọi tới: `setPadCanMove`→CoreShell.cpp, `getTradeState`→CoreShell.cpp, `LockSomeoneAction`→CoreShell.cpp, `LockObjectAction`→CoreShell.cpp, `getAngleSigned`→KHRocker - Copy.cpp, `getRad`→KHRocker - Copy.cpp, `setAttackSprVisible`→KgameWorld.cpp, `Active`→KStepLuaScript.cpp, `getDirection`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `setRoleDirPosition`→KgameWorld.cpp, `setRoleDirRotation`→KgameWorld.cpp, `setRoleDirVisible`→KgameWorld.cpp, `SetNpcCurPos`→CoreShell.cpp, `SendSerCommand`→KNpc.cpp

## `gamescene/KHRocker.h`
- 115 dòng. #include "KgameWorld.h"
- Gọi tới: `getDirection`→KHRocker - Copy.cpp, `Active`→KStepLuaScript.cpp, `Inactive`→KHRocker - Copy.cpp, `getAngleSigned`→KHRocker - Copy.cpp, `getRad`→KHRocker - Copy.cpp, `getVelocity`→KHRocker - Copy.cpp, `updateMovement`→KHRocker - Copy.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `onTouchCancelled`→KHRocker.cpp, `isTouchInSpecificArea`→KHRocker - Copy.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `create`→KHRocker.cpp, `setOnActiveChange`→KHRocker.cpp

## `gamescene/KIpoTree.cpp`
- 1701 dòng. 场景中的对象树
- Hàm: `KSelfBreathLight`, `KSelfBreathLight::Breath`, `KIpoTree`, `KIpoTree`, `KIpoTree::Paint`, `KIpoTree::Breathe`, `KIpoTree::Clear`, `KIpoTree::RemoveRtoGroupWithPermanentLeaf`, `KIpoTree::AddBranch`, `KIpoTree::Fell`, `KIpoTree::AddLeafLine`, `KIpoTree::AddLeafPoint`, `KIpoTree::PluckRto`, `KIpoTree::SetPermanentBranchPos`, `KIpoTree::StrewRtoLeafs`, `KIpoTree::ObjectsCallback`, `KIpoTree::FillLineObstacle`, `KIpoTree::RenderLightMap`, `KIpoTree::RenderLightMap`, `KIpoTree::RenderLightMap`, `KIpoTree::CanLighting`, `KIpoTree::CanLighting`, `KIpoTree::AddBuildinLight`, `KIpoTree::EnableBioLights`, `KIpoTree::EnableDynamicLights`
- Gọi tới: `RemoveAllRtoLeafs`→KIpotBranch.cpp, `Clear`→KIniFile.cpp, `AddLeafPoint`→KIpotBranch.cpp, `AddLeafLine`→KIpotBranch.cpp, `PaintObjectLayer`→KIpotBranch.cpp, `PaintNoneObjectLayer`→KIpotBranch.cpp, `AddBranch`→KIpotBranch.cpp, `IsPlayer`→KNpc.cpp, `GetColor`→KScenePlaceRegionC.cpp, `EnumerateObjects`→KIpotBranch.cpp, `g_Random`→KRandom.cpp, `Paint`→KMissle.cpp, `Breathe`→CoreShell.cpp, `AddAObject`→KIpotBranch.cpp, `CoreGetGameObjLightInfo`→CoreDrawGameObj.cpp

## `gamescene/KIpoTree.h`
- 243 dòng. 场景地图中对象集合树
- Gọi tới: `Breath`→KIpoTree.cpp, `KIpoTree`→KIpoTree.cpp, `KSelfBreathLight`→KIpoTree.cpp, `Paint`→KMissle.cpp, `Clear`→KIniFile.cpp, `Fell`→KIpoTree.cpp, `StrewRtoLeafs`→KIpoTree.cpp, `AddBranch`→KIpotBranch.cpp, `RemoveAllRtoLeafs`→KIpotBranch.cpp, `AddLeafLine`→KIpotBranch.cpp, `AddLeafPoint`→KIpotBranch.cpp, `SetPermanentBranchPos`→KIpoTree.cpp, `PluckRto`→KIpoTree.cpp, `Breathe`→CoreShell.cpp, `AddBuildinLight`→KIpoTree.cpp

## `gamescene/KIpotBranch.cpp`
- 645 dòng. 场景内对象树的树枝
- Hàm: `KIpotBranch`, `KIpotBranch`, `KIpotBranch::EnumerateObjects`, `KIpotBranch::PaintObjectLayer`, `KIpotBranch::PaintNoneObjectLayer`, `KIpotBranch::RemoveAllRtoLeafs`, `KIpotBranch::AddAObject`, `KIpotBranch::AddBranch`, `KIpotBranch::AddSubBranch`, `KIpotBranch::Clear`, `KIpotBranch::SetLine`, `KIpotBranch::AddLeafLine`, `KIpotBranch::AddLeafPoint`, `KIpotBranch::AddPointLeafToList`, `KIpotBranch::AddLineLeafToList`
- Gọi tới: `SM_Relation_PointLine`→SceneMath.cpp, `SM_Distance_PointLine`→SceneMath.cpp, `Clear`→KIniFile.cpp, `KIpotLeaf_EnumerateObjects`→KIpotLeaf.cpp, `KIpotLeaf_PaintObjectLayer`→KIpotLeaf.cpp, `getIniDataForGame`→KgameWorld.cpp, `BuildinObjNextFrame`→KIpotLeaf.cpp, `KIpotLeaf_PaintNoneObjectLayer`→KIpotLeaf.cpp, `KIpotLeaf_RemoveAllRtoLeafs`→KIpotLeaf.cpp, `SM_Relation_LineLine_CheckCut`→SceneMath.cpp, `Clone`→KIpotLeaf.cpp, `KIpotLeaf_Clear`→KIpotLeaf.cpp, `SM_Relation_PointLine_New`→SceneMath.cpp

## `gamescene/KIpotBranch.h`
- 183 dòng. 场景对象树上的树枝
- Gọi tới: `KIpotBranch`→KIpotBranch.cpp, `AddBranch`→KIpotBranch.cpp, `RemoveAllRtoLeafs`→KIpotBranch.cpp, `PaintObjectLayer`→KIpotBranch.cpp, `EnumerateObjects`→KIpotBranch.cpp, `PaintNoneObjectLayer`→KIpotBranch.cpp, `Clear`→KIniFile.cpp, `AddAObject`→KIpotBranch.cpp, `SetLine`→KIpotBranch.cpp, `AddLeafLine`→KIpotBranch.cpp, `AddLeafPoint`→KIpotBranch.cpp, `AddSubBranch`→KIpotBranch.cpp, `AddLineLeafToList`→KIpotBranch.cpp, `AddPointLeafToList`→KIpotBranch.cpp

## `gamescene/KIpotLeaf.cpp`
- 337 dòng. 场景对象树上的树叶的函数
- Hàm: `KIpotRuntimeObj::Pluck`, `KIpotLeaf_EnumerateObjects`, `KIpotLeaf_PaintObjectLayer`, `KIpotLeaf_PaintNoneObjectLayer`, `KIpotBuildinObj::PaintABuildinObject`, `KIpotLeaf_RemoveAllRtoLeafs`, `KIpotLeaf_Clear`, `KIpotBuildinObj::Clone`, `BuildinObjNextFrame`
- Gọi tới: `getIniDataForGame`→KgameWorld.cpp, `CoreDrawGameObj`→CoreDrawGameObj.cpp, `DrawPrimitives_BigMap`→KgameWorld.cpp, `DrawPrimitives`→KgameWorld.cpp, `ccMessageBox_new`→KCore.cpp, `GetImageParam`→KImageStore2.cpp, `IR_GetCurrentTime`→ImgRef.cpp, `IR_NextFrame`→ImgRef.cpp

## `gamescene/KIpotLeaf.h`
- 143 dòng. 场景中的对象树中的树叶结构定义
- Gọi tới: `KIpotLeaf_EnumerateObjects`→KIpotLeaf.cpp, `KIpotLeaf_PaintObjectLayer`→KIpotLeaf.cpp, `KIpotLeaf_PaintNoneObjectLayer`→KIpotLeaf.cpp, `KIpotLeaf_RemoveAllRtoLeafs`→KIpotLeaf.cpp, `KIpotLeaf_Clear`→KIpotLeaf.cpp, `Pluck`→KIpotLeaf.cpp, `Clone`→KIpotLeaf.cpp, `PaintABuildinObject`→KIpotLeaf.cpp, `BuildinObjNextFrame`→KIpotLeaf.cpp

## `gamescene/KScenePlaceC.cpp`
- 2893 dòng. ������ͼ���ͻ��˰棩
- Hàm: `ChaZhiColor`, `EnvironmentLight`, `EnvironmentLight::SetLight`, `EnvironmentLight::SetLight`, `EnvironmentLight::SetLight`, `EnvironmentLight::GetEnvironmentLight`, `KScenePlaceC`, `KScenePlaceC`, `KScenePlaceC::CreateEvent`, `KScenePlaceC::WaitForSingleObject`, `KScenePlaceC::CloseHandle`, `KScenePlaceC::SetEvent`, `KScenePlaceC::ResetEvent`, `KScenePlaceC::ClosePlace`, `KScenePlaceC::_LoadProcess`, `KScenePlaceC::Run`, `KScenePlaceC::Initialize`, `KScenePlaceC::OpenPlace`, `KScenePlaceC::checkPos`, `KScenePlaceC::initMapInfo`, `KScenePlaceC::GetObstacleByMap`, `KScenePlaceC::GetCellObstacle`, `KScenePlaceC::GetBarrierBuf`, `KScenePlaceC::SetHaveLoad`, `KScenePlaceC::SetRepresentAreaSize` …(+50)
- Gọi tới: `t_sprintf`→KStrBase.cpp, `GetInteger`→KTabFile.cpp, `Clear`→KIniFile.cpp, `SetFocusPosition`→KSubWorld.cpp, `GetRegionIndex`→KScenePlaceRegionC.cpp, `GetString`→KTabFile.cpp, `GetColor`→KScenePlaceRegionC.cpp, `PluckRto`→KIpoTree.cpp, `Paint`→KMissle.cpp, `GetNext`→KNode.h, `GetImageParam`→KImageStore2.cpp, `Load`→KIniFile.cpp, `gTraceLogFile`→KLogFile.cpp, `AddLeafPoint`→KIpotBranch.cpp, `GetHead`→KList.h

## `gamescene/KScenePlaceC.h`
- 695 dòng. 场景地图（客户端版）
- Gọi tới: `SetLight`→KScenePlaceC.cpp, `KScenePlaceC`→KScenePlaceC.cpp, `EnvironmentLight`→KScenePlaceC.cpp, `GetEnvironmentLight`→KScenePlaceC.cpp, `Initialize`→KLogFile.cpp, `Terminate`→KScenePlaceC.cpp, `OpenPlace`→KScenePlaceC.cpp, `ClosePlace`→KScenePlaceC.cpp, `Paint`→KMissle.cpp, `GetMapNextMovePos`→KScenePlaceC.cpp, `initMapInfo`→KScenePlaceC.cpp, `SetFocusPosition`→KSubWorld.cpp, `GetFocusPosition`→KScenePlaceC.cpp, `AddObject`→KuiCompoundItem.cpp, `MoveObject`→KgameWorld.cpp

## `gamescene/KScenePlaceRegionC.cpp`
- 2389 dòng. 场景地图的区域对象的类定义实现
- Hàm: `KScenePlaceRegionC`, `KScenePlaceRegionC`, `KScenePlaceRegionC::GetRegionIndex`, `KScenePlaceRegionC::ToLoad`, `KScenePlaceRegionC::LoadRe`, `KScenePlaceRegionC::GetFliePath`, `KScenePlaceRegionC::Clear`, `KScenePlaceRegionC::GetColor`, `KScenePlaceRegionC::PrerenderGround`, `KScenePlaceRegionC::SetNestRegion`, `KScenePlaceRegionC::LoadGroundLayer`, `KScenePlaceRegionC::AddGrundCoverObj`, `KScenePlaceRegionC::LoadObstacle`, `KScenePlaceRegionC::LoadTrap`, `KScenePlaceRegionC::LoadAboveGroundObjects`, `KScenePlaceRegionC::PaintGroundDirect_Part`, `KScenePlaceRegionC::PaintGroundDirect_full`, `KScenePlaceRegionC::PaintGroundDirect`, `KScenePlaceRegionC::ReomeGroundObj`, `KScenePlaceRegionC::PaintGroundDirect_old`, `KScenePlaceRegionC::PaintGround_old`, `KScenePlaceRegionC::PaintGround`, `KScenePlaceRegionC::PaintBuildinObj`, `KScenePlaceRegionC::PaintObstacle`, `KScenePlaceRegionC::GetNextMapPos` …(+10)
- Gọi tới: `t_sprintf`→KStrBase.cpp, `getIniDataForGame`→KgameWorld.cpp, `Read`→KFile.cpp, `Clear`→KIniFile.cpp, `DrawPrimitives`→KgameWorld.cpp, `Seek`→KFile.cpp, `Close`→KFile.cpp, `ccMessageBox_new`→KCore.cpp, `Open`→KFile.cpp, `DrawPrimitives_BigMap`→KgameWorld.cpp, `GetData`→KSellItem.cpp, `Size`→KFile.cpp, `GetFliePath`→KRegion.cpp, `LoadTrap`→KSubWorld.cpp, `Save`→KIniFile.cpp

## `gamescene/KScenePlaceRegionC.h`
- 447 dòng. 场景地图的区域对象的类声明
- Gọi tới: `KScenePlaceRegionC`→KScenePlaceRegionC.cpp, `Clear`→KIniFile.cpp, `ToLoad`→KScenePlaceRegionC.cpp, `getStatus`→KCheckbox.cpp, `LoadRe`→KScenePlaceRegionC.cpp, `GetRegionIndex`→KScenePlaceRegionC.cpp, `GetFliePath`→KRegion.cpp, `PrerenderGround`→KScenePlaceC.cpp, `GetColor`→KScenePlaceRegionC.cpp, `PaintGround_old`→KScenePlaceRegionC.cpp, `PaintGroundDirect_old`→KScenePlaceRegionC.cpp, `PaintGround`→KScenePlaceRegionC.cpp, `PaintBuildinObj`→KScenePlaceRegionC.cpp, `ReomeGroundObj`→KScenePlaceRegionC.cpp, `PaintGroundDirect`→KScenePlaceRegionC.cpp

## `gamescene/KSkillRocker.cpp`
- 277 dòng. #include "../gamecore/KCore.h"
- Hàm: `KSkillRocker::Active`, `KSkillRocker::Inactive`, `KSkillRocker::getAngleSigned`, `KSkillRocker::getRad`, `KSkillRocker::getDirection`, `KSkillRocker::getVelocity`, `KSkillRocker::onTouchBegan`, `KSkillRocker::onTouchMoved`, `KSkillRocker::onTouchEnded`, `KSkillRocker::setSpriteOpacity`, `KSkillRocker::setSpriteVisible`, `KSkillRocker::setSpritePiont`
- Gọi tới: `Active`→KStepLuaScript.cpp, `setPadCanMove`→CoreShell.cpp, `getTradeState`→CoreShell.cpp, `ccMessageBox_new`→KCore.cpp, `Inactive`→KHRocker - Copy.cpp, `getAngleSigned`→KHRocker - Copy.cpp, `getRad`→KHRocker - Copy.cpp, `create`→KHRocker.cpp, `getDirection`→KHRocker - Copy.cpp, `getVelocity`→KHRocker - Copy.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `LockSomeoneAction`→CoreShell.cpp, `LockObjectAction`→CoreShell.cpp, `onTouchEnded`→KHRocker - Copy.cpp

## `gamescene/KSkillRocker.h`
- 51 dòng. #include "KgameWorld.h"
- Gọi tới: `Active`→KStepLuaScript.cpp, `Inactive`→KHRocker - Copy.cpp, `getDirection`→KHRocker - Copy.cpp, `getAngleSigned`→KHRocker - Copy.cpp, `getRad`→KHRocker - Copy.cpp, `setSpritePiont`→KSkillRocker.cpp, `setSpriteVisible`→KSkillRocker.cpp, `setSpriteOpacity`→KSkillRocker.cpp, `getVelocity`→KHRocker - Copy.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp

## `gamescene/KUpdateLayer.cpp`
- 1379 dòng. #include "../../gameui/StrokeLabel.h"
- Hàm: `KUpdateLayer`, `KUpdateLayer::isFileExist`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `GetStringByKeyFromFile_old`→CXmlStream.cpp, `create`→KHRocker.cpp, `Load`→KIniFile.cpp, `Clear`→KIniFile.cpp, `GetString`→KTabFile.cpp, `GetInteger`→KTabFile.cpp, `GetStringByKeyFromFile`→CXmlStream.cpp, `copyData`→KgameWorld.cpp, `startload`→KTranSence.cpp, `isFileExist`→KgameWorld.cpp, `DownLoadFile`→KDownLoadFile.cpp, `SimplyDecrypt`→dataChecksum.cpp, `g_StrCopy`→KStrBase.cpp

## `gamescene/KUpdateLayer.h`
- 159 dòng. Sword3 Engine (c) 1999-2000 by Kingsoft
- Gọi tới: `create`→KHRocker.cpp, `KUpdateLayer`→KUpdateLayer.cpp, `init`→HelloWorldScene.cpp, `scene`→KgameWorld.cpp, `onEnter`→KgameWorld.cpp, `update`→KgameWorld.cpp, `startload`→KTranSence.cpp, `downLoadAllMapmusic`→KMapMusic.cpp, `copyData`→KgameWorld.cpp, `isFileExist`→KgameWorld.cpp, `loadSuccess`→Klogin.cpp, `loadingCallBack`→KTranSence.cpp, `menuTanCallback`→KuiCompoundItem.cpp

## `gamescene/KgameWorld.cpp`
- 15398 dòng. #include "../gameui/PopupLayer.h"
- Hàm: `KgameWorld`, `KgameWorld`, `KgameWorld::scene`, `KgameWorld::init`, `KgameWorld::selchatlistItemEvent`, `KgameWorld::startOpenAuto`, `KgameWorld::mQizCallback`, `KgameWorld::closeDyshopPadCallback`, `KgameWorld::mPaimaiCallback`, `KgameWorld::mTaskCallback`, `KgameWorld::closetaskPadCallback`, `KgameWorld::ccMessageBox_new`, `KgameWorld::_quitGame`, `KgameWorld::mOptionsCallback`, `KgameWorld::closeescPadCallback`, `KgameWorld::mFactionCallback`, `KgameWorld::closeTongPadCallback`, `KgameWorld::closetradePadCallback`, `KgameWorld::closeChatlistPad`, `KgameWorld::closegivePadCallback`, `KgameWorld::closeLaoPadCallback`, `KgameWorld::mTeamCallback`, `KgameWorld::closeTeamPadCallback`, `KgameWorld::mSkillsCallback`, `KgameWorld::closeDuanPadCallback` …(+228)
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `ccMessageBox_new`→KCore.cpp, `GetLocalPositionByMps`→KSubWorld.cpp, `g_StrLower`→KStrBase.cpp, `getpicPath`→Kgetinidata.cpp, `g_FileName2Id`→KFilePath.cpp, `UiSoundPlay_Ui`→UiSoundSetting.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `findinidata_one`→Kgetinidata.cpp, `_removeDelegate`→KuiAutoPlay.cpp, `removeShowSprite`→KuiShowSprite.cpp, `GetInteger`→KTabFile.cpp, `GetString`→KTabFile.cpp, `UpdateItem`→KSellItem.cpp

## `gamescene/KgameWorld.h`
- 657 dòng. Created by 2018.10 横刀向天笑 QQ:25557432 //tuanln
- Gọi tới: `KgameWorld`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `ccgetTxtData`→KgameWorld.cpp, `ccgetTxtData_g`→KgameWorld.cpp, `onTouchesBegan`→HelloWorldScene.cpp, `onTouchesMoved`→KgameWorld.cpp, `onTouchesEnded`→KgameWorld.cpp, `onTouchesCancelled`→KgameWorld.cpp, `init`→HelloWorldScene.cpp, `onEnter`→KgameWorld.cpp, `onExit`→KgameWorld.cpp, `onEnterTransitionDidFinish`→KgameWorld.cpp, `update`→KgameWorld.cpp, `scene`→KgameWorld.cpp, `setSkillNextUseTime`→KgameWorld.cpp

## `gamescene/LoginDef.h`
- 106 dòng. 界面--login窗口

## `gamescene/ObstacleDef.h`
- 24 dòng. (không có chú thích đầu)

## `gamescene/SceneDataDef.h`
- 432 dòng. 场景模块的一些数据定义
- Gọi tới: `GetColor`→KScenePlaceRegionC.cpp

## `gamescene/SceneMath.cpp`
- 591 dòng. 场景模块的一些数学计算
- Hàm: `SM_IsPointOnLine`, `SM_Distance_PointLine`, `SM_Relation_PointLine`, `SM_Relation_PointLine_New`, `SM_Relation_LineLine_CheckCut`, `SM_GetPointFromFloatSting32`, `ChangeFileName`
- Gọi tới: `GetElapseFrequency`→KTimer.cpp, `g_StrLen`→KStrBase.cpp, `Start`→KTimer.cpp, `qsqrt`→KMath.h

## `gamescene/SceneMath.h`
- 67 dòng. 场景模块的一些数学计算
- Hàm: `SM_Relation_LineLine`
- Gọi tới: `SM_IsPointOnLine`→SceneMath.cpp, `SM_Distance_PointLine`→SceneMath.cpp, `SM_Relation_PointLine`→SceneMath.cpp, `SM_Relation_PointLine_New`→SceneMath.cpp, `SM_Relation_LineLine_CheckCut`→SceneMath.cpp, `SM_GetPointFromFloatSting32`→SceneMath.cpp, `ChangeFileName`→SceneMath.cpp

## `gamescene/ScenePlaceMapC.cpp`
- 1285 dòng. 地图的类定义实现
- Hàm: `KScenePlaceMapC`, `KScenePlaceMapC`, `KScenePlaceMapC::Initialize`, `KScenePlaceMapC::Terminate`, `KScenePlaceMapC::SetShowElemsFlag`, `KScenePlaceMapC::CreateFolder`, `KScenePlaceMapC::SetFocusPosition`, `KScenePlaceMapC::FillCellsPicInfo`, `KScenePlaceMapC::CalcPicLayout`, `KScenePlaceMapC::Free`, `KScenePlaceMapC::PaintMap`, `KScenePlaceMapC::PaintSymbol`, `KScenePlaceMapC::MapGoTo`, `KScenePlaceMapC::PaintCharacters`, `KScenePlaceMapC::PaintMapPic`, `KScenePlaceMapC::SetSize`, `KScenePlaceMapC::GetMapRect`, `KScenePlaceMapC::SetGreenLine`, `KScenePlaceMapC::GetColor`, `KScenePlaceMapC::Draw`
- Gọi tới: `KSG_StringGetInt`→KSG_StringProcess.cpp, `t_sprintf`→KStrBase.cpp, `KSG_StringSkipSymbol`→KSG_StringProcess.cpp, `ccMessageBox_new`→KCore.cpp, `DrawPrimitives`→KgameWorld.cpp, `GetString`→KTabFile.cpp, `GetColor`→KScenePlaceRegionC.cpp, `Terminate`→KScenePlaceC.cpp, `SetFocusPosition`→KSubWorld.cpp, `g_FileName2Id`→KFilePath.cpp, `isFileExist`→KgameWorld.cpp, `SendSerCommand`→KNpc.cpp, `SendClientCmdRun`→KProtocol.cpp, `getIniDataForGame`→KgameWorld.cpp, `Initialize`→KLogFile.cpp

## `gamescene/ScenePlaceMapC.h`
- 181 dòng. 场景地图的小地图
- Gọi tới: `KScenePlaceMapC`→ScenePlaceMapC.cpp, `PaintSymbol`→ScenePlaceMapC.cpp, `Terminate`→KScenePlaceC.cpp, `Load`→KIniFile.cpp, `Free`→KMemClass.cpp, `SetFocusPosition`→KSubWorld.cpp, `SetShowElemsFlag`→ScenePlaceMapC.cpp, `SetSize`→ScenePlaceMapC.cpp, `PaintMap`→KScenePlaceC.cpp, `GetMapRect`→ScenePlaceMapC.cpp, `SetGreenLine`→ScenePlaceMapC.cpp, `DelGreenLine`→KScenePlaceC.cpp, `MapGoTo`→ScenePlaceMapC.cpp, `Draw`→KLittleMap.cpp, `Initialize`→KLogFile.cpp

## `gameui/DeviceInfo.cpp`
- 73 dòng. Thay "org/cocos2dx/cpp/AppActivity" bằng package của bạn nếu cần
- Hàm: `DeviceInfo::getDeviceBatteryPercentage`, `DeviceInfo::getOSVersion`

## `gameui/DeviceInfo.h`
- 18 dòng. Lấy phần trăm pin hiện tại của thiết bị (trên Android)
- Gọi tới: `getDeviceBatteryPercentage`→DeviceInfo.cpp, `getOSVersion`→DeviceInfo.cpp

## `gameui/GameSpaceChangedNotify.cpp`
- 544 dòng. 功能：接受游戏世界数据改变通知的函数   ---收到服务器通知打开响应窗口
- Hàm: `CoreDataChangedCallback`
- Gọi tới: `QueryAllChannel`→KgameWorld.cpp, `UpdateExBox`→KgameWorld.cpp, `UpdateMemberList`→KuiTongInfoVN.cpp, `OpenWindow_DuanZhao`→KgameWorld.cpp, `t_sprintf`→KStrBase.cpp, `UpDataToTeamInfo`→KgameWorld.cpp, `CreatNpcDialog`→KgameWorld.cpp, `UpdateItem`→KSellItem.cpp, `UpdateItemEx`→KgameWorld.cpp, `UpdateStoreBox`→KgameWorld.cpp, `UpdateImmediaItem`→KgameWorld.cpp, `NewRankArrive`→KgameWorld.cpp, `OpenWenItemDialog`→KgameWorld.cpp, `OpenComItemDialog`→KgameWorld.cpp, `OpenCreatTongSheet`→KgameWorld.cpp

## `gameui/GameSpaceChangedNotify.h`
- 5 dòng. 接受游戏世界数据改变通知的函数
- Gọi tới: `CoreDataChangedCallback`→GameSpaceChangedNotify.cpp

## `gameui/KCheckbox.cpp`
- 95 dòng. 创建,参数：未选中图片名，选中图片名，文字，状态（0-未选中，1-选中）
- Hàm: `KCheckbox::create`, `KCheckbox::click`, `KCheckbox::getStatus`
- Gọi tới: `create`→KHRocker.cpp, `setContentSize`→ComboBox.cpp

## `gameui/KCheckbox.h`
- 22 dòng. 创建checkbox
- Gọi tới: `create`→KHRocker.cpp, `click`→KCheckbox.cpp, `getStatus`→KCheckbox.cpp

## `gameui/KSelPlayer.cpp`
- 1197 dòng. #include "Klogin.h"
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `g_FileName2Id`→KFilePath.cpp, `isFileExist`→KgameWorld.cpp, `g_StrLower`→KStrBase.cpp, `GetRoleImageName`→KuiNewPlayer.cpp, `scene`→KgameWorld.cpp, `Cleanup`→ClientStage.cpp, `setBreakTheead`→SocketClient.cpp, `EnterGame`→KuiSelPlayer_new.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `setBufferEmpty`→ClientStage.cpp, `g_StrCmp`→KStrBase.cpp, `GetProtocolSize`→CoreShell.cpp

## `gameui/KSelPlayer.h`
- 107 dòng. 登陆界面 选择人物 创建 删除等
- Gọi tới: `init`→HelloWorldScene.cpp, `onEnter`→KgameWorld.cpp, `onExit`→KgameWorld.cpp, `onEnterTransitionDidFinish`→KgameWorld.cpp, `update`→KgameWorld.cpp, `scene`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `AcceptNetMsg`→KuiWarnInfo.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `copyData`→KgameWorld.cpp, `isFileExist`→KgameWorld.cpp, `buttonCallback`→KgameWorld.cpp, `EnterGame`→KuiSelPlayer_new.cpp, `GetRoleCount`→KuiNewPlayer.cpp, `mainEnterCallback`→KuiNewPlayer.cpp

## `gameui/KTranSence.cpp`
- 414 dòng. #include "../gameui/PopupLayer.h"
- Hàm: `KTranSence`, `KTranSence`, `KTranSence::scene`, `KTranSence::init`, `KTranSence::loadingCallBack`, `KTranSence::mianCancelCallback`, `KTranSence::loadSuccess`, `KTranSence::update`, `KTranSence::draw`, `KTranSence::isFileExist`, `KTranSence::copyData`, `KTranSence::startload`, `KTranSence::Run`, `KTranSence::onEnter`, `KTranSence::onExit`, `KTranSence::onEnterTransitionDidFinish`, `KTranSence::onTouchBegan`, `KTranSence::onTouchMoved`, `KTranSence::onTouchCancelled`, `KTranSence::onTouchEnded`, `KTranSence::ClearAccountPassword`, `KTranSence::ClearCachedata`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `scene`→KgameWorld.cpp, `ccMessageBox_new`→KCore.cpp, `isFileExist`→KgameWorld.cpp, `GetProtocolSize`→CoreShell.cpp, `init`→HelloWorldScene.cpp, `g_FileName2Id`→KFilePath.cpp, `loadSuccess`→Klogin.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `g_StrLower`→KStrBase.cpp, `mianCancelCallback`→Klogin.cpp, `Cleanup`→ClientStage.cpp, `setBreakTheead`→SocketClient.cpp, `update`→KgameWorld.cpp

## `gameui/KTranSence.h`
- 95 dòng. ��½���桡�����ʺ�����
- Gọi tới: `KTranSence`→KTranSence.cpp, `init`→HelloWorldScene.cpp, `update`→KgameWorld.cpp, `onEnter`→KgameWorld.cpp, `onExit`→KgameWorld.cpp, `onEnterTransitionDidFinish`→KgameWorld.cpp, `scene`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `loadSuccess`→Klogin.cpp, `loadingCallBack`→KTranSence.cpp, `mianCancelCallback`→Klogin.cpp, `AcceptNetMsg`→KuiWarnInfo.cpp, `copyData`→KgameWorld.cpp, `isFileExist`→KgameWorld.cpp, `onTouchesEnded`→KgameWorld.cpp

## `gameui/Klogin.cpp`
- 1122 dòng. #include "../gameui/PopupLayer.h"
- Hàm: `CcharToDouble`, `Klogin::scene`, `Klogin::init`, `Klogin::closeShowSpritePad`, `Klogin::mianCancelCallback`, `Klogin::mianLoginCallback`, `Klogin::mianSkillCallback`, `Klogin::loadSuccess`, `Klogin::update`, `Klogin::draw`, `Klogin::isFileExist`, `Klogin::copyData`, `Klogin::finish`, `Klogin::onEnter`, `Klogin::onExit`, `Klogin::onEnterTransitionDidFinish`, `Klogin::onTouchBegan`, `Klogin::onTouchMoved`, `Klogin::onTouchCancelled`, `Klogin::onTouchesBegan`, `Klogin::onTouchesMoved`, `Klogin::onTouchesEnded`, `Klogin::onTouchesCancelled`, `Klogin::onTouchEnded`, `Klogin::SetAccountPassword` …(+8)
- Gọi tới: `t_sprintf`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `create`→KHRocker.cpp, `scene`→KgameWorld.cpp, `isFileExist`→KgameWorld.cpp, `Clear`→KIniFile.cpp, `g_StrLower`→KStrBase.cpp, `Load`→KIniFile.cpp, `GetString`→KTabFile.cpp, `GetInteger`→KTabFile.cpp, `g_FileName2Id`→KFilePath.cpp, `AcceptNetMsg`→KuiWarnInfo.cpp, `init`→HelloWorldScene.cpp, `getpicPath`→Kgetinidata.cpp, `Cleanup`→ClientStage.cpp

## `gameui/Klogin.h`
- 89 dòng. 登陆界面　输入帐号密码
- Gọi tới: `init`→HelloWorldScene.cpp, `onEnter`→KgameWorld.cpp, `onExit`→KgameWorld.cpp, `onEnterTransitionDidFinish`→KgameWorld.cpp, `scene`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `update`→KgameWorld.cpp, `AcceptNetMsg`→KuiWarnInfo.cpp, `copyData`→KgameWorld.cpp, `isFileExist`→KgameWorld.cpp, `mianSkillCallback`→KgameWorld.cpp, `mianLoginCallback`→Klogin.cpp, `mianCancelCallback`→Klogin.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp

## `gameui/Klogin_f.cpp`
- 1878 dòng. #include "../gameui/PopupLayer.h"
- Hàm: `Klogin_f::onEnter`, `Klogin_f::onExit`, `Klogin_f::onEnterTransitionDidFinish`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `isFileExist`→KgameWorld.cpp, `GetInstance`→KgameWorld.cpp, `g_StrLower`→KStrBase.cpp, `DrawSubLable`→KgameWorld.cpp, `ccMessageBox_new`→KCore.cpp, `g_FileName2Id`→KFilePath.cpp, `init`→HelloWorldScene.cpp, `GetString`→KTabFile.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `GetInteger`→KTabFile.cpp, `Clear`→KIniFile.cpp, `scene`→KgameWorld.cpp, `SimplyDecrypt`→dataChecksum.cpp

## `gameui/Klogin_f.h`
- 90 dòng. #include "physics_nodes/CCPhysicsSprite.h"
- Gọi tới: `draw`→HelloWorldScene.cpp, `init`→HelloWorldScene.cpp, `update`→KgameWorld.cpp, `scene`→KgameWorld.cpp, `copyData`→KgameWorld.cpp, `isFileExist`→KgameWorld.cpp, `buttonCallback`→KgameWorld.cpp, `onTouchesEnded`→KgameWorld.cpp, `mianLoginCallback`→Klogin.cpp, `mianCancelCallback`→Klogin.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `onTouchCancelled`→KHRocker.cpp, `closeOptionCallback`→KuiEscInfo.cpp

## `gameui/KuiAccreg.cpp`
- 572 dòng. 有按钮的　ｔａｌｋ　对话框
- Gọi tới: `ccMessageBox_new`→KCore.cpp, `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `isFileExist`→KgameWorld.cpp, `g_StrLower`→KStrBase.cpp, `setContentSize`→ComboBox.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `g_FileName2Id`→KFilePath.cpp, `GetString`→KTabFile.cpp, `SimplyDecrypt`→dataChecksum.cpp, `scene`→KgameWorld.cpp, `KSG_StringToMD5String`→KSG_MD5_String.cpp

## `gameui/KuiAccreg.h`
- 83 dòng. #define FIGHT_SKILL_COUNT_PER_PAGE	25
- Gọi tới: `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `editBoxEditingDidBegin`→KgameWorld.cpp, `editBoxEditingDidEnd`→KgameWorld.cpp, `editBoxReturn`→KgameWorld.cpp, `editBoxTextChanged`→KgameWorld.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `mianLoginCallback`→Klogin.cpp, `mianCancelCallback`→Klogin.cpp

## `gameui/KuiAttackSkillsMenu.cpp`
- 275 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiAttackSkillsMenu`, `KuiAttackSkillsMenu`, `KuiAttackSkillsMenu::create`, `KuiAttackSkillsMenu::init`, `KuiAttackSkillsMenu::teseCallBakc`, `KuiAttackSkillsMenu::addDialogData`, `KuiAttackSkillsMenu::setcoloseButton`, `KuiAttackSkillsMenu::buttonCallBackFunc`, `KuiAttackSkillsMenu::closePopLayer`, `KuiAttackSkillsMenu::getRect`, `KuiAttackSkillsMenu::onTouchBegan`, `KuiAttackSkillsMenu::onTouchMoved`, `KuiAttackSkillsMenu::onTouchEnded`, `KuiAttackSkillsMenu::update`, `KuiAttackSkillsMenu::draw`
- Gọi tới: `create`→KHRocker.cpp, `init`→HelloWorldScene.cpp, `setContentSize`→ComboBox.cpp, `t_sprintf`→KStrBase.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `GetSceneFocus`→KScenePlaceC.cpp, `g_FileName2Id`→KFilePath.cpp, `isFileExist`→KgameWorld.cpp, `Size`→KFile.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp

## `gameui/KuiAttackSkillsMenu.h`
- 76 dòng. void _setPlayerFun(Kuiplayerfun * ver){nPlayerFun=ver;};
- Gọi tới: `KuiAttackSkillsMenu`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `teseCallBakc`→KuiAttackSkillsMenu.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `gameui/KuiAutoPlay.cpp`
- 6987 dòng. #include "engine/KPalette.h"
- Hàm: `ResetAuto`, `KuiAutoPlay`, `KuiAutoPlay`, `KuiAutoPlay::create`, `KuiAutoPlay::init`, `KuiAutoPlay::addDialogData`, `KuiAutoPlay::selectedMainListItemEvent`, `KuiAutoPlay::AddComboBox`, `KuiAutoPlay::ShowNodes`, `KuiAutoPlay::valueChangedOther`, `KuiAutoPlay::valueChanged`, `KuiAutoPlay::setcoloseButton`, `KuiAutoPlay::buttonCallBackFunc`, `KuiAutoPlay::buttonSaveCallBackFunc`, `KuiAutoPlay::closePopLayer`, `KuiAutoPlay::clearTempSelindex`, `KuiAutoPlay::getRect`, `KuiAutoPlay::SaveConfig`, `KuiAutoPlay::oktouchEvent`, `KuiAutoPlay::touchValueToggle`, `KuiAutoPlay::touchPageBtnEvent`, `KuiAutoPlay::onTouchBegan`, `KuiAutoPlay::setBtnTouchEnble`, `KuiAutoPlay::_removeDelegate`, `KuiAutoPlay::DoSkillBuff` …(+54)
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `GetInteger`→KTabFile.cpp, `WriteInteger`→KTabFileCtrl.cpp, `GetString`→KTabFile.cpp, `WriteString`→KTabFileCtrl.cpp, `GetMpsPos`→KMissle.cpp, `OperationRequest`→CoreShell.cpp, `g_Atoui`→KStrBase.cpp, `GetNextItem`→KInventory.cpp, `ClientShowMsg`→KNpc.cpp, `Load`→KIniFile.cpp, `__distance`→KScenePlaceCVN.cpp, `GetSkill`→KSkillManager.h, `setContentSize`→ComboBox.cpp

## `gameui/KuiAutoPlay.h`
- 599 dòng. PopupLayer.h
- Gọi tới: `KuiAutoPlay`→KuiAutoPlay.cpp, `Push`→KMemStack.cpp, `Reset`→KTimer.cpp, `SetValue`→KTabFileCtrl.cpp, `SellItems`→KuiAutoPlay.cpp, `IsInSellList`→KuiAutoPlay.cpp, `IsInBlackList`→KuiAutoPlay.cpp, `IsInRedList`→KuiAutoPlay.cpp, `UseTDP`→KuiAutoPlay.cpp, `UseTHP`→KuiAutoPlay.cpp, `GetSaveItems`→KuiAutoPlay.cpp, `GetSaveMoney`→KuiAutoPlay.cpp, `GetGroceries`→KuiAutoPlay.cpp, `GetPharmacy`→KuiAutoPlay.cpp, `GetReputation`→KuiAutoPlay.cpp

## `gameui/KuiBtnControl.cpp`
- 1207 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiBtnControl`, `KuiBtnControl`, `KuiBtnControl::create`, `KuiBtnControl::init`, `KuiBtnControl::addDialogData`, `KuiBtnControl::touchBtnEvent_baofu`, `KuiBtnControl::setcoloseButton`, `KuiBtnControl::buttonCallBackFunc`, `KuiBtnControl::closePopLayer`, `KuiBtnControl::getRect`, `KuiBtnControl::onTouchEnded`, `KuiBtnControl::onTouchMoved`, `KuiBtnControl::setBtnPosition`, `KuiBtnControl::moveLayer`, `KuiBtnControl::EndedLayer`, `KuiBtnControl::onTouchBegan`, `KuiBtnControl::UpItemData`, `KuiBtnControl::update`
- Gọi tới: `ccMessageBox_new`→KCore.cpp, `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `OperationRequest`→CoreShell.cpp, `GetGameData`→CoreShell.cpp, `GetID`→KFaction.cpp, `init`→HelloWorldScene.cpp, `GetAutoplayid`→CoreShell.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `findinidata_one`→Kgetinidata.cpp, `getPadCondition`→KgameWorld.cpp, `GetName`→KNpcResNode.cpp, `setTitle`→PopupLayer.cpp

## `gameui/KuiBtnControl.h`
- 92 dòng. Created by 2018.10 横刀向天笑 QQ:25557432
- Gọi tới: `KuiBtnControl`→KuiBtnControl.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `moveLayer`→KuiBtnControl.cpp, `EndedLayer`→KuiBtnControl.cpp, `setBtnPosition`→KuiBtnControl.cpp, `UpItemData`→KuiBtnControl.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp

## `gameui/KuiChatList.cpp`
- 1444 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiChatList`, `KuiChatList`, `KuiChatList::create`, `KuiChatList::init`, `KuiChatList::addDialogData`, `KuiChatList::Chat_ListBoxMenu`, `KuiChatList::AddChat_ListBoxMenu`, `KuiChatList::TinVang`, `KuiChatList::GanDay`, `KuiChatList::BieuCam`, `KuiChatList::FaceCallBackPad`, `KuiChatList::AnHopThoai`, `KuiChatList::Dong`, `KuiChatList::_removeDelegate`, `KuiChatList::selectedPlayersListItemEvent`, `KuiChatList::addmsg`, `KuiChatList::touchBtnEventBtn`, `KuiChatList::NewChannelMessageArrival`, `KuiChatList::_setPosition`, `KuiChatList::_getPosition`, `KuiChatList::setcoloseButton`, `KuiChatList::buttonCallBackFunc`, `KuiChatList::closePopLayer`, `KuiChatList::selectedItemEvent`, `KuiChatList::getRect` …(+6)
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `FilterTextColor`→Text.cpp, `setContentSize`→ComboBox.cpp, `UiSoundPlay_Ui`→UiSoundSetting.cpp, `getColorIndex`→Text.cpp, `g_Atoui`→KStrBase.cpp, `Size`→KFile.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `g_FileName2Id`→KFilePath.cpp, `hideListBoxMenu`→KgameWorld.cpp

## `gameui/KuiChatList.h`
- 127 dòng. #define FIGHT_SKILL_COUNT_PER_PAGE	25
- Gọi tới: `KuiChatList`→KuiChatList.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `Chat_ListBoxMenu`→KuiChatList.cpp, `AddChat_ListBoxMenu`→KuiChatList.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `addmsg`→KuiChatList.cpp, `NewChannelMessageArrival`→KuiChatList.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `_removeDelegate`→KuiAutoPlay.cpp, `selectedPlayersListItemEvent`→KuiChatList.cpp, `_setPosition`→KuiChatList.cpp, `_getPosition`→KuiChatList.cpp

## `gameui/KuiCometoMap.cpp`
- 2456 dòng. 有按钮的　ｔａｌｋ　对话框
- Hàm: `KuiCometoMap`, `KuiCometoMap`, `KuiCometoMap::create`, `KuiCometoMap::init`, `KuiCometoMap::addDialogData`, `KuiCometoMap::ArrangeDefaultData`, `KuiCometoMap::NewRankArrive`, `KuiCometoMap::NewIndexArrive`, `KuiCometoMap::StoreTempIni`, `KuiCometoMap::StoreNewIndexToTempFile`, `KuiCometoMap::StoreNewDataToTempFile`, `KuiCometoMap::AddRank`, `KuiCometoMap::AddIndex`, `KuiCometoMap::selectedListItemEvent_HuoDOng`, `KuiCometoMap::selectedMainListItemEvent`, `KuiCometoMap::LoadRankIni`, `KuiCometoMap::SendGetRankToCore`, `KuiCometoMap::UpdateRankData`, `KuiCometoMap::removeitems`, `KuiCometoMap::selectedMsgListItemEvent`, `KuiCometoMap::closeShowPad`, `KuiCometoMap::touchAwardBtnEvent`, `KuiCometoMap::touchPageBtnEvent`, `KuiCometoMap::setBtnTouchEnabled`, `KuiCometoMap::setBtnTouchEnble` …(+16)
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `GetInteger`→KTabFile.cpp, `GetString`→KTabFile.cpp, `Clear`→KIniFile.cpp, `Load`→KIniFile.cpp, `WriteInteger`→KTabFileCtrl.cpp, `findinidata_one`→Kgetinidata.cpp, `setBtnTouchEnble`→KuiAutoPlay.cpp, `ccMessageBox_new`→KCore.cpp, `g_StrLower`→KStrBase.cpp, `GetGameData`→CoreShell.cpp, `Reset`→KTimer.cpp, `GetCount`→KMissleSet.cpp

## `gameui/KuiCometoMap.h`
- 246 dòng. Created by 横刀向天笑 QQ:25557432
- Gọi tới: `KuiCometoMap`→KuiCometoMap.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `NewRankArrive`→KgameWorld.cpp, `NewIndexArrive`→KuiCometoMap.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `closeShowPad`→KuiCometoMap.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp

## `gameui/KuiCompoundItem.cpp`
- 3376 dòng. 有按钮的　ｔａｌｋ　对话框
- Hàm: `KuiCompoundItem`, `KuiCompoundItem`, `KuiCompoundItem::create`, `KuiCompoundItem::init`, `KuiCompoundItem::addDialogData`, `KuiCompoundItem::menuTanCallback`, `KuiCompoundItem::touchPageBtnEvent`, `KuiCompoundItem::changePage`, `KuiCompoundItem::setBtnTouchEnble`, `KuiCompoundItem::setcoloseButton`, `KuiCompoundItem::touchOperatioEvent`, `KuiCompoundItem::closePopLayer`, `KuiCompoundItem::closeItemPadCallback`, `KuiCompoundItem::getRectItem`, `KuiCompoundItem::onTouchEnded`, `KuiCompoundItem::onTouchMoved`, `KuiCompoundItem::onTouchBegan`, `KuiCompoundItem::btnCallBackFunc_quxia`, `KuiCompoundItem::getPadCondition`, `KuiCompoundItem::UpdateCurComItem`, `KuiCompoundItem::update`, `KuiCompoundItem::draw`, `KuiCompoundItem::AddObject_UpData`, `KuiCompoundItem::AddObject_Alts`, `KuiCompoundItem::AddObject` …(+1)
- Gọi tới: `t_sprintf`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `create`→KHRocker.cpp, `setBtnTouchEnble`→KuiAutoPlay.cpp, `GetName`→KNpcResNode.cpp, `GetID`→KFaction.cpp, `findinidata_one`→Kgetinidata.cpp, `g_StrLower`→KStrBase.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `GetString`→KTabFile.cpp, `OperationRequest`→CoreShell.cpp, `upItemDataUi`→KgameWorld.cpp, `PlaceItem`→KInventory.cpp, `setDialogPosition`→KuiEffect.cpp, `GetGameData`→CoreShell.cpp

## `gameui/KuiCompoundItem.h`
- 144 dòng. #define FIGHT_SKILL_COUNT_PER_PAGE	25
- Gọi tới: `KuiCompoundItem`→KuiCompoundItem.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `UpdateCurComItem`→KuiCompoundItem.cpp, `getPadCondition`→KgameWorld.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closeItemPadCallback`→KgameWorld.cpp, `btnCallBackFunc_quxia`→KuiCompoundItem.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp

## `gameui/KuiDialog.cpp`
- 516 dòng. (không có chú thích đầu)
- Hàm: `KuiDialog`, `KuiDialog`, `KuiDialog::create`, `KuiDialog::init`, `KuiDialog::addDialogData`, `KuiDialog::setcoloseButton`, `KuiDialog::closeShowPad`, `KuiDialog::buttonCallBackFunc`, `KuiDialog::closePopLayer`, `KuiDialog::getRect`, `KuiDialog::onTouchBegan`, `KuiDialog::update`, `KuiDialog::draw`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `g_StrLower`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `setContentSize`→ComboBox.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `CustomRichLabel`→KCoreVN.cpp, `setShowVisible`→KuiShowSprite.cpp, `closeShowPad`→KuiCometoMap.cpp

## `gameui/KuiDialog.h`
- 74 dòng. Created by 横刀向天笑 QQ:25557432
- Gọi tới: `KuiDialog`→KuiDialog.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `closeShowPad`→KuiCometoMap.cpp

## `gameui/KuiDynamicShop.cpp`
- 906 dòng. m_nMoney = 0;
- Hàm: `KuiDynamicShop`, `KuiDynamicShop`, `KuiDynamicShop::create`, `KuiDynamicShop::init`, `KuiDynamicShop::addDialoaData`, `KuiDynamicShop::setcoloseButton`, `KuiDynamicShop::touchPageBtnEvent`, `KuiDynamicShop::backCallBackFunc`, `KuiDynamicShop::nextCallBackFunc`, `KuiDynamicShop::buyCallBackFunc`, `KuiDynamicShop::closeCallBackFunc`, `KuiDynamicShop::closePopLayer`, `KuiDynamicShop::getRect`, `KuiDynamicShop::onTouchEnded`, `KuiDynamicShop::onTouchMoved`, `KuiDynamicShop::onTouchBegan`, `KuiDynamicShop::closedescPadCallback`, `KuiDynamicShop::update`, `KuiDynamicShop::draw`, `KuiDynamicShop::SellSortChange`, `KuiDynamicShop::Clear`, `KuiDynamicShop::AddObject`, `KuiDynamicShop::SetPage`, `KuiDynamicShop::UpdateData`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `g_StrLower`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `Clear`→KIniFile.cpp, `GetGameData`→CoreShell.cpp, `setContentSize`→ComboBox.cpp, `UpdateData`→KuiCometoMap.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `AddObject`→KuiCompoundItem.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `OperationRequest`→CoreShell.cpp

## `gameui/KuiDynamicShop.h`
- 103 dòng. 重写触摸注册函数，重新给定触摸级别
- Gọi tới: `KuiDynamicShop`→KuiDynamicShop.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `UpdateData`→KuiCometoMap.cpp, `addDialoaData`→KuiDynamicShop.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `touchPageBtnEvent`→KuiAutoPlay.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buyCallBackFunc`→KuiDynamicShop.cpp, `backCallBackFunc`→KuiDynamicShop.cpp

## `gameui/KuiEffect.cpp`
- 643 dòng. typedef struct fd_set FD_SET;
- Hàm: `KuiEffect`, `KuiEffect`, `KuiEffect::create`, `KuiEffect::create`, `KuiEffect::init`, `KuiEffect::setDialogTagKey`, `KuiEffect::getDialogTagKey`, `KuiEffect::setDialogColor`, `KuiEffect::setDialogPosition`, `KuiEffect::getDialogPosition`, `KuiEffect::getDialogSize`, `KuiEffect::setDialogSize`, `KuiEffect::addDialogData`, `KuiEffect::removeAllChildren_e`, `KuiEffect::setTempString_e`, `KuiEffect::getTempString_e`, `KuiEffect::isVisible_e`, `KuiEffect::setVisible_e`, `KuiEffect::addChild_e`, `KuiEffect::findChildByKey`, `KuiEffect::upItemColor`, `KuiEffect::onUpdateEffect`, `KuiEffect::onUpdateEffect_2`, `KuiEffect::setcoloseButton`, `KuiEffect::buttonCallBackFunc` …(+3)
- Gọi tới: `create`→KHRocker.cpp, `init`→HelloWorldScene.cpp, `ccMessageBox_new`→KCore.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `setContentSize`→ComboBox.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp

## `gameui/KuiEffect.h`
- 120 dòng. (không có chú thích đầu)
- Gọi tới: `KuiEffect`→KuiEffect.cpp, `create`→KHRocker.cpp, `init`→HelloWorldScene.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `setDialogTagKey`→KuiEffect.cpp, `getDialogTagKey`→KuiEffect.cpp, `setDialogPosition`→KuiEffect.cpp, `setDialogSize`→KuiEffect.cpp, `setDialogColor`→KuiEffect.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `getDialogPosition`→KuiEffect.cpp, `getDialogSize`→KuiEffect.cpp, `upItemColor`→KuiEffect.cpp, `addChild_e`→KuiEffect.cpp

## `gameui/KuiEffectMenu.cpp`
- 392 dòng. #include "KuiItem.h"
- Hàm: `KuiEffectMenu`, `KuiEffectMenu`, `KuiEffectMenu::getAngleSigned`, `KuiEffectMenu::getRad`, `KuiEffectMenu::create`, `KuiEffectMenu::menuWithItem`, `KuiEffectMenu::onTouchBegan`, `KuiEffectMenu::onTouchMoved`, `KuiEffectMenu::onTouchEnded`, `KuiEffectMenu::onTouchCancelled`, `KuiEffectMenu::setSpriteOpacity`, `KuiEffectMenu::setSpriteVisible`, `KuiEffectMenu::setDialogPosition`, `KuiEffectMenu::setSpriteOrder`, `KuiEffectMenu::setSpritePiont`, `KuiEffectMenu::setEffect`, `KuiEffectMenu::onUpdateEffect_2`, `KuiEffectMenu::draw`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `getTradeState`→CoreShell.cpp, `g_StrLower`→KStrBase.cpp, `g_FileName2Id`→KFilePath.cpp, `Size`→KFile.cpp, `getRad`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `setSpriteVisible`→KSkillRocker.cpp, `setSpritePiont`→KSkillRocker.cpp, `getpicPath`→Kgetinidata.cpp, `getAngleSigned`→KHRocker - Copy.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp

## `gameui/KuiEffectMenu.h`
- 63 dòng. Created by 横刀向天笑 QQ:25557432
- Gọi tới: `KuiEffectMenu`→KuiEffectMenu.cpp, `draw`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `menuWithItem`→KuiEffectMenu.cpp, `setSpritePiont`→KSkillRocker.cpp, `setSpriteVisible`→KSkillRocker.cpp, `setSpriteOpacity`→KSkillRocker.cpp, `setSpriteOrder`→KuiEffectMenu.cpp, `setDialogPosition`→KuiEffect.cpp, `setEffect`→KuiEffectMenu.cpp, `onUpdateEffect_2`→KuiEffect.cpp, `getAngleSigned`→KHRocker - Copy.cpp, `getRad`→KHRocker - Copy.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp

## `gameui/KuiEscInfo.cpp`
- 386 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiEscInfo`, `KuiEscInfo`, `KuiEscInfo::create`, `KuiEscInfo::init`, `KuiEscInfo::addDialogData`, `KuiEscInfo::setcoloseButton`, `KuiEscInfo::oktouchEvent`, `KuiEscInfo::btnCallBackFunc`, `KuiEscInfo::closeOptionCallback`, `KuiEscInfo::buttonCallBackFunc`, `KuiEscInfo::closePopLayer`, `KuiEscInfo::getRect`, `KuiEscInfo::onTouchEnded`, `KuiEscInfo::onTouchMoved`, `KuiEscInfo::onTouchBegan`, `KuiEscInfo::update`, `KuiEscInfo::draw`
- Gọi tới: `create`→KHRocker.cpp, `findinidata_one`→Kgetinidata.cpp, `t_sprintf`→KStrBase.cpp, `g_StrLower`→KStrBase.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `setContentSize`→ComboBox.cpp, `ccMessageBox_new`→KCore.cpp, `oktouchEvent`→KuiAutoPlay.cpp, `_quitGame`→KgameWorld.cpp, `OperationRequest`→CoreShell.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp

## `gameui/KuiEscInfo.h`
- 72 dòng. KuiEscInfo.h
- Gọi tới: `KuiEscInfo`→KuiEscInfo.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `oktouchEvent`→KuiAutoPlay.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `btnCallBackFunc`→KuiEscInfo.cpp, `closeOptionCallback`→KuiEscInfo.cpp

## `gameui/KuiFaceSelector.cpp`
- 315 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiFaceSelector`, `KuiFaceSelector`, `KuiFaceSelector::create_`, `KuiFaceSelector::init`, `KuiFaceSelector::addDialogData`, `KuiFaceSelector::closeShowSpritePad`, `KuiFaceSelector::setcoloseButton`, `KuiFaceSelector::buttonCallBackFunc`, `KuiFaceSelector::closePopLayer`, `KuiFaceSelector::getRect`, `KuiFaceSelector::onTouchEnded`, `KuiFaceSelector::onTouchBegan`, `KuiFaceSelector::onTouchMoved`, `KuiFaceSelector::moveLayer`, `KuiFaceSelector::EndedLayer`, `KuiFaceSelector::upRoleInfo`, `KuiFaceSelector::update`
- Gọi tới: `create`→KHRocker.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `t_sprintf`→KStrBase.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `setContentSize`→ComboBox.cpp, `Load`→KIniFile.cpp, `GetInteger`→KTabFile.cpp, `g_StrLower`→KStrBase.cpp, `setShowTga`→KuiShowSprite.cpp, `setShowVisible`→KuiShowSprite.cpp, `Clear`→KIniFile.cpp, `closeShowSpritePad`→KgameWorld.cpp, `ccMessageBox_new`→KCore.cpp

## `gameui/KuiFaceSelector.h`
- 93 dòng. class KImmediaItem_
- Gọi tới: `KuiFaceSelector`→KuiFaceSelector.cpp, `init`→HelloWorldScene.cpp, `create_`→KuiFaceSelector.cpp, `update`→KgameWorld.cpp, `moveLayer`→KuiBtnControl.cpp, `EndedLayer`→KuiBtnControl.cpp, `upRoleInfo`→KuiFaceSelector.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `closeShowSpritePad`→KgameWorld.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp

## `gameui/KuiFlyDialog.cpp`
- 1393 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiFlyDialog`, `KuiFlyDialog`, `KuiFlyDialog::create`, `KuiFlyDialog::init`, `KuiFlyDialog::addDialogData`, `KuiFlyDialog::onUpdatePosition`, `KuiFlyDialog::Clear`, `KuiFlyDialog::PickAMessage`, `KuiFlyDialog::AddMessage`, `KuiFlyDialog::SeparateMsg`, `KuiFlyDialog::AddToTail`, `KuiFlyDialog::upListData`, `KuiFlyDialog::setcoloseButton`, `KuiFlyDialog::buttonCallBackFunc`, `KuiFlyDialog::closePopLayer`, `KuiFlyDialog::getRect`, `KuiFlyDialog::onTouchBegan`, `KuiFlyDialog::onTouchMoved`, `KuiFlyDialog::onTouchEnded`, `KuiFlyDialog::update`, `KuiFlyDialog::draw`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `getColorIndex`→Text.cpp, `g_Atoui`→KStrBase.cpp, `Clear`→KIniFile.cpp, `init`→HelloWorldScene.cpp, `setContentSize`→ComboBox.cpp, `findinidata_one`→Kgetinidata.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `g_StrLower`→KStrBase.cpp, `AddMessage`→KStepLuaScript.cpp, `ccMessageBox_new`→KCore.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `setTouchEnabled`→KHRocker - Copy.cpp

## `gameui/KuiFlyDialog.h`
- 109 dòng. Created by 横刀向天笑 QQ:25557432
- Gọi tới: `KuiFlyDialog`→KuiFlyDialog.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `AddMessage`→KStepLuaScript.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `upListData`→KuiFlyDialog.cpp, `PickAMessage`→KuiFlyDialog.cpp, `SeparateMsg`→KuiFlyDialog.cpp, `AddToTail`→KuiFlyDialog.cpp

## `gameui/KuiGive_New.cpp`
- 1529 dòng. 有按钮的　ｔａｌｋ　对话框
- Hàm: `KuiGive_New`, `KuiGive_New`, `KuiGive_New::create`, `KuiGive_New::init`, `KuiGive_New::addDialogData`, `KuiGive_New::layerCallBakc`, `KuiGive_New::setcoloseButton`, `KuiGive_New::okCallBackFunc`, `KuiGive_New::btnCallBackFunc_quxia`, `KuiGive_New::buttonCallBackFunc`, `KuiGive_New::closePopLayer`, `KuiGive_New::closeItemPadCallback`, `KuiGive_New::getGiveItem`, `KuiGive_New::onTouchEnded`, `KuiGive_New::onTouchMoved`, `KuiGive_New::onTouchBegan`, `KuiGive_New::UpdateGiveItem`, `KuiGive_New::update`, `KuiGive_New::AddGiveObject`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `GetID`→KFaction.cpp, `findinidata_one`→Kgetinidata.cpp, `ccMessageBox_new`→KCore.cpp, `GetGameData`→CoreShell.cpp, `g_StrLower`→KStrBase.cpp, `OperationRequest`→CoreShell.cpp, `getColorIndex`→Text.cpp, `g_Atoui`→KStrBase.cpp, `setDialogPosition`→KuiEffect.cpp, `setDialogColor`→KuiEffect.cpp, `btnCallBackFunc_quxia`→KuiCompoundItem.cpp, `getGiveItem`→Kuigive.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp

## `gameui/KuiGive_New.h`
- 94 dòng. Created by 横刀向天笑 QQ:25557432
- Gọi tới: `KuiGive_New`→KuiGive_New.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `UpdateGiveItem`→KgameWorld.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closeItemPadCallback`→KgameWorld.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `btnCallBackFunc_quxia`→KuiCompoundItem.cpp

## `gameui/KuiInPutIp.cpp`
- 352 dòng. 有按钮的　ｔａｌｋ　对话框
- Hàm: `KuiInPutIp`, `KuiInPutIp`, `KuiInPutIp::create`, `KuiInPutIp::init`, `KuiInPutIp::addDialogData`, `KuiInPutIp::mianCancelCallback`, `KuiInPutIp::mianLoginCallback`, `KuiInPutIp::setcoloseButton`, `KuiInPutIp::buttonCallBackFunc`, `KuiInPutIp::closePopLayer`, `KuiInPutIp::getRect`, `KuiInPutIp::onTouchBegan`, `KuiInPutIp::update`, `KuiInPutIp::draw`, `KuiInPutIp::FilterTextColor`
- Gọi tới: `create`→KHRocker.cpp, `ccMessageBox_new`→KCore.cpp, `TClearSpecialCtrlInEncodedText`→Text.cpp, `setContentSize`→ComboBox.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `Clear`→KIniFile.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `t_sprintf`→KStrBase.cpp, `GetGameData`→CoreShell.cpp, `setTitle`→PopupLayer.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `mianCancelCallback`→Klogin.cpp, `mianLoginCallback`→Klogin.cpp

## `gameui/KuiInPutIp.h`
- 82 dòng. #define FIGHT_SKILL_COUNT_PER_PAGE	25
- Gọi tới: `KuiInPutIp`→KuiInPutIp.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `editBoxEditingDidBegin`→KgameWorld.cpp, `editBoxEditingDidEnd`→KgameWorld.cpp, `editBoxReturn`→KgameWorld.cpp, `editBoxTextChanged`→KgameWorld.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `FilterTextColor`→Text.cpp

## `gameui/KuiItem.cpp`
- 2138 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiItem`, `KuiItem`, `KuiItem::create`, `KuiItem::init`, `KuiItem::addDialogData`, `KuiItem::layerCallBakc`, `KuiItem::setcoloseButton`, `KuiItem::touchBtnEvent_zimudai`, `KuiItem::closePadCallback`, `KuiItem::saveMoneyCallBackFunc`, `KuiItem::closesavemonyPadCallback`, `KuiItem::zhengCallBackFunc`, `KuiItem::zhengCallBackFunc`, `KEquipmentArray::FindSame`, `KuiItem::kuaiCallBackFunc`, `KuiItem::buttonCallBackFunc`, `KuiItem::closePopLayer`, `KuiItem::getRect`, `KuiItem::onTouchEnded`, `KuiItem::onTouchMoved`, `KuiItem::onTouchBegan`, `KuiItem::checkTouchItem`, `KuiItem::onTouchItem`, `KuiItem::closeItemPadCallback`, `KuiItem::draw` …(+5)
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `GetID`→KFaction.cpp, `GetGameData`→CoreShell.cpp, `ccMessageBox_new`→KCore.cpp, `findinidata_one`→Kgetinidata.cpp, `g_StrLower`→KStrBase.cpp, `setDialogColor`→KuiEffect.cpp, `SendClientCmdMoveItem`→KProtocol.cpp, `OperationRequest`→CoreShell.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `ApplyAutoMoveItem`→KPlayer.cpp, `UpItemData`→KuiBtnControl.cpp, `FindSame`→KPlayerSet.cpp, `GetName`→KNpcResNode.cpp

## `gameui/KuiItem.h`
- 152 dòng. Created by 2018.10 横刀向天笑 QQ:25557432
- Gọi tới: `KuiItem`→KuiItem.cpp, `FindSame`→KPlayerSet.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `UpdateItemOrDer`→KuiItem.cpp, `UpdateItem`→KSellItem.cpp, `kuaiCallBackFunc`→KuiItem.cpp, `convertPixelToGrid`→KuiItem.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp

## `gameui/KuiItemEx.cpp`
- 1085 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiItemEx`, `KuiItemEx`, `KuiItemEx::create`, `KuiItemEx::init`, `KuiItemEx::addDialogData`, `KuiItemEx::layerCallBakc`, `KuiItemEx::setcoloseButton`, `KuiItemEx::zenliCallBackFunc`, `KuiItemEx::qiCallBackFunc`, `KuiItemEx::quCallBackFunc`, `KuiItemEx::buttonCallBackFunc`, `KuiItemEx::closePopLayer`, `KuiItemEx::getRect`, `KuiItemEx::onTouchEnded`, `KuiItemEx::onTouchMoved`, `KuiItemEx::onTouchBegan`, `KuiItemEx::closeItemPadCallback`, `KuiItemEx::draw`, `KuiItemEx::AddObject`, `KuiItemEx::selectedItemEvent`, `KuiItemEx::UpdateData`, `KuiItemEx::freeAllPosition`, `KuiItemEx::clearAllColor`, `KuiItemEx::getFreePosition`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `findinidata_one`→Kgetinidata.cpp, `ccMessageBox_new`→KCore.cpp, `setVisible_e`→KuiEffect.cpp, `GetGameData`→CoreShell.cpp, `g_StrLower`→KStrBase.cpp, `GetID`→KFaction.cpp, `addChild_e`→KuiEffect.cpp, `Size`→KFile.cpp, `findChildByKey`→KuiEffect.cpp, `UpdateData`→KuiCometoMap.cpp, `upItemColor`→KuiEffect.cpp, `setDialogColor`→KuiEffect.cpp, `setContentSize`→ComboBox.cpp

## `gameui/KuiItemEx.h`
- 96 dòng. virtual void update(float delta);
- Gọi tới: `KuiItemEx`→KuiItemEx.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `UpdateItem`→KSellItem.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `qiCallBackFunc`→KuiItemEx.cpp, `quCallBackFunc`→KuiItemEx.cpp

## `gameui/KuiItemEx_old.cpp`
- 1189 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiItemEx_old`, `KuiItemEx_old`, `KuiItemEx_old::create`, `KuiItemEx_old::init`, `KuiItemEx_old::addDialogData`, `KuiItemEx_old::layerCallBakc`, `KuiItemEx_old::setcoloseButton`, `KuiItemEx_old::zenliCallBackFunc`, `KuiItemEx_old::qiCallBackFunc`, `KuiItemEx_old::quCallBackFunc`, `KuiItemEx_old::buttonCallBackFunc`, `KuiItemEx_old::closePopLayer`, `KuiItemEx_old::getRect`, `KuiItemEx_old::onTouchEnded`, `KuiItemEx_old::onTouchMoved`, `KuiItemEx_old::onTouchBegan`, `KuiItemEx_old::UpdateItemOrDer`, `KuiItemEx_old::checkTouchItem`, `KuiItemEx_old::onTouchItem`, `KuiItemEx_old::closeItemPadCallback`, `KuiItemEx_old::draw`, `KuiItemEx_old::AddObject`, `KuiItemEx_old::UpdateData`, `KuiItemEx_old::checkFreePosition`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `ccMessageBox_new`→KCore.cpp, `GetID`→KFaction.cpp, `findinidata_one`→Kgetinidata.cpp, `GetGameData`→CoreShell.cpp, `g_StrLower`→KStrBase.cpp, `setDialogColor`→KuiEffect.cpp, `OperationRequest`→CoreShell.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `UpdateItemOrDer`→KuiItem.cpp, `UpdateData`→KuiCometoMap.cpp, `GetAutoplayid`→CoreShell.cpp, `onTouchItem`→KuiItem.cpp, `freeAllPosition`→KuiItemEx.cpp

## `gameui/KuiItemEx_old.h`
- 96 dòng. virtual void update(float delta);
- Gọi tới: `KuiItemEx_old`→KuiItemEx_old.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `UpdateItem`→KSellItem.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `qiCallBackFunc`→KuiItemEx.cpp, `quCallBackFunc`→KuiItemEx.cpp

## `gameui/KuiItemImmediaBox.cpp`
- 851 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiItemImmediaBox`, `KuiItemImmediaBox`, `KuiItemImmediaBox::create`, `KuiItemImmediaBox::init`, `KuiItemImmediaBox::addDialogData`, `KuiItemImmediaBox::setcoloseButton`, `KuiItemImmediaBox::mianYinCallback`, `KuiItemImmediaBox::TempUpdataImmediacy`, `KuiItemImmediaBox::mianQuCallback`, `KuiItemImmediaBox::buttonCallBackFunc`, `KuiItemImmediaBox::closePopLayer`, `KuiItemImmediaBox::getRect`, `KuiItemImmediaBox::onTouchEnded`, `KuiItemImmediaBox::onTouchMoved`, `KuiItemImmediaBox::moveLayer`, `KuiItemImmediaBox::EndedLayer`, `KuiItemImmediaBox::onTouchBegan`, `KuiItemImmediaBox::UpdateImmediaItem`, `KuiItemImmediaBox::HoldObject_`, `KuiItemImmediaBox::clearItemData`, `KuiItemImmediaBox::getcurPosition`, `KuiItemImmediaBox::CheckImmediacyBox`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `setContentSize`→ComboBox.cpp, `isFileExist`→KgameWorld.cpp, `UpdateImmediaItem`→KgameWorld.cpp, `GetGameData`→CoreShell.cpp, `g_StrLower`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `ClientShowMsg`→KNpc.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `g_FileName2Id`→KFilePath.cpp, `UiSoundPlay_Ui`→UiSoundSetting.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `gameui/KuiItemImmediaBox.h`
- 110 dòng. virtual void update(float delta);
- Gọi tới: `KuiItemImmediaBox`→KuiItemImmediaBox.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `UpdateImmediaItem`→KgameWorld.cpp, `moveLayer`→KuiBtnControl.cpp, `EndedLayer`→KuiBtnControl.cpp, `CheckImmediacyBox`→KgameWorld.cpp, `getcurPosition`→KuiItemImmediaBox.cpp, `clearItemData`→KuiItemImmediaBox.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp

## `gameui/KuiItemKuo.cpp`
- 1490 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiItemKuo`, `KuiItemKuo`, `KuiItemKuo::create`, `KuiItemKuo::init`, `KuiItemKuo::addDialogData`, `KuiItemKuo::setcoloseButton`, `KuiItemKuo::zenliCallBackFunc`, `KuiItemKuo::qiCallBackFunc`, `KuiItemKuo::quCallBackFunc`, `KuiItemKuo::buttonCallBackFunc_1`, `KuiItemKuo::buttonCallBackFunc_2`, `KuiItemKuo::buttonCallBackFunc_3`, `KuiItemKuo::buttonCallBackFunc`, `KuiItemKuo::closePopLayer`, `KuiItemKuo::getRect`, `KuiItemKuo::onTouchEnded`, `KuiItemKuo::onTouchMoved`, `KuiItemKuo::onTouchBegan`, `KuiItemKuo::closeItemPadCallback`, `KuiItemKuo::update`, `KuiItemKuo::AddObject`, `KuiItemKuo::selectedItemEvent`, `KuiItemKuo::UpdateData`, `KuiItemKuo::freeAllPosition`, `KuiItemKuo::clearAllColor` …(+2)
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `findinidata_one`→Kgetinidata.cpp, `UpdateData`→KuiCometoMap.cpp, `g_StrLower`→KStrBase.cpp, `GetID`→KFaction.cpp, `GetGameData`→CoreShell.cpp, `ccMessageBox_new`→KCore.cpp, `setVisible_e`→KuiEffect.cpp, `addChild_e`→KuiEffect.cpp, `setContentSize`→ComboBox.cpp, `AddObject`→KuiCompoundItem.cpp, `findChildByKey`→KuiEffect.cpp, `Size`→KFile.cpp, `clearAllColor`→KuiItemEx.cpp

## `gameui/KuiItemKuo.h`
- 96 dòng. Created by 横刀向天笑 QQ:25557432
- Gọi tới: `KuiItemKuo`→KuiItemKuo.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `UpdateItem`→KSellItem.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc_1`→KuiItemKuo.cpp, `buttonCallBackFunc_2`→KuiItemKuo.cpp

## `gameui/KuiItemKuo_old.cpp`
- 1753 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiItemKuo_old`, `KuiItemKuo_old`, `KuiItemKuo_old::create`, `KuiItemKuo_old::init`, `KuiItemKuo_old::addDialogData`, `KuiItemKuo_old::setcoloseButton`, `KuiItemKuo_old::zenliCallBackFunc`, `KuiItemKuo_old::qiCallBackFunc`, `KuiItemKuo_old::quCallBackFunc`, `KuiItemKuo_old::buttonCallBackFunc_1`, `KuiItemKuo_old::buttonCallBackFunc_2`, `KuiItemKuo_old::buttonCallBackFunc_3`, `KuiItemKuo_old::buttonCallBackFunc`, `KuiItemKuo_old::closePopLayer`, `KuiItemKuo_old::getRect`, `KuiItemKuo_old::onTouchEnded`, `KuiItemKuo_old::onTouchMoved`, `KuiItemKuo_old::onTouchBegan`, `KuiItemKuo_old::closeItemPadCallback`, `KuiItemKuo_old::update`, `KuiItemKuo_old::clearAllItem`, `KuiItemKuo_old::AddObject`, `KuiItemKuo_old::UpdateData`, `KuiItemKuo_old::UpdateItemOrDer`, `KuiItemKuo_old::checkTouchItem` …(+2)
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `findinidata_one`→Kgetinidata.cpp, `GetID`→KFaction.cpp, `ccMessageBox_new`→KCore.cpp, `UpdateData`→KuiCometoMap.cpp, `g_StrLower`→KStrBase.cpp, `GetGameData`→CoreShell.cpp, `UpdateItemOrDer`→KuiItem.cpp, `setDialogColor`→KuiEffect.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `AddObject`→KuiCompoundItem.cpp, `setContentSize`→ComboBox.cpp, `OperationRequest`→CoreShell.cpp, `GetAutoplayid`→CoreShell.cpp

## `gameui/KuiItemKuo_old.h`
- 101 dòng. Created by 横刀向天笑 QQ:25557432
- Gọi tới: `KuiItemKuo_old`→KuiItemKuo_old.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `UpdateItem`→KSellItem.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc_1`→KuiItemKuo.cpp, `buttonCallBackFunc_2`→KuiItemKuo.cpp

## `gameui/KuiItem_New.cpp`
- 1847 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiItem_New`, `KuiItem_New`, `KuiItem_New::create`, `KuiItem_New::init`, `KuiItem_New::addDialogData`, `KuiItem_New::chuanCallBackFunc`, `KuiItem_New::selectedItemEvent`, `KuiItem_New::getRect`, `KuiItem_New::closeItemPadCallback`, `KuiItem_New::setcoloseButton`, `KuiItem_New::touchBtnEvent_zimudai`, `KuiItem_New::zhengCallBackFunc`, `KuiItem_New::buttonCallBackFunc`, `KuiItem_New::kuaiCallBackFunc`, `KuiItem_New::ziCallBackFunc`, `KuiItem_New::saveMoneyCallBackFunc`, `KuiItem_New::closesavemonyPadCallback`, `KuiItem_New::closePadCallback`, `KuiItem_New::closePopLayer`, `KuiItem_New::draw`, `KuiItem_New::UpdateItemOrDer`, `KuiItem_New::AddObject`, `KuiItem_New::UpdateData`, `KuiItem_New::upItemToOnePosition`, `KuiItem_New::clearAllColor` …(+6)
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `GetGameData`→CoreShell.cpp, `findinidata_one`→Kgetinidata.cpp, `ccMessageBox_new`→KCore.cpp, `addChild_e`→KuiEffect.cpp, `GetID`→KFaction.cpp, `g_StrLower`→KStrBase.cpp, `setDialogColor`→KuiEffect.cpp, `setVisible_e`→KuiEffect.cpp, `OperationRequest`→CoreShell.cpp, `findChildByKey`→KuiEffect.cpp, `setContentSize`→ComboBox.cpp, `Size`→KFile.cpp, `upItemColor`→KuiEffect.cpp

## `gameui/KuiItem_New.h`
- 122 dòng. Created by 横刀向天笑 QQ:25557432
- Gọi tới: `KuiItem_New`→KuiItem_New.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `upItemToOnePosition`→KuiItem_New.cpp, `UpdateItem`→KSellItem.cpp, `UpdateItemOrDer`→KuiItem.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `closePadCallback`→KuiItem.cpp, `saveMoneyCallBackFunc`→KuiItem.cpp, `kuaiCallBackFunc`→KuiItem.cpp, `zhengCallBackFunc`→Kuigive.cpp, `ziCallBackFunc`→KuiItem_New.cpp

## `gameui/KuiItemdesc.cpp`
- 2377 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiItemdesc`, `KuiItemdesc`, `KuiItemdesc::create`, `KuiItemdesc::create`, `KuiItemdesc::init`, `KuiItemdesc::addshopdesc`, `KuiItemdesc::closeShowSpritePad`, `KuiItemdesc::addDialogData`, `KuiItemdesc::getLayerSize`, `KuiItemdesc::getLayerPos`, `KuiItemdesc::setLayerPosY`, `KuiItemdesc::setLayerPosX`, `KuiItemdesc::setLayerPos`, `KuiItemdesc::setcoloseButton`, `KuiItemdesc::buttonCallBackFunc`, `KuiItemdesc::closePopLayer`, `KuiItemdesc::getRect`, `KuiItemdesc::onTouchBegan`, `KuiItemdesc::onTouchEnded`, `KuiItemdesc::update`, `KuiItemdesc::draw`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `GetStringByKeyFromFile`→CXmlStream.cpp, `create`→KHRocker.cpp, `GetString`→KTabFile.cpp, `Load`→KIniFile.cpp, `GetDesc_New`→KMagicDesc.cpp, `Clear`→KIniFile.cpp, `GetDesc`→KMagicDesc.cpp, `TEncodeText`→Text.cpp, `ccMessageBox_new`→KCore.cpp, `GetInteger`→KTabFile.cpp, `g_StrLower`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `setContentSize`→ComboBox.cpp

## `gameui/KuiItemdesc.h`
- 108 dòng. 重写触摸注册函数，重新给定触摸级别
- Gọi tới: `KuiItemdesc`→KuiItemdesc.cpp, `create`→KHRocker.cpp, `init`→HelloWorldScene.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `getLayerPos`→KuiItemdesc.cpp, `setLayerPos`→KuiItemdesc.cpp, `setLayerPosY`→KuiItemdesc.cpp, `setLayerPosX`→KuiItemdesc.cpp, `getLayerSize`→KuiItemdesc.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `addshopdesc`→KuiItemdesc.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp

## `gameui/KuiJpgInage.cpp`
- 241 dòng. typedef struct fd_set FD_SET;
- Hàm: `KuiJpgInage`, `KuiJpgInage`, `KuiJpgInage::create`, `KuiJpgInage::init`, `KuiJpgInage::setDialogTagKey`, `KuiJpgInage::getDialogTagKey`, `KuiJpgInage::setDialogColor`, `KuiJpgInage::setDialogPosition`, `KuiJpgInage::getDialogPosition`, `KuiJpgInage::getDialogSize`, `KuiJpgInage::setDialogSize`, `KuiJpgInage::addDialogData`, `KuiJpgInage::setcoloseButton`, `KuiJpgInage::buttonCallBackFunc`, `KuiJpgInage::closePopLayer`, `KuiJpgInage::getRect`, `KuiJpgInage::ccTouchBegan`, `KuiJpgInage::update`, `KuiJpgInage::draw`
- Gọi tới: `create`→KHRocker.cpp, `init`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `setContentSize`→ComboBox.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `setTitle`→PopupLayer.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `setDialogTagKey`→KuiEffect.cpp, `getDialogTagKey`→KuiEffect.cpp, `setDialogColor`→KuiEffect.cpp, `setDialogPosition`→KuiEffect.cpp, `getDialogPosition`→KuiEffect.cpp, `getDialogSize`→KuiEffect.cpp, `setDialogSize`→KuiEffect.cpp

## `gameui/KuiJpgInage.h`
- 80 dòng. CREATE_FUNC(KuiJpgInage);
- Gọi tới: `KuiJpgInage`→KuiJpgInage.cpp, `create`→KHRocker.cpp, `init`→HelloWorldScene.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `setDialogTagKey`→KuiEffect.cpp, `getDialogTagKey`→KuiEffect.cpp, `setDialogPosition`→KuiEffect.cpp, `setDialogSize`→KuiEffect.cpp, `setDialogColor`→KuiEffect.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `getDialogPosition`→KuiEffect.cpp, `getDialogSize`→KuiEffect.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp

## `gameui/KuiLockscree.cpp`
- 292 dòng. 有按钮的　ｔａｌｋ　对话框
- Hàm: `KuiLockscree`, `KuiLockscree`, `KuiLockscree::create`, `KuiLockscree::init`, `KuiLockscree::addDialogData`, `KuiLockscree::tuoguanCallBackFunc`, `KuiLockscree::oktouchEvent`, `KuiLockscree::setcoloseButton`, `KuiLockscree::buttonCallBackFunc`, `KuiLockscree::closePopLayer`, `KuiLockscree::getRect`, `KuiLockscree::onTouchBegan`, `KuiLockscree::update`, `KuiLockscree::draw`
- Gọi tới: `create`→KHRocker.cpp, `findinidata_one`→Kgetinidata.cpp, `setContentSize`→ComboBox.cpp, `t_sprintf`→KStrBase.cpp, `g_StrLower`→KStrBase.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `ccMessageBox_new`→KCore.cpp, `GetGameData`→CoreShell.cpp, `setTitle`→PopupLayer.cpp, `OperationRequest`→CoreShell.cpp, `oktouchEvent`→KuiAutoPlay.cpp

## `gameui/KuiLockscree.h`
- 65 dòng. 重写触摸注册函数，重新给定触摸级别
- Gọi tới: `KuiLockscree`→KuiLockscree.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `tuoguanCallBackFunc`→KuiLockscree.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `oktouchEvent`→KuiAutoPlay.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `gameui/KuiMaxMap.cpp`
- 2445 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiMaxMap`, `KuiMaxMap`, `KuiMaxMap::create`, `KuiMaxMap::init`, `KuiMaxMap::addDialogData`, `KuiMaxMap::setcoloseButton`, `KuiMaxMap::buttonCallBackFunc`, `KuiMaxMap::closePopLayer`, `KuiMaxMap::oktouchEvent`, `KuiMaxMap::getRect`, `KuiMaxMap::onTouchBegan`, `KuiMaxMap::onTouchMoved`, `KuiMaxMap::onTouchEnded`, `KuiMaxMap::update`, `KuiMaxMap::ccgetTxtData_g`, `KuiMaxMap::ccgetTxtData_p`, `KuiMaxMap::ccgetTxtData`, `KuiMaxMap::setInRect_temp`, `KuiMaxMap::onRead`, `KuiMaxMap::draw`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `ccMessageBox_new`→KCore.cpp, `findinidata_one`→Kgetinidata.cpp, `g_StrLower`→KStrBase.cpp, `gTraceLogFile`→KLogFile.cpp, `GetLocalPositionByMps`→KSubWorld.cpp, `init`→HelloWorldScene.cpp, `setContentSize`→ComboBox.cpp, `isFileExist`→KgameWorld.cpp, `checkPos`→KScenePlaceC.cpp, `setFaceBookState`→AutoPathFinder.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `GetMpsPos`→KMissle.cpp, `NewMap2Mps`→KSubWorld.cpp

## `gameui/KuiMaxMap.h`
- 135 dòng. Created by 横刀向天笑 QQ:25557432
- Gọi tới: `KuiMaxMap`→KuiMaxMap.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `oktouchEvent`→KuiAutoPlay.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `onTouchesBegan`→HelloWorldScene.cpp, `onTouchesMoved`→KgameWorld.cpp, `onTouchesEnded`→KgameWorld.cpp

## `gameui/KuiMinMap.cpp`
- 1353 dòng. nPartNode         = NULL;
- Hàm: `KuiMinMap`, `KuiMinMap`, `KuiMinMap::create`, `KuiMinMap::init`, `KuiMinMap::getcurPosition`, `KuiMinMap::addDialogData`, `KuiMinMap::upDataMap`, `KuiMinMap::setcoloseButton`, `KuiMinMap::buttonCallBackFunc`, `KuiMinMap::closePopLayer`, `KuiMinMap::getRect`, `KuiMinMap::onTouchBegan`, `KuiMinMap::onTouchMoved`, `KuiMinMap::onTouchEnded`, `KuiMinMap::moveLayer`, `KuiMinMap::EndedLayer`, `KuiMinMap::setMapNameAndPoint`, `KuiMinMap::setMpsPos`, `KuiMinMap::onRead`, `KuiMinMap::custom_update`, `KuiMinMap::draw`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `init`→HelloWorldScene.cpp, `FindMemberID`→KPlayerTeam.cpp, `g_StrLower`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `setContentSize`→ComboBox.cpp, `GetSceneFocus`→KScenePlaceC.cpp, `ccMessageBox_new`→KCore.cpp, `NewMap2Mps`→KSubWorld.cpp, `GetRelation`→KNpcSet.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `g_FileName2Id`→KFilePath.cpp, `isFileExist`→KgameWorld.cpp

## `gameui/KuiMinMap.h`
- 129 dòng. Created by 横刀向天笑 QQ:25557432
- Gọi tới: `KuiMinMap`→KuiMinMap.cpp, `init`→HelloWorldScene.cpp, `custom_update`→KuiMinMap.cpp, `create`→KHRocker.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `moveLayer`→KuiBtnControl.cpp, `EndedLayer`→KuiBtnControl.cpp, `setMapNameAndPoint`→KuiMinMap.cpp, `upDataMap`→KuiMinMap.cpp, `setMpsPos`→KuiMinMap.cpp, `getcurPosition`→KuiItemImmediaBox.cpp, `onTouchBegan`→KHRocker - Copy.cpp

## `gameui/KuiMoveToMap.cpp`
- 564 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiMoveToMap`, `KuiMoveToMap`, `KuiMoveToMap::create`, `KuiMoveToMap::init`, `KuiMoveToMap::addDialogData`, `KuiMoveToMap::closeShowSpritePad`, `KuiMoveToMap::setcoloseButton`, `KuiMoveToMap::buttonCallBackFunc`, `KuiMoveToMap::closePopLayer`, `KuiMoveToMap::oktouchEvent`, `KuiMoveToMap::getRect`, `KuiMoveToMap::onTouchBegan`, `KuiMoveToMap::onTouchMoved`, `KuiMoveToMap::onTouchEnded`, `KuiMoveToMap::update`, `KuiMoveToMap::draw`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `setContentSize`→ComboBox.cpp, `GetInteger`→KTabFile.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `findinidata_one`→Kgetinidata.cpp, `ccMessageBox_new`→KCore.cpp, `g_StrLower`→KStrBase.cpp, `getpicPath`→Kgetinidata.cpp, `setShowVisible`→KuiShowSprite.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `Load`→KIniFile.cpp, `Clear`→KIniFile.cpp

## `gameui/KuiMoveToMap.h`
- 92 dòng. KuiMoveToMap.h
- Gọi tới: `KuiMoveToMap`→KuiMoveToMap.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `oktouchEvent`→KuiAutoPlay.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `onTouchesBegan`→HelloWorldScene.cpp, `onTouchesMoved`→KgameWorld.cpp, `onTouchesEnded`→KgameWorld.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp

## `gameui/KuiMyMenu.cpp`
- 1056 dòng. (không có chú thích đầu)
- Hàm: `KuiMyMenu`, `KuiMyMenu`, `KuiMyMenu::Active`, `KuiMyMenu::Inactive`, `KuiMyMenu::getAngleSigned`, `KuiMyMenu::getRad`, `KuiMyMenu::getDirection`, `KuiMyMenu::getVelocity`, `KuiMyMenu::create`, `KuiMyMenu::menuWithItem`, `KuiMyMenu::onTouchBegan`, `KuiMyMenu::onTouchMoved`, `KuiMyMenu::onTouchEnded`, `KuiMyMenu::updateMode`, `KuiMyMenu::onTouchCancelled`, `KuiMyMenu::setSpriteOpacity`, `KuiMyMenu::setSpriteVisible`, `KuiMyMenu::setDialogPosition`, `KuiMyMenu::setSpriteOrder`, `KuiMyMenu::setSpritePiont`, `KuiMyMenu::GetModelSkillByID`
- Gọi tới: `GetSkill`→KSkillManager.h, `setSpriteVisible`→KSkillRocker.cpp, `setAttackSprPosition`→KgameWorld.cpp, `create`→KHRocker.cpp, `setAttackSprVisible`→KgameWorld.cpp, `customSkillAttack`→KgameWorld.cpp, `Active`→KStepLuaScript.cpp, `getTradeState`→CoreShell.cpp, `setSpritePiont`→KSkillRocker.cpp, `Size`→KFile.cpp, `Inactive`→KHRocker - Copy.cpp, `getAngleSigned`→KHRocker - Copy.cpp, `getRad`→KHRocker - Copy.cpp, `ccMessageBox_new`→KCore.cpp, `onTouchEnded`→KHRocker - Copy.cpp

## `gameui/KuiMyMenu.h`
- 79 dòng. virtual bool init();
- Gọi tới: `KuiMyMenu`→KuiMyMenu.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `menuWithItem`→KuiEffectMenu.cpp, `setSpritePiont`→KSkillRocker.cpp, `setSpriteVisible`→KSkillRocker.cpp, `setSpriteOpacity`→KSkillRocker.cpp, `setSpriteOrder`→KuiEffectMenu.cpp, `setDialogPosition`→KuiEffect.cpp, `Active`→KStepLuaScript.cpp, `Inactive`→KHRocker - Copy.cpp, `updateMode`→KuiMyMenu.cpp, `getDirection`→KHRocker - Copy.cpp, `getAngleSigned`→KHRocker - Copy.cpp, `getRad`→KHRocker - Copy.cpp

## `gameui/KuiNewPlayer.cpp`
- 1287 dòng. #include "Klogin.h"
- Hàm: `KuiNewPlayer`, `KuiNewPlayer`, `KuiNewPlayer::scene`, `KuiNewPlayer::init`, `KuiNewPlayer::closeYeziSprPad`, `KuiNewPlayer::GetRoleCount`, `KuiNewPlayer::_GetBig5Count`, `KuiNewPlayer::mainEnterCallback`, `KuiNewPlayer::CreateRole`, `KuiNewPlayer::update`, `KuiNewPlayer::getRect`, `KuiNewPlayer::draw`, `KuiNewPlayer::isFileExist`, `KuiNewPlayer::copyData`, `KuiNewPlayer::onEnter`, `KuiNewPlayer::onExit`, `KuiNewPlayer::onEnterTransitionDidFinish`, `KuiNewPlayer::onTouchesBegan`, `KuiNewPlayer::closeRolePad_1`, `KuiNewPlayer::closeRolePad_2`, `KuiNewPlayer::onTouchesMoved`, `KuiNewPlayer::onTouchesEnded`, `KuiNewPlayer::onTouchesCancelled`, `KuiNewPlayer::GetRoleImageName`, `KuiNewPlayer::ProcessCreateRoleResponse` …(+2)
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `ccMessageBox_new`→KCore.cpp, `isFileExist`→KgameWorld.cpp, `g_StrLower`→KStrBase.cpp, `upSpriteData`→KuiShowSprite.cpp, `g_FileName2Id`→KFilePath.cpp, `setBreakTheead`→SocketClient.cpp, `Cleanup`→ClientStage.cpp, `scene`→KgameWorld.cpp, `setBufferEmpty`→ClientStage.cpp, `setShowVisible`→KuiShowSprite.cpp, `g_StrCmp`→KStrBase.cpp, `GetProtocolSize`→CoreShell.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `gameui/KuiNewPlayer.h`
- 105 dòng. ��½���� ѡ������ ���� ɾ����
- Gọi tới: `KuiNewPlayer`→KuiNewPlayer.cpp, `init`→HelloWorldScene.cpp, `update`→KgameWorld.cpp, `scene`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `AcceptNetMsg`→KuiWarnInfo.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `copyData`→KgameWorld.cpp, `isFileExist`→KgameWorld.cpp, `buttonCallback`→KgameWorld.cpp, `GetRoleCount`→KuiNewPlayer.cpp, `mainEnterCallback`→KuiNewPlayer.cpp, `GetRoleImageName`→KuiNewPlayer.cpp, `_GetBig5Count`→KuiNewPlayer.cpp, `onTouchesBegan`→HelloWorldScene.cpp

## `gameui/KuiOptions.cpp`
- 741 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiOptions`, `KuiOptions`, `KuiOptions::create`, `KuiOptions::init`, `KuiOptions::addDialogData`, `KuiOptions::checkboxValueChanged`, `KuiOptions::valueChanged`, `KuiOptions::setcoloseButton`, `KuiOptions::delConfigCallBackFunc`, `KuiOptions::btnUyThacBackFunc`, `KuiOptions::btnLogoutBackFunc`, `KuiOptions::leaveCallBackFunc`, `KuiOptions::buttonCallBackFunc`, `KuiOptions::closePopLayer`, `KuiOptions::getRect`, `KuiOptions::onTouchEnded`, `KuiOptions::onTouchMoved`, `KuiOptions::onTouchBegan`, `KuiOptions::update`, `KuiOptions::draw`
- Gọi tới: `WriteInteger`→KTabFileCtrl.cpp, `create`→KHRocker.cpp, `GetInteger`→KTabFile.cpp, `Clear`→KIniFile.cpp, `WriteFloat`→KTabFileCtrl.cpp, `Save`→KIniFile.cpp, `Load`→KIniFile.cpp, `GetFloat`→KTabFile.cpp, `ccMessageBox_new`→KCore.cpp, `Size`→KFile.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `valueChanged`→KuiAutoPlay.cpp, `SetGameVolume`→KMapMusic.cpp

## `gameui/KuiOptions.h`
- 109 dòng. Date:	2021.08.31
- Gọi tới: `KuiOptions`→KuiOptions.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `leaveCallBackFunc`→KuiOptions.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `valueChanged`→KuiAutoPlay.cpp, `btnUyThacBackFunc`→KuiOptions.cpp

## `gameui/KuiPaimaishop.cpp`
- 711 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiPaimaishop`, `KuiPaimaishop`, `KuiPaimaishop::create`, `KuiPaimaishop::init`, `KuiPaimaishop::addDialoaData`, `KuiPaimaishop::setcoloseButton`, `KuiPaimaishop::backCallBackFunc`, `KuiPaimaishop::nextCallBackFunc`, `KuiPaimaishop::buyCallBackFunc`, `KuiPaimaishop::closeCallBackFunc`, `KuiPaimaishop::closePopLayer`, `KuiPaimaishop::getRect`, `KuiPaimaishop::onTouchBegan`, `KuiPaimaishop::closedescPadCallback`, `KuiPaimaishop::update`, `KuiPaimaishop::draw`, `KuiPaimaishop::Clear`, `KuiPaimaishop::AddObject`, `KuiPaimaishop::SetPage`, `KuiPaimaishop::UpdateData`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `findinidata_one`→Kgetinidata.cpp, `g_StrLower`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `Clear`→KIniFile.cpp, `setContentSize`→ComboBox.cpp, `SetPage`→KuiDynamicShop.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `GetGameData`→CoreShell.cpp, `AddObject`→KuiCompoundItem.cpp, `addDialoaData`→KuiDynamicShop.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `UpdateData`→KuiCometoMap.cpp

## `gameui/KuiPaimaishop.h`
- 88 dòng. 重写触摸注册函数，重新给定触摸级别
- Gọi tới: `KuiPaimaishop`→KuiPaimaishop.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `UpdateData`→KuiCometoMap.cpp, `addDialoaData`→KuiDynamicShop.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buyCallBackFunc`→KuiDynamicShop.cpp, `backCallBackFunc`→KuiDynamicShop.cpp, `nextCallBackFunc`→KuiDynamicShop.cpp, `closeCallBackFunc`→KuiDynamicShop.cpp, `closedescPadCallback`→KuiDynamicShop.cpp

## `gameui/KuiPlayerSelFun.cpp`
- 509 dòng. (không có chú thích đầu)
- Hàm: `KuiPlayerSelFun`, `KuiPlayerSelFun`, `KuiPlayerSelFun::create`, `KuiPlayerSelFun::init`, `KuiPlayerSelFun::addDialogData`, `KuiPlayerSelFun::setcoloseButton`, `KuiPlayerSelFun::oktouchEvent`, `KuiPlayerSelFun::okCallBackFunc`, `KuiPlayerSelFun::buttonCallBackFunc`, `KuiPlayerSelFun::closePopLayer`, `KuiPlayerSelFun::closeItemPadCallback`, `KuiPlayerSelFun::getRectItem`, `KuiPlayerSelFun::onTouchBegan`, `KuiPlayerSelFun::setButtonEnble`, `KuiPlayerSelFun::update`, `KuiPlayerSelFun::draw`
- Gọi tới: `setTouchEnabled`→KHRocker - Copy.cpp, `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `ccMessageBox_new`→KCore.cpp, `init`→HelloWorldScene.cpp, `OperationRequest`→CoreShell.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `setContentSize`→ComboBox.cpp, `oktouchEvent`→KuiAutoPlay.cpp, `setchatCurChannel`→KgameWorld.cpp, `setchatInputText`→KgameWorld.cpp, `TradeApplyStart`→CoreShell.cpp, `__ApplyAddTeam`→CoreShell.cpp

## `gameui/KuiPlayerSelFun.h`
- 81 dòng. virtual bool init();
- Gọi tới: `KuiPlayerSelFun`→KuiPlayerSelFun.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `closeItemPadCallback`→KgameWorld.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `okCallBackFunc`→Kuiduan.cpp, `oktouchEvent`→KuiAutoPlay.cpp, `getRectItem`→KuiCompoundItem.cpp, `setButtonEnble`→KuiPlayerSelFun.cpp

## `gameui/KuiPlayerShop.cpp`
- 642 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiPlayerShop`, `KuiPlayerShop`, `KuiPlayerShop::create`, `KuiPlayerShop::init`, `KuiPlayerShop::addDialoaData`, `KuiPlayerShop::setcoloseButton`, `KuiPlayerShop::backCallBackFunc`, `KuiPlayerShop::nextCallBackFunc`, `KuiPlayerShop::buyCallBackFunc`, `KuiPlayerShop::getRect`, `KuiPlayerShop::onTouchBegan`, `KuiPlayerShop::closedescPadCallback`, `KuiPlayerShop::AddObject`, `KuiPlayerShop::UpdateItemImage`, `KuiPlayerShop::closeCallBackFunc`, `KuiPlayerShop::closePopLayer`, `KuiPlayerShop::layerCallBakc`, `KuiPlayerShop::SetPage`, `KuiPlayerShop::UpdateData`, `KuiPlayerShop::UpdateItem`, `KuiPlayerShop::update`, `KuiPlayerShop::draw`, `KuiPlayerShop::Clear`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `GetGameData`→CoreShell.cpp, `OperationRequest`→CoreShell.cpp, `findinidata_one`→Kgetinidata.cpp, `Size`→KFile.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `setContentSize`→ComboBox.cpp, `Clear`→KIniFile.cpp, `g_StrLower`→KStrBase.cpp, `UpdateItem`→KSellItem.cpp, `setchatDelegate`→KgameWorld.cpp, `SetPage`→KuiDynamicShop.cpp, `ccMessageBox_new`→KCore.cpp, `AddObject`→KuiCompoundItem.cpp

## `gameui/KuiPlayerShop.h`
- 88 dòng. 触摸函数onTouchBegan，返回true
- Gọi tới: `KuiPlayerShop`→KuiPlayerShop.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `UpdateItem`→KSellItem.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `UpdateData`→KuiCometoMap.cpp, `addDialoaData`→KuiDynamicShop.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `UpdateItemImage`→KuiPlayerShop.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buyCallBackFunc`→KuiDynamicShop.cpp, `backCallBackFunc`→KuiDynamicShop.cpp, `nextCallBackFunc`→KuiDynamicShop.cpp

## `gameui/KuiPlayerTrade.cpp`
- 2278 dòng. 有按钮的　ｔａｌｋ　对话框
- Hàm: `KuiPlayerTrade`, `KuiPlayerTrade`, `KuiPlayerTrade::create`, `KuiPlayerTrade::init`, `KuiPlayerTrade::addDialogData`, `KuiPlayerTrade::setcoloseButton`, `KuiPlayerTrade::zhengCallBackFunc`, `KuiPlayerTrade::tradeCallBackFunc`, `KuiPlayerTrade::okCallBackFunc_`, `KuiPlayerTrade::btnCallBackFunc_fangzhi`, `KuiPlayerTrade::btnCallBackFunc_quxia`, `KuiPlayerTrade::__ClosePad`, `KuiPlayerTrade::buttonCallBackFunc`, `KuiPlayerTrade::closePopLayer`, `KuiPlayerTrade::closeItemPadCallback`, `KuiPlayerTrade::gettarGiveItem`, `KuiPlayerTrade::getGiveItem`, `KuiPlayerTrade::getRectItem`, `KuiPlayerTrade::onTouchBegan`, `KuiPlayerTrade::UpdateTradeOperData`, `KuiPlayerTrade::UpdateTarGiveItem`, `KuiPlayerTrade::UpdateGiveItem`, `KuiPlayerTrade::UpdateItem`, `KuiPlayerTrade::OnModififyMoney`, `KuiPlayerTrade::OnAdjustedMoney` …(+12)
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `GetGameData`→CoreShell.cpp, `ccMessageBox_new`→KCore.cpp, `GetID`→KFaction.cpp, `findinidata_one`→Kgetinidata.cpp, `setDialogColor`→KuiEffect.cpp, `g_StrLower`→KStrBase.cpp, `OperationRequest`→CoreShell.cpp, `setContentSize`→ComboBox.cpp, `setVisible_e`→KuiEffect.cpp, `findChildByKey`→KuiEffect.cpp, `addChild_e`→KuiEffect.cpp, `Size`→KFile.cpp, `getDialogPosition`→KuiEffect.cpp

## `gameui/KuiPlayerTrade.h`
- 141 dòng. Created by 2018.10 �ᵶ����Ц QQ:25557432
- Gọi tới: `KuiPlayerTrade`→KuiPlayerTrade.cpp, `AddObject`→KuiCompoundItem.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `UpdateItem`→KSellItem.cpp, `UpdateGiveItem`→KgameWorld.cpp, `UpdateTarGiveItem`→KuiPlayerTrade.cpp, `UpdateTradeOperData`→KgameWorld.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `__ClosePad`→KuiPlayerTrade.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `closeItemPadCallback`→KgameWorld.cpp

## `gameui/KuiPlayerTrade_old.cpp`
- 2274 dòng. 有按钮的　ｔａｌｋ　对话框
- Hàm: `KuiPlayerTrade_old`, `KuiPlayerTrade_old`, `KuiPlayerTrade_old::create`, `KuiPlayerTrade_old::init`, `KuiPlayerTrade_old::addDialogData`, `KuiPlayerTrade_old::setcoloseButton`, `KuiPlayerTrade_old::zhengCallBackFunc`, `KuiPlayerTrade_old::tradeCallBackFunc`, `KuiPlayerTrade_old::okCallBackFunc_`, `KuiPlayerTrade_old::btnCallBackFunc_fangzhi`, `KuiPlayerTrade_old::btnCallBackFunc_quxia`, `KuiPlayerTrade_old::__ClosePad`, `KuiPlayerTrade_old::buttonCallBackFunc`, `KuiPlayerTrade_old::closePopLayer`, `KuiPlayerTrade_old::closeItemPadCallback`, `KuiPlayerTrade_old::gettarGiveItem`, `KuiPlayerTrade_old::getGiveItem`, `KuiPlayerTrade_old::getRectItem`, `KuiPlayerTrade_old::onTouchBegan`, `KuiPlayerTrade_old::UpdateTradeOperData`, `KuiPlayerTrade_old::UpdateTarGiveItem`, `KuiPlayerTrade_old::UpdateGiveItem`, `KuiPlayerTrade_old::UpdateItem`, `KuiPlayerTrade_old::OnModififyMoney`, `KuiPlayerTrade_old::OnAdjustedMoney` …(+12)
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `GetGameData`→CoreShell.cpp, `ccMessageBox_new`→KCore.cpp, `GetID`→KFaction.cpp, `findinidata_one`→Kgetinidata.cpp, `setDialogColor`→KuiEffect.cpp, `g_StrLower`→KStrBase.cpp, `OperationRequest`→CoreShell.cpp, `setContentSize`→ComboBox.cpp, `setVisible_e`→KuiEffect.cpp, `findChildByKey`→KuiEffect.cpp, `addChild_e`→KuiEffect.cpp, `Size`→KFile.cpp, `getDialogPosition`→KuiEffect.cpp

## `gameui/KuiPlayerTrade_old.h`
- 141 dòng. Created by 2018.10 横刀向天笑 QQ:25557432
- Gọi tới: `KuiPlayerTrade_old`→KuiPlayerTrade_old.cpp, `AddObject`→KuiCompoundItem.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `UpdateItem`→KSellItem.cpp, `UpdateGiveItem`→KgameWorld.cpp, `UpdateTarGiveItem`→KuiPlayerTrade.cpp, `UpdateTradeOperData`→KgameWorld.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `__ClosePad`→KuiPlayerTrade.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `closeItemPadCallback`→KgameWorld.cpp

## `gameui/KuiProgressbar.cpp`
- 238 dòng. 有按钮的　ｔａｌｋ　对话框
- Hàm: `KuiProgressbar`, `KuiProgressbar`, `KuiProgressbar::create`, `KuiProgressbar::init`, `KuiProgressbar::addDialogData`, `KuiProgressbar::setcoloseButton`, `KuiProgressbar::buttonCallBackFunc`, `KuiProgressbar::closePopLayer`, `KuiProgressbar::getRect`, `KuiProgressbar::onTouchBegan`, `KuiProgressbar::update`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `g_StrLower`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `GetGameData`→CoreShell.cpp, `OperationRequest`→CoreShell.cpp, `setContentSize`→ComboBox.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp

## `gameui/KuiProgressbar.h`
- 68 dòng. Created by 2018.10 横刀向天笑 QQ:25557432
- Gọi tới: `KuiProgressbar`→KuiProgressbar.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `gameui/KuiRankInfo.cpp`
- 616 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiRankInfo`, `KuiRankInfo`, `KuiRankInfo::create`, `KuiRankInfo::init`, `KuiRankInfo::addDialogData`, `KuiRankInfo::AddTaskIndex`, `KuiRankInfo::removeitems`, `KuiRankInfo::selectedMainListItemEvent`, `KuiRankInfo::showItemInfo`, `KuiRankInfo::setcoloseButton`, `KuiRankInfo::oktouchEvent`, `KuiRankInfo::btnCallBackFunc`, `KuiRankInfo::buttonCallBackFunc`, `KuiRankInfo::closePopLayer`, `KuiRankInfo::getRect`, `KuiRankInfo::onTouchEnded`, `KuiRankInfo::onTouchMoved`, `KuiRankInfo::onTouchBegan`, `KuiRankInfo::update`, `KuiRankInfo::draw`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `GetInteger`→KTabFile.cpp, `removeitems`→KuiCometoMap.cpp, `ccMessageBox_new`→KCore.cpp, `setContentSize`→ComboBox.cpp, `findinidata_one`→Kgetinidata.cpp, `g_StrLower`→KStrBase.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `Clear`→KIniFile.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `GetString`→KTabFile.cpp

## `gameui/KuiRankInfo.h`
- 104 dòng. KuiRankInfo.h
- Gọi tới: `KuiRankInfo`→KuiRankInfo.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `selectedMainListItemEvent`→KuiAutoPlay.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `oktouchEvent`→KuiAutoPlay.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `btnCallBackFunc`→KuiEscInfo.cpp

## `gameui/KuiRoleState.cpp`
- 3006 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiRoleState`, `KuiRoleState`, `KuiRoleState::create`, `KuiRoleState::init`, `KuiRoleState::addDialogData`, `KuiRoleState::setPadTouchEnabled`, `KuiRoleState::setMeridianLevelInfo`, `KuiRoleState::ClearVal`, `KuiRoleState::getPosText`, `KuiRoleState::touchMeridianBtnEvent`, `KuiRoleState::pointCallback_dan`, `KuiRoleState::pointCallback_Meridian_Font`, `KuiRoleState::pointCallback_Meridian`, `KuiRoleState::touchPageBtnEvent`, `KuiRoleState::setcoloseButton`, `KuiRoleState::addCallBackFunc`, `KuiRoleState::buttonxiuCallBackFunc`, `KuiRoleState::buttonEqCallBackFunc`, `KuiRoleState::buttonCallBackFunc`, `KuiRoleState::closePopLayer`, `KuiRoleState::UpdateAllEquips`, `KuiRoleState::addpicBox`, `KuiRoleState::layerCallBakc`, `KuiRoleState::UpdateEquip`, `KuiRoleState::getRect` …(+14)
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `GetInteger`→KTabFile.cpp, `findinidata_one`→Kgetinidata.cpp, `g_StrLower`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `GetGameData`→CoreShell.cpp, `Clear`→KIniFile.cpp, `Load`→KIniFile.cpp, `GetString`→KTabFile.cpp, `OperationRequest`→CoreShell.cpp, `getDialogPosition`→KuiEffect.cpp, `getDialogSize`→KuiEffect.cpp, `setContentSize`→ComboBox.cpp

## `gameui/KuiRoleState.h`
- 252 dòng. Created by 横刀向天笑 QQ:25557432 tuanln
- Gọi tới: `KuiRoleState`→KuiRoleState.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `setDialodPosition`→KuiRoleState.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `buttonEqCallBackFunc`→KuiRoleState.cpp, `buttonxiuCallBackFunc`→KuiRoleState.cpp

## `gameui/KuiSelNativePlace.cpp`
- 842 dòng. #include "Klogin.h"
- Hàm: `KuiSelNativePlace`, `KuiSelNativePlace`, `KuiSelNativePlace::scene`, `KuiSelNativePlace::init`, `KuiSelNativePlace::LoadList`, `KuiSelNativePlace::mainEnterCallback`, `KuiSelNativePlace::closeYeziSprPad`, `KuiSelNativePlace::update`, `KuiSelNativePlace::draw`, `KuiSelNativePlace::isFileExist`, `KuiSelNativePlace::copyData`, `KuiSelNativePlace::onEnter`, `KuiSelNativePlace::onExit`, `KuiSelNativePlace::onEnterTransitionDidFinish`, `KuiSelNativePlace::getRect`, `KuiSelNativePlace::onTouchesBegan`, `KuiSelNativePlace::CheckClick`, `KuiSelNativePlace::onTouchesMoved`, `KuiSelNativePlace::onTouchesEnded`, `KuiSelNativePlace::finish`, `KuiSelNativePlace::onTouchesCancelled`, `KuiSelNativePlace::ProcessToLoginGameServResponse`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `ccMessageBox_new`→KCore.cpp, `isFileExist`→KgameWorld.cpp, `scene`→KgameWorld.cpp, `g_StrLower`→KStrBase.cpp, `GetString`→KTabFile.cpp, `GetInteger`→KTabFile.cpp, `Cleanup`→ClientStage.cpp, `getpicPath`→Kgetinidata.cpp, `setBreakTheead`→SocketClient.cpp, `g_FileName2Id`→KFilePath.cpp, `Load`→KIniFile.cpp, `setBufferEmpty`→ClientStage.cpp, `init`→HelloWorldScene.cpp

## `gameui/KuiSelNativePlace.h`
- 110 dòng. 登陆界面 选择人物 创建 删除等
- Gọi tới: `KuiSelNativePlace`→KuiSelNativePlace.cpp, `init`→HelloWorldScene.cpp, `onEnter`→KgameWorld.cpp, `onExit`→KgameWorld.cpp, `onEnterTransitionDidFinish`→KgameWorld.cpp, `update`→KgameWorld.cpp, `scene`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `AcceptNetMsg`→KuiWarnInfo.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `copyData`→KgameWorld.cpp, `isFileExist`→KgameWorld.cpp, `buttonCallback`→KgameWorld.cpp, `mainEnterCallback`→KuiNewPlayer.cpp, `CheckClick`→KuiSelNativePlace.cpp

## `gameui/KuiSelPlayer_new.cpp`
- 1201 dòng. #include "Klogin.h"
- Hàm: `KuiSelPlayer_new`, `KuiSelPlayer_new`, `KuiSelPlayer_new::scene`, `KuiSelPlayer_new::init`, `KuiSelPlayer_new::closeRolePad_1`, `KuiSelPlayer_new::closeRolePad_2`, `KuiSelPlayer_new::closeRolePad_3`, `KuiSelPlayer_new::mainNewCallback`, `KuiSelPlayer_new::GetRoleCount`, `KuiSelPlayer_new::mainDelCallback`, `KuiSelPlayer_new::mainEnterCallback`, `KuiSelPlayer_new::update`, `KuiSelPlayer_new::getRect`, `KuiSelPlayer_new::draw`, `KuiSelPlayer_new::onTouchBegan`, `KuiSelPlayer_new::onTouchMoved`, `KuiSelPlayer_new::onTouchEnded`, `KuiSelPlayer_new::GetRoleImageName`, `KuiSelPlayer_new::ProcessToLoginGameServResponse`, `KuiSelPlayer_new::getCurTime`, `KuiSelPlayer_new::EnterGame`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `isFileExist`→KgameWorld.cpp, `upSpriteData`→KuiShowSprite.cpp, `g_StrLower`→KStrBase.cpp, `Cleanup`→ClientStage.cpp, `setBreakTheead`→SocketClient.cpp, `scene`→KgameWorld.cpp, `setBufferEmpty`→ClientStage.cpp, `g_FileName2Id`→KFilePath.cpp, `setShowVisible`→KuiShowSprite.cpp, `GetRoleImageName`→KuiNewPlayer.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `setContentSize`→ComboBox.cpp, `g_StrCmp`→KStrBase.cpp

## `gameui/KuiSelPlayer_new.h`
- 120 dòng. 登陆界面 选择人物 创建 删除等
- Gọi tới: `KuiSelPlayer_new`→KuiSelPlayer_new.cpp, `init`→HelloWorldScene.cpp, `update`→KgameWorld.cpp, `scene`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `AcceptNetMsg`→KuiWarnInfo.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `buttonCallback`→KgameWorld.cpp, `EnterGame`→KuiSelPlayer_new.cpp, `GetRoleCount`→KuiNewPlayer.cpp, `mainEnterCallback`→KuiNewPlayer.cpp, `mainNewCallback`→KuiSelPlayer_new.cpp, `mainDelCallback`→KuiSelPlayer_new.cpp, `GetRoleImageName`→KuiNewPlayer.cpp, `closeYeziSprPad`→KuiNewPlayer.cpp

## `gameui/KuiSellItem.cpp`
- 1413 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiSellItem`, `KuiSellItem`, `KuiSellItem::create`, `KuiSellItem::init`, `KuiSellItem::addDialogData`, `KuiSellItem::setcoloseButton`, `KuiSellItem::menuTanCallback`, `KuiSellItem::touchBtnEvent_tan`, `KuiSellItem::closegaoPadCallback`, `KuiSellItem::closesavemonyPadCallback`, `KuiSellItem::tuoguanCallBackFunc`, `KuiSellItem::gaoCallBackFunc`, `KuiSellItem::tanCallBackFunc`, `KuiSellItem::closelockPadCallback`, `KuiSellItem::biaoCallBackFunc`, `KuiSellItem::zhengCallBackFunc`, `KuiSellItem::buttonCallBackFunc`, `KuiSellItem::closePopLayer`, `KuiSellItem::getRect`, `KuiSellItem::onTouchEnded`, `KuiSellItem::onTouchMoved`, `KuiSellItem::onTouchBegan`, `KuiSellItem::closeItemPadCallback`, `KuiSellItem::update`, `KuiSellItem::draw` …(+4)
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `findinidata_one`→Kgetinidata.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `ccMessageBox_new`→KCore.cpp, `g_StrLower`→KStrBase.cpp, `GetGameData`→CoreShell.cpp, `GetID`→KFaction.cpp, `OperationRequest`→CoreShell.cpp, `setDialogColor`→KuiEffect.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `setContentSize`→ComboBox.cpp

## `gameui/KuiSellItem.h`
- 116 dòng. 设置确定取消按钮,参数：调用层对象，调用层回调函数
- Gọi tới: `KuiSellItem`→KuiSellItem.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `UpdateItem`→KSellItem.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `tuoguanCallBackFunc`→KuiLockscree.cpp, `zhengCallBackFunc`→Kuigive.cpp

## `gameui/KuiSelserver.cpp`
- 734 dòng. #include "../gameui/PopupLayer.h"
- Hàm: `KuiSelserver`, `KuiSelserver`, `KuiSelserver::scene`, `KuiSelserver::init`, `KuiSelserver::closeShowSpritePad`, `KuiSelserver::selectedMsgListItemEvent`, `KuiSelserver::removeitems`, `KuiSelserver::selServerCallBack`, `KuiSelserver::mianCancelCallback`, `KuiSelserver::mianLoginCallback`, `KuiSelserver::update`, `KuiSelserver::draw`, `KuiSelserver::isFileExist`, `KuiSelserver::copyData`, `KuiSelserver::finish`, `KuiSelserver::onTouchBegan`, `KuiSelserver::onTouchMoved`, `KuiSelserver::onTouchCancelled`, `KuiSelserver::onTouchEnded`, `KuiSelserver::editBoxEditingDidBegin`, `KuiSelserver::editBoxEditingDidEnd`, `KuiSelserver::editBoxTextChanged`, `KuiSelserver::editBoxReturn`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `GetInteger`→KTabFile.cpp, `g_StrLower`→KStrBase.cpp, `GetString`→KTabFile.cpp, `isFileExist`→KgameWorld.cpp, `ccMessageBox_new`→KCore.cpp, `removeitems`→KuiCometoMap.cpp, `Clear`→KIniFile.cpp, `Load`→KIniFile.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `g_FileName2Id`→KFilePath.cpp, `scene`→KgameWorld.cpp, `SimplyDecrypt`→dataChecksum.cpp, `setBreakTheead`→SocketClient.cpp

## `gameui/KuiSelserver.h`
- 93 dòng. 登陆界面　输入帐号密码
- Gọi tới: `KuiSelserver`→KuiSelserver.cpp, `init`→HelloWorldScene.cpp, `scene`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `update`→KgameWorld.cpp, `copyData`→KgameWorld.cpp, `isFileExist`→KgameWorld.cpp, `selServerCallBack`→KuiSelserver.cpp, `mianLoginCallback`→Klogin.cpp, `mianCancelCallback`→Klogin.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `onTouchCancelled`→KHRocker.cpp, `finish`→Klogin.cpp

## `gameui/KuiShop.cpp`
- 757 dòng. (không có chú thích đầu)
- Hàm: `KuiShop`, `KuiShop`, `KuiShop::create`, `KuiShop::init`, `KuiShop::addDialoaData`, `KuiShop::setcoloseButton`, `KuiShop::backCallBackFunc`, `KuiShop::nextCallBackFunc`, `KuiShop::buyCallBackFunc`, `KuiShop::closeCallBackFunc`, `KuiShop::closePopLayer`, `KuiShop::getRect`, `KuiShop::onTouchEnded`, `KuiShop::onTouchMoved`, `KuiShop::onTouchBegan`, `KuiShop::closedescPadCallback`, `KuiShop::update`, `KuiShop::draw`, `KuiShop::Clear`, `KuiShop::AddObject`, `KuiShop::SetPage`, `KuiShop::UpdateData`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `findinidata_one`→Kgetinidata.cpp, `g_StrLower`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `GetGameData`→CoreShell.cpp, `Clear`→KIniFile.cpp, `SetPage`→KuiDynamicShop.cpp, `setContentSize`→ComboBox.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `AddObject`→KuiCompoundItem.cpp, `addDialoaData`→KuiDynamicShop.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `UpdateData`→KuiCometoMap.cpp

## `gameui/KuiShop.h`
- 90 dòng. 触摸函数onTouchBegan，返回true
- Gọi tới: `KuiShop`→KuiShop.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `UpdateData`→KuiCometoMap.cpp, `addDialoaData`→KuiDynamicShop.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buyCallBackFunc`→KuiDynamicShop.cpp, `backCallBackFunc`→KuiDynamicShop.cpp, `nextCallBackFunc`→KuiDynamicShop.cpp

## `gameui/KuiShowSprite.cpp`
- 463 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiShowSprite`, `KuiShowSprite`, `KuiShowSprite::create`, `KuiShowSprite::init`, `KuiShowSprite::mianDialogSet`, `KuiShowSprite::addDialogData`, `KuiShowSprite::setcoloseButton`, `KuiShowSprite::nodeCallBackFunc`, `KuiShowSprite::buttonCallBackFunc`, `KuiShowSprite::closePopLayer`, `KuiShowSprite::getRect`, `KuiShowSprite::onTouchBegan`, `KuiShowSprite::onTouchMoved`, `KuiShowSprite::onTouchEnded`, `KuiShowSprite::setShowPosition`, `KuiShowSprite::removeShowSprite`, `KuiShowSprite::getShowSize`, `KuiShowSprite::update`, `KuiShowSprite::ccgetTxtData_s`, `KuiShowSprite::upSpriteData`, `KuiShowSprite::setShowTga`, `KuiShowSprite::setShowVisible`, `KuiShowSprite::getShowTga`, `KuiShowSprite::draw`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `g_StrLower`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `IR_UpdateTime`→ImgRef.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `g_FileName2Id`→KFilePath.cpp, `IR_GetCurrentTime`→ImgRef.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `setContentSize`→ComboBox.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `gameui/KuiShowSprite.h`
- 132 dòng. Created by 2018.10 横刀向天笑 QQ:25557432
- Gọi tới: `KuiShowSprite`→KuiShowSprite.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `getShowSize`→KuiShowSprite.cpp, `removeShowSprite`→KuiShowSprite.cpp, `setShowPosition`→KuiShowSprite.cpp, `upSpriteData`→KuiShowSprite.cpp, `setShowTga`→KuiShowSprite.cpp, `getShowTga`→KuiShowSprite.cpp, `setShowVisible`→KuiShowSprite.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `mianDialogSet`→KuiShowSprite.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp

## `gameui/KuiSkill.cpp`
- 720 dòng. (không có chú thích đầu)
- Hàm: `Kuiskill`, `Kuiskill`, `Kuiskill::create`, `Kuiskill::init`, `Kuiskill::addDialogData`, `Kuiskill::getfreeSkillNode`, `Kuiskill::UpdateSkill`, `Kuiskill::setcoloseButton`, `Kuiskill::buttonCallBackFunc`, `Kuiskill::closePopLayer`, `Kuiskill::getRect`, `Kuiskill::onTouchEnded`, `Kuiskill::onTouchMoved`, `Kuiskill::onTouchBegan`, `Kuiskill::closeSkilldescPadCallback`, `Kuiskill::closeDescCallback`, `Kuiskill::addskillpoint`, `Kuiskill::update`, `Kuiskill::draw`, `Kuiskill::GetiniData`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `GetGameData`→CoreShell.cpp, `setContentSize`→ComboBox.cpp, `GetSkill`→KSkillManager.h, `UpdateSkill`→KgameWorld.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `GetSkillName`→KThiefSkill.cpp, `GetSkillStyle`→KSkillManager.h, `FindSame`→KPlayerSet.cpp, `setTitle`→PopupLayer.cpp

## `gameui/KuiSkill.h`
- 87 dòng. Created by 横刀向天笑 QQ:25557432
- Gọi tới: `Kuiskill`→KuiSkill.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `UpdateSkill`→KgameWorld.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `addskillpoint`→KuiSkill.cpp, `closeDescCallback`→KuiSkill.cpp

## `gameui/KuiSkillSpecial.cpp`
- 474 dòng. (không có chú thích đầu)
- Hàm: `KuiSkillSpecial`, `KuiSkillSpecial`, `KuiSkillSpecial::create`, `KuiSkillSpecial::init`, `KuiSkillSpecial::mianDialogSet`, `KuiSkillSpecial::addDialogData`, `KuiSkillSpecial::setcoloseButton`, `KuiSkillSpecial::nodeCallBackFunc`, `KuiSkillSpecial::buttonCallBackFunc`, `KuiSkillSpecial::closePopLayer`, `KuiSkillSpecial::getRect`, `KuiSkillSpecial::onTouchBegan`, `KuiSkillSpecial::onTouchMoved`, `KuiSkillSpecial::onTouchEnded`, `KuiSkillSpecial::setShowPosition`, `KuiSkillSpecial::removeShowSprite`, `KuiSkillSpecial::getShowSize`, `KuiSkillSpecial::update`, `KuiSkillSpecial::ccgetTxtData_s`, `KuiSkillSpecial::upSpriteData`, `KuiSkillSpecial::setShowTga`, `KuiSkillSpecial::getShowTga`, `KuiSkillSpecial::draw`
- Gọi tới: `create`→KHRocker.cpp, `findinidata_one`→Kgetinidata.cpp, `t_sprintf`→KStrBase.cpp, `g_StrLower`→KStrBase.cpp, `IR_UpdateTime`→ImgRef.cpp, `GetLocalPositionByMps`→KSubWorld.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `mianDialogSet`→KuiShowSprite.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `g_FileName2Id`→KFilePath.cpp, `IR_GetCurrentTime`→ImgRef.cpp, `nodeCallBackFunc`→KuiShowSprite.cpp, `ccgetTxtData_s`→KuiShowSprite.cpp

## `gameui/KuiSkillSpecial.h`
- 126 dòng. Created by 2018.10 横刀向天笑 QQ:25557432
- Gọi tới: `KuiSkillSpecial`→KuiSkillSpecial.cpp, `ccgetTxtData_s`→KuiShowSprite.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `getShowSize`→KuiShowSprite.cpp, `removeShowSprite`→KuiShowSprite.cpp, `setShowPosition`→KuiShowSprite.cpp, `upSpriteData`→KuiShowSprite.cpp, `setShowTga`→KuiShowSprite.cpp, `getShowTga`→KuiShowSprite.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `mianDialogSet`→KuiShowSprite.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp

## `gameui/KuiSkilldesc.cpp`
- 705 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiSkilldesc`, `KuiSkilldesc`, `KuiSkilldesc::create`, `KuiSkilldesc::init`, `KuiSkilldesc::addDialogData`, `KuiSkilldesc::setcoloseButton`, `KuiSkilldesc::buttonCallBackFunc`, `KuiSkilldesc::closePopLayer`, `KuiSkilldesc::getRect`, `KuiSkilldesc::onTouchBegan`, `KuiSkilldesc::update`, `KuiSkilldesc::draw`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `GetStringByKeyFromFile`→CXmlStream.cpp, `create`→KHRocker.cpp, `GetSkill`→KSkillManager.h, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `setContentSize`→ComboBox.cpp, `TEncodeText_`→Text.cpp, `GetDescAboutLevel`→KSkills.cpp, `GetString`→KTabFile.cpp, `GetSkillName`→KThiefSkill.cpp, `TEncodeText`→Text.cpp, `ccMessageBox_new`→KCore.cpp, `GetGameData`→CoreShell.cpp

## `gameui/KuiSkilldesc.h`
- 81 dòng. 设置确定取消按钮,参数：调用层对象，调用层回调函数
- Gọi tới: `KuiSkilldesc`→KuiSkilldesc.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `gameui/KuiSortSkill_l.cpp`
- 304 dòng. 有按钮的　ｔａｌｋ　对话框
- Hàm: `KuiSortSkill_l`, `KuiSortSkill_l`, `KuiSortSkill_l::create`, `KuiSortSkill_l::init`, `KuiSortSkill_l::setCurPosition`, `KuiSortSkill_l::addDialogData`, `KuiSortSkill_l::skillCallback`, `KuiSortSkill_l::closeSkilldescPadCallback`, `KuiSortSkill_l::UpdateData`, `KuiSortSkill_l::setcoloseButton`, `KuiSortSkill_l::buttonCallBackFunc`, `KuiSortSkill_l::closePopLayer`, `KuiSortSkill_l::getRect`, `KuiSortSkill_l::onTouchBegan`, `KuiSortSkill_l::update`, `KuiSortSkill_l::draw`
- Gọi tới: `create`→KHRocker.cpp, `GetGameData`→CoreShell.cpp, `setContentSize`→ComboBox.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `GetSkill`→KSkillManager.h, `t_sprintf`→KStrBase.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `FindSame`→KPlayerSet.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `ccMessageBox_new`→KCore.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `g_StrLower`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp

## `gameui/KuiSortSkill_l.h`
- 76 dòng. #define FIGHT_SKILL_COUNT_PER_PAGE	25
- Gọi tới: `KuiSortSkill_l`→KuiSortSkill_l.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `setCurPosition`→KuiSortSkill_l.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `UpdateData`→KuiCometoMap.cpp, `skillCallback`→KuiAutoPlay.cpp, `closeSkilldescPadCallback`→KuiAutoPlay.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `gameui/KuiSortSkill_r.cpp`
- 305 dòng. 有按钮的　ｔａｌｋ　对话框
- Hàm: `KuiSortSkill_r`, `KuiSortSkill_r`, `KuiSortSkill_r::create`, `KuiSortSkill_r::init`, `KuiSortSkill_r::setCurPosition`, `KuiSortSkill_r::addDialogData`, `KuiSortSkill_r::skillCallback`, `KuiSortSkill_r::closeSkilldescPadCallback`, `KuiSortSkill_r::UpdateData`, `KuiSortSkill_r::setcoloseButton`, `KuiSortSkill_r::buttonCallBackFunc`, `KuiSortSkill_r::closePopLayer`, `KuiSortSkill_r::getRect`, `KuiSortSkill_r::onTouchBegan`, `KuiSortSkill_r::update`, `KuiSortSkill_r::draw`
- Gọi tới: `create`→KHRocker.cpp, `setContentSize`→ComboBox.cpp, `GetGameData`→CoreShell.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `GetSkill`→KSkillManager.h, `t_sprintf`→KStrBase.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `FindSame`→KPlayerSet.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `ccMessageBox_new`→KCore.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `setCurPosition`→KuiSortSkill_l.cpp, `g_StrLower`→KStrBase.cpp

## `gameui/KuiSortSkill_r.h`
- 78 dòng. Created by 横刀向天笑 QQ:25557432
- Gọi tới: `KuiSortSkill_r`→KuiSortSkill_r.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `setCurPosition`→KuiSortSkill_l.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `UpdateData`→KuiCometoMap.cpp, `skillCallback`→KuiAutoPlay.cpp, `closeSkilldescPadCallback`→KuiAutoPlay.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `gameui/KuiStateSkillControl.cpp`
- 295 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiStateSkillControl`, `KuiStateSkillControl`, `KuiStateSkillControl::create_`, `KuiStateSkillControl::init`, `KuiStateSkillControl::addDialogData`, `KuiStateSkillControl::setcoloseButton`, `KuiStateSkillControl::buttonCallBackFunc`, `KuiStateSkillControl::closePopLayer`, `KuiStateSkillControl::setLayerVisible`, `KuiStateSkillControl::getRect`, `KuiStateSkillControl::onTouchEnded`, `KuiStateSkillControl::onTouchBegan`, `KuiStateSkillControl::onTouchMoved`, `KuiStateSkillControl::moveLayer`, `KuiStateSkillControl::EndedLayer`, `KuiStateSkillControl::upRoleInfo`, `KuiStateSkillControl::update`, `KuiStateSkillControl::draw`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `GetInteger`→KTabFile.cpp, `GetString`→KTabFile.cpp, `create`→KHRocker.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `Load`→KIniFile.cpp, `create_`→KuiFaceSelector.cpp, `setContentSize`→ComboBox.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `Clear`→KIniFile.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `gameui/KuiStateSkillControl.h`
- 89 dòng. 技能状态小图显示
- Gọi tới: `KuiStateSkillControl`→KuiStateSkillControl.cpp, `init`→HelloWorldScene.cpp, `create_`→KuiFaceSelector.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `setLayerVisible`→KuiStateSkillControl.cpp, `moveLayer`→KuiBtnControl.cpp, `EndedLayer`→KuiBtnControl.cpp, `upRoleInfo`→KuiFaceSelector.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp

## `gameui/KuiSuperShop.cpp`
- 745 dòng. memset(Skills,0,sizeof(KUiSkillData) * 50);
- Hàm: `KuiSuperShop`, `KuiSuperShop`, `KuiSuperShop::create`, `KuiSuperShop::init`, `KuiSuperShop::addDialoaData`, `KuiSuperShop::setcoloseButton`, `KuiSuperShop::backCallBackFunc`, `KuiSuperShop::nextCallBackFunc`, `KuiSuperShop::buyCallBackFunc`, `KuiSuperShop::closeCallBackFunc`, `KuiSuperShop::closePopLayer`, `KuiSuperShop::getRect`, `KuiSuperShop::onTouchBegan`, `KuiSuperShop::closedescPadCallback`, `KuiSuperShop::update`, `KuiSuperShop::draw`, `KuiSuperShop::Clear`, `KuiSuperShop::AddObject`, `KuiSuperShop::SetPage`, `KuiSuperShop::UpdateData`, `KuiSuperShop::UpdateShop`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `findinidata_one`→Kgetinidata.cpp, `g_StrLower`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `Clear`→KIniFile.cpp, `setContentSize`→ComboBox.cpp, `SetPage`→KuiDynamicShop.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `GetGameData`→CoreShell.cpp, `AddObject`→KuiCompoundItem.cpp, `addDialoaData`→KuiDynamicShop.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `UpdateData`→KuiCometoMap.cpp

## `gameui/KuiSuperShop.h`
- 91 dòng. 触摸函数onTouchBegan，返回true
- Gọi tới: `KuiSuperShop`→KuiSuperShop.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `UpdateData`→KuiCometoMap.cpp, `addDialoaData`→KuiDynamicShop.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buyCallBackFunc`→KuiDynamicShop.cpp, `backCallBackFunc`→KuiDynamicShop.cpp, `nextCallBackFunc`→KuiDynamicShop.cpp, `closeCallBackFunc`→KuiDynamicShop.cpp, `closedescPadCallback`→KuiDynamicShop.cpp

## `gameui/KuiTalkDialog.cpp`
- 698 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiTalkDialog`, `KuiTalkDialog`, `KuiTalkDialog::create`, `KuiTalkDialog::init`, `KuiTalkDialog::addDialogData`, `KuiTalkDialog::Show`, `KuiTalkDialog::setcoloseButton`, `KuiTalkDialog::buttonCallBackFunc`, `KuiTalkDialog::closePopLayer`, `KuiTalkDialog::getRect`, `KuiTalkDialog::changeMsg`, `KuiTalkDialog::onTouchBegan`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `Show`→KLittleMap.cpp, `getColorIndex`→Text.cpp, `g_Atoui`→KStrBase.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `g_StrLower`→KStrBase.cpp, `setContentSize`→ComboBox.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `FilterTextColor`→Text.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp

## `gameui/KuiTalkDialog.h`
- 74 dòng. Created by 2018.10 横刀向天笑 QQ:25557432
- Gọi tới: `KuiTalkDialog`→KuiTalkDialog.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `Show`→KLittleMap.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `changeMsg`→KuiTalkDialog.cpp

## `gameui/KuiTalkDialog1.cpp`
- 456 dòng. 有按钮的　ｔａｌｋ　对话框
- Hàm: `KuiTalkDialog1`, `KuiTalkDialog1`, `KuiTalkDialog1::create`, `KuiTalkDialog1::init`, `KuiTalkDialog1::addDialogData`, `KuiTalkDialog1::setcoloseButton`, `KuiTalkDialog1::btnMuneallback`, `KuiTalkDialog1::buttonCallBackFunc`, `KuiTalkDialog1::closePopLayer`, `KuiTalkDialog1::getRect`, `KuiTalkDialog1::touchEvent`, `KuiTalkDialog1::onTouchBegan`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `OperationRequest`→CoreShell.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `TeamOperation`→CoreShell.cpp, `TongOperation`→CoreShell.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `ccMessageBox_new`→KCore.cpp, `setTitle`→PopupLayer.cpp, `g_StrLower`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `setContentSize`→ComboBox.cpp

## `gameui/KuiTalkDialog1.h`
- 73 dòng. Created by 2018.10 横刀向天笑 QQ:25557432
- Gọi tới: `KuiTalkDialog1`→KuiTalkDialog1.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `touchEvent`→KuiTalkDialog1.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `btnMuneallback`→KuiTalkDialog1.cpp

## `gameui/KuiTaskInfo.cpp`
- 1478 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiTaskInfo`, `KuiTaskInfo`, `KuiTaskInfo::create`, `KuiTaskInfo::init`, `KuiTaskInfo::addDialogData`, `KuiTaskInfo::addmsgInfo`, `KuiTaskInfo::addmsgBtnInfo`, `KuiTaskInfo::AddTaskIndex`, `KuiTaskInfo::removeitems`, `KuiTaskInfo::selectedMsgListItemEvent`, `KuiTaskInfo::selectedMainListItemEvent`, `KuiTaskInfo::setcoloseButton`, `KuiTaskInfo::touchPageBtnEvent`, `KuiTaskInfo::oktouchEvent`, `KuiTaskInfo::btnCallBackFunc`, `KuiTaskInfo::buttonCallBackFunc`, `KuiTaskInfo::closePopLayer`, `KuiTaskInfo::getRect`, `KuiTaskInfo::onTouchEnded`, `KuiTaskInfo::onTouchMoved`, `KuiTaskInfo::onTouchBegan`, `KuiTaskInfo::update`, `KuiTaskInfo::draw`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `ccMessageBox_new`→KCore.cpp, `setContentSize`→ComboBox.cpp, `removeitems`→KuiCometoMap.cpp, `findinidata_one`→Kgetinidata.cpp, `GetInteger`→KTabFile.cpp, `g_StrLower`→KStrBase.cpp, `getColorIndex`→Text.cpp, `g_Atoui`→KStrBase.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `Clear`→KIniFile.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp

## `gameui/KuiTaskInfo.h`
- 126 dòng. KuiTaskInfo.h
- Gọi tới: `KuiTaskInfo`→KuiTaskInfo.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `addmsgInfo`→KuiTaskInfo.cpp, `addmsgBtnInfo`→KuiTaskInfo.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `selectedMainListItemEvent`→KuiAutoPlay.cpp, `selectedMsgListItemEvent`→KuiCometoMap.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp

## `gameui/KuiTeam.cpp`
- 859 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiTeam`, `KuiTeam`, `KuiTeam::create`, `KuiTeam::init`, `KuiTeam::addDialogData`, `KuiTeam::setcoloseButton`, `KuiTeam::btnCallBackFunc`, `KuiTeam::buttonCallBackFunc`, `KuiTeam::closePopLayer`, `KuiTeam::selectedBoxStateEvent`, `KuiTeam::selectedPlayersListItemEvent`, `KuiTeam::selectedItemEvent`, `KuiTeam::getRect`, `KuiTeam::onTouchEnded`, `KuiTeam::onTouchMoved`, `KuiTeam::onTouchBegan`, `KuiTeam::OnRefresh`, `KuiTeam::UpdateData`, `KuiTeam::Clear`, `KuiTeam::update`, `KuiTeam::draw`
- Gọi tới: `create`→KHRocker.cpp, `findinidata_one`→Kgetinidata.cpp, `t_sprintf`→KStrBase.cpp, `TeamOperation`→CoreShell.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `g_StrLower`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `setContentSize`→ComboBox.cpp, `GetGameData`→CoreShell.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `UpdateData`→KuiCometoMap.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `Clear`→KIniFile.cpp

## `gameui/KuiTeam.h`
- 97 dòng. #define FIGHT_SKILL_COUNT_PER_PAGE	25
- Gọi tới: `KuiTeam`→KuiTeam.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `UpdateData`→KuiCometoMap.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `selectedItemEvent`→KuiChatList.cpp, `selectedPlayersListItemEvent`→KuiChatList.cpp, `selectedBoxStateEvent`→Kuiplayerfun.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp

## `gameui/KuiTeamInfo.cpp`
- 339 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiTeamInfo`, `KuiTeamInfo`, `KuiTeamInfo::Clear`, `KuiTeamInfo::create_`, `KuiTeamInfo::init`, `KuiTeamInfo::addDialogData`, `KuiTeamInfo::setcoloseButton`, `KuiTeamInfo::buttonCallBackFunc`, `KuiTeamInfo::UpdateData`, `KuiTeamInfo::closePopLayer`, `KuiTeamInfo::getRect`, `KuiTeamInfo::onTouchBegan`, `KuiTeamInfo::onTouchMoved`, `KuiTeamInfo::onTouchEnded`, `KuiTeamInfo::update`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `g_StrLower`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `Clear`→KIniFile.cpp, `create`→KHRocker.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `TeamOperation`→CoreShell.cpp, `ccMessageBox_new`→KCore.cpp, `create_`→KuiFaceSelector.cpp, `setContentSize`→ComboBox.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `Remove`→KLinkArray.cpp

## `gameui/KuiTeamInfo.h`
- 177 dòng. ccMessageBox_new("test002","test",true);
- Gọi tới: `Release`→KCache.cpp, `ccMessageBox_new`→KCore.cpp, `KuiTeamInfo`→KuiTeamInfo.cpp, `SearchID`→KItemSet.cpp, `Remove`→KLinkArray.cpp, `init`→HelloWorldScene.cpp, `create_`→KuiFaceSelector.cpp, `update`→KgameWorld.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `UpdateData`→KuiCometoMap.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp

## `gameui/KuiTongCreateSheet.cpp`
- 448 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiTongCreateSheet`, `KuiTongCreateSheet`, `KuiTongCreateSheet::create`, `KuiTongCreateSheet::init`, `KuiTongCreateSheet::addDialogData`, `KuiTongCreateSheet::setcoloseButton`, `KuiTongCreateSheet::btnCallBackFunc`, `KuiTongCreateSheet::buttonCallBackFunc`, `KuiTongCreateSheet::closePopLayer`, `KuiTongCreateSheet::getRect`, `KuiTongCreateSheet::onTouchEnded`, `KuiTongCreateSheet::onTouchMoved`, `KuiTongCreateSheet::onTouchBegan`, `KuiTongCreateSheet::update`, `KuiTongCreateSheet::draw`
- Gọi tới: `create`→KHRocker.cpp, `findinidata_one`→Kgetinidata.cpp, `t_sprintf`→KStrBase.cpp, `g_StrLower`→KStrBase.cpp, `setContentSize`→ComboBox.cpp, `ccMessageBox_new`→KCore.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `TeamOperation`→CoreShell.cpp, `btnCallBackFunc`→KuiEscInfo.cpp, `TongOperation`→CoreShell.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp

## `gameui/KuiTongCreateSheet.h`
- 79 dòng. KuiTongCreateSheet.h
- Gọi tới: `KuiTongCreateSheet`→KuiTongCreateSheet.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `btnCallBackFunc`→KuiEscInfo.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `gameui/KuiTongInfo.cpp`
- 593 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiTongInfo`, `KuiTongInfo`, `KuiTongInfo::create`, `KuiTongInfo::init`, `KuiTongInfo::addDialogData`, `KuiTongInfo::setcoloseButton`, `KuiTongInfo::touchPageBtnEvent`, `KuiTongInfo::btnCallBackFunc`, `KuiTongInfo::buttonCallBackFunc`, `KuiTongInfo::closePopLayer`, `KuiTongInfo::getRect`, `KuiTongInfo::onTouchEnded`, `KuiTongInfo::onTouchMoved`, `KuiTongInfo::onTouchBegan`, `KuiTongInfo::update`, `KuiTongInfo::draw`
- Gọi tới: `setBtnTouchEnabled`→KuiCometoMap.cpp, `findinidata_one`→Kgetinidata.cpp, `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `g_StrLower`→KStrBase.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `setBtnTouchEnble`→KuiAutoPlay.cpp, `RemoveTempFile`→KuiCometoMap.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `TeamOperation`→CoreShell.cpp, `touchPageBtnEvent`→KuiAutoPlay.cpp, `ccMessageBox_new`→KCore.cpp

## `gameui/KuiTongInfo.h`
- 106 dòng. Created by 横刀向天笑 QQ:25557432.
- Gọi tới: `KuiTongInfo`→KuiTongInfo.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `btnCallBackFunc`→KuiEscInfo.cpp, `touchPageBtnEvent`→KuiAutoPlay.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `gameui/KuiTopControl.cpp`
- 454 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiTopControl`, `KuiTopControl`, `KuiTopControl::create_`, `KuiTopControl::init`, `KuiTopControl::addDialogData`, `KuiTopControl::setcoloseButton`, `KuiTopControl::buttonCallBackFunc`, `KuiTopControl::closePopLayer`, `KuiTopControl::registerWithTouchDispatcher`, `KuiTopControl::getRect`, `KuiTopControl::onTouchEnded`, `KuiTopControl::onTouchBegan`, `KuiTopControl::onTouchMoved`, `KuiTopControl::moveLayer`, `KuiTopControl::EndedLayer`, `KuiTopControl::upRoleInfo`, `KuiTopControl::update`, `KuiTopControl::draw`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `g_StrLower`→KStrBase.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `setContentSize`→ComboBox.cpp, `create_`→KuiFaceSelector.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp

## `gameui/KuiTopControl.h`
- 97 dòng. class KImmediaItem_
- Gọi tới: `KuiTopControl`→KuiTopControl.cpp, `init`→HelloWorldScene.cpp, `create_`→KuiFaceSelector.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `moveLayer`→KuiBtnControl.cpp, `EndedLayer`→KuiBtnControl.cpp, `upRoleInfo`→KuiFaceSelector.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp

## `gameui/KuiTopchat.cpp`
- 666 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiTopchat`, `KuiTopchat`, `KuiTopchat::create`, `KuiTopchat::mianDialogSet`, `KuiTopchat::init`, `KuiTopchat::addDialogData`, `KuiTopchat::setChatPosition`, `KuiTopchat::Show`, `KuiTopchat::setcoloseButton`, `KuiTopchat::buttonCallBackFunc`, `KuiTopchat::closePopLayer`, `KuiTopchat::getRect`, `KuiTopchat::onTouchBegan`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `getColorIndex`→Text.cpp, `g_Atoui`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `mianDialogSet`→KuiShowSprite.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `Show`→KLittleMap.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `_ccHash`→KStrBase.cpp, `FilterTextColor`→Text.cpp, `g_FileName2Id`→KFilePath.cpp, `g_StrLower`→KStrBase.cpp

## `gameui/KuiTopchat.h`
- 70 dòng. Created by 2018.10 横刀向天笑 QQ:25557432
- Gọi tới: `KuiTopchat`→KuiTopchat.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `mianDialogSet`→KuiShowSprite.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `setChatPosition`→KuiTopchat.cpp, `Show`→KLittleMap.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `gameui/KuiViewRoleState.cpp`
- 606 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiViewRoleState`, `KuiViewRoleState`, `KuiViewRoleState::create`, `KuiViewRoleState::init`, `KuiViewRoleState::addDialogData`, `KuiViewRoleState::setcoloseButton`, `KuiViewRoleState::buttonCallBackFunc`, `KuiViewRoleState::closePopLayer`, `KuiViewRoleState::UpdateAllEquips`, `KuiViewRoleState::addpicBox`, `KuiViewRoleState::layerCallBakc`, `KuiViewRoleState::UpdateEquip`, `KuiViewRoleState::getRect`, `KuiViewRoleState::onTouchBegan`, `KuiViewRoleState::closedescPadCallback`, `KuiViewRoleState::UpdateData`, `KuiViewRoleState::UpdateBaseData`, `KuiViewRoleState::BreatheUpdateInfo`, `KuiViewRoleState::BreathAttributeUpdate`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `GetGameData`→CoreShell.cpp, `setContentSize`→ComboBox.cpp, `findinidata_one`→Kgetinidata.cpp, `UpdateAllEquips`→KuiRoleState.cpp, `UpdateEquip`→KuiRoleState.cpp, `addpicBox`→KuiRoleState.cpp, `ccMessageBox_new`→KCore.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `getDialogPosition`→KuiEffect.cpp, `getDialogSize`→KuiEffect.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `UpdateData`→KuiCometoMap.cpp

## `gameui/KuiViewRoleState.h`
- 94 dòng. virtual void update(float delta);
- Gọi tới: `KuiViewRoleState`→KuiViewRoleState.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `UpdateData`→KuiCometoMap.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `layerCallBakc`→KuiCompoundItem.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `closedescPadCallback`→KuiDynamicShop.cpp, `UpdateAllEquips`→KuiRoleState.cpp

## `gameui/KuiWarnInfo.cpp`
- 1013 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiWarnInfo`, `KuiWarnInfo`, `KuiWarnInfo::ccMessageBox_new`, `KuiWarnInfo::create`, `KuiWarnInfo::init`, `KuiWarnInfo::addDialogData`, `KuiWarnInfo::touchEvent`, `KuiWarnInfo::setcoloseButton`, `KuiWarnInfo::onUpdate`, `KuiWarnInfo::buttonCallBackFunc`, `KuiWarnInfo::closePopLayer`, `KuiWarnInfo::getRect`, `KuiWarnInfo::onTouchEnded`, `KuiWarnInfo::onTouchMoved`, `KuiWarnInfo::onTouchBegan`, `KuiWarnInfo::Run`, `KuiWarnInfo::ProcessAccountLoginResponse`, `KuiWarnInfo::ProcessRoleListResponse`, `KuiWarnInfo::coloseAccServer`, `KuiWarnInfo::ProcessToLoginGameServResponse`, `KuiWarnInfo::sendAccInfoToRelink`, `KuiWarnInfo::EnterGame`, `KuiWarnInfo::AcceptNetMsg`, `KuiWarnInfo::draw`, `KuiWarnInfo::update`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `setBreakTheead`→SocketClient.cpp, `create`→KHRocker.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `Cleanup`→ClientStage.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `setBufferEmpty`→ClientStage.cpp, `ccMessageBox_new`→KCore.cpp, `GetString`→KTabFile.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `g_StrCmp`→KStrBase.cpp, `Load`→KIniFile.cpp, `Clear`→KIniFile.cpp, `GetProtocolSize`→CoreShell.cpp

## `gameui/KuiWarnInfo.h`
- 94 dòng. Created by 2018.10 横刀向天笑 QQ:25557432
- Gọi tới: `KuiWarnInfo`→KuiWarnInfo.cpp, `init`→HelloWorldScene.cpp, `draw`→HelloWorldScene.cpp, `ccMessageBox_new`→KCore.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `sendAccInfoToRelink`→KuiWarnInfo.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `touchEvent`→KuiTalkDialog1.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp

## `gameui/KuiWenGamgItem.cpp`
- 3355 dòng. #include "../engine/KPalette.h"
- Hàm: `KuiWenGamgItem`, `KuiWenGamgItem`, `KuiWenGamgItem::create`, `KuiWenGamgItem::init`, `KuiWenGamgItem::addDialogData`, `KuiWenGamgItem::menuTanCallback`, `KuiWenGamgItem::touchPageBtnEvent`, `KuiWenGamgItem::changePage`, `KuiWenGamgItem::setBtnTouchEnble`, `KuiWenGamgItem::setcoloseButton`, `KuiWenGamgItem::touchOperatioEvent`, `KuiWenGamgItem::closePopLayer`, `KuiWenGamgItem::closeItemPadCallback`, `KuiWenGamgItem::getRectItem`, `KuiWenGamgItem::onTouchEnded`, `KuiWenGamgItem::onTouchMoved`, `KuiWenGamgItem::onTouchBegan`, `KuiWenGamgItem::btnCallBackFunc_quxia`, `KuiWenGamgItem::getPadCondition`, `KuiWenGamgItem::UpdateCurComItem`, `KuiWenGamgItem::update`, `KuiWenGamgItem::draw`, `KuiWenGamgItem::AddObject_UpData`, `KuiWenGamgItem::AddObject_Alts`, `KuiWenGamgItem::AddObject` …(+1)
- Gọi tới: `t_sprintf`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `create`→KHRocker.cpp, `setBtnTouchEnble`→KuiAutoPlay.cpp, `GetName`→KNpcResNode.cpp, `GetID`→KFaction.cpp, `findinidata_one`→Kgetinidata.cpp, `AddObject_UpData`→KuiCompoundItem.cpp, `g_StrLower`→KStrBase.cpp, `changePage`→KuiCompoundItem.cpp, `AddObject`→KuiCompoundItem.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `GetString`→KTabFile.cpp, `OperationRequest`→CoreShell.cpp, `upItemDataUi`→KgameWorld.cpp

## `gameui/KuiWenGamgItem.h`
- 144 dòng. #define FIGHT_SKILL_COUNT_PER_PAGE	25
- Gọi tới: `KuiWenGamgItem`→KuiWenGamgItem.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `UpdateCurComItem`→KuiCompoundItem.cpp, `getPadCondition`→KgameWorld.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closeItemPadCallback`→KgameWorld.cpp, `btnCallBackFunc_quxia`→KuiCompoundItem.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp

## `gameui/Kuiduan.cpp`
- 437 dòng. 有按钮的　ｔａｌｋ　对话框
- Hàm: `Kuiduan`, `Kuiduan`, `Kuiduan::create`, `Kuiduan::init`, `Kuiduan::addDialogData`, `Kuiduan::setcoloseButton`, `Kuiduan::okCallBackFunc`, `Kuiduan::buttonCallBackFunc`, `Kuiduan::closePopLayer`, `Kuiduan::closeItemPadCallback`, `Kuiduan::getRectItem`, `Kuiduan::onTouchEnded`, `Kuiduan::onTouchMoved`, `Kuiduan::onTouchBegan`, `Kuiduan::editBoxEditingDidBegin`, `Kuiduan::editBoxEditingDidEnd`, `Kuiduan::editBoxTextChanged`, `Kuiduan::editBoxReturn`, `Kuiduan::update`, `Kuiduan::draw`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `findinidata_one`→Kgetinidata.cpp, `g_StrLower`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `g_Atoui`→KStrBase.cpp, `Clear`→KIniFile.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `Load`→KIniFile.cpp, `UiSoundPlay_Ui`→UiSoundSetting.cpp, `OperationRequest`→CoreShell.cpp

## `gameui/Kuiduan.h`
- 94 dòng. Created by 横刀向天笑 QQ:25557432
- Gọi tới: `Kuiduan`→Kuiduan.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closeItemPadCallback`→KgameWorld.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `okCallBackFunc`→Kuiduan.cpp, `getRectItem`→KuiCompoundItem.cpp

## `gameui/KuigetMoney.cpp`
- 297 dòng. #include "../engine/KPalette.h"
- Hàm: `KuigetMoney`, `KuigetMoney`, `KuigetMoney::create`, `KuigetMoney::init`, `KuigetMoney::addDialogData`, `KuigetMoney::setcoloseButton`, `KuigetMoney::getmoneyCallBackFunc`, `KuigetMoney::buttonCallBackFunc`, `KuigetMoney::closePopLayer`, `KuigetMoney::getRect`, `KuigetMoney::onTouchBegan`, `KuigetMoney::update`, `KuigetMoney::draw`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `findinidata_one`→Kgetinidata.cpp, `getpicPath`→Kgetinidata.cpp, `g_StrLower`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `setContentSize`→ComboBox.cpp, `OperationRequest`→CoreShell.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `g_Atoui`→KStrBase.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp

## `gameui/KuigetMoney.h`
- 65 dòng. Created by 2018.10 横刀向天笑 QQ:25557432
- Gọi tới: `KuigetMoney`→KuigetMoney.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `editBoxEditingDidBegin`→KgameWorld.cpp, `editBoxEditingDidEnd`→KgameWorld.cpp, `editBoxReturn`→KgameWorld.cpp, `editBoxTextChanged`→KgameWorld.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `getmoneyCallBackFunc`→KuigetMoney.cpp

## `gameui/KuigetStringInUI.cpp`
- 702 dòng. #include "../engine/KPalette.h"
- Hàm: `KuigetStringInUI`, `KuigetStringInUI`, `KuigetStringInUI::create`, `KuigetStringInUI::init`, `KuigetStringInUI::addDialogData`, `KuigetStringInUI::setcoloseButton`, `KuigetStringInUI::_getstringgCallBackFunc`, `KuigetStringInUI::getStringNew`, `KuigetStringInUI::getstringgCallBackFunc`, `KuigetStringInUI::buttonCallBackFunc`, `KuigetStringInUI::closePopLayer`, `KuigetStringInUI::getRect`, `KuigetStringInUI::onTouchBegan`, `KuigetStringInUI::update`, `KuigetStringInUI::draw`, `KuigetStringInUI::editBoxEditingDidBegin`, `KuigetStringInUI::editBoxEditingDidEnd`, `KuigetStringInUI::editBoxTextChanged`, `KuigetStringInUI::editBoxReturn`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `isFileExist`→KgameWorld.cpp, `ccMessageBox_new`→KCore.cpp, `create`→KHRocker.cpp, `g_StrLower`→KStrBase.cpp, `g_FileName2Id`→KFilePath.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `setTitle`→PopupLayer.cpp, `findinidata_one`→Kgetinidata.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `OperationRequest`→CoreShell.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp

## `gameui/KuigetStringInUI.h`
- 78 dòng. Created by 2018.10 横刀向天笑 QQ:25557432
- Gọi tới: `KuigetStringInUI`→KuigetStringInUI.cpp, `editBoxEditingDidBegin`→KgameWorld.cpp, `editBoxEditingDidEnd`→KgameWorld.cpp, `editBoxTextChanged`→KgameWorld.cpp, `editBoxReturn`→KgameWorld.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `getstringgCallBackFunc`→KuigetStringInUI.cpp

## `gameui/Kuigive.cpp`
- 2086 dòng. 有按钮的　ｔａｌｋ　对话框
- Hàm: `Kuigive`, `Kuigive`, `Kuigive::create`, `Kuigive::init`, `Kuigive::addDialogData`, `Kuigive::layerCallBakc`, `Kuigive::setcoloseButton`, `Kuigive::zhengCallBackFunc`, `Kuigive::okCallBackFunc`, `Kuigive::btnCallBackFunc_fangzhi`, `Kuigive::btnCallBackFunc_quxia`, `Kuigive::buttonCallBackFunc`, `Kuigive::closePopLayer`, `Kuigive::closeItemPadCallback`, `Kuigive::getGiveItem`, `Kuigive::getRectItem`, `Kuigive::onTouchBegan`, `Kuigive::UpdateGiveItem`, `Kuigive::UpdateGiveItemData`, `Kuigive::UpdateItem`, `Kuigive::UpdateItemData`, `Kuigive::update`, `Kuigive::draw`, `Kuigive::AddGiveObject`, `Kuigive::AddObject`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `ccMessageBox_new`→KCore.cpp, `GetID`→KFaction.cpp, `findinidata_one`→Kgetinidata.cpp, `GetGameData`→CoreShell.cpp, `g_StrLower`→KStrBase.cpp, `OperationRequest`→CoreShell.cpp, `setContentSize`→ComboBox.cpp, `AddObject`→KuiCompoundItem.cpp, `getColorIndex`→Text.cpp, `g_Atoui`→KStrBase.cpp, `getRectItem`→KuiCompoundItem.cpp, `getDialogPosition`→KuiEffect.cpp, `getDialogSize`→KuiEffect.cpp

## `gameui/Kuigive.h`
- 121 dòng. Created by 横刀向天笑 QQ:25557432
- Gọi tới: `Kuigive`→Kuigive.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `UpdateItem`→KSellItem.cpp, `UpdateGiveItem`→KgameWorld.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `closeItemPadCallback`→KgameWorld.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `btnCallBackFunc_fangzhi`→Kuigive.cpp, `btnCallBackFunc_quxia`→KuiCompoundItem.cpp

## `gameui/Kuilaotou.cpp`
- 284 dòng. (không có chú thích đầu)
- Hàm: `Kuilaotou`, `Kuilaotou`, `Kuilaotou::create`, `Kuilaotou::AddDialogTitle`, `Kuilaotou::init`, `Kuilaotou::addDialogData`, `Kuilaotou::setcoloseButton`, `Kuilaotou::btnCallBackFunc`, `Kuilaotou::buttonCallBackFunc`, `Kuilaotou::closePopLayer`, `Kuilaotou::getRect`, `Kuilaotou::onTouchBegan`, `Kuilaotou::update`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `g_StrLower`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `ccMessageBox_new`→KCore.cpp, `setTitle`→PopupLayer.cpp, `setContentSize`→ComboBox.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `Load`→KIniFile.cpp, `GetString`→KTabFile.cpp, `Clear`→KIniFile.cpp

## `gameui/Kuilaotou.h`
- 64 dòng. Created by 2018.10 横刀向天笑 QQ:25557432
- Gọi tới: `Kuilaotou`→Kuilaotou.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `AddDialogTitle`→Kuilaotou.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `btnCallBackFunc`→KuiEscInfo.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `gameui/Kuiplayerfun.cpp`
- 3854 dòng. (không có chú thích đầu)
- Hàm: `Kuiplayerfun`, `Kuiplayerfun`, `Kuiplayerfun::create`, `Kuiplayerfun::init`, `Kuiplayerfun::addDialogData`, `Kuiplayerfun::checkboxValueChanged`, `Kuiplayerfun::touchPageBtnEvent`, `Kuiplayerfun::setchatCurChannel`, `Kuiplayerfun::setcoloseButton`, `Kuiplayerfun::_removeDelegate`, `Kuiplayerfun::btnCallBackFunc`, `Kuiplayerfun::buttonCallBackFunc`, `Kuiplayerfun::closePopLayer`, `Kuiplayerfun::selectedBoxStateEvent`, `Kuiplayerfun::selectedPlayersListItemEvent`, `Kuiplayerfun::setBtnTouchEnabled`, `Kuiplayerfun::getRect`, `Kuiplayerfun::onTouchEnded`, `Kuiplayerfun::onTouchMoved`, `Kuiplayerfun::onTouchBegan`, `Kuiplayerfun::addchatmsg`, `Kuiplayerfun::finish`, `Kuiplayerfun::closeShowPad`, `Kuiplayerfun::menuNameCallback`, `Kuiplayerfun::menuTtsCallback` …(+28)
- Gọi tới: `setTouchEnabled`→KHRocker - Copy.cpp, `setBtnTouchEnabled`→KuiCometoMap.cpp, `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `ccMessageBox_new`→KCore.cpp, `GetString`→KTabFile.cpp, `setchatCurChannel`→KgameWorld.cpp, `g_StrCmp`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `TeamOperation`→CoreShell.cpp, `setContentSize`→ComboBox.cpp, `IR_GetCurrentTime`→ImgRef.cpp, `OperationRequest`→CoreShell.cpp, `FilterTextColor`→Text.cpp, `TGetColor`→Text.cpp

## `gameui/Kuiplayerfun.h`
- 298 dòng. (không có chú thích đầu)
- Gọi tới: `Kuiplayerfun`→Kuiplayerfun.cpp, `GetChannelIndex`→KgameWorld.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `UpdateData`→KuiCometoMap.cpp, `QueryAllChannel`→KgameWorld.cpp, `ReleaseActivateChannelAll`→Kuiplayerfun.cpp, `PushChannelData`→Kuiplayerfun.cpp, `GetChannelData`→Kuiplayerfun.cpp, `PopChannelData`→Kuiplayerfun.cpp, `_removeDelegate`→KuiAutoPlay.cpp, `GetChannelID`→Kuiplayerfun.cpp, `GetChannelResourceIndex`→Kuiplayerfun.cpp

## `gameui/KuistoreBox.cpp`
- 1149 dòng. #include "../engine/KPalette.h"
- Hàm: `KuistoreBox`, `KuistoreBox`, `KuistoreBox::create`, `KuistoreBox::init`, `KuistoreBox::addDialogData`, `KuistoreBox::setcoloseButton`, `KuistoreBox::zenliCallBackFunc`, `KuistoreBox::diuCallBackFunc`, `KuistoreBox::chuCallBackFunc`, `KuistoreBox::getmoneyCallBackFunc`, `KuistoreBox::closegetmonyPadCallback`, `KuistoreBox::openboxCallBackFunc`, `KuistoreBox::closeItemKuoPadCallback`, `KuistoreBox::buttonCallBackFunc`, `KuistoreBox::closePopLayer`, `KuistoreBox::getRect`, `KuistoreBox::onTouchEnded`, `KuistoreBox::onTouchMoved`, `KuistoreBox::onTouchBegan`, `KuistoreBox::closeItemPadCallback`, `KuistoreBox::update`, `KuistoreBox::UpdateExItem`, `KuistoreBox::AddObject`, `KuistoreBox::selectedItemEvent`, `KuistoreBox::UpdateData` …(+4)
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `g_StrLower`→KStrBase.cpp, `setVisible_e`→KuiEffect.cpp, `GetGameData`→CoreShell.cpp, `ccMessageBox_new`→KCore.cpp, `GetID`→KFaction.cpp, `addChild_e`→KuiEffect.cpp, `Size`→KFile.cpp, `findChildByKey`→KuiEffect.cpp, `UpdateData`→KuiCometoMap.cpp, `clearAllColor`→KuiItemEx.cpp, `upItemColor`→KuiEffect.cpp, `setDialogColor`→KuiEffect.cpp

## `gameui/KuistoreBox.h`
- 108 dòng. virtual void draw(cocos2d::Renderer *renderer, const Mat4 &transform, uint32_t flags);
- Gọi tới: `KuistoreBox`→KuistoreBox.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `UpdateItem`→KSellItem.cpp, `UpdateExItem`→KuistoreBox.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `getmoneyCallBackFunc`→KuigetMoney.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp

## `gameui/KuistoreBox_old.cpp`
- 1261 dòng. #include "../engine/KPalette.h"
- Hàm: `KuistoreBox_old`, `KuistoreBox_old`, `KuistoreBox_old::create`, `KuistoreBox_old::init`, `KuistoreBox_old::addDialogData`, `KuistoreBox_old::setcoloseButton`, `KuistoreBox_old::zenliCallBackFunc`, `KuistoreBox_old::diuCallBackFunc`, `KuistoreBox_old::chuCallBackFunc`, `KuistoreBox_old::getmoneyCallBackFunc`, `KuistoreBox_old::closegetmonyPadCallback`, `KuistoreBox_old::openboxCallBackFunc`, `KuistoreBox_old::closeItemKuoPadCallback`, `KuistoreBox_old::buttonCallBackFunc`, `KuistoreBox_old::closePopLayer`, `KuistoreBox_old::getRect`, `KuistoreBox_old::onTouchEnded`, `KuistoreBox_old::onTouchMoved`, `KuistoreBox_old::onTouchBegan`, `KuistoreBox_old::closeItemPadCallback`, `KuistoreBox_old::update`, `KuistoreBox_old::UpdateExItem`, `KuistoreBox_old::AddObject`, `KuistoreBox_old::UpdateData`, `KuistoreBox_old::UpdateItemOrDer` …(+3)
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `GetID`→KFaction.cpp, `g_StrLower`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `GetGameData`→CoreShell.cpp, `setDialogColor`→KuiEffect.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `UpdateItemOrDer`→KuiItem.cpp, `UpdateData`→KuiCometoMap.cpp, `GetAutoplayid`→CoreShell.cpp, `OperationRequest`→CoreShell.cpp, `onTouchItem`→KuiItem.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp

## `gameui/KuistoreBox_old.h`
- 113 dòng. virtual void draw(cocos2d::Renderer *renderer, const Mat4 &transform, uint32_t flags);
- Gọi tới: `KuistoreBox_old`→KuistoreBox_old.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `UpdateItem`→KSellItem.cpp, `UpdateExItem`→KuistoreBox.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `getmoneyCallBackFunc`→KuigetMoney.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp

## `gameui/Kuitasktrace.cpp`
- 1321 dòng. (không có chú thích đầu)
- Hàm: `Kuitasktrace`, `Kuitasktrace`, `Kuitasktrace::create`, `Kuitasktrace::init`, `Kuitasktrace::getCurVisible`, `Kuitasktrace::setCurVisible`, `Kuitasktrace::getcurSize`, `Kuitasktrace::getcurPosition`, `Kuitasktrace::setCurPosition`, `Kuitasktrace::addDialogData`, `Kuitasktrace::setcoloseButton`, `Kuitasktrace::btnCallBackFunc`, `Kuitasktrace::buttonCallBackFunc`, `Kuitasktrace::closePopLayer`, `Kuitasktrace::selectedBoxStateEvent`, `Kuitasktrace::selectedPlayersListItemEvent`, `Kuitasktrace::getRect`, `Kuitasktrace::onTouchEnded`, `Kuitasktrace::onTouchMoved`, `Kuitasktrace::onTouchBegan`, `Kuitasktrace::Clear`, `Kuitasktrace::addmsgIntolist`, `Kuitasktrace::checkTaskNo`, `Kuitasktrace::closeTaskNoTrace`, `Kuitasktrace::upTaskdata` …(+4)
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `g_StrLower`→KStrBase.cpp, `setContentSize`→ComboBox.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `ClientExeItemScript`→KPlayer.cpp, `getpicPath`→Kgetinidata.cpp, `getColorIndex`→Text.cpp, `g_Atoui`→KStrBase.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `Size`→KFile.cpp, `getcurPosition`→KuiItemImmediaBox.cpp

## `gameui/Kuitasktrace.h`
- 110 dòng. (không có chú thích đầu)
- Gọi tới: `Kuitasktrace`→Kuitasktrace.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `setCurPosition`→KuiSortSkill_l.cpp, `setCurVisible`→Kuitasktrace.cpp, `getCurVisible`→Kuitasktrace.cpp, `getcurPosition`→KuiItemImmediaBox.cpp, `getcurSize`→Kuitasktrace.cpp, `addmsgIntolist`→Kuitasktrace.cpp, `upTaskdata`→Kuitasktrace.cpp, `checkTaskNo`→Kuitasktrace.cpp, `openTaskNoTrace`→Kuitasktrace.cpp, `closeTaskNoTrace`→Kuitasktrace.cpp

## `gameui/PopupLayer.cpp`
- 250 dòng. #include "../engine/KPalette.h"
- Hàm: `PopupLayer`, `PopupLayer::init`, `PopupLayer::onTouchBegan`, `PopupLayer::create`, `PopupLayer::setTitle`, `PopupLayer::setCallbackFunc`, `PopupLayer::onEnter`, `PopupLayer::onExit`, `PopupLayer::update`, `PopupLayer::draw`
- Gọi tới: `create`→KHRocker.cpp, `init`→HelloWorldScene.cpp, `setContentSize`→ComboBox.cpp, `onEnter`→KgameWorld.cpp, `onExit`→KgameWorld.cpp, `ccMessageBox_new`→KCore.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `registerWithTouchDispatcher`→KuiTopControl.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `t_sprintf`→KStrBase.cpp, `g_StrLower`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `buttonCallback`→KgameWorld.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp

## `gameui/PopupLayer.h`
- 69 dòng. PopupLayer.h
- Gọi tới: `PopupLayer`→PopupLayer.cpp, `init`→HelloWorldScene.cpp, `registerWithTouchDispatcher`→KuiTopControl.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `create`→KHRocker.cpp, `setTitle`→PopupLayer.cpp, `setCallbackFunc`→PopupLayer.cpp, `onEnter`→KgameWorld.cpp, `onExit`→KgameWorld.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `buttonCallback`→KgameWorld.cpp

## `gameui/StrokeLabel.cpp`
- 282 dòng. #include "engine/KPalette.h"
- Gọi tới: `init`→HelloWorldScene.cpp, `create_`→KuiFaceSelector.cpp, `create`→KHRocker.cpp, `draw`→HelloWorldScene.cpp

## `gameui/StrokeLabel.h`
- 90 dòng. USING_NS_CC;
- Gọi tới: `init`→HelloWorldScene.cpp, `create_`→KuiFaceSelector.cpp, `draw`→HelloWorldScene.cpp

## `gameui/UiSoundSetting.cpp`
- 115 dòng. ????????
- Hàm: `UiSoundLoadSetting`, `UiSoundPlay_Game`, `UiSoundPlay_Ui`, `UiSoundPlay`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `GetString`→KTabFile.cpp, `__replaceNmae`→KStrBase.cpp, `Load`→KIniFile.cpp, `Clear`→KIniFile.cpp

## `gameui/UiSoundSetting.h`
- 49 dòng. Author	:   Wooy(Wu yue)
- Gọi tới: `UiSoundLoadSetting`→UiSoundSetting.cpp, `UiSoundPlay_Game`→UiSoundSetting.cpp, `UiSoundPlay_Ui`→UiSoundSetting.cpp, `UiSoundPlay`→UiSoundSetting.cpp

## `gameui/Uiglobaldata.cpp`
- 43 dòng. int  nDisPlayMoDel = UI_SDISPLAY_MODEL_800;

## `gameui/Uiglobaldata.h`
- 647 dòng. #if (CC_TARGET_PLATFORM == CC_PLATFORM_ANDROID)

## `gameui/kuiCurlDown.cpp`
- 208 dòng. kuiCurlDown.cpp
- Hàm: `kuiCurlDown::download`, `kuiCurlDown::getLocalFileLength`

## `gameui/kuiCurlDown.h`
- 95 dòng. CurlDown.h
- Gọi tới: `download`→kuiCurlDown.cpp, `getLocalFileLength`→kuiCurlDown.cpp

## `gameui/uiSkill.cpp`
- 306 dòng. #include "../engine/KPalette.h"
- Hàm: `uiskill`, `uiskill::init`, `uiskill::onTouchBegan`, `uiskill::create`, `uiskill::setTitle`, `uiskill::setCallbackFunc`, `uiskill::onEnter`, `uiskill::onExit`, `uiskill::update`, `uiskill::draw`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `init`→HelloWorldScene.cpp, `setContentSize`→ComboBox.cpp, `g_StrLower`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `onEnter`→KgameWorld.cpp, `onExit`→KgameWorld.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `registerWithTouchDispatcher`→KuiTopControl.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `GetGameData`→CoreShell.cpp, `GetSkill`→KSkillManager.h, `DrawSkillIcon`→KSkills.cpp

## `gameui/uiSkill.h`
- 71 dòng. 需要重写触摸注册函数，重新给定触摸级别
- Gọi tới: `uiskill`→uiSkill.cpp, `init`→HelloWorldScene.cpp, `registerWithTouchDispatcher`→KuiTopControl.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `create`→KHRocker.cpp, `setTitle`→PopupLayer.cpp, `setCallbackFunc`→PopupLayer.cpp, `onEnter`→KgameWorld.cpp, `onExit`→KgameWorld.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `buttonCallback`→KgameWorld.cpp

## `manager/SoundManager.cpp`
- 324 dòng. #include "../common/MShare.h"
- Hàm: `SoundManager::GetInstance`, `SoundManager::Init`, `SoundManager`, `SoundManager`, `SoundManager::PlaySound`, `SoundManager::MyPlaySound`, `SoundManager::MyStopSound`, `SoundManager::LoadSoundList`, `SoundManager::AddSound`, `SoundManager::ReleaseSound`
- Gọi tới: `update`→KgameWorld.cpp, `isFileExist`→KgameWorld.cpp, `Init`→KCache.cpp, `__replaceNmae`→KStrBase.cpp, `GetInstance`→KgameWorld.cpp, `init`→HelloWorldScene.cpp, `PlaySound`→KMissleRes.cpp, `g_isFileExist`→KStrBase.cpp

## `manager/SoundManager.h`
- 226 dòng. #include "fmod.hpp"
- Gọi tới: `SoundManager`→SoundManager.cpp, `GetInstance`→KgameWorld.cpp, `Init`→KCache.cpp, `PlaySound`→KMissleRes.cpp, `MyPlaySound`→SoundManager.cpp, `MyStopSound`→SoundManager.cpp, `LoadSoundList`→SoundManager.cpp, `AddSound`→SoundManager.cpp, `ReleaseSound`→SoundManager.cpp

## `manager/common.cpp`
- 109 dòng. (không có chú thích đầu)
- Hàm: `ERRCHECK_fn`, `Common_Format`, `Common_Fatal`, `Common_Draw`
- Gọi tới: `Common_BtnStr`→common_platform.cpp, `Common_Update`→common_platform.cpp, `Common_Sleep`→common_platform.cpp, `Common_BtnPress`→common_platform.cpp, `Common_Exit`→common_platform.cpp, `Common_DrawText`→common_platform.cpp

## `manager/common.h`
- 78 dòng. (không có chú thích đầu)
- Gọi tới: `ERRCHECK_fn`→common.cpp, `Common_Format`→common.cpp, `Common_Fatal`→common.cpp, `Common_Draw`→common.cpp, `Common_Init`→common_platform.cpp, `Common_Close`→common_platform.cpp, `Common_Update`→common_platform.cpp, `Common_Sleep`→common_platform.cpp, `Common_Exit`→common_platform.cpp, `Common_DrawText`→common_platform.cpp, `Common_LoadFileMemory`→common_platform.cpp, `Common_UnloadFileMemory`→common_platform.cpp, `Common_BtnPress`→common_platform.cpp, `Common_BtnDown`→common_platform.cpp, `Common_BtnStr`→common_platform.cpp

## `manager/common_platform.cpp`
- 209 dòng. (không có chú thích đầu)
- Hàm: `Common_Init`, `Common_Close`, `Common_Update`, `Common_Sleep`, `Common_Exit`, `Common_DrawText`, `Common_LoadFileMemory`, `Common_UnloadFileMemory`, `Common_BtnPress`, `Common_BtnDown`, `Common_BtnStr`, `Common_MediaPath`, `Common_WritePath`, `Common_SuspendState`, `Java_org_fmod_example_MainActivity_getButtonLabel`, `Java_org_fmod_example_MainActivity_buttonDown`, `Java_org_fmod_example_MainActivity_buttonUp`, `Java_org_fmod_example_MainActivity_setStateCreate`, `Java_org_fmod_example_MainActivity_setStateStart`, `Java_org_fmod_example_MainActivity_setStateStop`, `Java_org_fmod_example_MainActivity_setStateDestroy`, `Java_org_fmod_example_MainActivity_main`
- Gọi tới: `FMOD_Main`→play_sound.cpp

## `manager/common_platform.h`
- 45 dòng. (không có chú thích đầu)
- Hàm: `Common_Mutex_Create`, `Common_Mutex_Destroy`, `Common_Mutex_Enter`, `Common_Mutex_Leave`
- Gọi tới: `Common_SuspendState`→common_platform.cpp

## `manager/play_sound.cpp`
- 158 dòng. (không có chú thích đầu)
- Hàm: `FMOD_Main`
- Gọi tới: `Common_Draw`→common.cpp, `Common_BtnPress`→common_platform.cpp, `Common_BtnStr`→common_platform.cpp, `Common_MediaPath`→common_platform.cpp, `Common_Init`→common_platform.cpp, `Common_Fatal`→common.cpp, `init`→HelloWorldScene.cpp, `Common_Update`→common_platform.cpp, `update`→KgameWorld.cpp, `Common_Sleep`→common_platform.cpp, `Common_Close`→common_platform.cpp

## `network/Cipher.h`
- 31 dòng. ProtocolType same as s2c_accountbegin in the protocol.h file

## `network/ClientStage.cpp`
- 411 dòng. CException;
- Hàm: `_Rand`, `RandMemSet`, `CGameClient`, `CGameClient::Startup`, `CGameClient::Cleanup`, `CGameClient::SendMsg`, `CGameClient::GetPackFromServer`, `CGameClient::setBufferEmpty`, `CGameClient::Shutdown`, `CGameClient::QueryInterface`, `CGameClient::AddRef`, `CGameClient::Release`, `CGameClient::ProcessCommand`, `CGameClient::GetMinimumMessageSize`, `CGameClient::GetMessageSize`, `CGameClient::ProcessDataStream`, `CGameClient::OnStartConnections`, `CGameClient::OnShutdownInitiated`, `CGameClient::OnShutdownComplete`, `CGameClient::OnStopConnections`, `CGameClient::ReadCompleted`, `CClientFactory`, `CClientFactory::AddRef`, `CClientFactory::Release`
- Gọi tới: `AddData`→KObjSet.cpp, `Release`→KCache.cpp, `Empty`→IOBuffer.cpp, `GetBuffer`→KLubCmpl_Blocker.cpp, `StopConnections`→SocketClient.cpp, `Allocate`→IOBuffer.cpp, `_Rand`→KCore.h, `RandMemSet`→KCore.h, `WaitForShutdownToComplete`→SocketClient.cpp, `KSG_EncodeBuf`→KSG_EncodeDecode.h, `AddRef`→KRegion.cpp, `KSG_DecodeBuf`→KSG_EncodeDecode.h, `ccMessageBox_new`→KCore.cpp, `CSocketClient`→SocketClient.cpp, `Start`→KTimer.cpp

## `network/ClientStage.h`
- 101 dòng. #include "tstring.h"
- Gọi tới: `CGameClient`→ClientStage.cpp, `AddRef`→KRegion.cpp, `Release`→KCache.cpp, `CClientFactory`→ClientStage.cpp, `Startup`→ClientStage.cpp, `Cleanup`→ClientStage.cpp, `SendMsg`→ClientStage.cpp, `GetPackFromServer`→ClientStage.cpp, `Shutdown`→ClientStage.cpp, `setBufferEmpty`→ClientStage.cpp, `QueryInterface`→ClientStage.cpp, `GetMessageSize`→ClientStage.cpp, `GetMinimumMessageSize`→ClientStage.cpp, `ProcessDataStream`→ClientStage.cpp, `ProcessCommand`→ClientStage.cpp

## `network/CriticalSection.cpp`
- 67 dòng. ::InitializeCriticalSection( &m_crit );
- Hàm: `CCriticalSection`, `CCriticalSection`, `CCriticalSection::Enter`, `CCriticalSection::Leave`, `CCriticalSection::TryEnter`, `Owner::~Owner`

## `network/CriticalSection.h`
- 136 dòng. #include "Utils.h"
- Hàm: `CCriticalSection::Enter`, `CCriticalSection::Leave`, `CCriticalSection::CCriticalSection`, `CCriticalSection::~CCriticalSection`, `CCriticalSection::TryEnter`, `Owner::~Owner`
- Gọi tới: `CCriticalSection`→CriticalSection.cpp, `Enter`→CriticalSection.cpp, `Leave`→CriticalSection.cpp, `TryEnter`→CriticalSection.cpp

## `network/Event.cpp`
- 137 dòng. (không có chú thích đầu)
- Hàm: `CEvent`, `CEvent::CreateEvent`, `CEvent::EnsureInitialized`, `CEvent::Set`, `CEvent::Reset`, `CEvent::Wait`
- Gọi tới: `CreateEvent`→KScenePlaceC.cpp, `Reset`→KTimer.cpp

## `network/Event.h`
- 164 dòng. stdio.h 如果没有这个头文件 会出现一些错误 意外类型的xxx 意思就是没有这个类型的 声明
- Hàm: `CEvent`, `CEvent::CreateEvent`, `CEvent::EnsureInitialized`, `CEvent::Set`, `CEvent::Reset`, `CEvent::Wait`
- Gọi tới: `EnsureInitialized`→Event.cpp, `CEvent`→Event.cpp, `CreateEvent`→KScenePlaceC.cpp, `Reset`→KTimer.cpp, `Wait`→Event.cpp

## `network/IOBuffer.cpp`
- 383 dòng. #include "stdafx.h"
- Hàm: `CIOBuffer`, `CIOBuffer::Empty`, `CIOBuffer::SplitBuffer`, `CIOBuffer::RemoveBuffer`, `CIOBuffer::AllocateNewBuffer`, `CIOBuffer::AddData`, `CIOBuffer::AddData`, `CIOBuffer::AddData`, `CIOBuffer::Release`, `Allocator::~Allocator`, `Allocator::Allocate`, `Allocator::Release`, `Allocator::DestroyBuffer`, `Allocator::Flush`, `InOrderBufferList::AddBuffer`, `InOrderBufferList::ProcessAndGetNext`, `InOrderBufferList::GetNext`, `InOrderBufferList::GetNext`, `InOrderBufferList::ProcessBuffer`, `InOrderBufferList::Reset`
- Gọi tới: `AddData`→KObjSet.cpp, `Release`→KCache.cpp, `PopNode`→NodeList.cpp, `PushNode`→NodeList.cpp, `GetNext`→KNode.h, `AddRef`→KRegion.cpp, `RemoveFromList`→NodeList.cpp, `Reset`→KTimer.cpp

## `network/IOBuffer.h`
- 273 dòng. Identifier was truncated to '255' characters
- Hàm: `CIOBuffer::ConsumeAndRemove`, `CIOBuffer::SetupZeroByteRead`, `CIOBuffer::SetupRead`, `CIOBuffer::SetupWrite`
- Gọi tới: `AddData`→KObjSet.cpp, `CIOBuffer`→IOBuffer.cpp, `Empty`→IOBuffer.cpp, `Release`→KCache.cpp, `GetNext`→KNode.h, `GetBuffer`→KLubCmpl_Blocker.cpp, `SplitBuffer`→IOBuffer.cpp, `RemoveBuffer`→IOBuffer.cpp, `AllocateNewBuffer`→IOBuffer.cpp, `AddRef`→KRegion.cpp, `Allocate`→IOBuffer.cpp, `Flush`→IOBuffer.cpp, `DestroyBuffer`→IOBuffer.cpp, `AddBuffer`→IOBuffer.cpp, `ProcessBuffer`→IOBuffer.cpp

## `network/KSG_EncodeDecode.cpp`
- 116 dòng. Version     :   1.0
- Hàm: `KSG_DecodeEncode`, `KSG_DecodeEncode_ASM`, `KSG_DecodeEncode_New`

## `network/KSG_EncodeDecode.h`
- 48 dòng. Version     :   1.0
- Hàm: `KSG_DecodeBuf`, `KSG_EncodeBuf`
- Gọi tới: `KSG_DecodeEncode`→KSG_EncodeDecode.cpp, `KSG_DecodeEncode_ASM`→KSG_EncodeDecode.cpp, `KSG_DecodeEncode_New`→KSG_EncodeDecode.cpp

## `network/NodeList.cpp`
- 123 dòng. #include "stdafx.h"
- Hàm: `CNodeList::PushNode`, `CNodeList::PopNode`, `CNodeList::RemoveNode`, `Node::~Node`, `Node::AddToList`, `Node::RemoveFromList`, `Node::Unlink`
- Gọi tới: `Next`→NodeList.h

## `network/NodeList.h`
- 126 dòng. #include <wtypes.h>
- Hàm: `Node::Next`, `PopNode`, `Head`, `Next`
- Gọi tới: `PopNode`→NodeList.cpp, `RemoveFromList`→NodeList.cpp, `AddToList`→NodeList.cpp, `Unlink`→NodeList.cpp, `PushNode`→NodeList.cpp, `Empty`→IOBuffer.cpp, `RemoveNode`→NodeList.cpp

## `network/Socket.cpp`
- 188 dòng. #include "Macro.h"
- Hàm: `CSocket`, `CSocket::Attach`, `CSocket::Detatch`, `CSocket::Close`, `CSocket::AbortiveClose`, `CSocket::Shutdown`, `CSocket::Listen`, `CSocket::Bind`, `CSocket::Bind`, `CSocket::Connect_`, `CSocket::Connect`, `CSocket::Connect`, `InternetAddress::InternetAddress`
- Gọi tới: `Close`→KFile.cpp, `ccMessageBox_new`→KCore.cpp, `Shutdown`→ClientStage.cpp

## `network/Socket.h`
- 112 dòng. typedef int  socklen_t;
- Gọi tới: `CSocket`→Socket.cpp, `Bind`→Socket.cpp, `Connect`→Socket.cpp, `InternetAddress`→Socket.cpp, `Attach`→Socket.cpp, `Detatch`→Socket.cpp, `Close`→KFile.cpp, `AbortiveClose`→Socket.cpp, `Shutdown`→ClientStage.cpp, `Listen`→Socket.cpp, `Connect_`→Socket.cpp

## `network/SocketClient.cpp`
- 575 dòng. #include "stdafx.h"
- Hàm: `_CreateEvent`, `WaitForSingleObject`, `CSocketClient`, `CSocketClient::StartConnections`, `CSocketClient::StopConnections`, `CSocketClient::InitiateShutdown`, `CSocketClient::WaitForShutdownToComplete`, `CSocketClient::setBreakTheead`, `CSocketClient::Run`, `CSocketClient::ReleaseBuffers`, `CSocketClient::OnError`, `CSocketClient::OnRead`, `CSocketClient::Write`, `CSocketClient::Write`, `CSocketClient::WaitAndVerifyCipher`, `CSocketClient::_wait`, `CSocketClient::_get_error_status`
- Gọi tới: `ccMessageBox_new`→KCore.cpp, `Terminate`→KScenePlaceC.cpp, `OnStartConnections`→ClientStage.cpp, `Write`→KFile.cpp, `CUsesWinsock`→UsesWinsock.cpp, `Connect`→Socket.cpp, `OnStopConnections`→ClientStage.cpp, `t_sprintf`→KStrBase.cpp, `Connect_`→Socket.cpp, `Allocate`→IOBuffer.cpp, `Release`→KCache.cpp, `CEvent`→Event.cpp, `CreateEvent`→KScenePlaceC.cpp, `WaitForSingleObject`→KScenePlaceC.cpp, `Wait`→Event.cpp

## `network/SocketClient.h`
- 134 dòng. #include "UsesWinsock.h"
- Gọi tới: `CSocketClient`→SocketClient.cpp, `Write`→KFile.cpp, `setBreakTheead`→SocketClient.cpp, `Connect`→Socket.cpp, `StartConnections`→SocketClient.cpp, `StopConnections`→SocketClient.cpp, `InitiateShutdown`→SocketClient.cpp, `WaitForShutdownToComplete`→SocketClient.cpp, `ReleaseBuffers`→SocketClient.cpp, `WaitAndVerifyCipher`→SocketClient.cpp, `OnStartConnections`→ClientStage.cpp, `OnStopConnections`→ClientStage.cpp, `OnShutdownInitiated`→ClientStage.cpp, `OnShutdownComplete`→ClientStage.cpp, `OnRead`→SocketClient.cpp

## `network/Thread.cpp`
- 240 dòng. #include "stdafx.h"
- Hàm: `CThread`, `CThread::GetHandle`, `CThread::Start`, `CThread::Wait`, `CThread::Wait`, `CThread::ThreadFunction`, `CThread::Terminate`, `CThread`, `CThread::GetHandle`, `CThread::setAutoDelete`, `CThread::ThreadFunction`, `CThread::Start`, `CThread::Terminate`, `CThread::Wait`, `CThread::Wait`
- Gọi tới: `Wait`→Event.cpp, `Terminate`→KScenePlaceC.cpp, `CloseHandle`→KScenePlaceC.cpp, `Start`→KTimer.cpp, `WaitForSingleObject`→KScenePlaceC.cpp

## `network/Thread.h`
- 108 dòng. namespace OnlineGameLib::Win32
- Gọi tới: `CThread`→Thread.cpp, `Wait`→Event.cpp, `GetHandle`→Thread.cpp, `Start`→KTimer.cpp, `Terminate`→KScenePlaceC.cpp, `ThreadFunction`→Thread.cpp, `setAutoDelete`→Thread.cpp

## `network/UsesWinsock.cpp`
- 20 dòng. #include "stdafx.h"
- Hàm: `CUsesWinsock`, `CUsesWinsock`

## `network/UsesWinsock.h`
- 34 dòng. No copies do not implement
- Gọi tới: `CUsesWinsock`→UsesWinsock.cpp

## `tools/ZipArchive--.cpp`
- 230 dòng. (không có chú thích đầu)
- Hàm: `ZipArchive`, `ZipArchive`, `ZipArchive::startDecompression`, `ZipArchive::decompress`, `ZipArchive::getCurProgress`, `ZipArchive::basename`

## `tools/ZipArchive--.h`
- 28 dòng. (không có chú thích đầu)
- Gọi tới: `ZipArchive`→ZipArchive--.cpp, `startDecompression`→ZipArchive--.cpp, `decompress`→ZipArchive--.cpp, `getCurProgress`→ZipArchive--.cpp, `basename`→ZipArchive--.cpp

## `vn/KTest.cpp`
- 148 dòng. Print useful error message instead of segfaulting when files are not there.
- Hàm: `KTest::createScene`, `problemLoading`, `KTest::init`, `KTest::menuCloseCallback`, `KTest::onTouchesBegan`
- Gọi tới: `create`→KHRocker.cpp, `problemLoading`→HelloWorldScene.cpp, `init`→HelloWorldScene.cpp, `createScene`→HelloWorldScene.cpp, `t_sprintf`→KStrBase.cpp, `FilterTextColor`→Text.cpp, `menuCloseCallback`→HelloWorldScene.cpp, `onTouchesBegan`→HelloWorldScene.cpp

## `vn/KTest.h`
- 158 dòng. (không có chú thích đầu)
- Hàm: `_code_convert`, `utf_tcvn`, `tcvn_gbk`
- Gọi tới: `gbk2utf8_`→KGbktoUtf8.h, `gbk2utf8`→KGbktoUtf8.h, `createScene`→HelloWorldScene.cpp, `init`→HelloWorldScene.cpp, `onTouchesBegan`→HelloWorldScene.cpp, `menuCloseCallback`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `utf2gbk_`→KGbktoUtf8.h, `utf2gbk`→KGbktoUtf8.h, `utf2tcvn`→KGbktoUtf8.h

## `vn/Translate.cpp`
- 202 dòng. Bản đồ sửa hiển thị sai → đúng theo người dùng nhìn
- Hàm: `UTF8To8859_1`

## `vn/Translate.h`
- 15 dòng. translateChinaToUTF8
- Gọi tới: `UTF8To8859_1`→Translate.cpp

## `vn/extensions/2d/CCMenu.cpp`
- 192 dòng. (không có chú thích đầu)
- Hàm: `MenuVN::create`, `MenuVN::onTouchBegan`, `MenuVN::onTouchEnded`
- Gọi tới: `create`→KHRocker.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp

## `vn/extensions/2d/CCMenu.h`
- 137 dòng. Menu state, it's used internally.
- Gọi tới: `create`→KHRocker.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp

## `vn/gamecore/ConnectionStatus.h`
- 86 dòng. InternetStatus.hpp

## `vn/gamecore/Connectivity.h`
- 30 dòng. Connectivity.h

## `vn/gamecore/KCoreVN.cpp`
- 483 dòng. 111<img=222.spr>333<img=444.spr>123456
- Hàm: `CustomRichLabel`, `MoneyDescType`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `GetStringByKeyFromFile`→CXmlStream.cpp, `getColorIndex`→Text.cpp, `g_Atoui`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `g_StrLower`→KStrBase.cpp

## `vn/gamecore/KCoreVN.h`
- 57 dòng. Small Towns
- Gọi tới: `CustomRichLabel`→KCoreVN.cpp, `MoneyDescType`→KCoreVN.cpp

## `vn/gamecore/KNpcResVN.cpp`
- 726 dòng. Created by FongKieu on 1/4/2022.
- Hàm: `KNpcResVN::Draw`
- Gọi tới: `getIniDataForGame`→KgameWorld.cpp, `GetNextFrame`→KSprControl.cpp, `SetCurFrame`→KSprControl.cpp, `DrawPrimitives`→KgameWorld.cpp, `CheckExist`→KSprControl.h, `SetCurDir64`→KSprControl.cpp, `DrawPrimitives_State`→KgameWorld.cpp, `CheckEnd`→KSprControl.cpp, `Release`→KCache.cpp, `IsPlayer`→KNpc.cpp, `Draw`→KLittleMap.cpp, `ChangeCurFrame`→KSprControl.cpp, `GetSoundName`→KNpcRes.cpp, `PlaySound`→KMissleRes.cpp, `GetnSort`→KNpcResNode.cpp

## `vn/gamecore/KNpcResVN.h`
- 17 dòng. Created by FongKieu on 1/4/2022.
- Gọi tới: `Draw`→KLittleMap.cpp

## `vn/gamescence/KScenePlaceCVN.cpp`
- 746 dòng. ##ModelId=3DD17A770383
- Hàm: `GetXYZ`, `KScenePlaceCVN`, `KScenePlaceCVN`, `KScenePlaceCVN::LoadDataMap`, `KScenePlaceCVN::__distance`, `KScenePlaceCVN::__distance`, `KScenePlaceCVN::MoveTo`, `KScenePlaceCVN::LoadNode`, `KScenePlaceCVN::PharseNode`, `KScenePlaceCVN::PharseNodeAI`, `KScenePlaceCVN::IsCity`, `KScenePlaceCVN::GetCurNode`, `KScenePlaceCVN::GetNextNode`, `KScenePlaceCVN::__getheight`, `KScenePlaceCVN::IsLagMoving`, `KScenePlaceCVN::NearestDriver`, `KScenePlaceCVN::Dijkstra`, `KScenePlaceCVN::RunningToPos`, `KScenePlaceCVN::RunningToPos`, `KScenePlaceCVN::RunningToPos`, `KScenePlaceCVN::UseTHP`, `KScenePlaceCVN::ClickToNpc`, `KScenePlaceCVN::CheckBarrier`
- Gọi tới: `OperationRequest`→CoreShell.cpp, `GetFocusPosition`→KScenePlaceC.cpp, `checkPos`→KScenePlaceC.cpp, `ResetAuto`→KuiAutoPlay.cpp, `SendSerCommand`→KNpc.cpp, `SendClientCmdRun`→KProtocol.cpp, `reSet`→AutoPathFinder.cpp, `getFaceBook`→AutoPathFinder.cpp, `setFaceBookState`→AutoPathFinder.cpp, `UseTHP`→KuiAutoPlay.cpp, `IsSectionExist`→KIniFile.cpp, `Load`→KIniFile.cpp, `GetString`→KTabFile.cpp, `LoadNode`→KScriptCache.cpp, `t_sprintf`→KStrBase.cpp

## `vn/gamescence/KScenePlaceCVN.h`
- 77 dòng. (không có chú thích đầu)
- Gọi tới: `KScenePlaceCVN`→KScenePlaceCVN.cpp, `__distance`→KScenePlaceCVN.cpp, `RunningToPos`→KScenePlaceCVN.cpp, `ClickToNpc`→KScenePlaceCVN.cpp, `MoveTo`→KScenePlaceCVN.cpp, `LoadNode`→KScriptCache.cpp, `PharseNode`→KScenePlaceCVN.cpp, `PharseNodeAI`→KScenePlaceCVN.cpp, `IsCity`→KScenePlaceCVN.cpp, `GetCurNode`→KScenePlaceCVN.cpp, `GetNextNode`→KScenePlaceCVN.cpp, `__getheight`→KScenePlaceCVN.cpp, `IsLagMoving`→KScenePlaceCVN.cpp, `UseTHP`→KuiAutoPlay.cpp, `NearestDriver`→KScenePlaceCVN.cpp

## `vn/gamescence/KUpdateLayerVN.cpp`
- 428 dòng. android
- Hàm: `KUpdateLayerVN::init`, `KUpdateLayerVN::loadSuccess`, `KUpdateLayerVN::checkGameVersion`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `Clear`→KIniFile.cpp, `ccMessageBox_new`→KCore.cpp, `SimplyDecrypt`→dataChecksum.cpp, `Load`→KIniFile.cpp, `GetStringByKeyFromFile`→CXmlStream.cpp, `init`→HelloWorldScene.cpp, `GetInteger`→KTabFile.cpp, `copyData`→KgameWorld.cpp, `setContentSize`→ComboBox.cpp, `GetStringByKeyFromFile_old`→CXmlStream.cpp, `UiSoundLoadSetting`→UiSoundSetting.cpp, `scene`→KgameWorld.cpp, `Size`→KFile.cpp

## `vn/gamescence/KUpdateLayerVN.h`
- 50 dòng. Date:	2021.09.18
- Gọi tới: `create`→KHRocker.cpp, `init`→HelloWorldScene.cpp, `scene`→KgameWorld.cpp, `loadSuccess`→Klogin.cpp, `checkGameVersion`→KUpdateLayerVN.cpp

## `vn/gamescence/KgameWorldVN.cpp`
- 7135 dòng. #include <gameui/PopupLayer.h>
- Hàm: `KgameWorldVN::init`, `KgameWorldVN::draw`, `KgameWorldVN::DrawPrimitives_minmap`, `KgameWorldVN::playerfunCallback`, `KgameWorldVN::ActiveAuto`, `KgameWorldVN::setAutoButtonBlink`, `KgameWorldVN::setchatCurChannel`, `KgameWorldVN::hideListBoxMenu`, `KgameWorldVN::hidechatCallback`, `KgameWorldVN::autoCallback_`, `KgameWorldVN::mMessageCallback`, `KgameWorldVN::mMessageCallback`, `KgameWorldVN::update`, `KgameWorldVN::custom_update`, `KgameWorldVN::onTouchesEnded`, `KgameWorldVN::onsendCallback`, `KgameWorldVN::DrawPrimitives_NpcOther`, `KgameWorldVN::MSNMessageArrival`, `KgameWorldVN::isTouchInSpecificArea`, `KUiPlayerBar`, `KUiPlayerBar`, `KUiPlayerBar::init`, `KUiPlayerBar::mQizCallback`, `KUiPlayerBar::mItemsCallback`, `KUiPlayerBar::closeItemPadCallback` …(+1)
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `Size`→KFile.cpp, `setContentSize`→ComboBox.cpp, `UiSoundPlay_Ui`→UiSoundSetting.cpp, `ccMessageBox_new`→KCore.cpp, `GetInteger`→KTabFile.cpp, `_removeDelegate`→KuiAutoPlay.cpp, `GetString`→KTabFile.cpp, `g_StrLower`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `isFileExist`→KgameWorld.cpp, `OperationRequest`→CoreShell.cpp, `AddMember`→KPlayerTeam.cpp

## `vn/gamescence/KgameWorldVN.h`
- 241 dòng. Created by 2018.10 ºáµ¶ÏòÌìÐ¦ QQ:25557432
- Gọi tới: `init`→HelloWorldScene.cpp, `KUiPlayerBar`→KgameWorldVN.cpp, `mOptionsCallback`→KgameWorld.cpp, `mItemsCallback`→KgameWorld.cpp, `mQizCallback`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `scene`→KgameWorld.cpp, `_quitGame`→KgameWorld.cpp, `ccMessageBox_new`→KCore.cpp, `update`→KgameWorld.cpp, `DrawPrimitives_minmap`→KgameWorld.cpp, `setchatDelegate`→KgameWorld.cpp, `OpenCreatTongSheet`→KgameWorld.cpp, `closeTongSheetPadCallback`→KgameWorld.cpp, `mMessageCallback`→KgameWorldVN.cpp

## `vn/gamescence/KgameWorldVN__.cpp`
- 8135 dòng. #include <gameui/PopupLayer.h>
- Hàm: `KgameWorldVN::init`, `KgameWorldVN::draw`, `KgameWorldVN::DrawPrimitives_minmap`, `KgameWorldVN::playerfunCallback`, `KgameWorldVN::setchatCurChannel`, `KgameWorldVN::hideListBoxMenu`, `KgameWorldVN::hidechatCallback`, `KgameWorldVN::ActiveAuto`, `KgameWorldVN::autoCallback_`, `KgameWorldVN::mMessageCallback`, `KgameWorldVN::update`, `KgameWorldVN::custom_update`, `KgameWorldVN::onTouchesEnded`, `KgameWorldVN::onsendCallback`, `KgameWorldVN::DrawPrimitives_NpcOther`, `KgameWorldVN::MSNMessageArrival`, `KgameWorldVN::isTouchInSpecificArea`, `KUiPlayerBar`, `KUiPlayerBar`, `KUiPlayerBar::init`, `KUiPlayerBar::mItemsCallback`, `KUiPlayerBar::closeItemPadCallback`, `KUiPlayerBar::closeescPadCallback`, `KUiPlayerBar::ActiveAuto`, `KUiPlayerBar::mMessageCallback` …(+4)
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `UiSoundPlay_Ui`→UiSoundSetting.cpp, `ccMessageBox_new`→KCore.cpp, `Size`→KFile.cpp, `setContentSize`→ComboBox.cpp, `GetInteger`→KTabFile.cpp, `_removeDelegate`→KuiAutoPlay.cpp, `findinidata_one`→Kgetinidata.cpp, `GetString`→KTabFile.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `g_StrLower`→KStrBase.cpp, `UpdateItem`→KSellItem.cpp, `Clear`→KIniFile.cpp, `OperationRequest`→CoreShell.cpp

## `vn/gamescence/KgameWorldVN__.h`
- 301 dòng. Created by 2018.10 ºáµ¶ÏòÌìÐ¦ QQ:25557432
- Gọi tới: `init`→HelloWorldScene.cpp, `KUiPlayerBar`→KgameWorldVN.cpp, `_quitGame`→KgameWorld.cpp, `ccMessageBox_new`→KCore.cpp, `DrawPrimitives_minmap`→KgameWorld.cpp, `mMessageCallback`→KgameWorldVN.cpp, `UpdateItem`→KSellItem.cpp, `custom_update`→KuiMinMap.cpp, `mOptionsCallback`→KgameWorld.cpp, `mItemsCallback`→KgameWorld.cpp, `mSkillsCallback`→KgameWorld.cpp, `mQizCallback`→KgameWorld.cpp, `mRoleStatusCallback`→KgameWorld.cpp, `mTaskCallback`→KgameWorld.cpp, `mTeamCallback`→KgameWorld.cpp

## `vn/gameui/CCLayerUI.cpp`
- 25 dòng. (không có chú thích đầu)
- Hàm: `CCLayerUI`, `CCLayerUI`, `CCLayerUI::init`
- Gọi tới: `init`→HelloWorldScene.cpp

## `vn/gameui/CCLayerUI.h`
- 26 dòng. Created by 2018.10 横刀向天笑 QQ:25557432
- Gọi tới: `CCLayerUI`→CCLayerUI.cpp, `init`→HelloWorldScene.cpp

## `vn/gameui/KTranSenceVN.cpp`
- 35 dòng. extern KImageStore2 m_ImageStore; //??????
- Hàm: `KTranSenceVN::scene`, `KTranSenceVN::loadSuccess`
- Gọi tới: `scene`→KgameWorld.cpp, `create`→KHRocker.cpp, `loadSuccess`→Klogin.cpp

## `vn/gameui/KTranSenceVN.h`
- 19 dòng. ��½���桡�����ʺ�����
- Gọi tới: `scene`→KgameWorld.cpp, `loadSuccess`→Klogin.cpp

## `vn/gameui/KloginVN.cpp`
- 475 dòng. 'scene' is an autorelease object
- Hàm: `KloginVN::scene`, `KloginVN::init`, `KloginVN::mianCancelCallback`, `KloginVN::mianLoginCallback`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `ccMessageBox_new`→KCore.cpp, `g_StrLower`→KStrBase.cpp, `isFileExist`→KgameWorld.cpp, `scene`→KgameWorld.cpp, `Load`→KIniFile.cpp, `Clear`→KIniFile.cpp, `GetString`→KTabFile.cpp, `GetInteger`→KTabFile.cpp, `g_FileName2Id`→KFilePath.cpp, `getpicPath`→Kgetinidata.cpp, `init`→HelloWorldScene.cpp, `Cleanup`→ClientStage.cpp, `setBreakTheead`→SocketClient.cpp

## `vn/gameui/KloginVN.h`
- 30 dòng. Date:	2021.09.18
- Gọi tới: `scene`→KgameWorld.cpp, `init`→HelloWorldScene.cpp, `mianCancelCallback`→Klogin.cpp, `mianLoginCallback`→Klogin.cpp, `loadSuccess`→Klogin.cpp

## `vn/gameui/Klogin_f_VN.cpp`
- 465 dòng. 'scene' is an autorelease object
- Hàm: `Klogin_f_VN::scene`, `Klogin_f_VN::init`, `Klogin_f_VN::mianLoginCallback`, `Klogin_f_VN::mianCancelCallback`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `isFileExist`→KgameWorld.cpp, `g_StrLower`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `g_FileName2Id`→KFilePath.cpp, `GetString`→KTabFile.cpp, `GetInteger`→KTabFile.cpp, `getpicPath`→Kgetinidata.cpp, `Clear`→KIniFile.cpp, `scene`→KgameWorld.cpp, `init`→HelloWorldScene.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `SimplyDecrypt`→dataChecksum.cpp, `Load`→KIniFile.cpp

## `vn/gameui/Klogin_f_VN.h`
- 30 dòng. Date:	2021.09.18
- Gọi tới: `scene`→KgameWorld.cpp, `init`→HelloWorldScene.cpp, `mianLoginCallback`→Klogin.cpp, `mianCancelCallback`→Klogin.cpp

## `vn/gameui/KuiChangeLockChestVN.cpp`
- 274 dòng. (không có chú thích đầu)
- Hàm: `KuiChangeLockChestVN`, `KuiChangeLockChestVN`, `KuiChangeLockChestVN::create`, `KuiChangeLockChestVN::init`, `KuiChangeLockChestVN::addDialogData`, `KuiChangeLockChestVN::setcoloseButton`, `KuiChangeLockChestVN::ChangePassCallBackFunc`, `KuiChangeLockChestVN::buttonCallBackFunc`, `KuiChangeLockChestVN::closePopLayer`, `KuiChangeLockChestVN::onTouchBegan`, `KuiChangeLockChestVN::getRect`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `ccMessageBox_new`→KCore.cpp, `g_StrLower`→KStrBase.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `SendClientCPChangeCmd`→KProtocol.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `vn/gameui/KuiChangeLockChestVN.h`
- 42 dòng. (không có chú thích đầu)
- Gọi tới: `KuiChangeLockChestVN`→KuiChangeLockChestVN.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `ChangePassCallBackFunc`→KuiChangeLockChestVN.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `vn/gameui/KuiCometoMapVN.cpp`
- 1507 dòng. popLayer->setTempString("Rank");
- Hàm: `KuiCometoMapVN::create`, `KuiCometoMapVN::init`, `KuiCometoMapVN::addDialogData`, `KuiCometoMapVN::setcoloseButton`, `KuiCometoMapVN::update`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `GetString`→KTabFile.cpp, `g_StrLower`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `GetInteger`→KTabFile.cpp, `MoneyDescType`→KCoreVN.cpp, `setContentSize`→ComboBox.cpp, `Load`→KIniFile.cpp, `Clear`→KIniFile.cpp, `getpicPath`→Kgetinidata.cpp, `setBtnTouchEnabled`→KuiCometoMap.cpp, `GetGameData`→CoreShell.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp

## `vn/gameui/KuiCometoMapVN.h`
- 19 dòng. (không có chú thích đầu)
- Gọi tới: `init`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `create`→KHRocker.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `update`→KgameWorld.cpp

## `vn/gameui/KuiDelLockChestVN.cpp`
- 151 dòng. (không có chú thích đầu)
- Hàm: `KuiDelLockChestVN`, `KuiDelLockChestVN`, `KuiDelLockChestVN::create`, `KuiDelLockChestVN::init`, `KuiDelLockChestVN::setcoloseButton`, `KuiDelLockChestVN::DelLockChestCallBackFunc`, `KuiDelLockChestVN::buttonCallBackFunc`, `KuiDelLockChestVN::closePopLayer`, `KuiDelLockChestVN::onTouchBegan`, `KuiDelLockChestVN::getRect`
- Gọi tới: `create`→KHRocker.cpp, `findinidata_one`→Kgetinidata.cpp, `t_sprintf`→KStrBase.cpp, `g_StrLower`→KStrBase.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `SendClientCPResetCmd`→KProtocol.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `vn/gameui/KuiDelLockChestVN.h`
- 51 dòng. KuiDelLockChestVNVN.h
- Gọi tới: `KuiDelLockChestVN`→KuiDelLockChestVN.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `DelLockChestCallBackFunc`→KuiDelLockChestVN.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `vn/gameui/KuiDynamicShopVN.cpp`
- 799 dòng. #include <gameui/KuigetStringInUI.h>
- Hàm: `KuiDynamicShopVN::create`, `KuiDynamicShopVN::init`, `KuiDynamicShopVN::addDialoaData`, `KuiDynamicShopVN::setcoloseButton`, `KuiDynamicShopVN::buyCallBackFunc`, `KuiDynamicShopVN::closeBuyPadCallback`, `KuiDynamicShopVN::CardCallBackFunc`, `KuiDynamicShopVN::MoneyDescType`, `KuiDynamicShopVN::AddObject`, `KuiDynamicShopVN::SetPage`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `findinidata_one`→Kgetinidata.cpp, `g_StrLower`→KStrBase.cpp, `GetStringByKeyFromFile`→CXmlStream.cpp, `setContentSize`→ComboBox.cpp, `Size`→KFile.cpp, `GetGameData`→CoreShell.cpp, `AddObject`→KuiCompoundItem.cpp, `addDialoaData`→KuiDynamicShop.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `Clear`→KIniFile.cpp, `MoneyDescType`→KCoreVN.cpp

## `vn/gameui/KuiDynamicShopVN.h`
- 33 dòng. CCRect getRect(CCNode* pNode, int i) override;
- Gọi tới: `create`→KHRocker.cpp, `init`→HelloWorldScene.cpp, `addDialoaData`→KuiDynamicShop.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `buyCallBackFunc`→KuiDynamicShop.cpp, `closeBuyPadCallback`→KuiDynamicShopVN.cpp, `CardCallBackFunc`→KuiDynamicShopVN.cpp, `MoneyDescType`→KCoreVN.cpp, `AddObject`→KuiCompoundItem.cpp, `SetPage`→KuiDynamicShop.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `vn/gameui/KuiFriendListVN.cpp`
- 740 dòng. 有按钮的　ｔａｌｋ　对话框
- Hàm: `AddList`, `AddFriend`, `AddBlackList`, `EraseFriend`, `SyncState`, `KuiFriendListVN`, `KuiFriendListVN`, `KuiFriendListVN::create`, `KuiFriendListVN::init`, `KuiFriendListVN::addDialogData`, `KuiFriendListVN::LoadPage`, `KuiFriendListVN::AddCustomItem`, `KuiFriendListVN::mianUpCallback`, `KuiFriendListVN::mianDownCallback`, `KuiFriendListVN::setcoloseButton`, `KuiFriendListVN::buttonCallBackFunc`, `KuiFriendListVN::selectedMainListItemEvent`, `KuiFriendListVN::getRect`, `KuiFriendListVN::onTouchEnded`, `KuiFriendListVN::onTouchMoved`, `KuiFriendListVN::onTouchBegan`, `KuiFriendListVN::update`, `KuiFriendListVN::InitPage`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `isFileExist`→KgameWorld.cpp, `create`→KHRocker.cpp, `g_StrLower`→KStrBase.cpp, `g_FileName2Id`→KFilePath.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `setTitle`→PopupLayer.cpp, `SendNewDataToServer`→CoreShell.cpp, `findinidata_one`→Kgetinidata.cpp, `Clear`→KIniFile.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp

## `vn/gameui/KuiFriendListVN.h`
- 78 dòng. (không có chú thích đầu)
- Gọi tới: `KuiFriendListVN`→KuiFriendListVN.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `InitPage`→KuiFriendListVN.cpp, `LoadPage`→KuiFriendListVN.cpp, `mianUpCallback`→KuiFriendListVN.cpp, `mianDownCallback`→KuiFriendListVN.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `selectedMainListItemEvent`→KuiAutoPlay.cpp

## `vn/gameui/KuiGiveVN.cpp`
- 823 dòng. (không có chú thích đầu)
- Hàm: `KuiGiveVN::create`, `KuiGiveVN::init`, `KuiGiveVN::addDialogData`, `KuiGiveVN::setcoloseButton`, `KuiGiveVN::onTouchBegan`, `KuiGiveVN::UpdateItemImage`, `KuiGiveVN::AddGiveObject`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `findinidata_one`→Kgetinidata.cpp, `Size`→KFile.cpp, `g_StrLower`→KStrBase.cpp, `setContentSize`→ComboBox.cpp, `getColorIndex`→Text.cpp, `g_Atoui`→KStrBase.cpp, `GetID`→KFaction.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `getGiveItem`→Kuigive.cpp, `UpdateItemImage`→KuiPlayerShop.cpp

## `vn/gameui/KuiGiveVN.h`
- 26 dòng. (không có chú thích đầu)
- Gọi tới: `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `UpdateItemImage`→KuiPlayerShop.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `AddGiveObject`→Kuigive.cpp

## `vn/gameui/KuiItemImmediaBoxVN.cpp`
- 331 dòng. 获得背景图片的大小
- Hàm: `KuiItemImmediaBoxVN::init`, `KuiItemImmediaBoxVN::create`, `KuiItemImmediaBoxVN::addDialogData`, `KuiItemImmediaBoxVN::setcoloseButton`, `KuiItemImmediaBoxVN::HoldObject_`, `KuiItemImmediaBoxVN::ImmediaCallback`, `KuiItemImmediaBoxVN::UpdateImmediaItem`, `KuiItemImmediaBoxVN::TempUpdataImmediacy`, `KuiItemImmediaBoxVN::clearItemData`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `UpdateImmediaItem`→KgameWorld.cpp, `HoldObject_`→KuiItemImmediaBox.cpp, `TempUpdataImmediacy`→KuiItemImmediaBox.cpp, `init`→HelloWorldScene.cpp, `setContentSize`→ComboBox.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `g_FileName2Id`→KFilePath.cpp, `GetName`→KNpcResNode.cpp, `GetNextItem`→KInventory.cpp, `GetGameData`→CoreShell.cpp, `OperationRequest`→CoreShell.cpp, `setTouchEnabled`→KHRocker - Copy.cpp

## `vn/gameui/KuiItemImmediaBoxVN.h`
- 31 dòng. (không có chú thích đầu)
- Gọi tới: `create`→KHRocker.cpp, `init`→HelloWorldScene.cpp, `UpdateImmediaItem`→KgameWorld.cpp, `TempUpdataImmediacy`→KuiItemImmediaBox.cpp, `clearItemData`→KuiItemImmediaBox.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `HoldObject_`→KuiItemImmediaBox.cpp, `ImmediaCallback`→KuiItemImmediaBoxVN.cpp

## `vn/gameui/KuiItemVN.cpp`
- 1684 dòng. 创建确定弹出框
- Hàm: `KuiItemVN::create`, `KuiItemVN::init`, `KuiItemVN::addDialogData`, `KuiItemVN::setcoloseButton`, `KuiItemVN::BayBanCallBackFunc`, `KuiItemVN::closeBayBan`, `KuiItemVN::tanCallBackFunc`, `KuiItemVN::gaoCallBackFunc`, `KuiItemVN::closegaoPadCallback`, `KuiItemVN::UpdateData`, `KuiItemVN::AddObject`, `KuiItemVN::onTouchItem`, `KuiItemVN::closeItemPadCallback`, `KuiItemVN::getRect`, `KuiItemVN::draw`
- Gọi tới: `AddMember`→KPlayerTeam.cpp, `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `ccMessageBox_new`→KCore.cpp, `GetGameData`→CoreShell.cpp, `Size`→KFile.cpp, `MoneyDescType`→KCoreVN.cpp, `GetString`→KTabFile.cpp, `g_StrLower`→KStrBase.cpp, `setDialogColor`→KuiEffect.cpp, `GetID`→KFaction.cpp, `OperationRequest`→CoreShell.cpp, `setContentSize`→ComboBox.cpp, `setPaintDinhGia`→KgameWorld.cpp

## `vn/gameui/KuiItemVN.h`
- 46 dòng. Created by 2021.09
- Gọi tới: `create`→KHRocker.cpp, `init`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `UpdateItemImage`→KuiPlayerShop.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `tanCallBackFunc`→KuiSellItem.cpp, `gaoCallBackFunc`→KuiSellItem.cpp, `biaoCallBackFunc`→KuiSellItem.cpp, `closegaoPadCallback`→KuiSellItem.cpp, `UpdateData`→KuiCometoMap.cpp, `AddObject`→KuiCompoundItem.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `onTouchItem`→KuiItem.cpp, `closeItemPadCallback`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp

## `vn/gameui/KuiItemdescVN.cpp`
- 3245 dòng. #include <engine/KPalette.h>
- Hàm: `KuiItemdescVN::create`, `KuiItemdescVN::create`, `KuiItemdescVN::addshopdesc`, `KuiItemdescVN::addDialogData`, `KuiItemdescVN::setLayerPosY`, `KuiItemdescVN::setLayerPosX`, `KuiItemdescVN::setLayerPos`, `KuiItemdescVN::update`, `KuiItemdescVN::ThemDaTauCallBackFunc`, `KuiItemdescVN::ThaoDaTauCallBackFunc`, `KuiItemdescVN::ThemTradeCallBackFunc`, `KuiItemdescVN::ThaoTradeCallBackFunc`, `KuiItemdescVN::kuoExCallBackFunc`, `KuiItemdescVN::BreakItemBackFunc`, `KuiItemdescVN::closeBreakItemBackFunc`, `KuiItemdescVN::BuyCallBackFunc`, `KuiItemdescVN::BuyPlayerCallBackFunc`, `KuiItemdescVN::closesavemonybiaoPadCallback`, `KuiItemdescVN::ThaoCallBackFunc`, `KuiItemdescVN::closeDinhGiaPadCallback`, `KuiItemdescVN::DinhItemCallBackFunc`, `KuiItemdescVN::DinhThaoItemCallBackFunc`, `KuiItemdescVN::ReturnSupportSeries`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `GetStringByKeyFromFile`→CXmlStream.cpp, `isFileExist`→KgameWorld.cpp, `g_StrLower`→KStrBase.cpp, `g_FileName2Id`→KFilePath.cpp, `ccMessageBox_new`→KCore.cpp, `ClientShowMsg`→KNpc.cpp, `OperationRequest`→CoreShell.cpp, `GetString`→KTabFile.cpp, `create`→KHRocker.cpp, `GetID`→KFaction.cpp, `Load`→KIniFile.cpp, `CustomRichLabel`→KCoreVN.cpp, `GetName`→KNpcResNode.cpp, `Clear`→KIniFile.cpp

## `vn/gameui/KuiItemdescVN.h`
- 65 dòng. ���Ӽ���ͼ��
- Gọi tới: `create`→KHRocker.cpp, `setLayerPosY`→KuiItemdesc.cpp, `setLayerPosX`→KuiItemdesc.cpp, `setLayerPos`→KuiItemdesc.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `addshopdesc`→KuiItemdesc.cpp, `BuyCallBackFunc`→KuiItemdescVN.cpp, `ThaoDaTauCallBackFunc`→KuiItemdescVN.cpp, `ThemDaTauCallBackFunc`→KuiItemdescVN.cpp, `BuyPlayerCallBackFunc`→KuiItemdescVN.cpp, `ThaoTradeCallBackFunc`→KuiItemdescVN.cpp, `ThemTradeCallBackFunc`→KuiItemdescVN.cpp, `kuoExCallBackFunc`→KuiItemdescVN.cpp, `ThaoCallBackFunc`→KuiItemdescVN.cpp, `chuanCallBackFunc`→KuiItem_New.cpp

## `vn/gameui/KuiLockChestVN.cpp`
- 247 dòng. (không có chú thích đầu)
- Hàm: `KuiLockChestVN`, `KuiLockChestVN`, `KuiLockChestVN::create`, `KuiLockChestVN::init`, `KuiLockChestVN::addDialogData`, `KuiLockChestVN::setcoloseButton`, `KuiLockChestVN::CreatePassCallBackFunc`, `KuiLockChestVN::onTouchBegan`, `KuiLockChestVN::buttonCallBackFunc`, `KuiLockChestVN::closePopLayer`, `KuiLockChestVN::getRect`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `ccMessageBox_new`→KCore.cpp, `g_StrLower`→KStrBase.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `SendClientCPResetCmd`→KProtocol.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `vn/gameui/KuiLockChestVN.h`
- 42 dòng. (không có chú thích đầu)
- Gọi tới: `KuiLockChestVN`→KuiLockChestVN.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `CreatePassCallBackFunc`→KuiLockChestVN.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `vn/gameui/KuiMaxMapVN.cpp`
- 675 dòng. 创建确定弹出框
- Hàm: `KuiMaxMapVN::create`, `KuiMaxMapVN::addDialogData`, `KuiMaxMapVN::setcoloseButton`, `KuiMaxMapVN::onTouchBegan`, `KuiMaxMapVN::onTouchMoved`, `KuiMaxMapVN::onTouchEnded`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `g_StrLower`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `isFileExist`→KgameWorld.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `t_printf`→KStrBase.cpp, `g_FileName2Id`→KFilePath.cpp, `setContentSize`→ComboBox.cpp, `getpicPath`→Kgetinidata.cpp, `setFaceBookState`→AutoPathFinder.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `checkPos`→KScenePlaceC.cpp

## `vn/gameui/KuiMaxMapVN.h`
- 28 dòng. Created by 横刀向天笑 QQ:25557432
- Gọi tới: `create`→KHRocker.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp

## `vn/gameui/KuiMinMapVN.cpp`
- 1422 dòng. #include "../Uiglobaldata.h"
- Hàm: `KuiMinMapVN`, `KuiMinMapVN`, `KuiMinMapVN::create`, `KuiMinMapVN::init`, `KuiMinMapVN::getcurPosition`, `KuiMinMapVN::addDialogData`, `KuiMinMapVN::upDataMap`, `KuiMinMapVN::setcoloseButton`, `KuiMinMapVN::buttonCallBackFunc`, `KuiMinMapVN::closePopLayer`, `KuiMinMapVN::getRect`, `KuiMinMapVN::onTouchBegan`, `KuiMinMapVN::onTouchMoved`, `KuiMinMapVN::onTouchEnded`, `KuiMinMapVN::moveLayer`, `KuiMinMapVN::EndedLayer`, `KuiMinMapVN::setMapNameAndPoint`, `KuiMinMapVN::setMpsPos`, `KuiMinMapVN::onRead`, `KuiMinMapVN::draw`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `init`→HelloWorldScene.cpp, `FindMemberID`→KPlayerTeam.cpp, `g_StrLower`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `setContentSize`→ComboBox.cpp, `GetSceneFocus`→KScenePlaceC.cpp, `ccMessageBox_new`→KCore.cpp, `NewMap2Mps`→KSubWorld.cpp, `GetRelation`→KNpcSet.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `g_FileName2Id`→KFilePath.cpp, `isFileExist`→KgameWorld.cpp

## `vn/gameui/KuiMinMapVN.h`
- 231 dòng. Created by 横刀向天笑 QQ:25557432
- Gọi tới: `create`→KHRocker.cpp, `KuiMinMapVN`→KuiMinMapVN.cpp, `init`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `moveLayer`→KuiBtnControl.cpp, `EndedLayer`→KuiBtnControl.cpp, `setMapNameAndPoint`→KuiMinMap.cpp, `upDataMap`→KuiMinMap.cpp, `setMpsPos`→KuiMinMap.cpp, `getcurPosition`→KuiItemImmediaBox.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp

## `vn/gameui/KuiNewPlayerVN.cpp`
- 721 dòng. 'scene' is an autorelease object
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `isFileExist`→KgameWorld.cpp, `g_StrLower`→KStrBase.cpp, `GetRoleImageName`→KuiNewPlayer.cpp, `ccMessageBox_new`→KCore.cpp, `g_FileName2Id`→KFilePath.cpp, `scene`→KgameWorld.cpp, `setBreakTheead`→SocketClient.cpp, `setBufferEmpty`→ClientStage.cpp, `Cleanup`→ClientStage.cpp, `upSpriteData`→KuiShowSprite.cpp, `setShowVisible`→KuiShowSprite.cpp, `init`→HelloWorldScene.cpp, `GetString`→KTabFile.cpp

## `vn/gameui/KuiNewPlayerVN.h`
- 24 dòng. Date:	2021.09.18
- Gọi tới: `init`→HelloWorldScene.cpp, `scene`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `mainEnterCallback`→KuiNewPlayer.cpp

## `vn/gameui/KuiPlayerSelFunVN.cpp`
- 772 dòng. 锟斤拷锟斤拷确锟斤拷锟斤拷锟斤拷锟斤拷
- Hàm: `KuiPlayerSelFunVN`, `KuiPlayerSelFunVN`, `KuiPlayerSelFunVN::create`, `KuiPlayerSelFunVN::init`, `KuiPlayerSelFunVN::addDialogData`, `KuiPlayerSelFunVN::setcoloseButton`, `KuiPlayerSelFunVN::onTouchBegan`, `KuiPlayerSelFunVN::playerItemChatCallback`, `KuiPlayerSelFunVN::playerItemFriendCallback`, `KuiPlayerSelFunVN::playerItemBlackListCallback`, `KuiPlayerSelFunVN::playerItemInviteTeamCallback`, `KuiPlayerSelFunVN::playerItemTeamCallback`, `KuiPlayerSelFunVN::playerItemFollowCallback`, `KuiPlayerSelFunVN::playerItemInfoCallback`, `KuiPlayerSelFunVN::playerItemSellCallback`, `KuiPlayerSelFunVN::playerItemBangCallback`, `KuiPlayerSelFunVN::playerItemPkCallback`, `KuiPlayerSelFunVN::playerItemTradeCallback`, `KuiPlayerSelFunVN::PlayerItemTurn`, `KuiPlayerSelFunVN::okCallBackFunc`, `KuiPlayerSelFunVN::draw`, `KuiPlayerSelFunVN::update`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `isFileExist`→KgameWorld.cpp, `g_StrLower`→KStrBase.cpp, `g_FileName2Id`→KFilePath.cpp, `create`→KHRocker.cpp, `OperationRequest`→CoreShell.cpp, `TeamOperation`→CoreShell.cpp, `GetMpsPos`→KMissle.cpp, `init`→HelloWorldScene.cpp, `__ApplyAddTeam`→CoreShell.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `okCallBackFunc`→Kuiduan.cpp, `setchatInputText`→KgameWorld.cpp, `GetMenuState`→KNpc.cpp

## `vn/gameui/KuiPlayerSelFunVN.h`
- 80 dòng. #include <gameui/KuiPlayerSelFun.h>
- Gọi tới: `KuiPlayerSelFunVN`→KuiPlayerSelFunVN.cpp, `init`→HelloWorldScene.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `PlayerItemTurn`→KuiPlayerSelFunVN.cpp, `playerItemChatCallback`→KuiPlayerSelFunVN.cpp, `playerItemFriendCallback`→KuiPlayerSelFunVN.cpp, `playerItemInviteTeamCallback`→KuiPlayerSelFunVN.cpp, `playerItemTeamCallback`→KuiPlayerSelFunVN.cpp, `playerItemFollowCallback`→KuiPlayerSelFunVN.cpp, `playerItemInfoCallback`→KuiPlayerSelFunVN.cpp

## `vn/gameui/KuiPlayerShopVN.cpp`
- 368 dòng. (không có chú thích đầu)
- Hàm: `KuiPlayerShopVN::create`, `KuiPlayerShopVN::init`, `KuiPlayerShopVN::addDialoaData`, `KuiPlayerShopVN::setcoloseButton`, `KuiPlayerShopVN::onTouchBegan`, `KuiPlayerShopVN::AddObject`, `KuiPlayerShopVN::UpdateItemImage`, `KuiPlayerShopVN::closeCallBackFunc`, `KuiPlayerShopVN::closePopLayer`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `findinidata_one`→Kgetinidata.cpp, `Size`→KFile.cpp, `setContentSize`→ComboBox.cpp, `g_StrLower`→KStrBase.cpp, `setchatDelegate`→KgameWorld.cpp, `addDialoaData`→KuiDynamicShop.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `UpdateItemImage`→KuiPlayerShop.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `UpdateItem`→KSellItem.cpp, `onTouchBegan`→KHRocker - Copy.cpp

## `vn/gameui/KuiPlayerShopVN.h`
- 24 dòng. (không có chú thích đầu)
- Gọi tới: `create`→KHRocker.cpp, `init`→HelloWorldScene.cpp, `addDialoaData`→KuiDynamicShop.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `AddObject`→KuiCompoundItem.cpp, `UpdateItemImage`→KuiPlayerShop.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `closeCallBackFunc`→KuiDynamicShop.cpp

## `vn/gameui/KuiPlayerTradeVN.cpp`
- 1908 dòng. 有按钮的　ｔａｌｋ　对话框
- Hàm: `KuiPlayerTradeVN::create`, `KuiPlayerTradeVN::init`, `KuiPlayerTradeVN::addDialogData`, `KuiPlayerTradeVN::setcoloseButton`, `KuiPlayerTradeVN::UpdateTradeOperData`, `KuiPlayerTradeVN::UpdateTarGiveItem`, `KuiPlayerTradeVN::AddtarGiveObject`, `KuiPlayerTradeVN::UpdateGiveItem`, `KuiPlayerTradeVN::AddGiveObject`, `KuiPlayerTradeVN::selectedItemEvent`, `KuiPlayerTradeVN::UpdateItem`, `KuiPlayerTradeVN::AddObject`, `KuiPlayerTradeVN::UpdateData`, `KuiPlayerTradeVN::clearAllColor`, `KuiPlayerTradeVN::getFreePosition`, `KuiPlayerTradeVN::freeAllPosition`, `KuiPlayerTradeVN::onTouchBegan`, `KuiPlayerTradeVN::OnModififyMoney`, `KuiPlayerTradeVN::okCallBackFunc_`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `setVisible_e`→KuiEffect.cpp, `Size`→KFile.cpp, `setContentSize`→ComboBox.cpp, `setDialogTagKey`→KuiEffect.cpp, `GetID`→KFaction.cpp, `GetGameData`→CoreShell.cpp, `MoneyDescType`→KCoreVN.cpp, `addChild_e`→KuiEffect.cpp, `findinidata_one`→Kgetinidata.cpp, `findChildByKey`→KuiEffect.cpp, `g_StrLower`→KStrBase.cpp, `upItemColor`→KuiEffect.cpp, `setDialogColor`→KuiEffect.cpp

## `vn/gameui/KuiPlayerTradeVN.h`
- 127 dòng. Created by 2018.10 横刀向天笑 QQ:25557432
- Gọi tới: `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `UpdateItem`→KSellItem.cpp, `UpdateGiveItem`→KgameWorld.cpp, `UpdateTarGiveItem`→KuiPlayerTrade.cpp, `UpdateTradeOperData`→KgameWorld.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `btnCallBackFunc_quxia`→KuiCompoundItem.cpp, `AddObject`→KuiCompoundItem.cpp, `AddGiveObject`→Kuigive.cpp, `AddtarGiveObject`→KuiPlayerTrade.cpp, `OnModififyMoney`→KuiPlayerTrade.cpp, `okCallBackFunc_`→KuiPlayerTrade.cpp, `UpdateItemData`→Kuigive.cpp

## `vn/gameui/KuiRoleStateVN.cpp`
- 973 dòng. (không có chú thích đầu)
- Hàm: `KuiRoleStateVN::create`, `KuiRoleStateVN::init`, `KuiRoleStateVN::addDialogData`, `KuiRoleStateVN::AddPointCallBack`, `KuiRoleStateVN::AvatarCallback`, `KuiRoleStateVN::DinhCallBack`, `KuiRoleStateVN::setcoloseButton`, `KuiRoleStateVN::addpicBox`, `KuiRoleStateVN::layerCallBakc`, `KuiRoleStateVN::onTouchEnded`, `KuiRoleStateVN::onTouchItem`, `KuiRoleStateVN::BreathAttributeUpdate`, `KuiRoleStateVN::CheckBoxCallBackFunc`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `isFileExist`→KgameWorld.cpp, `g_StrLower`→KStrBase.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `OperationRequest`→CoreShell.cpp, `g_FileName2Id`→KFilePath.cpp, `ccMessageBox_new`→KCore.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `findinidata_one`→Kgetinidata.cpp, `GetGameData`→CoreShell.cpp, `UpdateItemOrDer`→KuiItem.cpp, `onTouchItem`→KuiItem.cpp

## `vn/gameui/KuiRoleStateVN.h`
- 52 dòng. Created by 横刀向天笑 QQ:25557432
- Gọi tới: `create`→KHRocker.cpp, `init`→HelloWorldScene.cpp, `AvatarCallback`→KuiRoleStateVN.cpp, `DinhCallBack`→KuiRoleStateVN.cpp, `AddPointCallBack`→KuiRoleStateVN.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `addpicBox`→KuiRoleState.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `onTouchItem`→KuiItem.cpp, `BreathAttributeUpdate`→KuiRoleState.cpp, `CheckBoxCallBackFunc`→KuiRoleStateVN.cpp, `layerCallBakc`→KuiCompoundItem.cpp

## `vn/gameui/KuiSelNativePlaceVN.cpp`
- 317 dòng. 'scene' is an autorelease object
- Hàm: `KuiSelNativePlaceVN::scene`, `KuiSelNativePlaceVN::init`, `KuiSelNativePlaceVN::mainEnterCallback`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `isFileExist`→KgameWorld.cpp, `g_StrLower`→KStrBase.cpp, `scene`→KgameWorld.cpp, `getpicPath`→Kgetinidata.cpp, `init`→HelloWorldScene.cpp, `g_FileName2Id`→KFilePath.cpp, `GetString`→KTabFile.cpp, `GetInteger`→KTabFile.cpp, `setBreakTheead`→SocketClient.cpp, `setBufferEmpty`→ClientStage.cpp, `Cleanup`→ClientStage.cpp, `ccMessageBox_new`→KCore.cpp, `setTouchEnabled`→KHRocker - Copy.cpp

## `vn/gameui/KuiSelNativePlaceVN.h`
- 27 dòng. Date:	2021.09.18
- Gọi tới: `init`→HelloWorldScene.cpp, `scene`→KgameWorld.cpp, `mainEnterCallback`→KuiNewPlayer.cpp

## `vn/gameui/KuiSelPKStateVN.cpp`
- 163 dòng. (không có chú thích đầu)
- Hàm: `KuiSelPKStateVN`, `KuiSelPKStateVN`, `KuiSelPKStateVN::create`, `KuiSelPKStateVN::init`, `KuiSelPKStateVN::setcoloseButton`, `KuiSelPKStateVN::mainPkSwitchCallback`, `KuiSelPKStateVN::buttonCallBackFunc`, `KuiSelPKStateVN::onTouchBegan`, `KuiSelPKStateVN::update`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `isFileExist`→KgameWorld.cpp, `create`→KHRocker.cpp, `g_StrLower`→KStrBase.cpp, `g_FileName2Id`→KFilePath.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `setContentSize`→ComboBox.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `GetGameData`→CoreShell.cpp, `OperationRequest`→CoreShell.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `update`→KgameWorld.cpp

## `vn/gameui/KuiSelPKStateVN.h`
- 52 dòng. (không có chú thích đầu)
- Gọi tới: `KuiSelPKStateVN`→KuiSelPKStateVN.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `mainPkSwitchCallback`→KuiSelPKStateVN.cpp

## `vn/gameui/KuiSelPlayerChatFunVN.cpp`
- 181 dòng. (không có chú thích đầu)
- Hàm: `KuiSelPlayerChatFunVN`, `KuiSelPlayerChatFunVN`, `KuiSelPlayerChatFunVN::create`, `KuiSelPlayerChatFunVN::init`, `KuiSelPlayerChatFunVN::setcoloseButton`, `KuiSelPlayerChatFunVN::FriendCallBackFunc`, `KuiSelPlayerChatFunVN::BackListCallBackFunc`, `KuiSelPlayerChatFunVN::SearchNameCallBackFunc`, `KuiSelPlayerChatFunVN::buttonCallBackFunc`, `KuiSelPlayerChatFunVN::onTouchBegan`, `KuiSelPlayerChatFunVN::update`
- Gọi tới: `create`→KHRocker.cpp, `findinidata_one`→Kgetinidata.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `t_sprintf`→KStrBase.cpp, `g_StrLower`→KStrBase.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `OperationRequest`→CoreShell.cpp, `setContentSize`→ComboBox.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `setchatInputText`→KgameWorld.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `update`→KgameWorld.cpp

## `vn/gameui/KuiSelPlayerChatFunVN.h`
- 51 dòng. (không có chú thích đầu)
- Gọi tới: `KuiSelPlayerChatFunVN`→KuiSelPlayerChatFunVN.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `update`→KgameWorld.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `FriendCallBackFunc`→KuiSelPlayerChatFunVN.cpp, `BackListCallBackFunc`→KuiSelPlayerChatFunVN.cpp, `SearchNameCallBackFunc`→KuiSelPlayerChatFunVN.cpp

## `vn/gameui/KuiSelPlayerVN.cpp`
- 438 dòng. 'scene' is an autorelease object
- Hàm: `KuiSelPlayerVN::scene`, `KuiSelPlayerVN::init`, `KuiSelPlayerVN::mainNewCallback`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `isFileExist`→KgameWorld.cpp, `scene`→KgameWorld.cpp, `g_StrLower`→KStrBase.cpp, `g_FileName2Id`→KFilePath.cpp, `setShowVisible`→KuiShowSprite.cpp, `GetRoleImageName`→KuiNewPlayer.cpp, `setContentSize`→ComboBox.cpp, `init`→HelloWorldScene.cpp, `GetString`→KTabFile.cpp, `GetInteger`→KTabFile.cpp, `getpicPath`→Kgetinidata.cpp, `GetStringByKeyFromFile`→CXmlStream.cpp, `setBreakTheead`→SocketClient.cpp

## `vn/gameui/KuiSelPlayerVN.h`
- 28 dòng. Date:	2021.09.18
- Gọi tới: `init`→HelloWorldScene.cpp, `scene`→KgameWorld.cpp, `mainNewCallback`→KuiSelPlayer_new.cpp

## `vn/gameui/KuiSelserverVN.cpp`
- 472 dòng. 'scene' is an autorelease object
- Hàm: `KuiSelserverVN::scene`, `KuiSelserverVN::init`, `KuiSelserverVN::onServerButtonClicked`, `KuiSelserverVN::selServerCallBack`, `KuiSelserverVN::mianCancelCallback`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `ccMessageBox_new`→KCore.cpp, `GetString`→KTabFile.cpp, `Load`→KIniFile.cpp, `GetInteger`→KTabFile.cpp, `g_StrLower`→KStrBase.cpp, `getpicPath`→Kgetinidata.cpp, `Clear`→KIniFile.cpp, `isFileExist`→KgameWorld.cpp, `scene`→KgameWorld.cpp, `g_FileName2Id`→KFilePath.cpp, `SimplyDecrypt`→dataChecksum.cpp, `setBreakTheead`→SocketClient.cpp, `init`→HelloWorldScene.cpp

## `vn/gameui/KuiSelserverVN.h`
- 29 dòng. Date:	2021.09.18
- Gọi tới: `scene`→KgameWorld.cpp, `init`→HelloWorldScene.cpp, `selServerCallBack`→KuiSelserver.cpp, `mianCancelCallback`→Klogin.cpp, `onServerButtonClicked`→KuiSelserverVN.cpp

## `vn/gameui/KuiShopVN.cpp`
- 447 dòng. ����ȷ��������
- Hàm: `KuiShopVN::create`, `KuiShopVN::init`, `KuiShopVN::addDialoaData`, `KuiShopVN::setcoloseButton`, `KuiShopVN::AddObject`, `KuiShopVN::SetPage`, `KuiShopVN::UpdateData`, `KuiShopVN::onTouchBegan`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `setContentSize`→ComboBox.cpp, `g_StrLower`→KStrBase.cpp, `Size`→KFile.cpp, `GetGameData`→CoreShell.cpp, `addDialoaData`→KuiDynamicShop.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `UpdateData`→KuiCometoMap.cpp, `AddObject`→KuiCompoundItem.cpp, `GetItemIndex`→KBuySell.cpp, `SetPage`→KuiDynamicShop.cpp, `Clear`→KIniFile.cpp

## `vn/gameui/KuiShopVN.h`
- 29 dòng. (không có chú thích đầu)
- Gọi tới: `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `addDialoaData`→KuiDynamicShop.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `AddObject`→KuiCompoundItem.cpp, `SetPage`→KuiDynamicShop.cpp, `UpdateData`→KuiCometoMap.cpp, `onTouchBegan`→KHRocker - Copy.cpp

## `vn/gameui/KuiShowSpriteVN.cpp`
- 1 dòng. (không có chú thích đầu)

## `vn/gameui/KuiShowSpriteVN.h`
- 8 dòng. (không có chú thích đầu)

## `vn/gameui/KuiSkillVN.cpp`
- 487 dòng. popLayer->setTitle(title);
- Hàm: `KuiskillVN::create`, `KuiskillVN::init`, `KuiskillVN::addDialogData`, `KuiskillVN::onTouchBegan`, `KuiskillVN::setcoloseButton`, `KuiskillVN::UpdateSkill`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `GetiniData`→KuiSkill.cpp, `ccMessageBox_new`→KCore.cpp, `setContentSize`→ComboBox.cpp, `GetGameData`→CoreShell.cpp, `GetSkill`→KSkillManager.h, `UpdateSkill`→KgameWorld.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `g_StrLower`→KStrBase.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `GetSkillName`→KThiefSkill.cpp, `FindSame`→KPlayerSet.cpp

## `vn/gameui/KuiSkillVN.h`
- 31 dòng. Created by 横刀向天笑 QQ:25557432
- Gọi tới: `create`→KHRocker.cpp, `init`→HelloWorldScene.cpp, `UpdateSkill`→KgameWorld.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp

## `vn/gameui/KuiSkilldescVN.cpp`
- 1031 dòng. #include <engine/KPalette.h>
- Hàm: `KuiSkilldescVN::create`, `KuiSkilldescVN::addDialogData`, `KuiSkilldescVN::touchValueToggle`, `KuiSkilldescVN::GetModelSkillByID`, `KuiSkilldescVN::tutimCallBackFunc`, `KuiSkilldescVN::chidinhCallBackFunc`, `KuiSkilldescVN::dieuhuongCallBackFunc`, `KuiSkilldescVN::CheckSkill`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `GetStringByKeyFromFile`→CXmlStream.cpp, `isFileExist`→KgameWorld.cpp, `g_StrLower`→KStrBase.cpp, `GetSkill`→KSkillManager.h, `g_FileName2Id`→KFilePath.cpp, `GetModelSkillByID`→KuiMyMenu.cpp, `create`→KHRocker.cpp, `CustomRichLabel`→KCoreVN.cpp, `setContentSize`→ComboBox.cpp, `useSkillModel`→KgameWorld.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `Size`→KFile.cpp, `GetDescAboutLevel`→KSkills.cpp, `GetString`→KTabFile.cpp

## `vn/gameui/KuiSkilldescVN.h`
- 52 dòng. (không có chú thích đầu)
- Gọi tới: `create`→KHRocker.cpp, `tutimCallBackFunc`→KuiSkilldescVN.cpp, `dieuhuongCallBackFunc`→KuiSkilldescVN.cpp, `chidinhCallBackFunc`→KuiSkilldescVN.cpp, `touchValueToggle`→KuiAutoPlay.cpp, `GetModelSkillByID`→KuiMyMenu.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `CheckSkill`→KuiSkilldescVN.cpp

## `vn/gameui/KuiSkilldescVN_.cpp`
- 868 dòng. #include <engine/KPalette.h>
- Hàm: `KuiSkilldescVN::create`, `KuiSkilldescVN::addDialogData`, `KuiSkilldescVN::tutimCallBackFunc`, `KuiSkilldescVN::chidinhCallBackFunc`, `KuiSkilldescVN::dieuhuongCallBackFunc`, `KuiSkilldescVN::CheckSkill`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `GetStringByKeyFromFile`→CXmlStream.cpp, `isFileExist`→KgameWorld.cpp, `g_StrLower`→KStrBase.cpp, `GetSkill`→KSkillManager.h, `setContentSize`→ComboBox.cpp, `g_FileName2Id`→KFilePath.cpp, `Size`→KFile.cpp, `create`→KHRocker.cpp, `CustomRichLabel`→KCoreVN.cpp, `useSkillModel`→KgameWorld.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `TEncodeText_`→Text.cpp, `GetDescAboutLevel`→KSkills.cpp, `GetString`→KTabFile.cpp

## `vn/gameui/KuiStateSkillControlVN.cpp`
- 149 dòng. 创建确定弹出框
- Hàm: `KuiStateSkillControlVN`, `KuiStateSkillControlVN`, `KuiStateSkillControlVN::create_`, `KuiStateSkillControlVN::init`, `KuiStateSkillControlVN::draw`, `KuiStateSkillControlVN::update`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `init`→HelloWorldScene.cpp, `create_`→KuiFaceSelector.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `setContentSize`→ComboBox.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `draw`→HelloWorldScene.cpp, `GetHead`→KList.h, `GetSkill`→KSkillManager.h, `g_StrLower`→KStrBase.cpp, `GetNext`→KNode.h, `update`→KgameWorld.cpp

## `vn/gameui/KuiStateSkillControlVN.h`
- 17 dòng. (không có chú thích đầu)
- Gọi tới: `KuiStateSkillControlVN`→KuiStateSkillControlVN.cpp, `init`→HelloWorldScene.cpp, `create_`→KuiFaceSelector.cpp, `update`→KgameWorld.cpp, `draw`→HelloWorldScene.cpp

## `vn/gameui/KuiTalkDialog1VN.cpp`
- 285 dòng. popLayer->setTitle(title);
- Hàm: `KuiTalkDialog1VN::createVN`, `KuiTalkDialog1VN::addDialogData`, `KuiTalkDialog1VN::setcoloseButton`, `KuiTalkDialog1VN::touchEvent`
- Gọi tới: `create`→KHRocker.cpp, `OperationRequest`→CoreShell.cpp, `t_sprintf`→KStrBase.cpp, `TongOperation`→CoreShell.cpp, `TeamOperation`→CoreShell.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `ccMessageBox_new`→KCore.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `setTitle`→PopupLayer.cpp, `touchEvent`→KuiTalkDialog1.cpp

## `vn/gameui/KuiTalkDialog1VN.h`
- 23 dòng. (không có chú thích đầu)
- Gọi tới: `createVN`→KuiTalkDialog1VN.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `touchEvent`→KuiTalkDialog1.cpp

## `vn/gameui/KuiTaskInfoVN.cpp`
- 228 dòng. 创建确定弹出框 //VH by tuanln huong dan nhiem vu
- Hàm: `KuiTaskInfoVN::create`, `KuiTaskInfoVN::init`, `KuiTaskInfoVN::addDialogData`, `KuiTaskInfoVN::setcoloseButton`
- Gọi tới: `create`→KHRocker.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `getpicPath`→Kgetinidata.cpp, `t_sprintf`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `setContentSize`→ComboBox.cpp, `g_StrLower`→KStrBase.cpp, `Load`→KIniFile.cpp, `AddTaskIndex`→KuiRankInfo.cpp

## `vn/gameui/KuiTaskInfoVN.h`
- 29 dòng. KuiTaskInfo.h
- Gọi tới: `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp

## `vn/gameui/KuiTeamVN.cpp`
- 336 dòng. 创建确定弹出框
- Hàm: `KuiTeamVN::create`, `KuiTeamVN::init`, `KuiTeamVN::addDialogData`, `KuiTeamVN::setcoloseButton`, `KuiTeamVN::selectedBoxStateEvent`
- Gọi tới: `findinidata_one`→Kgetinidata.cpp, `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `g_StrLower`→KStrBase.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `TeamOperation`→CoreShell.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `setContentSize`→ComboBox.cpp, `UpdateData`→KuiCometoMap.cpp, `OnRefresh`→KuiTeam.cpp, `ClientShowMsg`→KNpc.cpp, `selectedBoxStateEvent`→Kuiplayerfun.cpp

## `vn/gameui/KuiTeamVN.h`
- 27 dòng. #define FIGHT_SKILL_COUNT_PER_PAGE	25
- Gọi tới: `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `selectedBoxStateEvent`→Kuiplayerfun.cpp

## `vn/gameui/KuiTongChangeCamVN.cpp`
- 373 dòng. (không có chú thích đầu)
- Hàm: `KuiTongChangeCamVN`, `KuiTongChangeCamVN`, `KuiTongChangeCamVN::create`, `KuiTongChangeCamVN::init`, `KuiTongChangeCamVN::setcoloseButton`, `KuiTongChangeCamVN::btnConfirmCallBackFunc`, `KuiTongChangeCamVN::btnCallBackFunc`, `KuiTongChangeCamVN::buttonCallBackFunc`, `KuiTongChangeCamVN::closePopLayer`, `KuiTongChangeCamVN::onTouchBegan`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `isFileExist`→KgameWorld.cpp, `g_StrLower`→KStrBase.cpp, `g_FileName2Id`→KFilePath.cpp, `btnCallBackFunc`→KuiEscInfo.cpp, `create`→KHRocker.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `GetCamp`→KFaction.cpp, `SetTongCamp`→KPlayerTong.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp

## `vn/gameui/KuiTongChangeCamVN.h`
- 59 dòng. KuiTongChangeCam.h
- Gọi tới: `KuiTongChangeCamVN`→KuiTongChangeCamVN.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `btnCallBackFunc`→KuiEscInfo.cpp, `btnConfirmCallBackFunc`→KuiTongChangeCamVN.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp

## `vn/gameui/KuiTongCreateSheetVN.cpp`
- 319 dòng. (không có chú thích đầu)
- Hàm: `KuiTongCreateSheetVN::create`, `KuiTongCreateSheetVN::init`, `KuiTongCreateSheetVN::addDialogData`, `KuiTongCreateSheetVN::setcoloseButton`, `KuiTongCreateSheetVN::btnCallBackFunc`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `isFileExist`→KgameWorld.cpp, `create`→KHRocker.cpp, `g_StrLower`→KStrBase.cpp, `g_FileName2Id`→KFilePath.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `btnCallBackFunc`→KuiEscInfo.cpp, `ccMessageBox_new`→KCore.cpp, `TongOperation`→CoreShell.cpp

## `vn/gameui/KuiTongCreateSheetVN.h`
- 28 dòng. (không có chú thích đầu)
- Gọi tới: `create`→KHRocker.cpp, `init`→HelloWorldScene.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `btnCallBackFunc`→KuiEscInfo.cpp

## `vn/gameui/KuiTongDelegateVN.cpp`
- 399 dòng. (không có chú thích đầu)
- Hàm: `KuiTongDelegateVN`, `KuiTongDelegateVN`, `KuiTongDelegateVN::create`, `KuiTongDelegateVN::init`, `KuiTongDelegateVN::addDialogData`, `KuiTongDelegateVN::setcoloseButton`, `KuiTongDelegateVN::btnCallBackFunc`, `KuiTongDelegateVN::confirmCallBackFunc`, `KuiTongDelegateVN::buttonCallBackFunc`, `KuiTongDelegateVN::closePopLayer`, `KuiTongDelegateVN::onTouchBegan`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `isFileExist`→KgameWorld.cpp, `g_StrLower`→KStrBase.cpp, `g_FileName2Id`→KFilePath.cpp, `create`→KHRocker.cpp, `ApplyInstate`→KPlayerTong.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `btnCallBackFunc`→KuiEscInfo.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp

## `vn/gameui/KuiTongDelegateVN.h`
- 57 dòng. KuiTongCreate.h
- Gọi tới: `KuiTongDelegateVN`→KuiTongDelegateVN.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `confirmCallBackFunc`→KuiTongDelegateVN.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `btnCallBackFunc`→KuiEscInfo.cpp, `onTouchBegan`→KHRocker - Copy.cpp

## `vn/gameui/KuiTongDiaryVN.cpp`
- 187 dòng. 创建确定弹出框
- Hàm: `KuiTongDiaryVN`, `KuiTongDiaryVN`, `KuiTongDiaryVN::create`, `KuiTongDiaryVN::init`, `KuiTongDiaryVN::addDialogData`, `KuiTongDiaryVN::setcoloseButton`, `KuiTongDiaryVN::confirmCallBackFunc`, `KuiTongDiaryVN::buttonCallBackFunc`, `KuiTongDiaryVN::closePopLayer`, `KuiTongDiaryVN::onTouchBegan`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `g_StrLower`→KStrBase.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `confirmCallBackFunc`→KuiTongDelegateVN.cpp, `ApplyChangeAnnounce`→KPlayerTong.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp

## `vn/gameui/KuiTongDiaryVN.h`
- 51 dòng. KuiTongDiaryVN.h
- Gọi tới: `KuiTongDiaryVN`→KuiTongDiaryVN.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `confirmCallBackFunc`→KuiTongDelegateVN.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp

## `vn/gameui/KuiTongInfoVN.cpp`
- 1946 dòng. (không có chú thích đầu)
- Hàm: `KuiTongInfoVN`, `KuiTongInfoVN`, `KuiTongInfoVN::create`, `KuiTongInfoVN::init`, `KuiTongInfoVN::addDialogData`, `KuiTongInfoVN::RefeshTongInfo`, `KuiTongInfoVN::ClearInfo`, `KuiTongInfoVN::setcoloseButton`, `GetFaction`, `GetSearchType`, `KuiTongInfoVN::UpdateInfo`, `KuiTongInfoVN::UpdateTongAnnounce`, `KuiTongInfoVN::UpdateMemberList`, `KuiTongInfoVN::UpdateMemberPower`, `KuiTongInfoVN::UpdatePlayerPower`, `KuiTongInfoVN::onTouchBegan`, `KuiTongInfoVN::onTouchMoved`, `KuiTongInfoVN::onTouchEnded`, `KuiTongInfoVN::closeChangeCallback`, `KuiTongInfoVN::HideShowFunc`, `KuiTongInfoVN::LoadTongFunc`, `KuiTongInfoVN::CheckRoleCanDo`, `KuiTongInfoVN::selectedMainListItemEvent`, `KuiTongInfoVN::UseMasterCallback`, `KuiTongInfoVN::UseKickCallback` …(+24)
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `isFileExist`→KgameWorld.cpp, `g_FileName2Id`→KFilePath.cpp, `g_StrLower`→KStrBase.cpp, `ApplyInfo`→KPlayerTong.cpp, `g_Atoui`→KStrBase.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `getColorIndex`→Text.cpp, `Clear`→KIniFile.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `findinidata_one`→Kgetinidata.cpp, `setContentSize`→ComboBox.cpp

## `vn/gameui/KuiTongInfoVN.h`
- 163 dòng. (không có chú thích đầu)
- Gọi tới: `KuiTongInfoVN`→KuiTongInfoVN.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `UpdateMemberList`→KuiTongInfoVN.cpp, `UpdateInfo`→KuiTongInfoVN.cpp, `UpdateTongAnnounce`→KuiTongInfoVN.cpp, `UpdateMemberPower`→KuiTongInfoVN.cpp, `UpdatePlayerPower`→KuiTongInfoVN.cpp, `RefeshTongInfo`→KuiTongInfoVN.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `HideShowFunc`→KuiTongInfoVN.cpp, `CheckRoleCanDo`→KuiTongInfoVN.cpp, `LoadTongFunc`→KuiTongInfoVN.cpp, `ClearInfo`→KuiTongInfoVN.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp

## `vn/gameui/KuiTongListVN.cpp`
- 254 dòng. (không có chú thích đầu)
- Hàm: `KuiTongListVN`, `KuiTongListVN`, `KuiTongListVN::create`, `KuiTongListVN::init`, `KuiTongListVN::addDialogData`, `KuiTongListVN::UpdateMemberList`, `KuiTongListVN::setcoloseButton`, `KuiTongListVN::btnCallBackFunc`, `KuiTongListVN::buttonCallBackFunc`, `KuiTongListVN::onTouchBegan`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `isFileExist`→KgameWorld.cpp, `ApplyInfo`→KPlayerTong.cpp, `g_StrLower`→KStrBase.cpp, `g_FileName2Id`→KFilePath.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `UpdateMemberList`→KuiTongInfoVN.cpp, `btnCallBackFunc`→KuiEscInfo.cpp, `onTouchBegan`→KHRocker - Copy.cpp

## `vn/gameui/KuiTongListVN.h`
- 51 dòng. (không có chú thích đầu)
- Gọi tới: `KuiTongListVN`→KuiTongListVN.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `UpdateMemberList`→KuiTongInfoVN.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `btnCallBackFunc`→KuiEscInfo.cpp, `onTouchBegan`→KHRocker - Copy.cpp

## `vn/gameui/KuiTongMemberChangeVN.cpp`
- 211 dòng. #include "gamecore/KPlayer.h"
- Hàm: `KuiTongMemberChangeVN`, `KuiTongMemberChangeVN`, `KuiTongMemberChangeVN::create`, `KuiTongMemberChangeVN::init`, `KuiTongMemberChangeVN::addDialogData`, `KuiTongMemberChangeVN::setcoloseButton`, `KuiTongMemberChangeVN::confirmCallBackFunc`, `KuiTongMemberChangeVN::buttonCallBackFunc`, `KuiTongMemberChangeVN::closePopLayer`, `KuiTongMemberChangeVN::onTouchBegan`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `g_StrLower`→KStrBase.cpp, `isFileExist`→KgameWorld.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `g_FileName2Id`→KFilePath.cpp, `TongOperation`→CoreShell.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `confirmCallBackFunc`→KuiTongDelegateVN.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp

## `vn/gameui/KuiTongMemberChangeVN.h`
- 54 dòng. KuiTongCreate.h
- Gọi tới: `KuiTongMemberChangeVN`→KuiTongMemberChangeVN.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `confirmCallBackFunc`→KuiTongDelegateVN.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp

## `vn/gameui/KuiTongNameVN.cpp`
- 238 dòng. 创建确定弹出框
- Hàm: `KuiTongNameVN`, `KuiTongNameVN`, `KuiTongNameVN::create`, `KuiTongNameVN::init`, `KuiTongNameVN::addDialogData`, `KuiTongNameVN::setcoloseButton`, `KuiTongNameVN::confirmCallBackFunc`, `KuiTongNameVN::buttonCallBackFunc`, `KuiTongNameVN::closePopLayer`, `KuiTongNameVN::onTouchBegan`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `g_StrLower`→KStrBase.cpp, `isFileExist`→KgameWorld.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `g_FileName2Id`→KFilePath.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `confirmCallBackFunc`→KuiTongDelegateVN.cpp, `ccMessageBox_new`→KCore.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp

## `vn/gameui/KuiTongNameVN.h`
- 59 dòng. KuiTongNameVN.h
- Gọi tới: `KuiTongNameVN`→KuiTongNameVN.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `confirmCallBackFunc`→KuiTongDelegateVN.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp

## `vn/gameui/KuiTongPositionVN.cpp`
- 420 dòng. (không có chú thích đầu)
- Hàm: `KuiTongPositionVN`, `KuiTongPositionVN`, `KuiTongPositionVN::create`, `KuiTongPositionVN::init`, `KuiTongPositionVN::addDialogData`, `KuiTongPositionVN::setcoloseButton`, `KuiTongPositionVN::btnCallBackFunc`, `KuiTongPositionVN::confirmCallBackFunc`, `KuiTongPositionVN::buttonCallBackFunc`, `KuiTongPositionVN::closePopLayer`, `KuiTongPositionVN::onTouchBegan`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `isFileExist`→KgameWorld.cpp, `g_StrLower`→KStrBase.cpp, `g_FileName2Id`→KFilePath.cpp, `create`→KHRocker.cpp, `ApplyInstate`→KPlayerTong.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `btnCallBackFunc`→KuiEscInfo.cpp, `confirmCallBackFunc`→KuiTongDelegateVN.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp

## `vn/gameui/KuiTongPositionVN.h`
- 64 dòng. KuiTongCreate.h
- Gọi tới: `KuiTongPositionVN`→KuiTongPositionVN.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `confirmCallBackFunc`→KuiTongDelegateVN.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `btnCallBackFunc`→KuiEscInfo.cpp, `onTouchBegan`→KHRocker - Copy.cpp

## `vn/gameui/KuiTongPowerVN.cpp`
- 346 dòng. (không có chú thích đầu)
- Hàm: `KuiTongPowerVN`, `KuiTongPowerVN`, `KuiTongPowerVN::create`, `KuiTongPowerVN::init`, `KuiTongPowerVN::addDialogData`, `KuiTongPowerVN::setcoloseButton`, `KuiTongPowerVN::buttonCallBackFunc`, `KuiTongPowerVN::valueChanged`, `KuiTongPowerVN::UpdateMemberPower`, `KuiTongPowerVN::onTouchBegan`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `isFileExist`→KgameWorld.cpp, `g_StrLower`→KStrBase.cpp, `g_FileName2Id`→KFilePath.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `ApplyInfo`→KPlayerTong.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `valueChanged`→KuiAutoPlay.cpp, `ApplyPower`→KPlayerTong.cpp, `UpdateMemberPower`→KuiTongInfoVN.cpp, `onTouchBegan`→KHRocker - Copy.cpp

## `vn/gameui/KuiTongPowerVN.h`
- 68 dòng. KuiTongInfo.h
- Gọi tới: `KuiTongPowerVN`→KuiTongPowerVN.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `UpdateMemberPower`→KuiTongInfoVN.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `valueChanged`→KuiAutoPlay.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp

## `vn/gameui/KuiTongSearchVN.cpp`
- 378 dòng. popLayer->addDialogData();
- Hàm: `KuiTongSearchVN`, `KuiTongSearchVN`, `KuiTongSearchVN::create`, `KuiTongSearchVN::init`, `KuiTongSearchVN::setcoloseButton`, `KuiTongSearchVN::btnConfirmCallBackFunc`, `KuiTongSearchVN::btnCallBackFunc`, `KuiTongSearchVN::buttonCallBackFunc`, `KuiTongSearchVN::closePopLayer`, `KuiTongSearchVN::onTouchBegan`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `isFileExist`→KgameWorld.cpp, `g_StrLower`→KStrBase.cpp, `g_FileName2Id`→KFilePath.cpp, `ApplyInfo`→KPlayerTong.cpp, `create`→KHRocker.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `btnCallBackFunc`→KuiEscInfo.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `btnConfirmCallBackFunc`→KuiTongChangeCamVN.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp

## `vn/gameui/KuiTongSearchVN.h`
- 61 dòng. KuiTongChangeCam.h
- Gọi tới: `KuiTongSearchVN`→KuiTongSearchVN.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `btnCallBackFunc`→KuiEscInfo.cpp, `btnConfirmCallBackFunc`→KuiTongChangeCamVN.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp

## `vn/gameui/KuiTopControlVN.cpp`
- 509 dòng. ´´½¨È·¶¨µ¯³ö¿ò tuanlnv2
- Hàm: `KuiTopControlVN::create_`, `KuiTopControlVN::init`, `KuiTopControlVN::addDialogData`, `KuiTopControlVN::upRoleInfo`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `g_StrLower`→KStrBase.cpp, `setContentSize`→ComboBox.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `isFileExist`→KgameWorld.cpp, `Load`→KIniFile.cpp, `GetInteger`→KTabFile.cpp, `Clear`→KIniFile.cpp, `create_`→KuiFaceSelector.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `g_FileName2Id`→KFilePath.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `setTouchEnabled`→KHRocker - Copy.cpp

## `vn/gameui/KuiTopControlVN.h`
- 37 dòng. class KImmediaItem_
- Gọi tới: `init`→HelloWorldScene.cpp, `create_`→KuiFaceSelector.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `upRoleInfo`→KuiFaceSelector.cpp

## `vn/gameui/KuiUnLockChestVN.cpp`
- 223 dòng. (không có chú thích đầu)
- Hàm: `KuiUnLockChestVN`, `KuiUnLockChestVN`, `KuiUnLockChestVN::create`, `KuiUnLockChestVN::init`, `KuiUnLockChestVN::addDialogData`, `KuiUnLockChestVN::setcoloseButton`, `KuiUnLockChestVN::OpenChestCallBackFunc`, `KuiUnLockChestVN::buttonCallBackFunc`, `KuiUnLockChestVN::closePopLayer`, `KuiUnLockChestVN::onTouchBegan`, `KuiUnLockChestVN::getRect`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `g_StrLower`→KStrBase.cpp, `ccMessageBox_new`→KCore.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `SendClientCPUnlockCmd`→KProtocol.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `vn/gameui/KuiUnLockChestVN.h`
- 44 dòng. (không có chú thích đầu)
- Gọi tới: `KuiUnLockChestVN`→KuiUnLockChestVN.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `OpenChestCallBackFunc`→KuiUnLockChestVN.cpp, `closePopLayer`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `getRect`→KuiAttackSkillsMenu.cpp

## `vn/gameui/KuiViewRoleStateVN.cpp`
- 404 dòng. (không có chú thích đầu)
- Hàm: `KuiViewRoleStateVN::create`, `KuiViewRoleStateVN::init`, `KuiViewRoleStateVN::addDialogData`, `KuiViewRoleStateVN::setcoloseButton`, `KuiViewRoleStateVN::addpicBox`, `KuiViewRoleStateVN::onTouchBegan`, `KuiViewRoleStateVN::UpdateBaseData`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `g_StrLower`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `init`→HelloWorldScene.cpp, `isFileExist`→KgameWorld.cpp, `Size`→KFile.cpp, `GetGameData`→CoreShell.cpp, `getDialogPosition`→KuiEffect.cpp, `getDialogSize`→KuiEffect.cpp, `getRect`→KuiAttackSkillsMenu.cpp, `UpdateData`→KuiCometoMap.cpp, `g_FileName2Id`→KFilePath.cpp

## `vn/gameui/KuiViewRoleStateVN.h`
- 32 dòng. (không có chú thích đầu)
- Gọi tới: `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `addpicBox`→KuiRoleState.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `UpdateBaseData`→KuiRoleState.cpp

## `vn/gameui/KuiWarnInfoVN.cpp`
- 306 dòng. if  (!g_pCoreShell) return;
- Hàm: `KuiWarnInfoVN::ccMessageBox_new`, `KuiWarnInfoVN::addDialogData`, `KuiWarnInfoVN::sendAccInfoToRelink`, `KuiWarnInfoVN::EnterGame`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `GetString`→KTabFile.cpp, `ccMessageBox_new`→KCore.cpp, `setTouchEnabled`→KHRocker - Copy.cpp, `Load`→KIniFile.cpp, `setBreakTheead`→SocketClient.cpp, `Clear`→KIniFile.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `sendAccInfoToRelink`→KuiWarnInfo.cpp, `Cleanup`→ClientStage.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `Start`→KTimer.cpp, `buttonCallBackFunc`→KuiAttackSkillsMenu.cpp, `reSet`→AutoPathFinder.cpp

## `vn/gameui/KuiWarnInfoVN.h`
- 24 dòng. Created by 2018.10 �ᵶ����Ц QQ:25557432
- Gọi tới: `ccMessageBox_new`→KCore.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `sendAccInfoToRelink`→KuiWarnInfo.cpp, `EnterGame`→KuiSelPlayer_new.cpp

## `vn/gameui/KuigetStringVN.cpp`
- 180 dòng. 创建确定弹出框
- Hàm: `KuigetStringVN::create`, `KuigetStringVN::addDialogData`, `KuigetStringVN::update`
- Gọi tới: `create`→KHRocker.cpp, `t_sprintf`→KStrBase.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp, `setTitle`→PopupLayer.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `g_StrLower`→KStrBase.cpp, `findinidata_one`→Kgetinidata.cpp, `update`→KgameWorld.cpp, `GetGameData`→CoreShell.cpp

## `vn/gameui/KuigetStringVN.h`
- 26 dòng. Created by 2018.10 横刀向天笑 QQ:25557432
- Gọi tới: `update`→KgameWorld.cpp, `create`→KHRocker.cpp, `addDialogData`→KuiAttackSkillsMenu.cpp

## `vn/gameui/KuistoreBoxVN.cpp`
- 1127 dòng. #include "../engine/KPalette.h"
- Hàm: `KuistoreBoxVN`, `KuistoreBoxVN::create`, `KuistoreBoxVN::init`, `KuistoreBoxVN::setcoloseButton`, `KuistoreBoxVN::changeStoreCallBackFunc`, `KuistoreBoxVN::sendMoneyCallBackFunc`, `KuistoreBoxVN::closesavemonyPadCallback`, `KuistoreBoxVN::ChangeLockCallBackFunc`, `KuistoreBoxVN::DelLockCallBackFunc`, `KuistoreBoxVN::Lock_Unlock_CallBackFunc`, `KuistoreBoxVN::CloseLockCallback`, `KuistoreBoxVN::UpdateExItem`, `KuistoreBoxVN::selectedItemEvent`, `KuistoreBoxVN::UpdateData`, `KuistoreBoxVN::AddObject`, `KuistoreBoxVN::getFreePosition`, `KuistoreBoxVN::update`
- Gọi tới: `t_sprintf`→KStrBase.cpp, `create`→KHRocker.cpp, `findinidata_one`→Kgetinidata.cpp, `g_StrLower`→KStrBase.cpp, `Size`→KFile.cpp, `setContentSize`→ComboBox.cpp, `isFileExist`→KgameWorld.cpp, `setVisible_e`→KuiEffect.cpp, `addChild_e`→KuiEffect.cpp, `setDialogTagKey`→KuiEffect.cpp, `UpdateData`→KuiCometoMap.cpp, `g_FileName2Id`→KFilePath.cpp, `findChildByKey`→KuiEffect.cpp, `GetGameData`→CoreShell.cpp, `GetID`→KFaction.cpp

## `vn/gameui/KuistoreBoxVN.h`
- 58 dòng. (không có chú thích đầu)
- Gọi tới: `init`→HelloWorldScene.cpp, `KuistoreBoxVN`→KuistoreBoxVN.cpp, `create`→KHRocker.cpp, `setcoloseButton`→KuiAttackSkillsMenu.cpp, `changeStoreCallBackFunc`→KuistoreBoxVN.cpp, `sendMoneyCallBackFunc`→KuistoreBoxVN.cpp, `closesavemonyPadCallback`→KuiItem.cpp, `ChangeLockCallBackFunc`→KuistoreBoxVN.cpp, `DelLockCallBackFunc`→KuistoreBoxVN.cpp, `CloseLockCallback`→KuistoreBoxVN.cpp, `Lock_Unlock_CallBackFunc`→KuistoreBoxVN.cpp, `UpdateData`→KuiCometoMap.cpp, `UpdateExItem`→KuistoreBox.cpp, `selectedItemEvent`→KuiChatList.cpp, `update`→KgameWorld.cpp

## `vn/gameui/UiglobaldataVN.cpp`
- 256 dòng. copyData(copysrc[i], copydst[i]);//-- /storage/emulated/0/Download/com.konis.jx1m.cocos.mobile/jx50a
- Hàm: `InitAuto`, `creatAutoPlayDir`, `CreateFolder`, `DelFile`, `isFileExist`, `copyData`, `copyFileResource`, `getTempDirectory`, `KSG_GetCurSec`, `KSG_StringGetValue`
- Gọi tới: `isFileExist`→KgameWorld.cpp, `copyData`→KgameWorld.cpp, `t_sprintf`→KStrBase.cpp, `CreateFolder`→KMapMusic.cpp, `ClientShowMsg`→KNpc.cpp, `CreatFile`→KTabFile.cpp

## `vn/gameui/UiglobaldataVN.h`
- 35 dòng. #define UOC_PLAYERSHOP 101
- Gọi tới: `InitAuto`→UiglobaldataVN.cpp, `creatAutoPlayDir`→UiglobaldataVN.cpp, `CreateFolder`→KMapMusic.cpp, `DelFile`→UiglobaldataVN.cpp, `isFileExist`→KgameWorld.cpp, `copyData`→KgameWorld.cpp, `copyFileResource`→UiglobaldataVN.cpp, `getTempDirectory`→UiglobaldataVN.cpp, `KSG_GetCurSec`→UiglobaldataVN.cpp, `KSG_StringGetValue`→UiglobaldataVN.cpp

## `vn/gameui/combobox/ComboBox.cpp`
- 352 dòng. (không có chú thích đầu)
- Hàm: `ComboBox`, `ComboBox::create`, `ComboBox::getLabel`, `ComboBox::setLabel`, `ComboBox::init`, `ComboBox::setComboBoxDataList`, `ComboBox::setComboBoxDataFromContinuousInt`, `ComboBox::setComboBoxDataFromContinuousFloat`, `ComboBox::clearDataList`, `ComboBox::setContentSize`, `ComboBox::onTouchBegan`, `ComboBox::onTouchMoved`, `ComboBox::onTouchEnded`, `ComboBox::onTouchCancelled`, `ComboBox::touchUpInside`, `ComboBoxTableViewLayer`, `ComboBoxTableViewLayer::create`, `ComboBoxTableViewLayer::init`, `ComboBoxTableViewLayer::tableCellTouched`, `ComboBoxTableViewLayer::cellSizeForTable`, `ComboBoxTableViewLayer::tableCellAtIndex`, `ComboBoxTableViewLayer::numberOfCellsInTableView`, `ComboBoxTableViewLayer::reloadDataList`, `ComboBoxTableViewLayer::onTouchBegan`, `ComboBoxTableViewLayer::onTouchMoved` …(+2)
- Gọi tới: `create`→KHRocker.cpp, `init`→HelloWorldScene.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchCancelled`→KHRocker.cpp, `setTouchEnabled`→KHRocker - Copy.cpp

## `vn/gameui/combobox/ComboBox.h`
- 101 dòng. (không có chú thích đầu)
- Gọi tới: `ComboBox`→ComboBox.cpp, `init`→HelloWorldScene.cpp, `create`→KHRocker.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `onTouchCancelled`→KHRocker.cpp, `ComboBoxTableViewLayer`→ComboBox.cpp, `touchUpInside`→ComboBox.cpp, `setComboBoxDataList`→ComboBox.cpp, `setComboBoxDataFromContinuousInt`→ComboBox.cpp, `setComboBoxDataFromContinuousFloat`→ComboBox.cpp, `clearDataList`→ComboBox.cpp, `getLabel`→ComboBox.cpp, `setLabel`→ComboBox.cpp

## `vn/gameui/combobox/MyTableView.cpp`
- 92 dòng. CCLog("touch begin");
- Hàm: `MyTableView::create`, `MyTableView::create`, `MyTableView::onTouchBegan`, `MyTableView::onTouchMoved`, `MyTableView::onTouchEnded`
- Gọi tới: `create`→KHRocker.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp, `cellSizeForTable`→ComboBox.cpp, `numberOfCellsInTableView`→ComboBox.cpp, `tableCellTouched`→ComboBox.cpp

## `vn/gameui/combobox/MyTableView.h`
- 31 dòng. #include <sys/time.h>
- Gọi tới: `create`→KHRocker.cpp, `onTouchBegan`→KHRocker - Copy.cpp, `onTouchMoved`→KHRocker - Copy.cpp, `onTouchEnded`→KHRocker - Copy.cpp

