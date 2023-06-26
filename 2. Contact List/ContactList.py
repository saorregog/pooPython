class ContactList:
    def __init__(self):
        self.contacts = {}

    def load_contacts(self):
        name = input("Name: ")
        cellphone = input("Cellphone: ")
        email = input("Email: ")
        self.contacts[name] = [cellphone, email]
        print("LOAD FINISHED")
        print("")

    def show_full_contact_list(self):
        print("FULL CONTACT LIST")
        for contact in self.contacts:
            print(
                f"{contact} / {self.contacts[contact][0]} / {self.contacts[contact][1]}")
        print("END OF THE LIST")
        print("")

    def search_contact_name(self):
        searched_name = input("Searched name: ")

        if (searched_name in self.contacts):
            print(
                f"{searched_name} / {self.contacts[searched_name][0]} / {self.contacts[searched_name][1]}")
            print("")
        else:
            print("The contact doesn't exist!")
            print("")

    def options_menu(self):
        option = 0

        while (option != 4):
            print("OPTIONS MENU")
            print("1 - Load new contact")
            print("2 - Show full contact list")
            print("3 - Search contact by name")
            print("4 - Exit")
            print("")

            option = int(input("Choose one option: "))
            print("")

            if (option == 1):
                self.load_contacts()
            elif (option == 2):
                self.show_full_contact_list()
            elif (option == 3):
                self.search_contact_name()


contact_list_1 = ContactList()
contact_list_1.options_menu()
