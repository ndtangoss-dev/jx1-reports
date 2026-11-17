# L-03 - Quy trình dựng APK client (17/11/2026)

## TÓM TẮT
1. Máy thật dựng được APK; mất khoảng vài chục phút ở mức ưu tiên BelowNormal.
2. APK ký bằng khóa debug trong `D:\Android\user` (cert SHA-256 bắt đầu `a48601f7…`). Không tạo khóa mới, không in/ghi mật khẩu, không commit khóa hay APK.
3. Cài đè cần: cùng package `com.jxclient.hoiuctruyenky`, cùng khóa, versionCode cao hơn (jx-qh7 = 17).
4. Luôn build từ BẢN COPY của `D:\JX-backup\Client-qh7`, không build trên `D:\Android\b\Client`.
5. Phát APK: đặt vào `D:\JX1_U003_build\serve` (cổng 8091 đã chạy sẵn trên địa chỉ Tailscale máy thật, không đụng forwarder 56722/51189).
Cần tôi quyết định: không

## Các bước
1. Sao chép: `robocopy <bản vá> D:\JX-build\<tên> /E /XD .git`. Sửa `proj.android\app\build.gradle`: `versionCode` lớn hơn 17.
2. Biến môi trường (chỉ trong phiên): `JAVA_HOME=D:\Android\jdk`, `ANDROID_HOME=D:\Android\sdk`, `ANDROID_USER_HOME=D:\Android\user` (bắt buộc, nếu thiếu Gradle tạo khóa mới và cài đè hỏng), `GRADLE_USER_HOME=D:\Android\gradle`, `GRADLE_OPTS=-Xmx512m`.
3. Build từ `<bản copy>\proj.android`:
   `D:\Android\gradle-8.7\bin\gradle.bat assembleDebug --offline --no-daemon -PPROP_APP_ABI=arm64-v8a -Dorg.gradle.jvmargs=-Xmx12g`
   Đặt `PriorityClass=BelowNormal` cho tiến trình. Kết quả: `app\build\outputs\apk\debug\projectdebug-debug.apk`. Chú ý: thư mục `build` được copy theo, nên kiểm tra thời gian file, tránh lấy nhầm bản cũ.
4. Kiểm tra: `aapt2 dump badging` (versionCode), `apksigner verify --print-certs` (cert `a48601f7…`), ghi SHA-256.
5. Đổi tên riêng (vd `jx-qh9-smooth-A.apk`), chép vào `D:\JX1_U003_build\serve`. Không ghi đè `jx-qh7.apk`.
6. Link: `http://100.95.186.86:8091/<tên>.apk` (chỉ điện thoại Tailscale `100.123.183.6` vào được).
7. Máy chủ APK trỏ tới: giữ nguyên cấu hình client qh7 (chưa đổi `package.ini`).

## Lưu ý
- Mã nguồn client là GBK: vá bằng Python latin-1 với mỏ neo duy nhất.
- Hoàn tác bản vá L-02: `git apply -R L02/A-subpixel.patch`.
- Chưa kiểm tra: build lại khi xây từ máy khác.
