def power(N,R):
    if(R==0):
        return 1
    M=1000000007
    y=power(N,math.floor(R/2))  #just splitting R into 2 parts each time, (divide and conquer) and computing smaller parts,because they are all the same
    if int(R)&1:  #if R is odd
        return((y%M)*(y%M*N)%M)   # *N because it is odd
    else:
        return((y%M)*(y%M)%M)

#Try using modulus property with fast exponentian:

#Property 1:
#(m * n) % p has a very interesting property:
#(m * n) % p =((m % p) * (n % p)) % p

#Property 2:
#if b is even:
#(a ^ b) % c = ((a ^ b/2) * (a ^ b/2))%c ? this suggests divide and conquer
#if b is odd:
#(a ^ b) % c = (a * (a ^( b-1))%c

#Property 3:
#If we have to return the mod of a negative number x whose absolute value is less than y:
#then (x + y) % y will do the trick

#Note:
#Also as the product of (a ^ b/2) * (a ^ b/2) and a * (a ^( b-1) may cause overflow,
#hence we must be careful about those scenarios
import math
def main():
    T=int(input())
    while(T>0):
        N=input()
        R=N[::-1]
        ans=power(int(N),int(R))
        print(ans)
        T-=1
if __name__=="__main__":
    main()
