def countSetBits(n):
    c=0
    for i in range(1,n+1):
        while(i):
            i=i&(i-1)  #Kerninghan algorithm
            c+=1
    return c

import math
def main():
    T=int(input())
    while(T>0):
        n=int(input())
        print(countSetBits(n))
        T-=1
if __name__=="__main__":
    main()

#execution 0.04
