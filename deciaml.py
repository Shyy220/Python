
decimal_numbers = [10, 19, 0]

for num in decimal_numbers:
    original_num = num
    binary_string = ""
    

    if num == 0:
        binary_string = "0"
    
    while num > 0:
        remainder = num % 2               
        binary_string = str(remainder) + binary_string  
        num = num // 2                       
        
    
    print(f"Decimal {original_num} in binary is: {binary_string}")