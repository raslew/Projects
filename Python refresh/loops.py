
my_variable = "hello"
my_list = [1, 3, 5, 7, 9]
my_set = {11, 33, 55, 77, 99}
my_tuple = (10, 20, 30, 40, 50)

#olika varianter for loops.
#Det får att iterera igenom strings, lists, sets, tuple and more...

'''for c in my_variable:
    print(c)

for l in my_list:
    print(l)
    # '**' upphöjt i x
    print(l ** 2)
    print(l ** 3)

for s in my_set:
    print(s)

for t in my_tuple:
    print(t)'''

user_wants_number = True
count = 0
while user_wants_number == True and count <10:
    print(10)
    count += 1
    if count == 9:
        print("last round")

while user_wants_number == True:
    user_input = input("Wanna continue y/n?")
    if user_input == "n":
        user_wants_number = False
        print("The End")




