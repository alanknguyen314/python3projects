number = 10
sum1 = 0
sum2 = 0
y = 1

for i in range (0, 101, 1):
    sum1 = sum1 + i*i
    print("The sum of all squares is: ", sum1)
    
for i in range (0, 101, 1):
    sum2 = sum2 + i
    print("The sum of all squared is: ", sum2)
    
final_result = sum2*sum2 - sum1
print(final_result)
