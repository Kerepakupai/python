#!/usr/bin/python

numero = int(input("Introduzca Numero: \n"))
factorial = numero

for item in range(1, numero):
	factorial = factorial * item

print(factorial)

temp = numero - 1
factorial = numero
while temp > 1:
	factorial = factorial * temp
	temp = temp - 1

print(factorial)