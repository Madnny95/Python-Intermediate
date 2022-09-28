"""
item1 = 'Phone'
item1_price = 100
item1_quantity = 5
item1_price_total = item1_price * item1_quantity
"""

# La salida indica que cada tipo de dato es una instancia.
#   Todo tipo de dato es un objeto que fue instanciado por una clase
##  para la variable item1 esta fue instanciada por la clase llamada string

"""
print(type(item1))  # str
print(type(item1_price))  # int
print(type(item1_quantity))  # int
print(type(item1_price_total))  # int
"""

#   crear una instancia o un objeto es lo mismo.
#   para configurar metodos se tiene que hacer dentro de la clase con la palabra reservada DEF.
## Los metodos son Funciones que van dentro de las clases.
### SELF: autogenerado, se pasa como primer argumento como si fuera el mismo un objeto
### Es para que siempre esste recibiendo un parametro y no genere errores. Siempre se debe de recibir
### al menos 1 parametro.


#### Se puede usar para inicializar objetos diferentes de una misma instancia
"""
class Item:.
    def __int__(self):

    def calculate_total_price(self, x, y):
        return x * y
"""

## cada uno de los atributos(Phone, 100, 5) esta siendo relacionado a un instancia(name,price,quantity) de la clase
"""
item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
"""
# Es una instancia mas del ITEM.

"""
item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
"""


## Ambas instancias son del mismo objeto.


#
class Item:

    # en este punto corre el init por cada INSTANCIA.
    ## Se pueden usar mas parametros dentro del init
    ## PUEDO DECLARAR LOS ATRIBUTOS USANDO EL SELF PARA DECLARARLOS

    # Puedo poner 0 a un argumento para que no se tenga que declarar el atributo para que no de error si no se coloca.'

    def __int__(self, name, price, quantity):
        print("I AM CREATED")
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self, x, y):
        return x * y


### ESTO ES UNA INSTANCIA
item1 = Item("Phone", 100, 5)

item2 = Item("Laptop", 1000, 3)
