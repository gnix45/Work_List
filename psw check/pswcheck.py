def psw_check(psw):
    sp_char = "!@#$%^&*()+}{][?/:;-_"
    if (len(psw) >=8 and
        any (char.isupper() for char in psw) and
        any(char.islower() for char in psw) and
        any(char.isdigit() for char in psw) and
        any(char in sp_char for char in psw)):
        
        return "Valid Password You can then use this in any of your accounts"
    else:
        return "Does not meet the minimum requirements"
    
pswd = input("Input password for the test: ")
print(psw_check(pswd))