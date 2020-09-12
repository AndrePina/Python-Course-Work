# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	return miles * 1.6  # approximately 1.6 km in 1 mile

km = str(convert_distance(55))

round_trip = str(my_trip_km * 2)

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(55)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + km)

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + round_trip)