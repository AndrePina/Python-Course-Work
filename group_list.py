def group_list(group, users):
	# i = 0
	for x in range(0, len(users)+1):
		# if len(users) == "":
			# print("this is the length of users: " +str(len(users)))
			# team = 
		# # members = users
		# print(len(group))
		# print(len(users))
		# print (users[i]) 
		# print(x)
		# print(len(users)) 
		users = str(users)
		# print(str(group) + ":" + str(users))
		team = (group) + ": " + str((users[1:len(users)-1]))
		# x = x + 1
		# i = i + 1

		# print (users[1:len(users)-1]) 
		# print(x)
		return team

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"
