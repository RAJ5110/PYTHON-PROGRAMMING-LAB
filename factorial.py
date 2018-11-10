n=int(input("Enter the no."))
result=1
for i in range(n,0,-1):
	result=result*i
print("fact of",n,"is",result)