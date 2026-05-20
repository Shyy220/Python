height = float(input("Enter your height: "))
weight = float(input("Enter your weight"))
BMI = (weight/height/100)**2

if BMI <= 18.4 :
    print("you are underweight")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are overweight")
elif BMI <= 34.9:
    print("You are severely overweight")
elif BMI <= 39.9:
    print("You are obese")

