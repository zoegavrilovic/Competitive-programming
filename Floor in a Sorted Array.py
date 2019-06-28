#Given a sorted array arr[] of size N without duplicates, and given a value x. Find the floor of x in given array.
#Floor of x is defined as the largest element K in arr[] such that K is smaller than or equal to x

#How did this work for K smaller than x (if x is not present?) :/
def binary(l,r,A,K):
    while l<=r:
        mid=l+(r-l)//2
        #print(mid,end=" ")
        if A[mid]==K:
            return mid
        if A[mid]<K:
            l=mid+1
        if A[mid]>K:
            r=mid-1
    return -1
def findFloor(A,N,X):
    if X>A[N-1]:
        return N-1
    if X<A[0]:
        return -1
    return binary(0,N-1,A,X)

import math
def main():
        T=int(input())
        while(T>0):
            NX=[int(x) for x in input().strip().split()]
            N=NX[0]
            X=NX[1]
            A=[int(x) for x in input().strip().split()]
            print(findFloor(A,N,X))
            T-=1
if __name__ == "__main__":
    main()
