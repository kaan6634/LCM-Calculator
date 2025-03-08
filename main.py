import math

def find_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("LCM of", num1, "and", num2, "is:", find_lcm(num1, num2))
