def double_word(word):
	words = (word * 2) + str(len(word) * 2)
	return words

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0