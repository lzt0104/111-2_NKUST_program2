class PasswordDecrypter:
    def __init__(self, encrypted_password):
        self.encrypted_password = encrypted_password

    def decrypt_password(self):
        decrypted_password = ""
        for digit in self.encrypted_password:
            decrypted_digit = str((int(digit) * 3) % 10)
            decrypted_password += decrypted_digit
        return decrypted_password