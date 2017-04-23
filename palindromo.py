#!/usr/bin/python

def is_palindromo(palabra):
	# palabra=input("Ingrese una Palabra: \n")
	palabra = palabra.lowercase
	i = 0
	l = len(palabra)-1
	while palabra[i]==palabra[l] and i < l:
		i = i + 1
		l = i - 1
	if i > l:
		print("Palabra Palindromo")
	else:
		print("No es una Palabra Palindromo")

def is_palindromo2(palabra):
	palabra = palabra.lowercase
	i = 0
	for i in range(len(palabra)):
		



palabra = input("Ingrese una Palabra: \n\t")
is_palindromo(palabra)