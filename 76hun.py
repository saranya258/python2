sar=int(input())
k=[]
for i in range(sar):
	l1=[int(x) for x in input().split()]
	m=sum(l1)
	k.append(m)
m=sum(k)/(sar*sar)
print("%.6f" %m)
