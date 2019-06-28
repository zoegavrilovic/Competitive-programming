def maxSubArraySum(a,size):
    maxs = 0
    maxe = 0
    if all(i<0 for i in a):
        return max(a)  #if all elements in a are negative, max sum is the largest number

    for i in range(0,size):
        maxe = maxe + a[i]
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
            print(maxSubArraySum(arr,n))
            T-=1
if __name__ == "__main__":
    main()
