def my_input():
    n, m = map(int, input().split())
    g = [list() for _ in range(n)]
    h = [list() for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1].append(b-1)
        h[b-1].append(a-1)
    return n, m, g, h

def dfs1(v):
    global tout, used
    used[v] = True
    for u in g[v]:
        if not used[u]:
            dfs1(u)
    tout.append(v)

def dfs2(v):
    global component, col, es
    component[v] = col
    for u in h[v]:
        if component[u] == 0:
            dfs2(u)
        elif component[u] != col:
            es.append((col, component[u]))
    
def main():
    global used, tout, component, col, es, g, h
    n, m, g, h = my_input()
    used = [0]*n
    tout = []
    component = [0]*n
    col = 1
    es = []
    for v in range(n):
        if not used[v]:
            dfs1(v)
    for v in tout[::-1]:
        if component[v] == 0:
            dfs2(v)
            col += 1
    return len(set(es))
if __name__ == '__main__':
    print(main())
