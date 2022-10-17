from collections import defaultdict

n, e = list(map(int, input().split()))
ver = defaultdict(list)
j, ths = list(map(int, input().split()))
for i in range(e):
    a, b = list(map(int, input().split()))
    ver[a].append(b)
    ver[b].append(a)
ans1 = defaultdict(int)
ans = []
for i in range(1, n+1):
    visited = [0]*(n+1)
    stack = [i]
    cth = 1
    found = False
    visited[i] = 1
    while stack:
        node = stack.pop(0)
        for k in ver[node]:
            if not visited[k]:
                stack.insert(0, k)
                visited[k] = 1
            if k == j and cth <= ths:
                ans.append([node, cth])
                found = True
                break
            elif k == j and cth > ths:
                found = True
                break
            # print(i, node ,k,cth, "ans", ans)
        cth += 1
        # if found: break
ans.sort(key = lambda x: x[1])
for i in ans:
    print(i[0],end=' ')  
