start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))


all_numbers = list(range(start, end + 1))

even_numbers = []
odd_numbers = []

for num in all_numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print(f"\nAll Numbers: {all_numbers}")
print(f"Even Numbers: {even_numbers}")
print(f"Odd Numbers: {odd_numbers}")
