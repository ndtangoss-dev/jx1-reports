# Dựng APK debug và sự cố VirtualBox

## TÓM TẮT 5 DÒNG
1. Đã dựng APK debug `arm64-v8a` trên bản copy ở ổ D:, 78,9 MB, ký bằng khóa Android Debug.
2. APK có `package.ini` trỏ địa chỉ Tailscale máy thật, `network_security_config` có 2 địa chỉ Tailscale. Keystore thật không bị đụng.
3. Lỗi `Java heap space` là do client Gradle chỉ có 64 MB, không phải heap build. Sửa bằng client 512 MB và ghi log thẳng ra file.
4. `VBoxSVC` crash khi snapshot live; VM phải tắt cứng, sau đó khởi động lại được, không lỗi đĩa. 5 exe server chưa chạy lại.
5. Chưa cài APK lên điện thoại, chưa mở cổng, chưa thử vào game.

Cần tôi quyết định: có

## Đã làm
- Cài vào `D:\Android`, không Admin, mỗi gói được chủ máy duyệt:
  - Temurin JDK 17.0.21 (SHA256 khớp).
  - Command-line tools (SHA1 khớp). `platforms;android-34`, `build-tools;34.0.0`, `ndk;25.2.9519653`, `cmake;3.30.5` qua `sdkmanager`.
  - Gradle 8.7 (SHA256 khớp), dùng thay `gradle-wrapper.jar` không rõ nguồn trong gói.
- Bản copy `D:\Android\b\Client`, không chép `*.jks`, `*.keystore`, `<file-mat-khau-keystore>`.
- Trong bản copy: `Resources\package.ini` thay bằng bản đã sinh, `network_security_config.xml` thêm 2 địa chỉ Tailscale, bỏ `jcenter()`.
- Rà script build: file Gradle không có lệnh chạy tiến trình hay URL lạ; CMake chỉ có lệnh chép file của cocos2d.
- Lệnh build: `--no-daemon`, `-Xmx12g`, `-PPROP_APP_ABI=arm64-v8a`, `GRADLE_OPTS=-Xmx512m`, `GRADLE_USER_HOME=D:\Android\gradle`. Tất cả chỉ trong phiên build, không đổi biến môi trường hệ thống.
- Không tạo snapshot cho bước build, theo yêu cầu của chủ máy.

## Bằng chứng
- `BUILD SUCCESSFUL in 2m 55s`.
- APK: `D:\Android\b\Client\proj.android\app\build\outputs\apk\debug\projectdebug-debug.apk`, SHA256 `A4E5A88CC911BF8C474444884482C5FD964B0E81334A216F4BBFEEA0851CCF50`.
- `aapt2`: `com.jxclient.hoiuctruyenky`, `native-code: arm64-v8a`, target SDK 34.
- `apksigner`: `CN=Android Debug`. Không có file keystore trong APK.
- `assets/package.ini` `down=` giải mã ra đúng địa chỉ Tailscale máy thật.
- `git status -- Folder`: bản gốc không đổi.

## Sự cố
- 15:56:45 `VBoxSVC.exe` crash (`0xc0000005`), 15:57:22 `VirtualBox.exe` crash, khi snapshot live `apk-bat-dau` đang chạy.
- Log VM dừng ở `detected unresponsive VBoxSVC`. Chủ máy chọn tắt cứng; VM bật lại lúc 16:07. Không có lỗi `Ntfs`, `disk`. SQL chạy, cấu hình và `roledb` rỗng còn nguyên.
- Nguyên nhân gốc của crash chưa xác định. `apk-bat-dau` (14,4 GB) còn trong danh sách, dở dang.
- Hết heap 3 lần: 10 GB, 16 GB (đã dừng giữa chừng, vượt giới hạn mới), 12 GB. Log tiến trình build chạy đúng `-Xmx12g`, không có `OutOfMemoryError`, chỉ có `client disconnection detected`. Client mặc định `-Xmx64m` bị ngập 238 572 dòng cảnh báo trình biên dịch.

## Chưa kiểm tra
- APK chưa cài lên thiết bị. Không biết client có tải và đăng nhập được không.
- File `app\release\projectdebug-release.apk` trong bản copy là bản cũ của gói, không phải bản dựng này.

## Bước kế
Chạy lại 5 exe (cần duyệt), mở cổng qua `tailscale_mo_cong.ps1 -WithCdn`, chạy `cdn_server.py`, cài APK lên điện thoại.
