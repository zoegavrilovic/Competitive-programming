def checkRotatedAndSorted(arr,n):
    countdown=0
    countup=0
    for i in range(1,n):
        if arr[i]>arr[i-1]:
            countup=countup+1  #for an increasingly sorted and rotated array, all numbers will be larger than the prev one except one
        elif arr[i]<arr[i-1]:
            countdown=countdown+1  #same for decreasingly sorted, all nums will be smaller than prev except one
    #print(countup,countdown)
    if((countup==n-2 and countdown==1 and arr[n-1]<arr[0]) or (countdown==n-2 and countup==1 and arr[n-1]>arr[0])):
        #if array is inc sorted and rotated, the last element will be smaller than the first one
        #else if it dec sorted and rotated, the last element will be bigger than the first one
        return True
    else:
        return False

import math

def main():
        T=int(input())
        while(T>0):
            n=int(input())
            arr=[int(x) for x in input().strip().split()]
            flag=False
            flag=checkRotatedAndSorted(arr, n)
            if flag is False:
                print("No")
            else:
                print("Yes")
            T-=1
if __name__ == "__main__":
    main()
