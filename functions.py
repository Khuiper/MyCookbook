def greet_user():
    """Generic greeting for users"""
    print('Hello!')

    print('Welcome')

def greet_user_by_name(name, greeting='Hello!'):
    """Customized greeting"""
    print(greeting +', ' +name)

def cube(base_number):
    cubed_value = base_number * base_number * base_number
    return cubed_value

greet_user()
greet_user_by_name(input('What is your name? '))

eleven_cubed = cube(2000)
print(eleven_cubed)

