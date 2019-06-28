def convertToWave(A,N):
    for i in range(0,N-1,2):
        if A[i]<A[i+1]:  #didn't need this because the array is sorted
            A[i],A[i+1]=A[i+1],A[i]
    return A

import math
def main():
    T=int(input())
    while(T>0):
        N=int(input())
        A=[int(x) for x in input().split()]
        convertToWave(A,N)
        for i in A:
            print(i,end=" ")
        print()
        T-=1
if __name__=="__main__":
    main()
