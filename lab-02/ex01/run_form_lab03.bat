@echo off
echo Bai Kiem Tra Buoi 6 - Ma Hoa - PHI BAO LOC
echo =======================================

REM Kiểm tra và cài đặt các thư viện cần thiết
echo Kiem tra cac thu vien can thiet...
pip show flask > nul 2>&1
IF ERRORLEVEL 1 (
    echo Dang cai dat Flask...
    pip install flask
)
pip show PyQt5 > nul 2>&1
IF ERRORLEVEL 1 (
    echo Dang cai dat PyQt5...
    pip install PyQt5
)
pip show requests > nul 2>&1
IF ERRORLEVEL 1 (
    echo Dang cai dat Requests...
    pip install requests
)

REM Khởi động API server lab-03 trong một cửa sổ mới
echo Dang khoi dong API server lab-03...
cd ..\..\
set LAB_ROOT=%cd%
cd %LAB_ROOT%\lab-03
start cmd /k "python api.py"

REM Đợi 3 giây để API server khởi động
echo Dang cho API server khoi dong...
timeout /t 3 /nobreak > nul

REM Chạy ứng dụng web
cd %LAB_ROOT%\lab-02\ex01
echo Dang khoi dong ung dung web tren cong 5050...
start cmd /k "python app.py"

REM Đợi 3 giây để web server khởi động
echo Dang cho web server khoi dong...
timeout /t 3 /nobreak > nul

REM Mở trình duyệt web
echo Dang mo trinh duyet web...
start http://localhost:5050

echo.
echo === HUONG DAN SU DUNG ===
echo 1. Truy cap vao http://localhost:5050 neu trinh duyet khong tu dong mo
echo 2. Click vao cac nut tren trang web de mo form ma hoa tuong ung
echo 3. Da mo 2 cua so terminal: mot cho API server, mot cho web server
echo 4. De dung chuong trinh, dong ca hai cua so terminal bang cach nhan Ctrl+C hoac X
echo.
echo Neu xuat hien loi:
echo - Dam bao cong 5000 va 5050 khong bi su dung boi ung dung khac
echo - Dam bao PyQt5 va Flask da duoc cai dat dung cach
echo - Dam bao da dong tat ca cac phien ban dang chay cua ung dung
echo.

pause
