#This is the encoder and decoder in Julian's repo

def printMenu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    

def encode(pswd):
    return "".join([str(int(dig)+3) for dig in pswd])
    
def decode(pswd):
    pass


currPswd = ""

while(True):
    printMenu()
    option = int(input("Please enter an option: "))
    if(option == 3):
        break
    if(option == 1):
        pswd = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!")
        currPswd = encode(pswd)
    if(option == 2):
        pass
    print()
