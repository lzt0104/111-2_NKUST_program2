from abc import abstractmethod,ABCMeta

class Person(metaclass=ABCMeta):
    def __init__(self,age,career,gender):
        self.age = age
        self.career = career
        self.gender = gender

    @abstractmethod
    def getCareer(self):
        return self.career
    def _record(self):
        pass
    def getDescription(self):
        return f"I am {self.age},{self.career},{self.gender}"
    
class Student(Person):
    def __init__(self, age, career, gender):
        super().__init__(age, career, gender)
        self.career = "Student"
    def getCareer(self):
        return super().getCareer()
    def getDescription(self):
        return f"I am a student,{self.age},{self.gender}"
    def getPersonDescription(self):
        return super().getDescription()

class Accountant(Person):
    def __init__(self, age, career, gender):
        super().__init__(age, career, gender)
        self.career = "Accountant"
    def getCareer(self):
        return super().getCareer()
    

p1 = Person(age=10, career="people", gender="boy")
print(p1.getDescription())

s1 = Student(age=20, career="", gender="female")
print(s1.getPersonDescription())
print(s1.getDescription())

a1 = Accountant(age=30, career="", gender="male")
print(a1.getDescription())
