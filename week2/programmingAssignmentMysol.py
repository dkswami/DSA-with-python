def mystringreverse(m):
    reversedstring = ""
    for i in range(len(m),1):
        reversedstring = reversedstring[:] + m[i] 
    return(reversedstring)

