def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# print(group,users)
		# print(users)
		# print(items)
		# Now go through the users in the group
		for user in users:
			# print(group)
			# print(users)
			# print(user)
			if user in user_groups:
				user_groups[user].append(group)
			else:
				user_groups[user] = [group]
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))