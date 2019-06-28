def toString(List):
    return ''.join(List)

def permute(a,l,r,answer):
    if l==r:
        answer.append(toString(a))
    else:
        for i in range(l,r+1):
            a[l],a[i]=a[i],a[l]
            permute(a,l+1,r,answer)
            a[l],a[i]=a[i],a[l]

def possibleWords(a,N):
    li=[]
    for i in a:
        if i==2:
            li.extend(['a','b','c'])
        elif(i==3):
            li.extend(['d','e','f'])
        elif(i==4):
            li.extend(['g','h','i'])
        elif(i==5):
            li.extend(['j','k','l'])
        elif(i==6):
            li.extend(['m','n','o'])
        elif(i==7):
            li.extend(['p','q','r','s'])
        elif(i==8):
            li.extend(['t','u','v'])
        elif(i==9):
            li.extend(['w','x','y','z'])
    answer=[]
    n=len(li)
    permute(li,0,n-1,answer)
    answer.sort()
    for i in answer:
        print(i,end=" ")
