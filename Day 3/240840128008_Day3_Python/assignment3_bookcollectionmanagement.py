dicto = {}
while True:
    choice = int(
        input("Enter 1.Add Books \n Enter 2. Update Books\n Enter 3. Delete Books \n Enter 4 to View\nEnter 5 to Exit"))
    def addBook():

        global dicto
        k = []
        name = input("Enter the name of contact")
        phoneno = input("Enter phonenumber:")
        k.append(phoneno)
        email = input("Enter email")
        k.append((email))
        dicto[name] = k

    def deleteContact():
        global dicto
        name = input("Enter the name of contact you want to delete")
        del (dicto[name])

    def show():
        print(dicto)