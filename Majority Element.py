def majorityElement(A,N):
    A.sort()
    c=0
    for i in range(1,N):
        if(A[i]==A[i-1]):
            c=c+1
            if c==N//2:  #if element occures N/2 times, it's the majority element. Here the arr is sorted so occurrences are continuous
                return A[i]
        else:
            c=0  #if the chain breaks and the former element wasn't found N/2 times, reset counter
    return -1  

import math
from sys import stdin
def main():
        T=int(input())
        while(T>0):
            N=int(input())
            A=[int(x) for x in input().strip().split()]
            print(majorityElement(A,N))
            T-=1
if __name__ == "__main__":
    main()
