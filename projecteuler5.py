import time
start_time = time.time()

number = int(input("Please enter your number!"))
x = 1

while number > x:
    if x % 2 == 0 and x % 3 == 0 and x % 4 == 0 and x % 5 == 0 \
       and x % 7 == 0 and x % 8 == 0 and x % 9 == 0 and x % 10 == 0 \
       and x % 11 == 0 and x % 12 == 0 and x % 13 == 0 and x % 14 == 0 \
       and x % 15 == 0 and x % 16 == 0 and x % 17 == 0 and x % 18 == 0 \
       and x % 19 == 0 and x % 20 == 0:
        print("This is the number", x)
        break
    x += 1
    
        
def factorial(n):
    result = 1
    while n >= 1:
        result *= n
        n -= 1
    return result

print(" Execution time: --- %s seconds ---" % (time.time() - start_time))

# Since the original takes lots of time, we can reduce the amount of work
# need to check by the program by using larger intervals
# Since the number has to be divisible by 20, we can start at 20 and goes up by 20
"""
import time
start_time = time.time()

number = int(input("Please enter your number!"))
x = 20

while number > x:
    if x % 2 == 0 and x % 3 == 0 and x % 4 == 0 and x % 5 == 0 \
       and x % 7 == 0 and x % 8 == 0 and x % 9 == 0 and x % 10 == 0 \
       and x % 11 == 0 and x % 12 == 0 and x % 13 == 0 and x % 14 == 0 \
       and x % 15 == 0 and x % 16 == 0 and x % 17 == 0 and x % 18 == 0 \
       and x % 19 == 0 and x % 20 == 0:
        print("This is the number", x)
        break
    x += 20
    
        
def factorial(n):
    result = 1
    while n >= 1:
        result *= n
        n -= 1
    return result

print(" Execution time: --- %s seconds ---" % (time.time() - start_time))
"""
    
