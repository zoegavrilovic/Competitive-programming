#Initialize an array arr[] to 0.
#For each range i, add +1 at Li index and -1 at index 1 + Ri (1 BASED INDEXING)
#of the array.
#Find the prefix sum of the array and find the smallest index
#having maximum prefix sum.
#STILL DON'T KNOW HOW THIS WORKS
def maxOccured(L,R,N,maxx):
    maxL=max(L)
    maximum=max(maxL,maxx)
    global A
    A=A[:maximum+1]  #array containing all ranges in L and R, thus max range+1
    for j in range(0,N):
        A[L[j]-1]=A[L[j]-1]+1
    for j in range(0,N):
        A[R[j]]=A[R[j]]-1
    for i in range(1,maximum):
        A[i]=A[i]+A[i-1]   #prefix sum
    maxA=max(A)
    return A.index(maxA)+1   #one based indexing min index of max element

import math
A=[0]*1000000
def main():
    T=int(input())
    while(T>0):
        global A
        A=[0]*1000000
        N=int(input())
        L=[int(x) for x in input().strip().split()]
        R=[int(x) for x in input().strip().split()]
        maxx=max(R)
        print(maxOccured(L,R,N,maxx))
        T-=1
if __name__=="__main__":
    main()
