def lucky_number(name):
  number = len(name) * 9
  return "Hello " + name + ". Your lucky number is " + str(number)
 
print(lucky_number("Kay"))
print(lucky_number("Cameron"))