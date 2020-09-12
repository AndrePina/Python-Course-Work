def highlight_word(sentence, word):
	test = "tEst"
	# print(sentence)
	# print(word)
	# print(sentence.find(word))
	# print(sentence[7])  #.upper()

	for i in range(len(sentence)):
		# print(sentence[i])
		# print(sentence.find(word))
		# print((word).upper())
		# print(len(sentence.find(word)))
		# print("{} {}".format(beasts, tentacles))
		# print(sentence.replace(str(sentence.find(word)), ((word).upper())))
		newSentence = sentence.replace(word, word.upper())	
		# print((word).upper())
		# print(newSentence)


		return newSentence

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
