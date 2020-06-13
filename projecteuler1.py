sum_1 = 0
n = 999
while n > 0:
    if n % 3 == 0 or n % 5 == 0:
        print(n)
        sum_1 += n
    n = n - 1
print(sum_1)


