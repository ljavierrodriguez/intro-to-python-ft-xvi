"""

Comentario de Multiples Lineas (Triple Comillas Dobles o Simples al Inicio y al Final)

"""

# Comentario Simple

# String, Number, Boolean, None, Dictionaries, (Lists, Tuples, Sets) => Array

nombre = "Luis"
apellido = 'Rodriguez'
direccion = ''' 

Esto es una direccion 

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Qui aliquam saepe 
consectetur nisi quos assumenda sed ea a totam eius! Praesentium, facilis. 
Incidunt assumenda officiis hic, ab vitae non qui.

'''

age = 20 
price = 30.40
grade = -30

single = None
other = None

person = {
    "name": "Luis",
    "lastname": "Rodriguez"
}

nombres = ["Hugo", "Paco", "Luis"] # Lista (list)
status = ("Active", "Inactive", "Canceled", "Approved", "Rejected") # Tupla (tuple)
frutas = { "Pera", "Manzana", "Uva" } # Sets (set)

nombres[0] = "Maria" # True

status[0] = "Suspended" # False

status.append("Suspended")

flag = True # False