def josephus(n,k):
    if(n==1):
        return 1
    return (josephus(n-1,k)+k-1)%n+1  #k-1 means changing the position by k-1, -1 because we include the person holding the sword
    #%n is done if the value exceedes n so it comes back and +1 is the next person killed
#After the first person (kth from begining) is killed, n-1 persons are left.
#So we call josephus(n – 1, k) to get the position with n-1 persons. But the position returned by
#josephus(n – 1, k) will consider the position starting from k%n + 1.
#So, we must make adjustments to the position returned by josephus(n – 1, k).

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        n=nk[0]
        k=nk[1]
        print(josephus(n,k))
        T-=1
if __name__=="__main__":
    main()
