""" 
    Condicionales
"""

""" 

if condition:
    sentences

if condition:
    sentences
else:
    sentences

if condition:
    sentences
elif condition:
    sentences
else:
    sentences

"""

if 5 > 6:
    print("Verdadero")

if 5 > 6:
    print("Verdadero")
else:
    print("Falso")

a = 5
b = 8
c = 4

if a > b and a > c:
    print("A")
elif b > c:
    print("B")
else:
    print("C")

# and or not

"""

true and true = true
true and false = false
false and false = false

true or true = true
true or false = true
false or false = false

not true and not true = false
not true and not false = false
not false and not false = true

not true or not true = false
not true or  not false = true
not false or not false = true

"""

if not a > b:
    pass