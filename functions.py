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

def bienvenida(name = "John", lastname = "Doe"):
    #return "Bienvenido, {} {}".format(namem, lastname)
    #return "Bievenido, %s %s" % (name, lastname)
    return f"Bievenido, {name} {lastname}" 

print(bienvenida())