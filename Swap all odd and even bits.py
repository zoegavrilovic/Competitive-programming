def swapBits(n):
    n=bin(n)[2:]
    if len(n)&1==1:  #if number of bits is odd, add a 0 in front 
        n='0'+n
    res="".join([n[x:x+2][::-1] for x in range(0,len(n),2)])  #swapping pairs of bits
    return int(res,2)

import math
def main():
    T=int(input())
    while(T>0):
        n=int(input())
        print(swapBits(n))
        T-=1
if __name__=="__main__":
    main()
