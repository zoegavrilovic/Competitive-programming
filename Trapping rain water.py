def trappingWater(arr,n):
    leftmaxes=[0]*n
    rightmaxes=[0]*n
    leftmaxes[0]=arr[0]
    rightmaxes[n-1]=arr[n-1]
    water=0
    for i in range(1,n):
        leftmaxes[i]=max(leftmaxes[i-1], arr[i])  #looking for max on the left of every element
    for i in range(n-2,-1,-1):
        rightmaxes[i]=max(rightmaxes[i+1],arr[i])  #max on the right of every element
    for i in range(0,n):
        water=water+min(leftmaxes[i],rightmaxes[i])-arr[i]  #just draw a picture and you'll understand why
    return water

import math
def main():
        T=int(input())
        while(T>0):
            n=int(input())
            arr=[int(x) for x in input().strip().split()]
            print(trappingWater(arr,n))
            T-=1
if __name__ == "__main__":
    main()
