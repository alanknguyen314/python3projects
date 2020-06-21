import time
start_time = time.time()
def printPrime(number_range):
    list_1 = []
    def isPrime(number):
        for i in range (2, number, 1):
            if number % i == 0:
                return False
        
    for i in range (2, number_range + 1, 1):
        if isPrime(i) == None:
            list_1.append(i)
            if len(list_1) >= 10001:
                print("STOP")
                print(i)
                break       
    print(list_1, "Length of list equal: ", len(list_1))
            

printPrime(150000)
print("The execution time is ", time.time() - start_time)

