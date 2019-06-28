def prime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while(i<=int(math.sqrt(n))):
        if n%i==0 or n%(i+2)==0:
            return False
        i=i+6
    return True
    
def exactly3Divisors(N):
    c=0
    for i in range(N):
        if(math.sqrt(N)>=i and prime(i)):
            c=c+1
    return c

#The logic behind this is, such numbers can have only three numbers as their divisor and also that include
#1 and that number itself resulting into just a single divisor other than number, so we can easily conclude that
#required are those numbers which are squares of prime numbers so that they can have only three divisors
#(1, number itself and sqrt(number)). So all primes i, such that i*i is less than equal to N are three-prime numbers.
#Note: We can generate all primes within a set using any sieve method efficiently and then we should all primes i,
#such that i*i <=N.
