class Person:
    def __init__(self, input_name, input_age, input_email):
        self.name = input_name
        self.age = input_age
        self.email = input_email


class Student(Person):
    def __init__(self, input_name, input_age, input_email, input_student_id, input_year_entry):
        super().__init__(input_name, input_age, input_email)
        self.student_id = input_student_id
        self.year_entry = input_year_entry
        self.modules_enrolled_in = None

    def enroll_modules(self, *input_modules):
        self.modules_enrolled_in = list(input_modules)


class Lecturer(Person):
    def __init__(self, input_name, input_age, input_email, input_office_num):
        super().__init__(input_name, input_age, input_email)
        self.office_num = input_office_num
        self.modules_teached = None
        self.students_supervised = None
        self.tutor_of = None

    def teach_modules(self, *input_modules):
        self.modules_teached = list(input_modules)

    def supervise_student(self, *input_students):
        for student in input_students:
            if (student.education == "Postgraduate"):
                if (self.students_supervised == None):
                    self.students_supervised = list()
                
                self.students_supervised.append(student)
                student.supervised_by = self
                print(f"{student.name} is an postgraduate student")
            else:
                print(f"{student.name} is not an postgraduate student")

    def tutor_of_student(self, *input_students):
        for student in input_students:
            if (student.education == "Undergraduate"):
                if (self.tutor_of == None):
                    self.tutor_of = list()
                
                self.tutor_of.append(student)
                student.tutor = self
                print(f"{student.name} is an undergraduate student")
            else:
                print(f"{student.name} is not an undergraduate student")


class Postgraduate(Student):
    def __init__(self, input_name, input_age, input_email, input_student_id, input_year_entry):
        super().__init__(input_name, input_age, input_email, input_student_id, input_year_entry)
        self.education = "Postgraduate"
        self.supervised_by = None


class Undergraduate(Student):
    def __init__(self, input_name, input_age, input_email, input_student_id, input_year_entry):
        super().__init__(input_name, input_age, input_email, input_student_id, input_year_entry)
        self.education = "Undergraduate"
        self.tutor = None


ignacio = Postgraduate("Ignacio Ochoa", 30, "io@gmail.com", 321, 2020)

roberto = Undergraduate("Roberto Vargas", 25, "rv@gmail.com", 123, 2023)
roberto.enroll_modules("History", "Math")

carlos = Lecturer("Carlos Isaza", 45, "ci@gmail.com", 21)
carlos.teach_modules("Art")
carlos.supervise_student(roberto, ignacio)
carlos.tutor_of_student(roberto, ignacio)

print(roberto.tutor.name)
print(ignacio.supervised_by.name)
