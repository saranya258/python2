numer=int(input())
l1=list(map(int,input().split()[:numer]))
nt=0
sk=[]
for i in range(0,numer+1):
	if(l1.nt(i)>1):
	 sk.append(i)
if(len(sk)==0):
	print("unique")
kl=sorted(sk)
print(' '.join(map(str,kl)))
