def rotateArr(A,D,N):
    B=A[0:D]
    del A[:D]
    A.extend(B)
    return A
#execution 1.49
import math
def main():
    T=int(input())
    while(T>0):
        nd=[int(x) for x in input().strip().split()]
        N=nd[0]
        D=nd[1]
        A=[int(x) for x in input().strip().split()]
        rotateArr(A,D,N)
        for i in A:
            print(i,end=" ")
        print()
        T-=1
if __name__=="__main__":
    main()
