#Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.
# index = letterList.index(letter)
# str = 'string'
# >>> for i in range(0, len(str)):
# ...     print str[i]

def pig_latin(text):
	words = str(text).split()
	say = "ay"
	i = 0
	loText = len(text)
	NumWords = len(words)
	lengthOfWord = 0
	lengthOfWord = len(words)
	lengthOfWord2 =  str(words[0:5]).split()
	#for c in range(0, (lengthOfWord-1)):
	  				# print(words[c])
	  				#print(len(words[c])) 
	for d in range(0, len(words[c])+1):
				#print(words[c][d])
				q = (len(words[c]))
				#print(q-1)
				firstLetter = words[c][0]
				middleWord = words[c][1:]
				lastLetter = words[c][q-1]
				newString = (str(middleWord)) + str(firstLetter) + say
				#print(newString)
				#print(lastLetter)
				return newString
				d = d + 1

    # Create the pig latin word and add it to the list
	#return newString
    
    # Turn the list back into a phrase

		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
#print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"