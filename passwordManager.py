file = open("passwordTextFile.txt","a")
file.close ()

def view () :

        file = open ("passwordTextFile.txt","r")
    
        print ()
        print ("Your Passwords : ")
        print ()
        print ( file.read() )
        print()

        file.close ()

        SelectMode()

def add () :

    file = open ("passwordTextFile.txt","a")

    EmailUsername = input ("Enter the email or username : ")
    Password = input ("Enter the password : ")

    file.write (EmailUsername)
    file.write (" ")
    file.write (Password)
    file.write ("\n")

    file.close ()

    print ()
    print ("Added !")

    SelectMode ()

def invalidCode () :

    print ("You entered an invalid code as a mode !")
    
    SelectMode ()

def SelectMode () :

    print ()
    Mode = input ("Enter view if you want to view your passwords,\nadd if you want to add a new password\nand exit if you want to quit the program : ")
    print ()

    if Mode == "view" :
        view()

    if Mode == "add" :
        add()

    elif Mode == "exit" :
        quit()
    
    else :
        invalidCode()

SelectMode ()
