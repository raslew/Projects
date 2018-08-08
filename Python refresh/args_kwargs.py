#Tar två argument
def my_method(args1, args2):
    return args1 + args2

def my_long_method(args1, args2, args3, args4, args5, args6):
    return args1 + args2 + args3 + args4 + args5 + args6

def my_list_addition(list_arg):
    return sum(list_arg)

print(my_method(5, 6))
print(my_long_method(1, 3, 5, 7, 9, 11))
print(my_list_addition([1, 3, 5, 7, 9, 11]))

###
#argumentet *args hjälper oss att tolka vad som skickas in i metoden och konverterar om argumenten till en lista.
def addtion_simplified(*args):
    return sum(args)

addtion_simplified(1, 3, 5, 7, 9, 11)

###
#
def what_is_kwargs(*args, **kwargs):
    #kommer printa en tuple
    print(args)
    #kw = key words
    #kommer att printa en set
    print(kwargs)

what_is_kwargs(43, 46, 33, 11)
what_is_kwargs(43, 46, 33, 11, "Anna")
what_is_kwargs(43, 46, 33, 11, name = "Lisa", location = 'Norge')
