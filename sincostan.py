import math

def calculate_trig_values(degree_angle):
    # Convert the angle from degrees to radians
    radian_angle = math.radians(degree_angle)
    
    # Calculate trigonometric values
    sine_val = math.sin(radian_angle)
    cosine_val = math.cos(radian_angle)
    tangent_val = math.tan(radian_angle)
    
    # Return rounded results to handle floating-point precision quirks
    return round(sine_val, 4), round(cosine_val, 4), round(tangent_val, 4)

# Get input from the user
try:
    user_angle = float(input("Enter an angle in degrees: "))
    sin_res, cos_res, tan_res = calculate_trig_values(user_angle)
    
    print(f"\nResults for {user_angle}°:")
    print(f"  sin({user_angle}) = {sin_res}")
    print(f"  cos({user_angle}) = {cos_res}")
    
   
    if user_angle % 180 == 90:
        print(f"  tan({user_angle}) = Undefined (Asymptote)")
    else:
        print(f"  tan({user_angle}) = {tan_res}")

except ValueError:
    print("Please enter a valid numeric value.")
