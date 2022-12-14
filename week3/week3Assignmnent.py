def contracting(l):
    for z in range(0, len(l)-3):
        A = abs(l[z+2]-l[z+1])
        B = abs(l[z+1]-l[z])
        if A < B:
            continue
        else:
            return (False)
    return (True)


def counthv(l):
    hill_count, valley_count = 0, 0
    if len(l) > 2:
        for i in range(1, len(l)-1):
            if l[i] > l[i-1] and l[i] > l[i+1]:
                hill_count += 1
            elif l[i] < l[i-1] and l[i] < l[i+1]:
                valley_count += 1
    return ([hill_count, valley_count])


def leftrotate(m):
    ans = list()
    for a in range(len(m)):
        ans.append([])
        for b in range(len(m)):
            ans[a].append(m[b][len(m)-a-1])
    return(ans)


def remdup(l):
    L = []
    for i in l:
        if i not in L:
            L.append(i)
    return(L)


def sumsquare(l):
    odd_sum = 0
    even_sum = 0
    for a in l:
        if a % 2 != 0:
            odd_sum += a*a
        else:
            even_sum += a*a
    return([odd_sum, even_sum])


def transpose(m):
    ans = list()
    for i in range(len(m[0])):
        a = []
        for j in range(len(m)):
            a.append(m[j][i])
        ans.append(a)
    return(ans)


wickets = {"Tests": {"Bumrah": [3, 5, 2, 3],
                     "Shami": [4, 4, 1, 0],
                     "Ashwin": [2, 1, 7, 4]},
            "ODI": {"Bumrah": [2, 0],
                    "Shami": [1, 2]}
          }
