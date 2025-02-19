Name = "santhoshkumar"
name = "monish"
nAME = "sanjay"
NAME = "sara" 

print(Name)
print(name)
print(nAME)
print(NAME)
print ("abdulkalam")

Name = 10
print(Name)

# Firstname = sandy --> camel case, pascal case, snake case
# firstName --> camel case
# Firstname --> pascal case
# First_Name --> snake case -- uper,lowercase - underscore*

'''
Middle_Name 
Firstname
lastname
'''
a = 10
print("10")
print("a")
print(a)

# variables starting contains _ , letters followed  by letters,underscore and numbers
# It do not contain special characters or special keywords like def, class and do not start with numbers.
# 1st version - 1991, guido van rossum - founder, used in web, data analytics, data sience, robotics and much more,...
# general purpose language and interpreted language
# comments - single line - #, multiline - '''  ''', """""" """"""
'''
 DataTypes 
 1. Integers           - whole numbers - +,-, infinite length
 2. Floats             - decimal numbers - +. -, infinite length
 3. Complex numbers    - 3+4j - combination of both real and imaginary numbers.
 4. Strings            - sequence of characters - single quotes, double quotes - "Monish", 'santhosh'
 5. Boolean            - true or false

 '''
# integer
a = 10
b = -10000
c = a+b
print(c)

# float
a = 1000.00
b = -10000.00
c=a+b
print(c)
print(type(a))
print(type(b))

#complex number
x = 10+5j
y = 20+100j
z = (x+y)
print(z)
print(type(x))

#do's
a = int(input("Enter the number"))
b = int(input("Enter the number"))
c=a+b
print(c)

h = 3e5
print(h)


k = float(input("enter the float value"))
print(k)

l = complex(input("Enter the complex number"))
print(l)
m = complex(input("Enter the complex number"))
print(m)
n = l+m
print(n)

''' dont's
a = input("Enter the name")
b = int(input("enter the number"))
c = a+b
print(c) '''

#string
a = "monish"
print(a)

#string slicing [start:end:count] - M   o   n   i   s   h
#                                   0   1   2   3   4   5
#                                  -6  -5  -4  -3  -2  -1
b = ' General Knowledge '
print(len(b))
print(b[0:])
print(b[0:8])
print(b[-11:-1])
print(b[0: :2])
print(b[ :-1])
print(a[0:])
print(a[:-1])

# string concatenation - Adding two strings. Giving a string as a value to a particular variable, so that we can add two or more strings like a number.

r = 'teddy'
s = "bear"
print(r+s)
print(r+" "+s)
print(r+' '+s)

t = str(input("Enter the first word"))
u = str(input("Enter the second word"))
v = t+u
print(v)

# string modification - change to lowercase, uppercase, replace - replace a string, strip - removes a white space, split - split 2 strings
# lowercase = .lower(), uppercase = .upper(), replace = ("old","new",count), strip = remove starting and ending white spaces, split = changes into two or more strings (separator, maxsplit)
a = ' Karadiii '
b = '  Papaaa  '
c = a+ " " +b
print(c)
print(c.lower())
print(c.upper())
print(c.strip())
print(c.replace('a','o'), c.replace("i" , "e"), c.replace("Karadiii" , "Teddy")) 
print(c.split())
d = c.lower()
print(d)

x = 'santhoshkumar'
y = x.lower()
print(y)
print(x.split("t"))
print(x.split("s",2))

'''
1) Introduction - 1991, guido van rossum, general purpose language, interpreted language, used in data analytics, science, aiml, robotics
2) comments - singleline - #, multiline - """ """, ''' '''
3) variables - used to store values - letters and underscore = allowed, special keys and characters = not allowed, 2nd letter of variable can be number, letter or underscore.
4) Data types 
5) Types of Data Types - integer, float, complex, string.
integer - number with no decimal
float - number with decimal
complex - real and imaginary numbers, e - powers, e=10, 3e2 = 3 10^2 = 3*100 = 300 *e,j*
string - slicing, concatenation, modification - lowercase, uppercase, split, replace, strip.
'''
b = 'monish'
print(b[0: :2])

# string format: This is used to add a word or number to a existing string.
# Steps: assign a variable and value, assign an existing string to a variable, prinnt by using format() function.

# Method - 1

Name = "Santhosh"
Degree = "B.Tech"
College = "MNMJEC"
Cgpa = 9
Intro = "My name is {}, currently persuing {} in {}. My current cgpa is {}."
print(Intro.format(Name, Degree, College, Cgpa))

# Method - 2

Name = "Monish"
Degree = "B.Tech"
College = "MNMJEC"
Cgpa = 9.5
Intro = "My name is {}, currently persuing {} in {}. My current cgpa is {}."
Self_Intro = "My name is {1}, currently persuing {3} in {2}. My current cgpa is {0}."
print(Intro.format(Cgpa, Name, Degree, College))
print(Self_Intro.format(Cgpa, Name, College, Degree))

# Method - 3

Name = str(input("Enter the name"))
Role = str(input("Enter the role"))
Company = str(input("Enter the company"))
Experience = int(input("Enter the number"))
Intro = "My name is {}. I'm working as a {} in {}. I have {} years of experience."
print(Intro.format(Name,Role,Company,Experience))
Self_Intro = "My name is {1}. I'm working as a {0} in {3}. I have {2} years of experience."
print(Self_Intro.format(Role,Name,Experience,Company))
         
# f-string - Here you can directly insert the variable name inside the string instead of using format() function. It is faster than format() function.

Name = "santhoshkumar"
Role = "Data Analyst"
Company = "Google"
My_Intro = f"I'm {Name}. I'm working as a senior {Role} in {Company}. "
print(My_Intro)

#Boolean - True or False. Any inputs like string, int, float, list, tuple, dictionary, set are true except empty values and 0. If no values mentioned then it is considered as false.

# Method - 1
a = True
print(type(a))
b = "Monish"
print(bool(b))
c = ""
print(bool(c))
d = -1.24
print(bool(d))
e = 0
print(bool(e))
f = [1,2,3,4]
print(bool(f))
g = 5<4
print(bool(g))

# Method - 2

print(bool(0))
print(bool("sara"))
print(bool([1,3,5,7]))

# Review:

'''
1) Introduction
2) Comments
3) Variables
4) Data Types - Integer, Float, Complex, String, Boolean.
5) String - slicing, concatenation, modification - Lowercase, uppercase, split, strip, replace, format, f-string.
6) Boolean - True or False
'''

a = "monish" 
print(a)
print(bool(" ")) 
