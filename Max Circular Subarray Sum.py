def circularSubarraySum(arr,n):
    maxs = 0
    maxe = arr[n-1]
    if all(i<0 for i in arr):
        return max(arr)  #if all elements in a are negative, max sum is the largest number

    for i in range(0,n-1):
        maxe = maxe + arr[i]
        if maxe < 0:
            maxe = 0   #resetting to 0
        if(maxs < maxe):
            maxs = maxe
    return maxs

import math
def main():
        T=int(input())
        while(T>0):
            n=int(input())
            arr=[int(x) for x in input().strip().split()]
            print(circularSubarraySum(arr,n))
            T-=1
if __name__ == "__main__":
    main()
