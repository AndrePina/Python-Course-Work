
def factorial(n):
    result = 1
    for x in range(1,n):
        result = result +  (result * x)
    return result

for n in range(0,10):
    print(n, factorial(n ))