from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayfairCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
import os
import sys
import subprocess
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

# ---------------- Caesar Routes ----------------
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# ---------------- Playfair Routes ----------------
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    cipher = PlayfairCipher(key)
    encrypted_text = cipher.encrypt(text)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    cipher = PlayfairCipher(key)
    decrypted_text = cipher.decrypt(text)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# ---------------- Vigenere Routes ----------------
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    cipher = VigenereCipher()
    encrypted_text = cipher.encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    cipher = VigenereCipher()
    decrypted_text = cipher.decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# ---------------- Rail Fence Routes ----------------
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    rails = int(request.form['inputKeyPlain'])
    cipher = RailFenceCipher()
    encrypted_text = cipher.encrypt(text, rails)
    return f"text: {text}<br/>rails: {rails}<br/>encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    rails = int(request.form['inputKeyCipher'])
    cipher = RailFenceCipher()
    decrypted_text = cipher.decrypt(text, rails)
    return f"text: {text}<br/>rails: {rails}<br/>decrypted text: {decrypted_text}"

# Route mới để mở các form từ lab-03
@app.route("/open-form/<cipher_type>")
def open_form(cipher_type):
    try:
        print(f"Đang mở form {cipher_type}...")
        
        # Đường dẫn đến thư mục lab-03
        current_dir = os.path.dirname(os.path.abspath(__file__))
        lab03_path = os.path.abspath(os.path.join(current_dir, '../../lab-03'))
        print(f"Đường dẫn lab-03: {lab03_path}")
        
        # Map tên cipher với file tương ứng
        app_map = {
            'caesar': 'caesar_cipher.py',
            'playfair': 'playfair_cipher.py',
            'vigenere': 'vigenere_cipher.py',
            'railfence': 'railfence_cipher.py'
        }
        
        if cipher_type not in app_map:
            print(f"Không tìm thấy ứng dụng: {cipher_type}")
            return jsonify({'status': 'error', 'message': f'Không tìm thấy ứng dụng: {cipher_type}'}), 404
        
        app_file = app_map[cipher_type]
        app_path = os.path.join(lab03_path, app_file)
        print(f"Đường dẫn ứng dụng: {app_path}")
        
        if not os.path.exists(app_path):
            print(f"File không tồn tại: {app_path}")
            return jsonify({'status': 'error', 'message': f'File không tồn tại: {app_path}'}), 404
        
        # Chạy ứng dụng PyQt trong một thread riêng biệt
        def run_app():
            print(f"Chạy lệnh: python {app_file}")
            subprocess.Popen([sys.executable, app_path], cwd=lab03_path)
            print(f"Đã khởi động form {cipher_type}")
        
        thread = threading.Thread(target=run_app)
        thread.daemon = True
        thread.start()
        
        return jsonify({'status': 'success', 'message': f'Đã mở form {cipher_type.title()} thành công'})
    except Exception as e:
        print(f"Lỗi: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
