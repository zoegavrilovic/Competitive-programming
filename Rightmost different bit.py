def posOfRightMostDiffBit(m,n):
    if m==n:
        return -1
    for k in range(0,31):
        if((m ^ n)&(1<<k)):  #if the bits at k position are different
            return math.log2((m ^ n)&(1<<k))+1  #return THE POSITION, not the value, of those bits

def main():
    T=int(input())
    while(T):
        mn=[int x for x in input().strip().split()]
        m=mn[0]
        n=mn[1]
        print(math.floor(posOfRightMostDiffBit(m,n)))
        T-=1

if __name__=="__main__":
    main()

#execution 0.01
