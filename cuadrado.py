#!/usr/bin/python

numeros = int(input("Ingrese cantidad de Numeros: \n\t"))

a = range(1, numeros)

for i in range(0, numeros - 1):
	print ("EL cuadrado de: ", a[i], "es: ", a[i] ** 2)
