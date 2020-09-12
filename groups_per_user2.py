# data = {'ItemA': [123456, 123654], 'ItemB': [456789, 456987]}
# for key in data:
#     for items in data[key]:
#         print(key ,':' , items)
# dictionary[key] = value
def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	i = 0
	# for key, value in group_dictionary.items():
	for groups, users in group_dictionary.items():
		# Now go through the users in the group
		# print(groups)
		# print(users)
		# group = group_dictionary.keys()
		# users = str(group_dictionary.items()).strip("', '")
		# my_list = group_dictionary.keys()
		# print(i)
		# newValue = value[i]
		# print(newValue)
		# print(value[i],key)
		i += 1
		# print(i)
		# print("Len of items: " +str(group_dictionary.items()) + " is :"+str(len(group_dictionary.items())))
		# Now go through the users in the group
		for items in users:
			print(items)
			

		# Now add the group to the the list of groups for this user, creating the entry in the dictionary if necessary

		# return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))