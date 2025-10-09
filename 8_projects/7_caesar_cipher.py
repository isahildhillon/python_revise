import re


    
def encrypt_msg(msg,num):
    encrypted_msg=""
    for alphabet in msg:
        new_char_int=num%25+ord(alphabet)
        if 90>=ord(alphabet)>=65 :
            if(new_char_int>90):
                new_char_int-=26
            encrypted_msg+=chr(new_char_int)
        elif  122>=ord(alphabet)>=97:
            if new_char_int>122:
                 new_char_int-=26
            encrypted_msg+=chr(new_char_int)
        else:
            encrypted_msg+=alphabet
    return encrypted_msg
# print(ord('a'),ord('z')) # A-65 Z-90 , a-97 z- 122

def decrypt_msg(msg,num):
    decrypted_msg=""
    for alphabet in msg:
        new_char_int=ord(alphabet)-num%25
        if 90>=ord(alphabet)>=65 :
            if(new_char_int<65):
                new_char_int+=26
            decrypted_msg+=chr(new_char_int)
        elif  122>=ord(alphabet)>=97:
            if new_char_int<97:
                 new_char_int+=26
            decrypted_msg+=chr(new_char_int)
        else:
            decrypted_msg+=alphabet
    return decrypted_msg

if __name__=="__main__":
    print("Welcome to caesar cipher")
    print("1. Encrypt a Message")
    print("2. Decrypt a message")
    print("3. Exit")
    while not (option:=int(input("Enter your option : "))) in [1,2,3]:
        continue
    if(option==3):
        exit()

    match option:
        case 3:
            exit()
        case 1 | 2:
            key= int(input("Enter your key : "))
            msg=input("Enter your key : ")
            new_msg=""
            if option==1:
                new_msg=encrypt_msg(msg,key)
            else :
                new_msg=decrypt_msg(msg,key)
            print(f"Your {"encrypted" if option==1 else "decrypted"} msg is : ",new_msg)
            