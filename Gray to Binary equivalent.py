def invert(i):
    if i=='0':
        return '1'
    else:
        return '0'
def grayToBinary(n):
    n=bin(n)[2:]
    binary=n[0]
    for i in range(1,len(n)):
        if n[i]=='0':
            binary+=binary[i-1]
        else:
            binary+=invert(binary[i-1])
    return int(binary,2)

import math
def main():
    T=int(input())
    while(T>0):
        n=int(input())
        print(grayToBinary(n))
        T-=1
if __name__=="__main__":
    main()
