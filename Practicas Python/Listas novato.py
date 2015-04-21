l = [2, "tres",True, ["uno",10],6]
l2 = l[2]
l3 = l[3][0] #accedo a un elemento de la lista dentro de la lista principal
print l3

#Copiar elementos de una lista a otra

l4 = l[0:3] #dice de la posicion 0 copia 3 elementos 

#si no ponemos valor en el rango se define ele limite de todo el arreglo
l5 = l[0::2] #[inicio: num de elementos: condicion de numeros a copiar +1 ]

print l5
 # Remplazar elemenstos

l[0:3] = [3,"asda",False]

print l

#remplazo de elemnetos saltandose uno 
l[0::2] = [3,"asda",False]
print l


#anadir elemnetos a las listas
l.append("Holis")
print l

#insertar
l.insert(2, "insertar")
print l

#extend concatena listas
l.extend(["holis","somos la prueba extend"])
print l

#eliminar elementos

l.remove("asda")

print l
