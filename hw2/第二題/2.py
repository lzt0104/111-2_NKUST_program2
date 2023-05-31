from password import PD

encrypted_password = input("請輸入加密後的密碼 Y：")
decrypter = PD(encrypted_password)
decrypted_password = decrypter.decrypt()
print("解密後的密碼 X：", decrypted_password)