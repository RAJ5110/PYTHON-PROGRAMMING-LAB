a=str(input("Enter the name of 1st student:"))
b=int(input("Enter the marks scrored in maths:"))
c=int(input("Enter the marks scored in english:"))
d=int(input("Enter the marks scored in science:"))
l1=[a,"maths",b,"english",c,"science",d]
e=str(input("Enter the name of 2nd student:"))
f=int(input("Enter the marks scrored in maths:"))
g=int(input("Enter the marks scored in english:"))
h=int(input("Enter the marks scored in science:"))
l2=[e,"maths",f,"english",g,"science",h]
i=(b+c+d)/3
j=(f+g+h)/3
if i>j:
	print("the student securing highest marks is "+a)
elif j>i:
	print("the student securing highest marks is "+e)