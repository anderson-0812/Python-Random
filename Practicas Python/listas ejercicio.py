print("Escribe el limite de palabras a ingresar")
limite = input()
limite = int(limite) #convierto el str a int
li = []
for i in range(limite): #doy limite al bucle
	print("el rango es " + str(len(li)) )
	print("Escribe la palabra")
	li.append(raw_input(''))#leo los datos de entrada y gaurdo en la lista
print("la lista es ")
print li