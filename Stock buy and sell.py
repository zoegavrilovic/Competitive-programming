def stockBuySell(A,n):
    start=0
    end=0
    pairs=[]
    for i in range(1,n):
        if(A[i]>=A[end]):
            end=i   #moving the sell day by one if the price keeps increasing
        else:
            if A[start]!=A[end]:  #if we're not talking about the same date
                pairs.extend([start,end])  #if the price is lower than yesterday, means it's time to sell and reset the start and end day
            start=i
            end=i
    if(A[start]!=A[end]):
        pairs.extend([start,end])  #adding the final pair in case the last element is bigger than the second from end
        #because in that case the else above wouldn't happen and the last buy-sell range wouldn't be added to pairs
    if len(pairs)==0:
        print("No Profit",end="")
    else:
        for i in range(0,len(pairs)-1,2):  #it's ugly but more efficient than turning the list into list of tuples x)
            print("(",end="")
            print(pairs[i],end=" ")
            print(pairs[i+1],end="")
            print(")",end=" ")

import math
def main():
        T=int(input())
        while(T>0):
            n=int(input())
            arr=[int(x) for x in input().strip().split()]
            stockBuySell(arr,n)
            print()
            T-=1
if __name__ == "__main__":
    main()
