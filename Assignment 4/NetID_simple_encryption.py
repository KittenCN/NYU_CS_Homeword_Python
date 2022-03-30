import NetID_encryption_module

if __name__ == "__main__":
    text = input("Enter the text: ")
    key = input("Enter the key: ")
    print("encrypt: " + NetID_encryption_module.encrypt(key, text))
    print("decrypt: " + NetID_encryption_module.decrypt(key, NetID_encryption_module.encrypt(key, text)))