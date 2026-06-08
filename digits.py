num = int(input("Enter a number: "))

if num == 0:
    count = 1
else:
    count = 0
    
 
    if num < 0:
        num = -num

    
    while num > 0:
        num = num // 10 
        count += 1       

print("Total number of digits:", count)