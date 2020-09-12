# Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.

# return [x for x in range(0, n + 1) if x % 2 != 0]
# words = sentence.split(".")

# x = "ain" in txt
# print(x)

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")

import re
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]


def reName(filenames):
	newNames = []
	words2 = ""
	words3 = ""
	for x in range(len(filenames)-1):
		words = filenames
		#words = str(filenames)
		#words = words.split(".")
		#words = str(words).split(",")
		#words = str(words).strip("[")
		#print("stripped: " + words[x])
		#print(len(words))
		#print("This is words[x] value: " +str(words[x]))
		if words[x].endswith(".hpp"):
			#words = str(words).split(",")
			#words = str(words).split(",")
			words2 = str(words).replace(".hpp", ".h")
			#print(words2)
			#print("-------This is the hpp word: " +str(words[x]))

			#newNames.append(words)
			
		else:
			#newNames.append(words)
			#print("newNames = " + str(newNames))
			words3 = str(words)
			#print(words3)

		#x = x + 1
		newNames = words2
	return newNames# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
#___  

# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
print(reName(filenames))