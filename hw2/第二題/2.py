from password_decrypter import PasswordDecrypter

encrypted_password = input("請輸入加密後的密碼 Y：")
decrypter = PasswordDecrypter(encrypted_password)
decrypted_password = decrypter.decrypt_password()
print("解密後的密碼 X：", decrypted_password)