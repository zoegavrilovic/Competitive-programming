def leaders(A,N):
    stack=[]
    curr_max=0
    for i in range(N-1,-1,-1):
        if A[i]>=curr_max:
            curr_max=A[i]
            stack.append(curr_max)
    return stack[::-1]
            

import math
def main():
    T=int(input())
    while(T>0):
        N=int(input())
        A=[int(x) for x in input().strip().split()]
        A=leaders(A,N)
        for i in A:
            print(i,end=" ")
        print()
        T-=1
if __name__=="__main__":
    main()
