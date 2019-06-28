#their solution:

#Maintain 2 iterators, i and j for arr1 and arr2. and iterate from 0 to min(size of arr1, size of arr2).
#While iterating,
#if the element of arr1 is less than elemen at arr2, then print this element and increement i,
#else if element at arr2 is less than element at arr 1, print this element and increement j,
#else print any element, and increement both iterators
#Also, to print only distinct elements and avoid printing repeated elements in same array also, see if consecutive
#elements are equal before these cases, for both arrays,  and if yes then increement the iterator respectively.
#After this first loop, print the remaining elements in any of the loop, as above loop iterates to
#min (sizeof arr1, sizeof arr2).

from collections import Counter,OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
def findUnion(a,b,n,m):

    c=OrderedCounter(a+b)
    for i in c.keys():
        print(i,end=" ")
    print()

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,m=map(int,input().strip().split())
        a=list(map(int,input().strip().split()))
        b=list(map(int,input().strip().split()))
        findUnion(a,b,n,m)
