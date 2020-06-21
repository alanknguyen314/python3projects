number = 2**1000
sum_1 = 0
string_number = str(number)
for i in range (0, len(string_number), 1):
    sum_1 += int(string_number[i])
    
print(sum_1)
