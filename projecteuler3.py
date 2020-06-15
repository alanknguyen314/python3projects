import time
start_time = time.time()

number_1 = 0
def isPrime(n): 
      
    if (n <= 1): 
        return False
  
    for i in range(2, n): 
        if (n % i == 0): 
            return False
  
    return True

for i in range (1, 600851475143, 1):
    if isPrime(i) == True:
        if number_1 <= i:
            number_1 = i
            
print(number_1)
print(" Execution time: --- %s seconds ---" % (time.time() - start_time))
      


