import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.vigenere import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt_3.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt_3.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        key_text = self.ui.txt_key_3.toPlainText()
        plain_text = self.ui.txt_plain_text_3.toPlainText()
        if not key_text:
            QMessageBox.warning(self, "Lỗi", "Key không được để trống!")
            return
        if not plain_text:
            QMessageBox.warning(self, "Lỗi", "Plain text không được để trống!")
            return
        url = "http://127.0.0.1:5050/api/vigenere/encrypt"
        payload = {
            "plain_text": plain_text,
            "key": key_text
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                encrypted = data.get("encrypted_text")
                if encrypted:
                    self.ui.txt_cipher_text_3.setText(encrypted)

                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Encryption Successful")
                    msg.exec_()
                else:
                    QMessageBox.warning(self, "Lỗi", "API không trả về kết quả mã hóa hợp lệ!")
            else:
                QMessageBox.warning(self, "Lỗi", f"Lỗi khi gọi API: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi kết nối API: {e}")

    def call_api_decrypt(self):
        key_text = self.ui.txt_key_3.toPlainText()
        cipher_text = self.ui.txt_cipher_text_3.toPlainText()
        if not key_text:
            QMessageBox.warning(self, "Lỗi", "Key không được để trống!")
            return
        if not cipher_text:
            QMessageBox.warning(self, "Lỗi", "Cipher text không được để trống!")
            return
        url = "http://127.0.0.1:5050/api/vigenere/decrypt"
        payload = {
            "cipher_text": cipher_text,
            "key": key_text
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                decrypted = data.get("decrypted_text")
                if decrypted:
                    self.ui.txt_plain_text_3.setText(decrypted)

                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Decrypted Successfully")
                    msg.exec_()
                else:
                    QMessageBox.warning(self, "Lỗi", "API không trả về kết quả giải mã hợp lệ!")
            else:
                QMessageBox.warning(self, "Lỗi", f"Lỗi khi gọi API: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi kết nối API: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())