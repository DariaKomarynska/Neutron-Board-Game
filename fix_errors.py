'''
a = "true" if 3 > 5 \
    else "false"
print(a)
'''
lista1 = [3, 5, 60]
lista2 = lista1.copy()
lista2.remove(lista2[0])
print(f"id(lista1) - {id(lista1)} \
    id(lista2) - {id(lista2)} \
    lista1 = {lista1}")
