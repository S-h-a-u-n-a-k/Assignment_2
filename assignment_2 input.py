#QUESTION 1 
string="Python is a case sensitive language"
length=len(string)
print("length of the input string is ",length)
x=string[::-1]
print("reverse order of the input string  --> ",x)
x=string[10:26]
print("New string =",x)
x=string.replace("a case sensitive" , "object oriented")
print("d part: ",x)
x=string.find("a")
print("index of substring a in input string  --> ",x)
x=string.replace(" " , "")
print("f part",x)

print("\n\n\n")

#QUESTION 2
_name=str(input("enter your name: "))
_SID=int(input("enter your SID: "))
_branch=str(input("enter your department: "))
_CGPA=float(input("enter your CGPA: "))
print("Hey, ",_name," here!")
print("My SID is ",_SID,)
print("I am from ",_branch," department and my CGPA is ",_CGPA)

print("\n\n\n")

#QUESTION 3
a=56
b=10
print("a&b  -->  ",a&b)
print("a|b  -->  ",a|b)
print("a^b  -->  ",a^b)
print("left shift a with 2 bits (a<<2)  -->  ",a<<2)
print("left shift b with 2 bits (b<<2)  -->  ",b<<2)
print("right shift a with 2 bits (a>>2)  -->  ",a>>2)
print("right shift b with 4 bits (b>>4)  -->  ",b>>4)

print("\n\n\n")

#QUESTION 4
p=input("enter first number: ")
q=input("enter second number: ")
r=input("enter third number: ")
print(max(p,q,r))

print("\n\n\n")

#QUESTION 5
string=str(input("enter a string: "))
if 'name' in string:
    print("yes")
else:
    print("no")

print("\n\n\n")

#QUESTION 6
x=int(input("enter the first side: "))
y=int(input("enter the second side: "))
z=int(input("enter the third side: "))
if (y+z>=x and x+z>=y and x+y>=z):
    print("yes")
else:
    print("no")



 
