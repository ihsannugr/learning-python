#Exercise 11

#Ask the user for a number and determine whether the number is prime or not.

#define print result function
def print_result(number):
    prime = check_prime(number)
    if prime :
        print(str(number) + " is prime")
    else :
        print(str(number) + " is not prime")

#define get number function
def get_number(help_text = "Give me a number: "):
    return int(input(help_text))

#define check prime function
def check_prime(number):
    if number == 1 :
        prime = False
    elif number == 2 :
        prime = True
    else :
        list = range(1, number + 1)
        divisor = [elem for elem in list if number % elem == 0]
        if len(divisor) != 2 :
            prime = False
        else :
            prime = True
   			
    return prime

#execute
while 1 == 1 :
    print_result(get_number())


