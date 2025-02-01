class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, message):
        encrypted_message = ""
        for char in message:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                encrypted_char = chr((ord(char) - ascii_offset + self.shift) % 26 + ascii_offset)
                encrypted_message += encrypted_char
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt(self, encrypted_message):
        decrypted_message = ""
        for char in encrypted_message:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                decrypted_char = chr((ord(char) - ascii_offset - self.shift) % 26 + ascii_offset)
                decrypted_message += decrypted_char
            else:
                decrypted_message += char
        return decrypted_message

def main():
    shift = int(input("Enter the shift value: "))
    cipher = CaesarCipher(shift)

    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Quit")

        option = input("Choose an option: ")

        if option == "1":
            message = input("Enter the message to encrypt: ")
            encrypted_message = cipher.encrypt(message)
            print(f"Encrypted message: {encrypted_message}")
        elif option == "2":
            encrypted_message = input("Enter the message to decrypt: ")
            decrypted_message = cipher.decrypt(encrypted_message)
            print(f"Decrypted message: {decrypted_message}")
        elif option == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()

