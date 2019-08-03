Sar=int(input())
Sa=list(map(str,input().split()))[:Sar]
pa=[]
t=[]
for i in range(0,len(Sa)):
    pa.append(Sa[i].lower())
for i in range(0,Sar):
      m=min(pa)
      t.append(m)
      pa.remove(min(pa))
for i in t:
    print(i)
