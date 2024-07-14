n = [int(i) for i in input().split()]
m = [i for i in range(1, n[0]+1)]

m = m[:n[1]-1]+list(reversed(m[n[1]-1: n[2]])) + m[n[2]:]
m = m[:n[3]-1]+list(reversed(m[n[3]-1: n[4]])) + m[n[4]:]
print(*m)