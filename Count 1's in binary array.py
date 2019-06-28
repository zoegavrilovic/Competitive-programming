def countOnes(A,N):  #the binary (0s and 1s) array is decreasing
    l=0
    r=N-1
    while l<=r:
        mid=l+(r-l)//2
        if A[mid]==1 and (mid==N-1 or A[mid+1]!=1):  #finding the last occurrence of 1 (mid==N-1 so the index wouldn't get out of range)
            return mid+1  #index of last occurrence+1 will be number of occurrences
        elif A[mid]<1:
            r=mid-1
        else:
            l=mid+1

import math
def main():
        T=int(input())
        while(T>0):
            N=int(input())
            A=[int(x) for x in input().strip().split()]
            print(countOnes(A,N))
            T-=1
if __name__ == "__main__":
    main()
