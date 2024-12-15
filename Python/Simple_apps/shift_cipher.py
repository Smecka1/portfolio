# A = 65 / Z = 90  |  a = 97 / z = 122
characters = "., !?-_"

def cipher_function(encrypt_or_decrypt, string, shift):
    encrypted_text = ""
    for letter in string:
        if ord("a") <= ord(letter) <= ord("z"):
            if encrypt_or_decrypt == "1":
                encrypted_text += chr((ord(letter) - 97 + shift) % 26 + 97)  # ord("a") = 97
            else:
                encrypted_text += chr((ord(letter) - 97 - shift) % 26 + 97)  # ord("a") = 97
        elif ord("A") <= ord(letter) <= ord("Z"):
            if encrypt_or_decrypt == "2":
                encrypted_text += chr((ord(letter) - 65 + shift) % 26 + 65)  # ord("A") = 65
            else:
                encrypted_text += chr((ord(letter) - 65 - shift) % 26 + 65)  # ord("A") = 65
        elif letter in characters:
            encrypted_text += letter
    return encrypted_text

def user_interface():
    while True:
        encrypt_decrypt = input("Pro šifrování zadej: 1, pro dešifrování 2:\n")
        if encrypt_decrypt != "1" and encrypt_decrypt != "2":
            print("Validní přikaz je: 1 nebo 2 ")
        cipher = input("Zadej výraz k zašifrování, či dešifrování:\n")
        shift_num = 0
        try:
            shift_num = int(input("Zadej o kolik písmen posunout:\n"))
        except ValueError:
            print("Musíš zadat číslo.")
        print(cipher_function(encrypt_decrypt, cipher, shift_num))
        again = input("Pro ukončení zmáčkni: q + ENTER")
        if again == "q":
            break


print(user_interface())
