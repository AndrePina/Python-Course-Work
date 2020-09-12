# Let's revisit our lucky_number function. We want to change it, so that 
# instead of printing the message, it returns the message. This way, the 
# calling line can print the message, or do something else with it if 
# needed. Fill in the blanks to complete the code to make it work.


def lucky_number(name):
  number = len(name) * 9
  ___ = "Hello " + name + ". Your lucky number is " + str(number)
  ___
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))