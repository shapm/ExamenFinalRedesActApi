# api.py
# Elaborado por Roberto Santos Moisés - A00823311
from fastapi import FastAPI, File, Form, UploadFile
from cryptography.fernet import Fernet
import os

app = FastAPI()

# Si no existe el directorio para guardar las imagenes, crearlo
if not os.path.exists("decrypted_images"):
    os.makedirs("decrypted_images")

# Ruta para recibir la imágen
@app.post("/upload/")
async def upload_file(encrypted_image: UploadFile = File(...), key: str = Form(...)):
    fernet = Fernet(key.encode())

    # Leer y desencriptar la imágen
    encrypted_data = await encrypted_image.read()
    decrypted_data = fernet.decrypt(encrypted_data)

    # Guardar la imágen 
    file_path = f"decrypted_images/{encrypted_image.filename}"
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

    return {"filename": file_path}
