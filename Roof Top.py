def maxStep(a,n):
    m=0
    c=0
    for i in range(1,n):
        if a[i]>a[i-1]:
            c=c+1
            if c>m:
                m=c
        else:
            c=0
    return m

import math
def main():
        T=int(input())
        while(T>0):
            N=int(input())
            A=[int(x) for x in input().strip().split()]
            print(maxStep(A,N))
            T-=1
if __name__ == "__main__":
    main()
