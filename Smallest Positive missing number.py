def findMissingInteger(arr,n):
    arr.sort()
    #print(arr)
    if arr[0]>1:
        return 1
    for i in range(1,n):
        if arr[i]>1 and arr[i-1]<=0:
            return 1
        elif arr[i]-arr[i-1]>1 and arr[i]>0 and arr[i-1]>0:
            return arr[i-1]+1

import math
def main():
        T=int(input())
        while(T>0):
            n=int(input())
            arr=[int(x) for x in input().strip().split()]
            print(findMissingInteger(arr,n))
            T-=1
if __name__ == "__main__":
    main()
