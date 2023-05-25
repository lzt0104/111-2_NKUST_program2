class PasswordDecrypter:
    def __init__(self, encrypted_password):
        self.encrypted_password = encrypted_password

    def decrypt_password(self):
        decrypted_digits = []
        for digit in str(self.encrypted_password):
            decrypted_digit = (int(digit) * 3) % 10
            decrypted_digits.append(str(decrypted_digit))
        decrypted_password = int(''.join(decrypted_digits))
        return decrypted_password


# 主程式
encrypted_password = input("請輸入加密後的密碼 Y：")
decrypter = PasswordDecrypter(encrypted_password)
decrypted_password = decrypter.decrypt_password()
print("解密後的密碼 X：", decrypted_password)
