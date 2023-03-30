class Person:
    def __init__(self,na):
        self.name = na
    
    def print_name(self):
        print({self.name})

class Student(Person):
    def __init__(self, name,gender):
        self.gender = gender
        super().__init__(name)

    def print_info(self):
        print(f'name:{self.name},gender:{self.gender}')

student = Student('aaaa', 'boy')
student.print_info()
student.print_name()