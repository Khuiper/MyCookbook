'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old.
'''


import datetime
now = datetime.datetime.now()


name = input("What's your name?: ")
age = int(input("How old are you {}: ".format(name)))

year_100 = (now.year + 100) - age

result = (name + " You will have 100 years old in the year " + str(year_100))
print(result)
new_word = int(input("Please write any number: "))

counter = 1

while counter <= new_word:
    print(result)
    counter +=1 
