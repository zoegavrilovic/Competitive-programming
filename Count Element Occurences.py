from collections import Counter
def countOccurence(arr,n,k):
    c=Counter(arr)
    count=0
    for index,key in enumerate(c):
        if(c[key]>n//k):   #c[key] is the value of key
            count=count+1
    return count

import math
def main():
        T=int(input())
        while(T>0):
            N=int(input())
            A=list(map(int,input().split()))
            K=int(input())
            print(countOccurence(A, N, K))
            T-=1
if __name__ == "__main__":
    main()
