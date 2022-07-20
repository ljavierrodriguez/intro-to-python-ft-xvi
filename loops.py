""" 
    Loops
"""

""" 

for value in values:
    sentences

while condition:
    sentences


"""
start = 1 # default = 0 -> optional
stop = 11
step = 1 # default = 1 -> optional

for i in range(start, stop, step):
    print(i)

nombres = ["Hugo", "Paco", "Luis"]

for i in range(len(nombres)):
    print(nombres[i])

for nombre in nombres:
    print(nombre)

i = 0
while i < len(nombres):
    print(nombres[i])
    i = i + 1