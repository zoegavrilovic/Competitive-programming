def getMax(n,a,b,c):
    if n<0:
        return -1
    if n==0:
        return 0
    ca=getMax(n-a,a,b,c)
    cb=getMax(n-b,a,b,c)
    cc=getMax(n-c,a,b,c)
    res=max(ca,cb,cc)
    if res==-1:
        return -1
    else:
        return res+1

n=int(input())
a=int(input())
b=int(input())
c=int(input())
print(getMax(n,a,b,c))
