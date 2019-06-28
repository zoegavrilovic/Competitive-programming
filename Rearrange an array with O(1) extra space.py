def arrange(arr, n):
    for i in range(0,n):
        arr[i]=(arr[arr[i]]%n)*n+arr[i]  #Dividend=Quotient*Divisor+Remainder, %n is needed because with every iteration
        #it takes arr[arr[i]] which might already be multiplied and stuff xD fml I would never think of this
    for i in range(0,n):
        arr[i]=arr[i]//n  #to get it to arr[arr[i]] state of original array

import math
def main():
        T=int(input())
        while(T>0):
            n=int(input())
            arr=[int(x) for x in input().strip().split()]
            arrange(arr,n)
            for i in arr:
                print(i,end=" ")
            print()
            T-=1
if __name__ == "__main__":
    main()
