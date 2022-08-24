def h(x):
    (d,n) = (1,0)
    while d <= x:
        (d,n) = (d*3,n+1)
    return(n)

def g(n): 
    s=0
    for i in range(2,n):
        if n%i == 0:
           s = s+1
    return(s)

def f(n): 
    s=0
    for i in range(1,n+1):
        if n//i == i and n%i == 0:
           s = 1
    return(s%2 == 1)

def foo(m):
    if m == 0:
      return(0)
    else:
      return(m+foo(m-1))
