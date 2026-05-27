string =input("please enter your own string: ")

string2 = ('')
for i in string:
    string2 = i + string2

print("\nThe Original String = ", string)
print("The reversed String=", string2)