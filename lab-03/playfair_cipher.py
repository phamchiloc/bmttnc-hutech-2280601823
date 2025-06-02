import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.playfair import Ui_MainWindow
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
        if not key_text:
            QMessageBox.warning(self, "Lỗi", "Key không được để trống!")
            return
        url = "http://127.0.0.1:5000/api/playfair/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain_text_3.toPlainText(),
            "key": key_text
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text_3.setText(data["encrypted_text"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encryption Successful")
                msg.exec_()
            else:
                print("error while calling API")
        except requests.exceptions.RequestException as e:
            print("error: %s" % e)

    def call_api_decrypt(self):
        key_text = self.ui.txt_key_3.toPlainText()
        if not key_text:
            QMessageBox.warning(self, "Lỗi", "Key không được để trống!")
            return
        url = "http://127.0.0.1:5000/api/playfair/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher_text_3.toPlainText(),
            "key": key_text
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text_3.setText(data["decrypted_text"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())