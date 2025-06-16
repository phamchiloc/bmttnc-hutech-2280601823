@echo off
echo Ứng dụng Lab 02 - Các thuật toán mã hóa
echo =======================================

REM Kiểm tra môi trường ảo
IF EXIST "..\..\.venv\Scripts\activate.bat" (
    echo Đang kích hoạt môi trường ảo...
    call "..\..\.venv\Scripts\activate.bat"
) ELSE (
    echo Kiểm tra cài đặt Flask...
    pip show flask > nul 2>&1
    IF ERRORLEVEL 1 (
        echo Đang cài đặt Flask...
        pip install -r requirements.txt
    ) ELSE (
        echo Flask đã được cài đặt!
    )
)

echo.
echo Đang khởi động Flask Web Server trên cổng 5050...
echo Truy cập http://localhost:5050 để xem ứng dụng
echo.
echo Nhấn Ctrl+C để dừng ứng dụng
echo.

python app.py
