#Python Program to calculate simple interest
p = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate (in percentage): "))
t = float(input("Enter time in years: "))
simple_interest = (p * r * t) / 100

print("Simple interest:", simple_interest)
