from collections import defaultdict
import sys

n, e = list(map(int, input().split()))
ver = defaultdict(list)
for i in range(e):
        a, b = list(map(int, input().split()))
        ver[a].append(b)
a,b,c = list(map(int, input().split()))
if b in ver[a]:
        print("YES")
        sys.exit(0)
stack = [a]
visited = [0]*n
while stack:
        node = stack.pop(0)
        if node == c: continue
        visited[node] = 1
        for i in ver[node]:
            stack.insert(0, i)
            if i == b:
                print("YES")
                sys.exit(0)
print("NO")

