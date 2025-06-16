from flask import Flask, request, jsonify
import sys
import os

# Thêm thư mục gốc vào sys.path để import được các module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import các module cần thiết
import vigenere_cipher as vigenere_module
import playfair_cipher as playfair_module
import railfence_cipher as railfence_module
import caesar_cipher as caesar_module

app = Flask(__name__)

# Vigenere cipher routes
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    # Giả sử vigenere_cipher là module có hàm vigenere_encrypt
    encrypted_text = vigenere_encrypt_impl(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_decrypt_impl(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# Playfair cipher routes
@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    # Implement playfair encrypt
    encrypted_text = playfair_encrypt_impl(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    # Implement playfair decrypt
    decrypted_text = playfair_decrypt_impl(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# Implement cipher algorithms
def vigenere_encrypt_impl(plain_text, key):
    # Đơn giản hóa cho ví dụ
    encrypted = ""
    key = key.upper()
    plain_text = plain_text.upper()
    key_length = len(key)
    for i, char in enumerate(plain_text):
        if char.isalpha():
            # E = (P + K) mod 26
            offset = (ord(char) - ord('A') + ord(key[i % key_length]) - ord('A')) % 26
            encrypted += chr(ord('A') + offset)
        else:
            encrypted += char
    return encrypted

def vigenere_decrypt_impl(cipher_text, key):
    # Đơn giản hóa cho ví dụ
    decrypted = ""
    key = key.upper()
    cipher_text = cipher_text.upper()
    key_length = len(key)
    for i, char in enumerate(cipher_text):
        if char.isalpha():
            # D = (C - K + 26) mod 26
            offset = (ord(char) - ord(key[i % key_length]) + 26) % 26
            decrypted += chr(ord('A') + offset)
        else:
            decrypted += char
    return decrypted

def playfair_encrypt_impl(plain_text, key):
    # Simple implementation for testing
    # In a real application, you would implement the proper Playfair algorithm
    return "ENCRYPTED: " + plain_text.upper()

def playfair_decrypt_impl(cipher_text, key):
    # Simple implementation for testing 
    return "DECRYPTED: " + cipher_text.upper()

if __name__ == '__main__':
    app.run(debug=True, port=5000)