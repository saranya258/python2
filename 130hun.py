sar=int(input())
grp=[]
a=0
for i in range(2,sar):
    s=0
    for j in range(2,i):
        if(i%j==0):
            s=1
    if(s==0): 
        grp.append(i)
for i in range(0,len(grp)):
    if(grp[i]==3 or grp[i]%10==3):
        a=a+grp[i]
print(a)
