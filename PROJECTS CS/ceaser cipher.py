def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char  # Keep punctuation/spaces as-is
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("🔐 Caesar Cipher Encryption/Decryption Tool 🔐")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()

    if choice not in ['E', 'D']:
        print("❌ Invalid choice. Please select E or D.")
        return

    message = input("Enter your message: ")

    try:
        shift = int(input("Enter the shift value (number): "))
    except ValueError:
        print("❌ Shift must be a number.")
        return

    if choice == 'E':
        encrypted = encrypt(message, shift)
        print("🔒 Encrypted Message:", encrypted)
    else:
        decrypted = decrypt(message, shift)
        print("🔓 Decrypted Message:", decrypted)


if __name__ == "__main__":
    main()
