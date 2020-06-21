def factorial(number):
    if number == 1:
        return 1
    else:
        return (number * factorial(number - 1))

num = factorial(6)
sum_1 = 0
string_num = str(num)
for i in range (0, len(string_num), 1):
    sum_1 += int(string_num[i])
    
print(sum_1)
