lista_nombre = ['anderson', 'eduardo','carolina']
lista_email = ['anderson@coditeck.ec','edu@gmail.com','flakisbellis@hotmail.es']

""" la funcion zip asocia dos listas convirtiendolas en tuplas
"""
for n, e in zip(lista_nombre,lista_email):
	print 'nombre:', n, 'mail:',e
#la funcion dict convierte a diccionario la lista
print '\nListas convertidas a dicccionario', dict(zip(lista_nombre,lista_email))
