""" 
    Arrays
"""

nombres = []

print(dir(nombres))

nombres.append("Hugo")
nombres.append("Paco")

#nombres.pop()

nombres = list(filter(lambda elem: elem != 'Hugo', nombres))

nombres = list(map(lambda elem: elem.upper(), nombres))

print(nombres)