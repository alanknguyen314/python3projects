import time
start_time = time.time()

def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])

m = 999
const = 0
for i in range (1, 50 , +1):
    for i1 in range (999, 900, -1):
        print (m * i1)
        if isPal(str(m * i1)) == True:
            print(m * i1, "is Palindromic!")
            if m * i1 > const:
                const = (m * i1)
    m -= 1
print("The largest palindrome that is a product of 2 3-digit numbers",
      const)
print(" Execution time: --- %s seconds ---" % (time.time() - start_time))

