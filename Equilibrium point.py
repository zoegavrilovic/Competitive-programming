#1) Initialize leftsum  as 0
#2) Get the total sum of the array as sum
#3) Iterate through the array and for each index i, do following.
#    a)  Update sum to get the right sum.
#           sum = sum - arr[i]
#       // sum is now right sum
#    b) If leftsum is equal to sum, then return current index.
#    c) leftsum = leftsum + arr[i] // update leftsum for next iteration.
#4) return -1 // If we come out of loop without returning then
#             // there is no equilibrium index
def equilibriumPoint(A,N):
    s=sum(A)
    leftsum=0
    for i in range(0,N):
        s=s-A[i]
        if(leftsum==s):
            return i+1
        leftsum=leftsum+A[i]
    return -1

import math
def main():
    T=int(input())
    while(T>0):
        N=int(input())
        A=[int(x) for x in input().strip().split()]
        print(equilibriumPoint(A,N))
        T-=1
if __name__=="__main__":
    main()
