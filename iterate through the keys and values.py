# Complete the code to iterate through the keys and values of the cool_beasts dictionary. Remember that the items method returns a tuple of key, value for each element in the dictionary.

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for beasts, tentacles in cool_beasts.items():
	# print(cool_beasts.items())
    print("{} have {}".format(beasts, tentacles))