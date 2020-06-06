def leapyr(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    else:
        return False

n = int(input("Ingresa un ano para verificar si es bisiesto: "))
#leapyr(n)
if leapyr(n) == True:
    print("Es bisiesto")
else:
    print("No es bisiesto")