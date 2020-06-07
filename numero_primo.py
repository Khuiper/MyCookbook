def is_prime(num):
    if num != 0:
        for i in range(2, num):
            if num % i == 0:
                return False
            return True
    return False


num = int(input("Ingresa un numero para verificar si es primo:"))

if is_prime(num) == True:
    print('El numero', +num ,'es Primo!')

else:
    print('El numero', +num ,'no es Primo!')