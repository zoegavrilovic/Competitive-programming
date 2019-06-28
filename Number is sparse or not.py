def isSparse(n):
    while(n):
        if(n&(n>>1)):  #if MS set B & the next one are set, the number is not sparse
            return 0
        else:
            n=n>>1 
    return 1

import math
def main()
    T=int(input())
    while(T>0):
        n=int(input())
        if isSparse(n):
            print("1")
        else:
            print("0")
        T-=1
if __name__=="__main__":
    main()

#execution: 0.02
