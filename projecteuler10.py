import time
start_time = time.time()
def printPrime(number_range):
    sum_1 = 0
    list_1 = []
    def isPrime(number):
        for i in range (2, number, 1):
            if number % i == 0:
                return False
        
    for i in range (2, number_range + 1, 1):
        if isPrime(i) == None:
            sum_1 += i
            
    print(sum_1)

printPrime(100) 
            


print("The execution time is ", time.time() - start_time)


