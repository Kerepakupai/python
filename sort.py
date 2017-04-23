#!/usr/bin/python

import sys

def insert_sort(a):
	
	i=1
	for i in range(len(a)):
		key = a[i];

		i = i-1
		while i >= 0 and a[i] > key:
			a[i+1] = a[i]
			i = i-1
		a[i+1] = key

	for item in a:
		print(item)

# array = [5, 2, 4, 6, 1, 3, 7, 6, 4, 9, 3]
# insert_sort(array)

def buscar(lista, numero):
	i = 0
	for i in range(len(lista)):
		if lista[i] == numero:
			print(i)
			sys.exit(0)
	print(-1)

a = [1, 3, 2, 45, 76, 8, 9, 3, 7]
buscar(a, 7)