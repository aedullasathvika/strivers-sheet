# Read two integers from the user input
n1 = int(input())
n2 = int(input())

# Initialize gcd to 1 (starting point for finding the greatest common divisor)
gcd = 1

# Loop through all numbers from 1 to the minimum of n1 and n2
for i in range(1, min(n1, n2) + 1):
    # Check if i is a divisor of both n1 and n2
    if n1 % i == 0 and n2 % i == 0:
        # If i is a common divisor, update gcd to i
        gcd = i

# Print the greatest common divisor
print(gcd)