#Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.
 
def pig_latin(text):
	words = str(text).split()
	say = "ay"
	c = 0
	newString = ""
	q = (len(words[c]))
	lengthOfWord = len(words[c][0:])
	for x in range(0,(q)):
				# print("This is q: " + str(q))
				# # print(NumWords)
				# print(lengthOfWord)
				firstLetter = words[c][0]
				middleWord = words[c][1:]
				lastLetter = words[c][q-1:]
				newString = newString + (str(middleWord)) + str(firstLetter) + say + " "
				# print(firstLetter)
				# print(middleWord)
				# print(lastLetter)
				# print(newString)
				c = c + 1
				#print("---This is print(words[c][0]): " + words[c][0])

	x = x + 1
				#d = d + 1
				#print(c)
			
	return newString
	#c = 0
    # Create the pig latin word and add it to the list
	#return newString
    
    # Turn the list back into a phrase

		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
#print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"