@echo off
echo ======================================
echo = BAI KIEM TRA TICH HOP LAB-02 + LAB-03 =
echo ======================================

REM Cài đặt các thư viện cần thiết
echo Dang cai dat cac thu vien can thiet...
pip install flask PyQt5 requests

REM Đường dẫn tới các file quan trọng
set ROOT_DIR=C:\Users\pc\Desktop\bmttnc-hutech-2280601823
set LAB02_DIR=%ROOT_DIR%\lab-02\ex01
set LAB03_DIR=%ROOT_DIR%\lab-03

REM Chạy API server của lab-03 
echo Dang khoi dong API server...
start cmd /k "cd %LAB03_DIR% && python api.py"

REM Đợi 3 giây để API server khởi động
echo Dang cho API server khoi dong...
timeout /t 3 /nobreak > nul

REM Chạy web server với file app sửa lỗi
echo Dang khoi dong web server...
start cmd /k "cd %LAB02_DIR% && python app_fixed.py"

REM Đợi 2 giây để web server khởi động
echo Dang cho web server khoi dong...
timeout /t 2 /nobreak > nul

REM Mở trình duyệt
echo Dang mo trinh duyet web...
start http://localhost:5050

echo.
echo HUONG DAN SU DUNG:
echo 1. Truy cap http://localhost:5050
echo 2. Click vao cac nut ma hoa de mo form tuong ung
echo 3. Neu co loi, hay kiem tra trong cua so terminal
echo.
pause
