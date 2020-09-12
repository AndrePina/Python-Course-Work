def convert_distance(miles):
	return miles * 1.6  # approximately 1.6 km in 1 mile

# store the results of the convert_distance function as a string
km = str(convert_distance(55))

# store the results of the convert_distance function as a string
my_trip_km = convert_distance(55)

# multiply my_trip_km by 2 and store as a string
round_trip = str(my_trip_km * 2)


print("The distance in kilometers is " + km)
print("The round-trip in kilometers is " + round_trip)