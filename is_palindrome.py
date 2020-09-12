# The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read from left to right or right to left, omitting blank spaces, and ignoring capitalization. Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.

# txt = "Hello World"[::-1]
# print(txt)

def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = input_string[::-1]
	#print(input_string)
	#print(reverse_string)
	# Traverse through each letter of the input string
	for eachLetter in input_string:
		a = 0
		if input_string[a].lower() == reverse_string[a].lower():
			print("Split_input_string = " + str(input_string.split()))
			#print(input_string.split())
			return True
			a = a+1
		else:
			#print("input_string = " + input_string)
			#print("Split_input_string = " + str(input_string.split()))
			#print("Split_reverse_string = " + str(reverse_string.split()))
			
			return False
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
	#	if ___:
	#		new_string = ___
	#		reverse_string = ___
	# Compare the strings
	#if ___:
	#	return True
	#return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True