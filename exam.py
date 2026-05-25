medical_cause = str(input("Do you have any medical conditions(Y/N):" ))
if medical_cause =='Y':
    print("You are allowed to attend exam")
else:
    attendence = int(input("Enter your attendence rate: "))

    if attendence>=75:
     print("You can write the exam")
    else:
     print("You can't write the exam")
    