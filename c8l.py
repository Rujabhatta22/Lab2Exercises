#Given a three-digit number. Find the sum of its digits.
num= int(input("enter the integer"))
a = num//100
b = num//10 % 10
c = num%10
print(a + b + c)