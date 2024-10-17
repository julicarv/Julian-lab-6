#This is the encoder and decoder in Julian's repo
#Decoder function by Elias (EJ) Quintos

def printMenu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    

#As it is this will give problems with digits 7 through 9
def encode(pswd):
    return "".join([str(int(dig)+3) for dig in pswd])
    
def decode(currPswd):
    res = ''
    for i in currPswd:
        temp = int(i) + 10
        res = res + str(int(temp) - 3)[-1]
    return res


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
        print(f'The encoded password is {currPswd}, and the original password is {decode(currPswd)}')
    print()
