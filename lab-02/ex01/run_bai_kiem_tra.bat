@echo off
echo Bai Kiem Tra Buoi 6 - Ma Hoa
echo =======================================

REM Kiểm tra môi trường ảo
IF EXIST "..\.venv\Scripts\activate.bat" (
    echo Dang kich hoat moi truong ao...
    call "..\.venv\Scripts\activate.bat"
) ELSE (
    echo Kiem tra cai dat Flask va PyQt5...
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
)

REM Kiểm tra API server trong lab-03 có đang chạy không
echo Kiem tra API server dang chay...
powershell -Command "if ((Get-NetTCPConnection -LocalPort 5000 -ErrorAction SilentlyContinue).Count -eq 0) { echo 'API server chua chay, dang khoi dong...' } else { echo 'API server da duoc chay' }"

REM Khởi động API server trong một cửa sổ mới
start cmd /k "cd ..\lab-03 && python api.py"

REM Đợi 2 giây để API server khởi động
timeout /t 2 /nobreak > nul

REM Chạy ứng dụng web
echo Dang khoi dong ung dung web tren cong 5050...
start cmd /k "python app.py"

echo.
echo Dang mo trinh duyet web...
REM Mở trình duyệt web với địa chỉ của ứng dụng
timeout /t 3 /nobreak > nul
start http://localhost:5050

echo.
echo Huong dan:
echo - Truy cap vao http://localhost:5050 neu trinh duyet khong tu dong mo
echo - Click vao cac link tren trang web de mo form ma hoa tuong ung
echo - Nhan Ctrl+C trong cua so terminal de dung cac ung dung
echo.
pause
