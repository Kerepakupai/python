#!/usr/bin/python

numero = 28
suma = 0
for i in range(1, numero-1):
	if numero > 0:
		if numero % i == 0:
			suma = suma + i
	else:
		if numero % -i == 0:
			suma = -i + suma		
			
if numero == suma:
	print("El numero es perfecto");
else:
	print("El numero no es perfecto");
