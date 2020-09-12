def multiples_of_7(n):
	for x in range(0,101):
		if n % 7 == 0:
			print(n)
			n = n - 1
		else:
			#print(n)
			n = n - 1

multiples_of_7(100)