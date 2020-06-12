# Declaring variables
num_0 = 0
num_1 = 1
num_2 = 0
add_num = 1
check_list = []
check_list_2 = []
# Take in a number and find the triangular numbers. Put those into an array.
range_for_numbers = int(input("Please enter the number of triangular numbers you wish to print!"))
for i in range (range_for_numbers):
    num_0 += add_num
    add_num += 1
    check_list_2.append(num_0)
    
print(check_list_2)
# For each items in check_list_2 which contains the triangular numbers, check ecah one for their factors and put them in an array
for i in check_list_2:
    num = i
    print(num)
    while num >= num_1:
        if num % num_1 == 0:
            check_list.append(num_1)
        num_1 += 1
    num_1 = 1
    print("The length is, ", len(check_list))
    if len(check_list) >= 500: # first num to have over 500 divisors
        print("Stop!")
        break
    check_list.clear()
    

    
        

    

        
        

    

    
    
    
    
    

