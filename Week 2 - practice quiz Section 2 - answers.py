
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)