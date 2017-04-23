#!/usr/bin/python

def promedio(notas):
	suma = 0
	
	for item in notas:
		suma = suma + item

	promedio = suma / len(notas)
	print("El promedio es: ", promedio)

notas = [10, 5, 20, 5, 10]
promedio(notas)