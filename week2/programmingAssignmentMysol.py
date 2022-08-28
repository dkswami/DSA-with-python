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

print(matched(')sdw%('))
