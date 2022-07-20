""" 
    Functions
"""

""" 

def functionName():
    sentences


variableName = lambda express


"""


def saludo():
    print("Hola")

saludo()

saludo2 = lambda : print("Hola 2")

saludo2()

def suma(a, b):
    return a + b

print(suma(10, 5)) # 15

resta = lambda a, b: a - b

print(resta(4, 5)) # -1

def bienvenida(name = "John", lastname = "Doe", age = 10):
    #return "Bienvenido, {} {}, edad: {}".format(name, lastname, age)
    #return "Bievenido, %s %s, edad: %i" % (name, lastname, age)
    #return f"Bievenido, {name} {lastname} {age}" 
    return "Bievenido, " + name + " " + lastname + ", edad: " + str(age) # int(value)

print(bienvenida())