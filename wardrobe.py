# In Python, a dictionary can only hold a single value for a given key. To workaround this, our single value can be a list containing multiple values. Here we have a dictionary called "wardrobe" with items of clothing and their colors. Fill in the blanks to print a line for each item of clothing with each color, for example: "red shirt", "blue shirt", and so on.
# wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}

# for article, colors in wardrobe.items():

# 	for __:
# 		print("{} {}".format(__))

# n = 0
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for article, colors in wardrobe.items():
	# print(article)
	n = 0
	# print (colors)
	for color in colors:
		# newString = article 
		article1 = article
		print("{} {}".format(colors[n], article))
		# print(len(colors))
		# print(colors[n]+ " " + article)
		# print(len(wardrobe))
		n += 1
 	