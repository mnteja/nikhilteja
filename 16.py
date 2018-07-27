a,v=input().split()
a=int(a)
v=int(v)
for z in range(a+1,v):
	count=0
	for i in range(1,z+1):
		if z%i==0:
			count=count+1
	if count==2:
print (z,end=" ")
