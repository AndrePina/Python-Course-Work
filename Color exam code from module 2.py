def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
		#print("Line 4 : " + color)
		#print("Line 4 hex_color : " + hex_color)
		return hex_color
	elif color == "green":
		hex_color = "#00ff00"
		return hex_color
	elif color == "blue":
		hex_color = "#0000ff"
		return hex_color
	else:
		hex_color = "unknown"
		#print("Line 10 : " + color)
	return "unknown"

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown