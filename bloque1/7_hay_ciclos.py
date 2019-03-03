from collections import defaultdict

def dfs(x, col, adj, parent=None):
    if col[x] == 1: return True
    if col[x] == 2: return False
    col[x] = 1
    res = False
    for y in adj[x]:
        if y == parent: continue
        if dfs(y, col, adj, x): res = True
    col[x] = 2
    return res

def hay_ciclo(g):
    adj = defaultdict(set)
    col = defaultdict(int)
    for x, y in g:
        adj[x].add(y)
        adj[y].add(x)
    
    for x in adj:
        if dfs(x, col, adj):  
            return True      
    return False        

print hay_ciclo([(1,2),(3,4),(2,3),(3,4)])    