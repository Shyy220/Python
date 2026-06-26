try:
    int(input("Enter a number: "))
except ValueError:
    print("You have to write only numbers")



try:
    int(input("Enter a number"))
except ValueError:
    print("You have to write only numbers")
finally:
    print("Program Ended")


age = -5
if age < 0:
    raise ValueError("Age can't be negative")
