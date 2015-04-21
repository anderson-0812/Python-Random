lista1 = [1,2,3,4]
lista2 = [3,4,5,6]

print 'devuelve los valores de lista1 q no se repite en la lista2\n',set(lista1)-set(lista2)

print 'valores no repetidos de lista2\n',set(lista2)- set(lista1)

print 'Valores repetidos en ambas listas\n', set(lista1) & set(lista2)
