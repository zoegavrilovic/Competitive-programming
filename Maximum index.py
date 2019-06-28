def maxIndexDiff(arr, n):  #max difference j-i for A[i]<=A[j]
    maxdiff=0
    if n==2:
        return 1
    for i in range(0,int(n/2)+1):
        for j in range(n-1,int(n/2),-1):
            if arr[i]<=arr[j]:
                if j-i>maxdiff:
                    maxdiff=j-i
                    #print(i,j,maxdiff)
    return maxdiff

import math
def main():
        T=int(input())
        while(T>0):
            n=int(input())
            arr=[int(x) for x in input().strip().split()]
            print(maxIndexDiff(arr,n))
            T-=1
if __name__ == "__main__":
    main()
