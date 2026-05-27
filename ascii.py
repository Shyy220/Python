asci = input("Enter a single character: ")

# 2. Get and print the ASCII value
if len(asci) == 1:
    ascii_value = ord(asci)
    print(f"The ASCII value of 'asci' is {ascii_value}")
else:
    print("Please enter exactly one character.")
