Number = int(input("Enter a number: "))
if Number % 20 ==0:
    print("twist")
elif Number % 15 == 0:
    pass
elif Number % 5 ==0:
    print("fizz")
elif Number % 3 ==0:
    print("buzz")
else:
    print(Number)

