a=input()
b=len(a)
c=int(a)
s=0
i=0
while(i<b):
	s=s+int(a[i])**b
	i=i+1
if s==c:
	print("it is an armstrong number")
else :
	print("it is not an armstrong number")
