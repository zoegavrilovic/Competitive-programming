def xor(a,b):
    if(a==b):
        return '0'
    else:
        return '1'
def greyConverter(n):
    n=bin(n)[2:]  #because the string starts with 0b
    gray=n[0]  #because the first bit is the same for binary and gray
    for i in range(1,len(n)):
        gray+=xor(n[i],n[i-1])
    return int(gray,2)  #to decimal number

import math
def main():
    T=int(input())
    while(T>0):
        n=int(input())
        print(greyConverter(n))
        T-=1
if __name__=="__main__":
    main()
