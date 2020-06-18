import time
start_time = time.time()
for a in range (2, 50000, 1):
    m = a
    n = 1
    while m < (m + 100) and n < (100 - (m - n)):
        a = m**2 - n**2
        b = 2*m*n
        c = n**2 + m**2
        print(a, b, c)
        m += 1
        n += 1
        if (a + b + c == 1000):
            print(a*b*c, 'This is the answer  AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA FINALLY')
            break
print("Total execution time: ", time.time() - start_time)
