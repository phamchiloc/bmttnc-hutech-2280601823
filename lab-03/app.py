from flask import Flask, request, jsonify

app = Flask(__name__)

def vigenere_decrypt(cipher_text, key):
    # Hàm giải mã Vigenere, bạn cần thay bằng code thật của bạn
    # Ví dụ đơn giản:
    decrypted = ""
    key = key.upper()
    cipher_text = cipher_text.upper()
    key_length = len(key)
    for i, char in enumerate(cipher_text):
        if char.isalpha():
            offset = (ord(char) - ord(key[i % key_length])) % 26
            decrypted += chr(ord('A') + offset)
        else:
            decrypted += char
    return decrypted

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt_api():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = data.get('key')
    if not cipher_text or not key:
        return jsonify({'error': 'Missing data'}), 400
    decrypted = vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted})

if __name__ == '__main__':
    app.run(debug=True)