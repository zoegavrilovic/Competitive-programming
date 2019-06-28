def maxAND(arr,n):
    m=0
    for i in range(0,n):
        for j in range(i+1,n):  #can't start at i because i&i is probably the max and xD
            if arr[i]&arr[j]>m:
                m=arr[i]&arr[j]
    return m

import math
def main():
    T=int(input())
    while(T>0):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        print(maxAND(arr,n))
        T-=1
if __name__=="__main__":
    main()
