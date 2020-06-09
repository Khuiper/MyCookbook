dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
words = ['gato', 'leon', 'caballo']

for word in words:
    if word in dict:
        print(word, "->", dict[word])
    else:
        print(word, "no está en el diccionario")


"""¿Pueden los diccionarios ser examinados utilizando el bucle for, como las listas o tuplas?
No y si.
No, porque un diccionario no es un tipo de dato secuencial - el bucle for no es útil aquí.
Si, porque hay herramientas simples y muy efectivas que pueden adaptar cualquier diccionario a 
los requerimientos del bucle for (en otras palabras, se construye un enlace intermedio entre el 
diccionario y una entidad secuencial temporal).
El primero de ellos es un método denominado keys(), el cual es parte de todo diccionario. 
El método retorna o regresa una lista de todas las claves dentro del diccionario. Al tener 
una lista de claves se puede acceder a todo el diccionario de una manera fácil y útil.
A continuación se muestra un ejemplo:"""

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for key in dict.keys():
    print(key, "->", dict[key])