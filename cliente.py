# cliente.py
# Elaborado por Roberto Santos Moisés - A00823311
import requests
import os
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    return encrypted_data

def send_file(url, encrypted_data, key, filename):
    files = {'encrypted_image': (filename, encrypted_data, 'application/octet-stream')}
    data = {'key': key}
    response = requests.post(url, files=files, data=data)
    return response

def main():
    # Generar la llave de encriptación.
    key = Fernet.generate_key().decode()
    file_path = 'testimage.jpg'
    encrypted_data = encrypt_file(file_path, key)
    url = 'http://localhost:8000/upload/'
    response = send_file(url, encrypted_data, key, os.path.basename(file_path))
    print(response.text)

if __name__ == "__main__":
    main()
