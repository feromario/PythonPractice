# Armstrong number
# - a number that is equal to the sum of its own digits,
#   each raised to the power of the number of digits
# EX: 153 = 1^3 + 5^3 + 3^3

# Mathematical method
print("Mathematical method.")
num = int(input("Enter a number: "))
n = num
power = len(str(num))          # gives number of digits
total = 0

while n > 0:
    digit = n % 10             # mod to extract each digit
    total += digit ** power    # digit raised to power
    n //= 10                   # floor division

if total == num:
    print("Number is an Armstrong Number")
else:
    print("Number is not an Armstrong Number")

# String conversion method
print("String method.")
num = int(input("Enter a number: "))
num_string = str(num)
power = len(num_string)
total = 0

for digit in num_string:
    total += int(digit) ** power

if total == num:
    print("Number is an Armstrong Number")
else:
    print("Number is not an Armstrong Number")

# Functional style
print("Functional method.")
n = int(input("Enter a number: "))
s = n
b = len(str(n))
sum1 = 0

while n != 0:
    r = n % 10
    sum1 = sum1 + (r ** b)
    n = n // 10

if s == sum1:
    print(s, " is an Armstrong Number")
else:
    print(s, " is not an Armstrong Number")

# Recursive method
print("Recursive method.")
num = int(input("Enter a number: "))
power = len(str(num))

def arm_sum(x):
    if x == 0:
        return 0
    return (x % 10) ** power + arm_sum(x // 10)

if arm_sum(num) == num:
    print("Number is an Armstrong Number")
else:
    print("Number is not an Armstrong Number")


























