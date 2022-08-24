from itertools import count


def factors(n):
    factorlist = []
    for i in range(1,n+1):
        if(n%i == 0):
            factorlist.append(i)
    return(factorlist)

def isPrime(n):
    return( factors(n) == [1,n])

def primeUpto(n):
    primeList = []
    for i in range(1,n+1):
        if isPrime(i):
            primeList.append(i)
    return primeList

def mynprimes(n):
    (i,nprimeList) = (1,[])
    while len(nprimeList) < n:
        if isPrime(i):
            nprimeList.append(i)
        i = i+1
    return(nprimeList)

def nprimes(n):
    (count,i,plist) = (0,1,[])
    while(count<n):
        if isPrime(i):
            (count,plist) = (count+1,plist+[i])
        i=i+1
    return(plist)
