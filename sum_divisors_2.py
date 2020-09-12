# Fill in the empty function so that it returns the sum of all the divisors of a number, without including it. 
# A divisor is a number that divides into another without a remainder.

def sum_divisors(n):
	#sum = 0
	divisor_1 = 1
	#divisor_2 = 1
	#new_n = 0
	x = 0
	# Return the sum of all divisors of n, not including n
	while x < 37 :
	 	#if (n != 0):  
					if n % divisor_1 == 0: 
						
						#print("Upper n % divisor_1 & n =  " +str(n % divisor_1) + str(n))
						#print("What is good n? " +str(n))
						
						print("Divisor 1 A = " +str(divisor_1))
						divisor_1 = divisor_1 + 1
						print("Divisor 1 B = " +str(divisor_1))
						#n = n - 1
						#print("New_n_A = " +str(n))
						x = x + 1
						#print("X BEFORE elif = " +str(x))
					
					elif n % divisor_1 != 0:
						#print("--Lower divisor_1 & n =  " +str(n % divisor_1) + " - " + str(n))
						n = n - 1
						#print("New_n_B = " +str(n))
						x = x + 1
						#print("X after elif = " +str(x))
						print("--Failed on = " +str(x))
						#print("--failed ")

	#return sum


#print(sum_divisors(0))
# 0
#print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
#print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
