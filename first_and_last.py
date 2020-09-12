def first_and_last(message):
	if message == "":
		return True
	elif message[0] != message[-1]:
		return False
	elif message[0] == message[-1]:
		return True
	

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))