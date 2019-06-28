def countBitsFlip(a,b):
    i=a^b  #calculates xor
    c=0
    while(i):
            i=i&(i-1)  #then counts set bits(how many bits differ in a and b)
            c+=1
    return c

import math
def main()
    T=int(input())
    while(T>0):
        ab=[int(x) for x in input().strip().split()]
        a=ab[0]
        b=ab[1]
        print(countBitsFlip(a,b))
        T-=1
if __name__=="__main__":
    main()

#execution 0.02
