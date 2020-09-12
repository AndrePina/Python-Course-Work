# The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values.
# cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
# for beasts, tentacles in cool_beasts.items():
# 	# print(cool_beasts.items())
#     print("{} have {}".format(beasts, tentacles))

def groups_per_user(group_dictionary):
  user_groups = {}
	# Go through group_dictionary
for groups in group_dictionary.keys():
		# Now go through the users in the group
		# print(groups)
		# print(group_dictionary.keys())
		# print(group_dictionary.values())
		# print(group_dictionary.items())
		groups = [group_dictionary.keys()]
		users = [group_dictionary.items()]
		# print(groups)
		print(users)
		# user_groups.update(group_dictionary.items())		
		# user_groups.update(group_dictionary.values())

		# print(user_groups)
		# for users in :
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))