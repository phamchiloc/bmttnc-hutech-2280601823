@app.route('/api/vigenere/decrypt', methods = ['POST'])
def Vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'encrypted_text': decrypted_text})  # Sai key name