def my_input():
    n, m = map(int, input().split())
    g = [list() for _ in range(n)]
    h = [list() for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1].append(b-1)
        h[b-1].append(a-1)
    return n, m, g, h

def dfs1():
    global tout, used, stack, stack_parents
    while stack != []:
        v = stack[-1]
        if v == stack_parents[-1]:
            del stack_parents[-1]
            del stack[-1]
            tout.append(v)
        elif not used[v]:
            stack_parents.append(v)
            used[v] = True
            for u in g[v]:
                if not used[u]:
                    stack.append(u)
        else:
            del stack[-1]

def dfs2():
    global component, col, es, stack_parents
    while stack != []:
        v = stack.pop()
        component[v] = col
        for u in h[v]:
            if component[u] == 0:
                stack.append(u)
            elif component[u] != col:
                es.append((col, component[u]))
    
def main():
    global col, component, stack, stack_parents, g, h, es, tout, used
    n, m, g, h = my_input()
    used = [0]*n
    tout = []
    component = [0]*n
    col = 1
    es = []
    i = 0
    stack = []
    stack_parents = []
    for v in range(n):
        if not used[v]:
            stack = [v]
            stack_parents = [-1]
            dfs1()
    for v in tout[::-1]:
        if component[v] == 0:
            stack = [v]
            dfs2()
            col += 1
    return len(set(es))
if __name__ == '__main__':
    print(main())
