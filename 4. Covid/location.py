class Location:
    '''
    A class used for defining locations in our virtual COVID space and who is 
    currently there.
    note: as this a virtual problem, proximity between people cannot be calculated
    through GPS or bluetooth.
    '''

    def __init__(self, name):
        self.name = name
        # people at that location at that specific time
        self.people_present = set()

    def add_person(self, person_code):
        self.people_present.add(person_code)
    
    def remove_person(self, person_code):
        if (person_code in self.people_present):
            self.people_present.discard(person_code)
        else:
            print("The person has not entered!")
