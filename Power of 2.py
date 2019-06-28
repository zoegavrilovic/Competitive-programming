def isPowerofTwo(n):
    if n==0 or n&(n-1):  #when a power of 2 number is &ed with number-1, only the ones after the number position remain so the & is 0
        return 0
    else:
        return 1

import math
def main():
    T=int(input())
    while(T>0):
        n=int(input())
        if isPowerofTwo(n):
            print("YES")
        else:
            print("NO")
        T-=1
if __name__=="__main__":
    main()
