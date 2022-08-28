def mystringreverse(m):
    reversedstring = ""
    for i in range(len(m),1):
        reversedstring = reversedstring[:] + m[i] 
    return(reversedstring)

def intreverse(n):
  ans = 0
  while n > 0:
    (d,n) = (n%10,n//10)
    ans = 10*ans + d
  return(ans)

def matched(s):
    nested = 0
    for i in range(0, len(s)):
        if s[i] == '(':
            nested += 1
        elif s[i] == ')':
            nested -= 1
            if nested < 0:
                return(False)
    return(nested == 0)

#print(matched(')sdw%('))

def factors(n):
    flist = []
    for i in range(1, n+1):
        if n%i==0:
            flist.append(i)
    return(flist)
#print(factors(56))

def isPrime(n):
    return(factors(n) == [1,n])
#print(isPrime(13))
#print(isPrime(24))

def sumprimes(l):
    sum=0
    for i in l:
        if isPrime(i):
            sum += i
    return(sum)

print(sumprimes([3,3,1,13]))
print(sumprimes([2,4,6,9,11]))
print(sumprimes([-3,1,6]))