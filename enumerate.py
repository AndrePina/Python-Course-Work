# Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to return every other element from the list, this time using the enumerate function to check if an element is on an even position or an odd position.


def skip_elements(elements):
	lenOfElements = (len(elements))
	print("First lenOfElements: " +str(lenOfElements))
	r = 0

	while r < lenOfElements :
		print("Second lenOfElements: " +str(lenOfElements))
		newList = (list(enumerate(elements)))
		print(newList)
		r = r + 1
		print("r =: " +str(lenOfElements))
	return newList[r]
	
	print("Third i: " +str(i))

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']