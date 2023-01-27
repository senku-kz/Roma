"""
python student.py
python -c 'from student import Student; print(Student("Stefano","Guarino"))'
"""


class Person:
    # first_name = ''
    # last_name = ''

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Student(Person):
    degree_course = 'any course'

    def __init__(self, first_name, last_name, degree_course='any course'):
        self.first_name = first_name
        self.last_name = last_name
        self.degree_course = degree_course

    def __str__(self):
        return "{} {} is registered to {}".format(self.first_name, self.last_name, self.degree_course)


if __name__ == "__main__":
    f_name = input("Insert first name: ")
    l_name = input("Insert last name: ")
    ch = input("Are you a student? (y/n)")
    while True:
        if ch == "y":
            program = input("Please insert your degree course: ")
            student = Student(f_name, l_name, program)
            print(student)
            break
        elif ch == "n":
            person = Person(f_name, l_name)
            print(person)
            break
        else:
            ch = input("Please type \"y\" or \"n\": ")
