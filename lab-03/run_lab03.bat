@echo off
echo Starting Lab 03 API Server...

REM Kiểm tra xem môi trường ảo có tồn tại không
IF EXIST "..\\.venv\\Scripts\\activate.bat" (
    echo Activating virtual environment...
    call "..\\.venv\\Scripts\\activate.bat"
) ELSE (
    echo Virtual environment not found. Creating new one...
    python -m venv ..\.venv
    call "..\\.venv\\Scripts\\activate.bat"
    echo Installing dependencies...
    pip install -r requirements.txt
)

REM Chạy API server
start cmd /k "echo Starting API Server... && python api.py"

REM Đợi 2 giây để server khởi động
timeout /t 2 /nobreak > nul

REM Hiển thị menu cho người dùng chọn
echo.
echo ==== Lab 03 Cryptography Applications ====
echo 1. Caesar Cipher
echo 2. Vigenere Cipher
echo 3. Playfair Cipher
echo 4. Rail Fence Cipher
echo 5. Exit
echo.

:menu
set /p choice="Choose a cipher (1-5): "

if "%choice%"=="1" (
    echo Starting Caesar Cipher Application...
    start cmd /k "python caesar_cipher.py"
    goto menu
) else if "%choice%"=="2" (
    echo Starting Vigenere Cipher Application...
    start cmd /k "python vigenere_cipher.py" 
    goto menu
) else if "%choice%"=="3" (
    echo Starting Playfair Cipher Application...
    start cmd /k "python playfair_cipher.py"
    goto menu
) else if "%choice%"=="4" (
    echo Starting Rail Fence Cipher Application...
    start cmd /k "python railfence_cipher.py"
    goto menu
) else if "%choice%"=="5" (
    echo Exiting...
    exit
) else (
    echo Invalid choice. Please try again.
    goto menu
)
