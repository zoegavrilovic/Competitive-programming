#The minimum element is the only element whose previous is greater than it. If there is no previous element element,
#then there is no rotation (first element is minimum). We check this condition for middle element by comparing it with
#(mid-1)’th and (mid+1)’th elements.
#If minimum element is not at middle (neither mid nor mid + 1), then minimum element lies in either left half or right half.
#If middle element is smaller than last element, then the minimum element lies in left half
#Else minimum element lies in right half.
import sys
def minNumber(arr,low,high):
    if low<=high and len(arr)>3:
        mid=low+(high-low)//2
        #print(mid,end=" ")
        if arr[mid+1]<arr[mid]:
            return arr[mid+1]
        if arr[mid]<arr[mid-1] and arr[mid]<arr[mid+1]:
            return arr[mid]
        if arr[mid]>arr[0]:
            return minNumber(arr,mid+1,high)

        if arr[mid]<arr[len(arr)-1]:
            return minNumber(arr,low,mid-1)
    m=sys.maxsize
    for i in range(0,len(arr)):  #in case there are only 3 elements, this binary search won't work so I handled it separately
        if arr[i]<m:
            m=arr[i]
    return m
import math
def main():
        T=int(input())
        while(T>0):
            N=int(input())
            A=[int(x) for x in input().strip().split()]
            print(minNumber(A,0,N-1))
            T-=1
if __name__ == "__main__":
    main()
