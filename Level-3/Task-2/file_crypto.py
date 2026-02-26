from cryptography.fernet import Fernet


# Generate and save key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


# Load existing key
def load_key():
    return open("secret.key", "rb").read()


# Encrypt file
def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename + ".encrypted", "wb") as file:
        file.write(encrypted_data)

    print("File encrypted successfully!")


# Decrypt file
def decrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    new_name = filename.replace(".encrypted", ".decrypted")

    with open(new_name, "wb") as file:
        file.write(decrypted_data)

    print("File decrypted successfully!")


# Main program
if __name__ == "__main__":
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")

    choice = input("Choose an option: ")

    if choice == "1":
        generate_key()
        print("Key generated and saved as secret.key")

    elif choice == "2":
        file_name = input("Enter file name to encrypt: ")
        encrypt_file(file_name)

    elif choice == "3":
        file_name = input("Enter file name to decrypt: ")
        decrypt_file(file_name)

    else:
        print("Invalid choice")