def rearrange(arr, n):  #max, min, second max,sexond min... array is sorted already
    j=0
    while(j<n):
        temp=arr.pop(n-1)
        arr.insert(j,temp)
        #print(j)
        #print(arr)
        j=j+2
    #print(arr)
    return arr

import math
def main():
    T=int(input())
    while(T>0):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        rearrange(arr,n)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1
if __name__ == "__main__":
    main()
