def counter(start, stop):
	x = start
	#print("X1 = " + str(x))
	if start > stop:
		#print("X2 = " + str(x))
		return_string = "Counting down: "
		while x >= stop:
			
			return_string += str(x)
			#print("Xdown = " + str(x))
			#return_string += ","
			if x > stop:
					return_string += ","
			x = x - 1
	else:
		return_string = "Counting up: "
		while x <= stop:
			#print("X4 = " + str(x) + return_string)
			return_string += str(x)
			#print("Xup = " + str(x))
			if x < stop:
					return_string += ","

			if x == 0:
				#print("X5 = " + str(x))
				return_string += ","
			x = x + 1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"