def checkKthBit(n,k):
    k=2**k
    if n&k:  #if the value on n & the value of the bit where k is are 1, then the kth bit in n is set
        return 1
    else:
        return 0

import math
def main():
    T=int(input())
    while(T>0):
        n=int(input())
        k=int(input())
        if checkKthBit(n,k):
            print("Yes")
        else:
            print("No")
        T-=1
if __name__=="__main__":
    main()

#execution 0.01
