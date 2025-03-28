import tkinter as tk
from tkinter import filedialog
from Crypto.Cipher import AES #aes encryption 
from Crypto.Util.Padding import unpad #remove padding


def decrypt(input, output, key):#input an output are path
    
    with open(input,'rb') as f: #rb opens the file in binary read mode
        iv = f.read(16) #read the first 16 bytes as initialisation vector(iv): required for AESdecryption in cbc node
        ciphertext = f.read() #read the remaining file as cipher
    #create a cipher which is a tool
    cipher = AES.new(key,AES.MODE_CBC,iv)#creates AES cipher object using the key an the cbc mode (cipher block chaining)
    
    #decrypt data in text using AES
    decrypted_padded = cipher.decrypt(ciphertext)
    #remove padding from decypted
    decrypted_text = unpad(decrypted_padded, AES.block_size)
    
     # Try to detect if output is text or binary
     #first try utf-8 if it  fails will assume its a binary data
     #if its text store as .txt if it's binary store as raw binary==
     #then use the try an except to handle errors
    try:
        decoded_text = decrypted_text.decode("utf-8")  # Try UTF-8 to test the encoding
        is_text = True #mean input was originally a text
    except UnicodeDecodeError:
        is_text = False  # If it fails, it's binary
        
    if is_text:
        with open(output, 'w', encoding="utf-8") as f: #opens the file in write mode and as f assigns the file object  to var f
                f.write(decoded_text)  # Save as UTF-8 text file
        print(f"Decryption complete! File saved as {output} (UTF-8 text).")
    else:
        with open(output, 'wb') as f:#write in binary mode
            f.write(decrypted_text)  # Save as raw binary file
        print(f"Decryption complete! File saved as {output} (Binary file).")

#gui for tkinter
root = tk.Tk()
root.withdraw() #hide the main window
#open the menu to selected the encrypted file
file_path = filedialog.askopenfilename(type= "Select Encrypted File",filetypes=[("Text Files",".txt")])

if file_path: #if the correct file is chosen
     
    #encryption key 
    #key = b'mysecretpassword' #b means the str is in byte
    key = input("Please provide your decryption key(16by min): ").encode()
    output = "decrypted.txt"
    #decrypt file
    decrypt(file_path,output,key) 
else:
    print("No .txt file seclected")
  