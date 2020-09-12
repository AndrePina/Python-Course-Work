def highlight_word(sentence, word):
	for i in range(len(sentence)): 
		newSentence = sentence.replace(word, word.upper())
		return newSentence
print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
