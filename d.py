import tkinter as tk
from tkinter import filedialog
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        iv = f.read(16)  # Extract the first 16 bytes (IV)
        ciphertext = f.read()  # Read the remaining encrypted content

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(ciphertext)

    try:
        decrypted_text = unpad(decrypted_padded, AES.block_size)  # Remove padding correctly
    except ValueError:
        print("Padding error: Check encryption/decryption process!")
        return

    # Try decoding as text
    try:
        decoded_text = decrypted_text.decode("utf-8")
        is_text = True
    except UnicodeDecodeError:
        is_text = False

    # Save decrypted file
    if is_text:
        with open(output_file, 'w', encoding="utf-8") as f:
            f.write(decoded_text)  # Save as a UTF-8 text file
        print(f"Decryption complete! File saved as {output_file} (UTF-8 text).")
    else:
        with open(output_file, 'wb') as f:
            f.write(decrypted_text)  # Save as binary file
        print(f"Decryption complete! File saved as {output_file} (Binary file).")

# File selection GUI
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(title="Select Encrypted File", filetypes=[("Encrypted Files", "*.*")])
if file_path:
    key = b'mysecretpassword12'  # Ensure 16, 24, or 32-byte key
    output_file = "decrypted_output.txt"
    decrypt_file(file_path, output_file, key)
else:
    print("No file selected.")