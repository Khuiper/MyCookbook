'''
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are
less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the
elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from
the original list a that are smaller than that number given by the user.
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 4, 2, 3, 1, 6, 0, 5]
b = []

#for a in a: //Solución 1
#    if a <=5:
#        b.append(a)

#b = [x for x in a if x<=5] //Solucion en una linea

b = list(filter(lambda x: x<=5, a)) #Tercera solucion 
print(b)
