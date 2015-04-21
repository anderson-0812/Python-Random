diccionario = {'v':24, 'a':135, 'b':-56}

lista = [1,4,6,2,'kfjsd','aafs']

print 'Lista Ordenada de mayor a menor',sorted(lista, reverse=True) #se ordena en reversa de menor a mayor

#ordenar diccionario x valor y con reverse 
#ojo l,a funcion lambda es con una variable de valor anonimo
#aqui trabaja q a lambda es varible x que apunta al key del dicc
#que una vez comvertido en tubla el dicci por medio de items()
#le digo q x[1] (x de posicion 1 (x = 'v', 24))
print 'Diccionario Ordenado', sorted(diccionario.items(), reverse = True, key=lambda x: x[1])


#ordenar una lista de diccionarios
lista_dicc = [{'item': 'cafe','valor':2},{'item':'azucar','valor':4},{'item':'manzana','valor': 1},{'item':'taza','valor':-2}]

print 'Lista de dicc sin ordenar ', lista_dicc
#a la variable lambda le pasamos en vez de indice la llave x la cual va a ordenar
print 'Lista de dicc Ordenada ', sorted(lista_dicc, key= lambda x: x['valor'])