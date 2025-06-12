# Get input from the user
num = input("Enter a three-digit number: ")

# Check if the input is a three-digit number
if not (num.isdigit() and len(num) == 3):
    print("Please enter a valid three-digit number.")
else:
    num = int(num)
    # Extract digits
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10

    # Calculate the sum of the cubes of the digits
    armstrong_sum = hundreds**3 + tens**3 + ones**3

    # Check if the number is an Armstrong number
    if armstrong_sum == num:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")