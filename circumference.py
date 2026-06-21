import math


def calculate_circumference(radius):
    """Calculates the circumference of a circle given its radius."""
    return 2 * math.pi * radius


user_radius = float(input("Enter the radius of the circle: "))

result = calculate_circumference(user_radius)

print(f"The circumference of the circle is: {result:.2f}")