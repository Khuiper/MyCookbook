'''
Create a program that asks the user for a number and then prints out
a list of all the divisors of that number. (If you don’t know what a
divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

num = int(input("Ingresa un numero: "))
b = []

counter = 1

while counter <= num:
    if num % counter == 0:
        b.append(counter)

    counter +=1

print("Los numeros divisores de {} son: ".format(num), b)
