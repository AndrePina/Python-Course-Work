# Python program to illustrate 
# Various examples and working of float() 
# for integers 
print(float(21.89)) 

# for floating point numbers 
print(float(8)) 

# for integer type strings 
print(float("23")) 

# for floating type strings 
print(float("-16.54")) 

# for string floats with whitespaces 
print(float("	 -24.45 \n")) 

# for inf/infinity 
print(float("InF")) 
print(float("InFiNiTy")) 

# for NaN 
print(float("nan")) 
print(float("NaN")) 

# Error is generated at last 
print(float("Geeks")) 


math.modf(x)