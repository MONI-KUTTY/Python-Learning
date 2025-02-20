# Python Operators
# Python operators is used to evaluate, compare both the variables. It tells whether the two variables equal or not, true or false and so on.
"""
There are 7 types of operators in python.

1. Arithmetic Operator
2. Assignment Operator
3. Comparison Operator
4. Logical Operator
5. Identity Operator
6. Membership Operator
7. Bitwise Operator

Aal Aaluku CLImb panikranga MB ah - AACLIMB
-   -      ---              --
"""
# ----------------------------------------------------------------------------------------------------------------------------------------
# 1. Arithmetic Operator - + - addition, - - subtraction, * - multiplication, / - division, % - Modulus, ** - Exponential, // - Floor Divi.

# Addition:
a = 50
b = 2
print(a+b)
print(50+2)

# Subtraction:
a = 50
b = 60
print(a-b)
print(50-60)

# Multiplication:
a = 10
b = 20
print(a*b)
print(10*20)

# Division: - Print the quotient and returns value in float
a = 100
b = 200
print(a/b)
print(100/200)

# Floor Division: 
a = 100
b = 200
print(a//b)
print(100//200)

# Modulus: - Prints the Remainder - It do not consider remainder. It returns the lowest number as the remainder in the below case.
# Since 100 is less than 200, we can divide but quotient is in decimal and remainder is 0. But as the rule says it do not consider decimal
# It returns the lower number.
a = 100
b = 200
print(a%b)
print(100%200)

# Exponential: - Here 1st is the normal value and the following second value after ** is considered as power value. 
# Eg: 2**3 mean 2^3 - 2*2*2 = 8.
a = 2
b = 4
print(a**b)
print(2**4)

# ----------------------------------------------------------------------------------------------------------------------------------------

# 2. Assignment Operator - += addition equal to, -= subtraction equal to, *= multiplication equal to, /= division equal to
# %= modulus equal to, **= exponential equal to, //= floor division equal to.

# Addition Equalto +=
a = 10
b = 20
b += a
print(b)

# Subtraction Equalto -=
a = 10
b = 20
b -= a # b = b-a
print(b)

a = 10
b = 20
a -= b # a = a-b
print(a)

# Multiplication Equalto *=
a = 20
b = 2
a *= b # a = a*b
print(a)

a = 5
a *= 2
print(a)

# Division Equalto /=
a = 50
b = 2
a /= b
print(a)

a = 50
b = 2
b /= a
print(b)

a = 10
a /= 2
print(a)

# Floor Division Equalto //=
a = 50
b = 2
a //= b
print(a)

a = 50
b = 2
b //= a
print(b)

a = 10
a //= 2
print(a)

# Modulus Equalto %=
a = 50
b = 2
a %= b
print(a)

a = 50
b = 2
b %= a
print(b)

a = 10
a %= 2
print(a)

# Exponentiation Equalto **=
a = 2
b = 3
a **= b
print(a)

a = 2
b = 3
b **= a
print(b)

a = 5
a **= 2 # a= 5 ** 2 = 5 ^ 2 = 25
print(a)

# ----------------------------------------------------------------------------------------------------------------------------------------

# Comparison Operators - == - equalto, != - not equalto, > - greater than, < - less than, >= - greater than or equal to, <= - less than or equalto

# Method - 1
a = 10
b = 20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# Method - 2
a = int(input("Enter The Number"))
b = int(input("Enter The Number"))
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# Method - 3
print(10.5==20)
print(10!=20)
print(10>20)
print(10<20)
print(10>=20)
print(10<=20)
print(5+6j == 6+6j)

# Method - 4 - checks based on ascii value
a = "Monish"
b = "Sara"
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# Method - 5
a = ['Abdul']
b = ['Snthoshkumar']
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# ----------------------------------------------------------------------------------------------------------------------------------------

# Logical Operator - AND - Prints True If Both The Cases Are True, OR - Prints True If Either The Case Is True, NOT - Contradiction 
# AND - check for false, OR - check for true, 

#  Method - 1
Monish = 8.5
Sara = 9.5
print(Monish and Sara) # T AND T = 2nd Value as o/p, F and T = 1st value as o/p, T and F = 2nd value as o/p, F and F = 1st value as o/p 
print(Monish or Sara) # or T or T = 1st value as o/p, F or T = 2nd value as o/p, T or F = 1st value as o/p, F or F = 2nd value as o/p
print(not Monish and Sara) # F and 9.5 = False
print(not Monish or Sara) # F or 9.5 = 9.5
print(not Monish and not Sara) # F and F = False
print(not Monish or not Sara) # F or F = False
print(Monish and not Sara) # 8.5 and False = False
print(Monish or not Sara) # 8.5 or False = 8.5

# Method - 2 
print(Monish == 8.5 and Sara == 9.5) # T and T = T
print(Monish == 9.5 and Sara == 9.5) # F and T = F
print(Monish == 8.5 and Sara == 7.5) # T and F = F
print(Monish == 9.5 and Sara == 7.5) # F and F = F
print(Monish == 8.5 or Sara == 9.5) # T or T = T
print(Monish == 9.5 or Sara == 9.5) # F or T = T
print(Monish == 8.5 or Sara == 7.5) # T or F = T
print(Monish == 9.5 or Sara == 7.5) # F or F = F
print(not Monish == 8.5 and Sara == 9.5) # F and T = F
print(Monish == 9.5 and not Sara == 9.5) # F and F = F
print(Monish == 8.5 and Sara == 7.5) # T and F = F
print(not Monish == 9.5 and not Sara == 7.5) # T and T = T
print(not Monish == 8.5 or Sara == 9.5) # F or T = T
print(Monish == 9.5 or not Sara == 9.5) # F or F = F
print(Monish == 8.5 or Sara == 7.5) # T or F = T
print(not Monish == 9.5 or not Sara == 7.5) # T or T = T

# ---------------------------------------------------------------------------------------------------------------------------------------

# Identity Operator - If same value assigned for 2 variables mean the o/p is true, orelse it is false. It chks whether the val is sme or nt
a = 5
b = 10
print(a is b)
print (a is not b)

c = 10
d = 10
print(c is d)
print(c is not d)

e = 10
f = 10.0
g = e
print(e is f)
print(e is not f)
print(e is g)
print(e is not g)

Name1 = 'Monish'
Name2 = ['Monish']
print(Name1 is Name2)
print(Name1 is not Name2)

# ---------------------------------------------------------------------------------------------------------------------------------------

# Membership Operator - It checks whether the value is present in the list or not. It returns true if the value is present in the list, 
# else it returns false. In and Not In are the two types present in membership operator.
# Membership can be used in list, tuple, string, dictionary, set, frozenset.

a = [1,2,3]
b = "1,2,3,4,5"
c = (1,2,3,4)
d = {1:1, 2:2}
e = {1:"Monish", 2:"Sara"}
f = {"1","2", "3"}

print(1 in a)
print(3 not in a)
print("4" in b)
print("6" not in b)
print(1 in c)
print(4 not in c)
print(1 in d)
print(3 not in d)
print(1 in e)
print(3 not in e)
print("Monish" in e) # Don't give output because it checks only keys
print("Rahul" in e) # Don't give output because it checks only keys
print("1" in f)
print("4" not in f)

# ---------------------------------------------------------------------------------------------------------------------------------------

# Bitwise Operator - It is used to perform operations on the binary numbers.
#  - and, | - or, ^ - xor, ~ - not, << - left shift, >> - right shift.

# & - and 1-1 = 1, remaining are all 0
# | - or 0-0=0, remaining are all 1
# ^ - xor 1-0=1, 0-1=1, 1-1=0, 0-0=0
# ~ - not 1-0, 0-1
# << - Left Shift - add 0 at right
# >> - Right Shift - add 0 at left

a = 2
b = 5
print(a & b) 
print(a | b)
print(a ^ b)
print(~a)
print(a << b)
print(a >> b)  
print(a<<3)
print(b>>2)

'''
To perform all the operations, ascii value, truth table and binary values should be remembered.
'''

# ---------------------------------------------------------------------------------------------------------------------------------------
