# The skip_elements function returns a list containing every other element from an input list, starting with the first element. Complete this function to do that, using the for loop to iterate through the input list.

def skip_elements(elements):
	# Initialize variables
	new_list = []
	_2nd_list = []
	#range01 = len(elements)
	#print("This is the range01: " + str(range01))
	#i = 3

	# Iterate through the list
	for i in elements:
		#print(i)
		new_list.append(i)
		x = new_list.index(i)
		if x % 2 == 0:
				#print("this is x: " + str(x))
				_2nd_list.append(i)

	return _2nd_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []


