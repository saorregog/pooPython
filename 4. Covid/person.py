import random
import string

class Person:
    all_people = list()
    all_unique_codes = set()

    def __init__(self, name, email, start_loc):
        self.name = name

        Person.all_people.append(self.name)

        self.email = email
        self.loc = start_loc

        # for privacy sake a person shall share their unique code not their name
        self.unique_code = self.gen_unique_code()

        # set containing codes of the people which the person has been in contact with
        self.contact_list = set()

        # send code to start location
        self.loc.add_person(self.unique_code)


    def gen_unique_code(self, length=20):
        '''
        Method which generates a random code for the person of length, length
        '''
        # return int(random.random()*(10**length)) # Random Code Generator 1
        unique_code = "".join(random.sample(string.digits + string.ascii_letters, k=length)) # Random Code Generator 2

        if (unique_code in Person.all_unique_codes):
            unique_code = self.gen_unique_code()
        else:
            Person.all_unique_codes.add(unique_code)
            return unique_code
        
        return unique_code

    
    def move_location(self, new_location):
        '''
        Method which moves the person
        input:
        new_location: type --> class instance
        '''

        # check to see who is here and log unique codes
        self.register_contacts()

        self.loc.remove_person(self.unique_code)

        new_location.add_person(self.unique_code)
        self.loc = new_location

        # check to see who is here
        self.register_contacts()


    def register_contacts(self):
        self.contact_list = self.contact_list.union(self.loc.people_present)

    
    def check_to_isolate(self, covid_codes):
        if any(code in self.contact_list for code in covid_codes):
            print(f'{self.name} needs to self isolate')
        else:
            print(f'{self.name} does NOT need to self isolate')
