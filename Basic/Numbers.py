# Add two numbers
a = 12
b = 3
result = a + b
print("Addition: ", result)

# Maximum of two numbers
c = 8
d = 10
print("Max number: ", max(c, d))

# Factorial of a number
import math
n = 6
print("Factorial: ", math.factorial(n))

# Find simple interest
# I = (P x T x R) / 100
def function(p, t, r):
    return (p * t * r) / 100

p, t, r = 8, 6, 8
interest = function(p, t, r)
print("Simple interest: ", interest)

# Find compound interest
# A = P(1 + R / 100)^t
# CI = A - P

P = 1200
R = 5.4
T = 2
A = P * (1 + R / 100) ** T
CI = A - P
print("Compound interest: ", CI)