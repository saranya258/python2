try:
    sa,sp=map(int,input().split())
    saav=list(map(int,input().split()))
    saav1=sorted(saav)
    print(saav1[sa-sp])
except ValueError:
    print("invalid")
