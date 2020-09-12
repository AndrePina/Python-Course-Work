# Fill in the empty function so that it returns the sum of all the divisors of a number, without including it. 
# A divisor is a number that divides into another without a remainder.

def sum_divisors(n):
	sum = 0
	divisor_1 = 1
	divisor_2 = 1
	x = 0
	# Return the sum of all divisors of n, not including n
	for x in range(n):
	 	if (n != 0):  
			#while n % divisor_1 == 0:
					if n % divisor_1 == 0: 
						print("What is n? " +str(n))
						#print("Modulus = " +str(n % divisor_1))
						#sum = divisor_1	 		
						#print("Divisor 1st = " +str(divisor_1))
						divisor_1 = divisor_1 + 1
						print("Divisor 2nd = " +str(divisor_1))
						#print("Current Sum = " +str(sum))
					
					if n % divisor_1 != 0:
						divisor_1 = divisor_1 + 1
						print("Does not equal 0")
						#return sum
						#continue
		#return sum
	x + 1

#print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
#print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
#print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
