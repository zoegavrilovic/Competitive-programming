def printIntersection(a,b,n,m):
    i=j=0
    while i<n and j<m:
        if a[i]==b[j]:
            print(a[i],end=" ")
            i=i+1
            j=j+1
        elif a[i]<b[j]:
            i=i+1
        else:
            j=j+1
    print()

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,m=map(int,input().strip().split())
        a=list(map(int,input().strip().split()))
        b=list(map(int,input().strip().split()))
        printIntersection(a,b,n,m)    
