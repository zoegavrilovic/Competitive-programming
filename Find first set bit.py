def getFirstSetBit(n):
    if n==0:
        return 0
    c=1
    while n:
        if n&1==1:
            return c
        else:
            c=c+1
            n=n>>1

def main():
    T=int(input())
    while(T):
        n=int(input())
        print(getFirstSetBit(n))
        T-=1

if __name__=="__main__":
    main()

#execution 0.02

#A set bit will give n&(1<<k) as 1, k starts from zero.
#Use right shift operator as ((x>>i)&1).Iterate 'i' until you get value 1. 
