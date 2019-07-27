from itertools import permutations
sarapavi=input()
sarapavi=list(sarapavi)
perm=permutations(sarapavi)
ant=[]
for j in list(perm):
    ant.append(''.join(list(j)))
sarapaviav=list(set(ant))
sa=[]
for i in range(len(sarapaviav)):
    sa.append(sarapaviav[i])
sa.sort()
for i in range(len(sa)):
    print(sa[i])
