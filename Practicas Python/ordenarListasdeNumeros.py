lista = [1,34,7,2,9,-4,-3,-3,0,6]
positivos = [] #lista vacia
print 'Lista desordenada\n',lista


print 'Lista ordenada de numeros positivos:\n'
for l in lista:
	if l>0:
		positivos.append(l)

print positivos,'\nForma mas practica en python\n'

positivos = []

positivos = [l for l in lista if l >0]#comparo los positivos y agrego a la lista
#se traduce que dede for l recorre la lista y compara si es positivo regresa a la
# primera l que es la que se almacena en la lista 
print 'Lista de positivos forma Python\n',positivos,'\n\nValores Pares de un diccionario\n'

diccionario = {'a':4,'b':7,'c':2}

pares=[{k:v} for k,v in diccionario.items() if v%2==0]
print pares