
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average():
        return sum(self.marks) / len(self.marks)

    #@classmethod
    #def friend(cls, friend_name, origin, salary):
    #    return cls(friend_name, origin.school, salary)

    #*args kommer ta emot ett eller flera argument (beroende på hur konstruktorn ser ut) och skicka tillbaka till WorkingStudent och placers i "self.salary" & "self.job_title".
    #@classmethod
    #def friend_2(cls, friend_name, origin, *args):
    #    return cls(friend_name, origin.school, *args)

    #*kwargs tar emot keywords och skicka till self.salary, job_title. Pga man talar om vart de skall placeras så behöver de inte vara i ordning.
    #@classmethod
    #def friend_3(cls, friend_name, origin, **kwargs):
    #    return cls(friend_name, origin.school, **kwargs)

    #Går även att mixa
    @classmethod
    def friend_4(cls, friend_name, origin, *args, **kwargs):
        return cls(friend_name, origin.school, *args, **kwargs)

##
#Ärver från klassen "Student" men endast "name" & "school".
class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title

lee = WorkingStudent("Lee", "MIT", 25.00, "Data Scientist")
#print(lee.salary)

#Skapar upp ett nytt objekt av klassen WorkingStudent. Kommer åt friend-metoden pga WorkingStudent äver från Student-klassen.
#lees_friend = WorkingStudent.friend("Anna", lee, 20.00, "")
#print(lees_friend.name, lees_friend.school, lees_friend.salary)


#lees_friend_2 = WorkingStudent.friend_2("Johanna", lee, 25.00, "Utvecklare")
#print(lees_friend_2.job_title, lees_friend_2.salary)

#lees_friend_3 = WorkingStudent.friend_3("Nils", lee, job_title="Ingenjör", salary=19.00)
#print(lees_friend_3.salary, lees_friend_3.job_title)

lees_friend_4 = WorkingStudent.friend_4("Nils", lee, job_title="Ingenjör", salary=19.00)
print(lees_friend_4.salary, lees_friend_4.job_title)
