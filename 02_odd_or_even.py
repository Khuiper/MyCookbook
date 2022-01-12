'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

'''

number = int(input("Ingresa un numero: "))

if number % 4 == 0:
    print("Tu numero {} es multiplo de cuatro!".format(number))

elif number % 2 == 0:
    print("El numero {} es par".format(number))

else:
    print("El numero {} es impar".format(number))

num = int(input("Ingresa un numero para verificar si son multiplos: "))
check = int(input("Ingresa otro numero para verificar si son multiplos: "))


if num < check:
    if check % num == 0:
        print("Tu numero {} es multiplo divisor de {}".format(num, check))
    else:
        print("No son multiplos")

elif num % check == 0:
    print("Tu numero {} es multiplo divisor de {}".format(check, num))


    
