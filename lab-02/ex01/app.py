from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayfairCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)  
