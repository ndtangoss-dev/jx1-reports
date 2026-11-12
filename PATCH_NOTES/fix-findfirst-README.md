Sua 1 dong trong gameserver/Sources/Core/Src/KSortScript.cpp:328 (ban build D:\JX-build\src18, co .bak):
  long dir = _findfirst("*.*", &FindData);   ->   intptr_t dir = _findfirst("*.*", &FindData);
Ly do: x64 tra handle 64-bit; `long` cat cut -> _findnext ghi vao dia chi rac 0xFFFFFFFFB4D86390 -> 0xC0000005 luc nap script (LoadScriptInDirectory).
minidbg.cs: bo go loi nho (CreateProcess DEBUG_ONLY_THIS_PROCESS, ghi RIP/stack + MiniDumpWriteDump) dung bat crash; chay trong VM JX-Test-36.
Ban goc repo SwordOnline chua sua. Con 3 cho `long ... _findfirst` khac o Goddess/S3Relay (32-bit, khong anh huong).
