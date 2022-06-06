addCount = 0

def view (addCountLocal) :

    if addCountLocal >= 1 :

        file = open ("passwordTextFile.txt","r")
    
        print ()
        print ("Your Passwords : ")
        print ()
        print ( file.read() )
        print()

        file.close ()

        SelectMode(addCountLocal)
    
    else :

        print()
        print ("You haven't added anything yet !")
        print()
        SelectMode(addCountLocal)

def add (addCountLocal) :

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

    SelectMode (addCountLocal)

def invalidCode (addCountLocal) :

    print ("You entered an invalid code as a mode !")
    
    SelectMode (addCountLocal)

def SelectMode (addCountLocal) :

    print ()
    Mode = input ("Enter view if you want to view your passwords,\nadd if you want to add a new password\nand exit if you want to quit the program : ")
    print ()

    if Mode == "view" :
        view(addCountLocal)

    if Mode == "add" :
        addCountLocal += 1
        add(addCountLocal)

    elif Mode == "exit" :
        quit()
    
    else :
        invalidCode(addCountLocal)

SelectMode (addCount)