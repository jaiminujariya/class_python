#1.hello world 
#print("hellow")

#2.add two number 
#a = float(input("enter your number:"))
#b = float(input("enter your sevond number:"))
#print(a + b)

#3.even and odd
#n = int(input("enter your number:"))
#print("Even" if n % 2 == 0 else "Odd")

#4.check leap year
#y = int(input("enter a year:"))
#print("Leap year" if (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)) else "Not a leap year")

#5.pi value 
#from math import pi
#print(pi)

#6.store and print constant value
#MY_CONSTANT = 42  # constant by convention (uppercase)
#print(MY_CONSTANT)

#7.sqare of a number 
#n = float(input())
#print(n * n)

#8.area of circle
#from math import pi
#r = float(input("Radius: "))
#print(pi * r * r)


#9.check data type 
#x = 3.14
#print(type(x))          
#print(type(x).__name__) 
#print(isinstance(x, float)) 

#10.use math function
#import math

# basic unary functions
#n = float(input("Enter a number: "))
#print("sqrt:", math.sqrt(n) if n >= 0 else "undefined for negative")
#print("sin:", math.sin(n))
#print("cos:", math.cos(n))
#print("exp:", math.exp(n))
#print("log (natural):", math.log(n) if n > 0 else "undefined for <= 0")
#print("ceil:", math.ceil(n))
#print("floor:", math.floor(n))
# factorial only for non-negative integers
#if n.is_integer() and n >= 0:
 #   print("factorial:", math.factorial(int(n)))
#else:
 #   print("factorial: requires a non-negative integer")
# convert degrees to radians
#deg = float(input("Enter degrees to convert to radians: "))
#print("radians:", math.radians(deg))
# gcd of two integers
#a, b = map(int, input("Enter two integers for gcd (a b): ").split())
#print("gcd:", math.gcd(a, b))
# constants
#print("pi:", math.pi)
#print("e :", math.e)
 
 #11.find power
#@ base = float(input("Base: "))
#exp = float(input("Exponent: "))
#print(base ** exp)

#12.check positive or negative
#n = float(input())
#if n > 0:
    print("Positive")
#elif n < 0:
 #   print("Negative")
#else:
#    print("Zero")