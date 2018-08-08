
#Kan t.ex. användas för att skicka med login uppgifter som argument för en användare till en websida för att se om hen skall få se admin-verktygen

import functools

def my_decotrator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator!")
        #fuck() = my_function och kommer printa "I'm the function!"
        func()
        print("After the decorator")
    return function_that_runs_func

#my_decotrator kommer ta och byta ut "my_function" och sedan använda "my_function" som argument.
@my_decotrator
def my_function():
    print("I'm the function!")

#my_function()

##

my_list = [1, 3, 4]

def decorators_with_arguments(numbers):
    def my_decotrator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("In the decorator!")
            if numbers == 55:
                func(*args, **kwargs)
            else:
                print("Not running the function")
            print("After the decorator")
        return function_that_runs_func
    return my_decotrator


#@decorators_with_arguments(my_list)
#def my_function_too():
#    print("Hello")

#skickar in som *args
#@decorators_with_arguments(1, 3, 4)
#def my_function_too():
#    print("Hello")

@decorators_with_arguments(55)
def my_function_too(x ,y):
    print("Skriver ut {}".format(x + y))

my_function_too(33, 67)
