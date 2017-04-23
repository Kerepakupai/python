#!/usr/bin/python

def buscar(lista, elemento):
	count = 0
	array = []
	for i in range(len(lista)):
		if elemento == lista[i]:
			count = count + 1
			array.append(i)
			if count == 1:
				print("La primera coincidencia del elemento fue en la posicion:", i)
		i = i + 1
	print("Se encontro", count, "veces el elemento buscado")
	if count > 0: 
		for item in array:
			print(item) 


a = [1, 4, 12, 34, 54, 3, 4, 7, 8, 4, 2, 3, 4, 6, 8, 4, 6, 4, 8, 0, 5]

buscar(a, 4)


