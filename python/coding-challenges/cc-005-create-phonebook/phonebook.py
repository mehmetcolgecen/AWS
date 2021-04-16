class Phonebook:
    def __init__(self, Name=None, PhoneNumber=None, PhoneBook={}):
        self.name = Name
        self.number = PhoneNumber
        self.book = PhoneBook

    def insert(self):
        self.name = input("Insert name of the person :")
        try:
            self.number = int(input("Insert phone number of the person :"))
        except:
            print("Invalid input format, cancelling operation ...")
        else:
            self.book[self.name] = self.number
            print(f"Phone number of {self.name} is inserted into the phonebook")
    
    def find(self):
        name = input("Find the phone number of :")
        try:
            print(self.book[name])
        except:
            print(f"{name} does not exist on the phonebook")

    def delete(self):
        name = input("Whom to delete from phonebook :")
        try:
            del self.book[name]
        except:
            print(f"{name} does not exist on the phonebook")
        else:
            print(f"{name} is deleted from the phonebook")

    def display(self):
        for k,v in self.book.items():
            print(f"{k}: {v}")

    def exe(self):
        while True:
            try:
                case = int(input('''
Welcome to the phonebook application
1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) :'''))
            except:
                print("Invalid input format, Please enter 1, 2 or 3")
                continue
            if case == 1:
                self.find()
            elif case == 2:
                self.insert()
            elif case == 3:
                self.delete()
            elif case == 4:
                print("Exiting Phonebook, your current Phone Book is :")
                self.display()
                break
            else:
                print("Invalid input format, Please enter 1, 2 or 3")
                continue