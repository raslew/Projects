'''var = "hello"

#Nedan säger if true...
if var:
    print(var)

know_people = ["Rasmus", "Rolf", "John"]
person = input("Enter a person you know: ")

if person in know_people:
    print("You know " + person + "!")
    print("You know {}!".format(person))
else:
    print("You don't know {}".format(person))

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even_numbers(number):
    evens = []
    for n in number:
        if n % 2 == 0:
            evens.append(n)
    return evens

print(even_numbers(number))

def user_menu(choice):
    if choice == "q":
        return "quit"
    else:
        return "add"

print(user_menu(input("Type q/a")))'''

list_of_people = ["Rasmus","John","Lee"]

'''def who_do_you_know():
    count = 0
    for i in range(3):
        if count == 0:
            print("Give me a name of someone you know")
            print(list_of_people.append(input()))
            count += 1
        elif count <3:
            print(list_of_people.append(input("One more")))
            count += 1
    print(list_of_people)'''

'''def who_do_you_know():
    names = input("Give me three names:")
    people_list = names.split(" ")
    return people_list

def ask_user():
    #new_list = who_do_you_know()
    x = input("Enter a name of someone you know.")
    #Det går att köra en metod i en if-sats!!
    if x in who_do_you_know():
        print("You know {}".format(x))
    else:
        print("You don't know {}".format(x))

ask_user()'''

#Strip tar bort alla whitespaces
list_to_strip = ["Lee ", " Ann", " John "]
striped_list = []
for person in list_to_strip:
    striped_list.append(person.strip())
print(striped_list)