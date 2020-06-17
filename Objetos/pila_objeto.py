class Pila:    # define la clase Pila
    def __init__(self):    # define la función del constructor
        #print("¡Hola!")
        #self.listaPila = [] #Agregamos una propiedad al nuevo objeto
        self.__listaPila = []
        """Cuando cualquier componente de la clase tiene un nombre que comienza 
        con dos guiones bajos (__), se vuelve privado - esto significa que solo 
        se puede acceder desde la clase. La salida arrojara un error
        
        Ahora es el momento de que las dos funciones (métodos) implementen las 
        operaciones push y pop. Python supone que una función de este tipo debería 
        estar inmersa dentro del cuerpo de la clase - como el constructor.
        Queremos invocar estas funciones para agregar (push) y quitar (pop) valores de la pila. 
        Esto significa que ambos deben ser accesibles para el usuario de la clase (en contraste 
        con la lista previamente construida, que está oculta para los usuarios de la clase ordinaria).
        
        Tal componente es llamado publico, por ello no puede comenzar su nombre con dos (o más) guiones bajos.
        Hay un requisito más - el nombre no debe tener más de un guión bajo."""

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self): #self Permite que el método acceda a entidades (propiedades y actividades / métodos) del objeto.
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val

    """Hay una cosa más que requiere explicación: la forma en que se invocan los métodos desde la variable __listaPila.
    Afortunadamente, es mucho más simple de lo que parece:

    La primera etapa entrega el objeto como un todo → self.
    A continuación, debes llegar a la lista __listaPila → self.__listaPila.
    Con __listaPila lista para ser usada, puedes realizar el tercer y último paso → self.__listaPila.append(val).
    """

objetoPila = Pila()    # instanciando el objeto
#print(len(objetoPila.listaPila)) #¡no uses paréntesis! No deseas invocar un método, deseas acceder a una propiedad.
#print(len(objetoPila.__listaPila))

objetoPila.push(3)
objetoPila.push(2)
objetoPila.push(1)

print(objetoPila.pop())
print(objetoPila.pop())
print(objetoPila.pop())
