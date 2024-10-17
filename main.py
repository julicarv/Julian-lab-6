def printMenu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    
pswd = ""
ePswd = ""
while(True):
    printMenu()
    option = int(input("Please enter an option: "))
    if(option == 3):
        break
    if(option == 1):
        pswd = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!")
        ePswd = "".join([str(int(dig)+3) for dig in pswd])
    if(option == 2):
        print(f"The encoded password is {ePswd}, and the original password is {pswd}.")
    print()
