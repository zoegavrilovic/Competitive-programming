def binary(l,r,A,K):
    if l>r:
        return -1
    mid=l+(r-l)//2
    if A[mid]==K:
        return 1
    if A[mid]<K:
        return binary(mid+1,r,A,K)
    if A[mid]>K:
        return binary(l,mid-1,A,K)
def searchInSorted(A,N,K):
    return binary(0,N-1,A,K)

import math
def main():
        T=int(input())
        while(T>0):
            NK=(input().strip().split())
            N=int(NK[0])
            K=int(NK[1])
            A=[int(x) for x in input().strip().split()]
            print(searchInSorted(A,N,K))
            T-=1
if __name__ == "__main__":
    main()
