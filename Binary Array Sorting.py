def binSort(arr, n):
    c0=arr.count(0)
    if c0==0 or c0==n:
        pass
    else:
        for i in range(0,c0):
            arr[i]=0;
        for i in range(c0,n):
            arr[i]=1;

import math
def main():
        T=int(input())
        while(T>0):
            N=int(input())
            A=list(map(int,input().split()))
            binSort(A,N)
            for i in A:
                print(i,end=" ")
            print()
            T-=1
if __name__ == "__main__":
    main()
