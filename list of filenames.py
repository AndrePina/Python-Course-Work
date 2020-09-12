# Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.

# return [x for x in range(0, n + 1) if x % 2 != 0]
# words = sentence.split(".")

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

def reName(filenames):
	for i in filenames:
		words = str(filenames)
		words = words.split(".")
		print(words)
		print("this is iA: " + str(i))
		print(i)
		print(type(words))
		print("Length of words = " +str(len(words)))
		print("Length of filenames = " +str(len(filenames)))
		#i += 1
		print("this is iB: " + str(i))
		#print("this is x: " + str(x))
		return [x for x in range(len(words)) if x >= 0]
		#print (enumerate(filenames))
		#return [x for x in range(0, len(filenames)) if x  ]

# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
#___  

#print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
print(reName(filenames))