def reverseInGroups(A,N,K):
    B=A[0:K]
    B=B[::-1]
    j=K
    for i in range(K,len(A)):
        C=A[K:K+j]
        C=C[::-1]
        B.extend((C))
        C=[]
        K=K+j
    return B
#execution 1.62

#Using sliding window:
#You can take a window of size K. Now, this problem is reduced to reversing an array.
#After reversing the first group, go for next group if there are atleast k elements.
#In this way, reverse all the groups of size K.

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        A=[int(x) for x in input().strip().split()]
        A=reverseInGroups(A,N,K)
        for i in A:
            print(i,end=" ")
        print()
        T-=1
if __name__=="__main__":
    main()
