import hashlib

def hashpsw(psw, salt):
    #encode to bytes
    psw_bytes = psw.encode("Utf-8")
    salt_bytes = salt.encode("utf-8")
    #salt psw
    salted_psw = psw_bytes + salt_bytes
    #encode
    hash_object = hashlib.sha256(salted_psw)
    
    #set to hexadecimal
    psw_hash = hash_object.hexdigest()
    return psw_hash

pswd = input("Enter your psw: ")
salt = input("Enter a random string for salting: ")
print(f"the hash is: ",hashpsw(pswd, salt))


    