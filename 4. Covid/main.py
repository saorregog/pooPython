from location import Location
from person import Person

if __name__ == "__main__":
    # instantiate some locations:
    imperial_cluster = Location('Imperial College London computer cluster')
    h_bar = Location('Postgraduate Bar')
    imperial_library  = Location('Imperial College London Library')
    vna = Location('Victoria and Albert Museum')
    natural_history = Location('Natural History Museum')
    imperial_gym = Location('Ethos')

    # some people
    harry = Person('Harry', 'hgc19@ic.ac.uk', imperial_cluster)
    joe = Person('Joe', 'j.stacey20@ic.ac.uk', vna)
    luca = Person('Luca', 'lg16@ic.ac.uk', imperial_gym)
    william = Person('William', 'wh18@ic.ac.uk', h_bar)

    # people go about their day
    harry.move_location(imperial_gym)
    luca.move_location(imperial_cluster)
    william.move_location(imperial_cluster)
    joe.move_location(imperial_gym)
    joe.move_location(h_bar)
    harry.move_location(h_bar)
    
    print(f'Harry has been in contact with the following anonymous codes: {harry.contact_list}')

    # luca has tested positive for COVID
    # This should return that everyone apart from Joe needs self isolate.

    covid_codes =  [luca.unique_code]

    harry.check_to_isolate(covid_codes)
    joe.check_to_isolate(covid_codes)
    luca.check_to_isolate(covid_codes)
    william.check_to_isolate(covid_codes)

    print(f"Total people instantiated: {len(Person.all_unique_codes)} => {Person.all_people}")
