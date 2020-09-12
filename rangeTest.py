def votes(params):
	for vote in params:
	    print("Possible option:" + vote)

print(votes(["yes","no","maybe"]))