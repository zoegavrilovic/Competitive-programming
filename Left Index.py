#for some reason not working for some tc, done it correctly in c++
def leftIndex(N,A,x):
    if A[0]==x:
        return 0
    if A[N-1]==x:
        return N-1
    l=1
    r=N-1
    while l<=r:
        mid=l+(r-l)//2
        if A[mid]==x and A[mid-1]!=x:
            return mid
        elif A[mid]>x:
            r=mid-1
        else:
            l=mid+1
