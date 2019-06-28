def merge(a,n,b,m):
    for j in range (0,m):
        for i in range (0,n):
            if a[i]>=b[j]:
                k=b.pop(j)
                a.insert(i,k)
                l=a.pop(n)
                b.insert(m-1,l)
    a.sort()
    b.sort()

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        merge(a,n,b,m)
        if(len(a)!=n and len(b)!=m):
            print("Do in O(1) space")
        print(*a,end=" ")
        print(*b)
