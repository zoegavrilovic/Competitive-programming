def search(A,N,x):
    for i in range(0,N):
        if A[i]==x:
            return i
    return -1

import math
def main():
        T=int(input())
        while(T>0):
            N=int(input())
            A=[int(x) for x in input().strip().split()]
            x=int(input())
            print(search(A,N,x))
            T-=1
if __name__ == "__main__":
    main()
