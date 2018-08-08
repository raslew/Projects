def methodception(another):
    return another()

def add_two_numbers():
    return 33+77

#print(methodception(add_two_numbers))

#lambda_functions är alltid på en rad.
print(methodception(lambda: 33 + 77))

my_list = [13, 45, 67, 88]

def not_thirteen(x):
    return x != 13

#filter är en inbyggd funktion som måste inringas av list om den skall returneras som en lista.
#Filtrerar "my_list" på "13" genom att använda lambda-funktionen
print(list(filter(lambda x : x != 13, my_list)))

#samma operation men med (metod, argument)
print(list(filter(not_thirteen, my_list)))

#med list_comprehension, föredras av pythonprogrammare. (obs! detta är unikt för python och några andra språk...)
print([x for x in my_list if x != 13])
