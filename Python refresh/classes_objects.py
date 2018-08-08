
lottery_player_dict = {
    'name' : 'Lee',
    'numbers' : (1, 3, 5, 7)
}

class LotterPlayer:
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = numbers

    def total(self):
        return sum(player.numbers)

player = LotterPlayer('Lee', (1, 3, 6, 10, 13))
print(player.name)
print(sum(player.numbers))
print(player.total())

##

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    #SELF kommer alltid skickas med som argument ifall man inte skriver
    #@classmethod: skickar med "cls" vilket istället för objektet är klassen, i detta fallet
    #är STUDENT
    @classmethod
    def go_to_school_classmethod(cls):
        print("classmethod_test.... I'm a {}".format(cls))
    #eller @staticmethod eller...
    #Spelar ingen roll vilket objekt som kallar på metoden, alla får samma svar.
    @staticmethod
    def go_to_school_static():
        print("staticmethod_test")


lee = Student("Lee", "MIT")
lee.marks.append(44)
print(lee.marks)
lee.go_to_school_classmethod()
#pga att metoden är @staticmethod så behöver inte objektet användas för att kalla på metoden, endast klassen (i detta fallet "Student").
Student.go_to_school_static()
