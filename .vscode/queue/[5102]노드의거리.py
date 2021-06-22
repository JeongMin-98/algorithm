T = int(input())

def GraphLength(SP, G):
    global node

    visited = [False] * len(node)
    stack = []
    v = SP

    visited[v] = True
    stack.append(v)
    i = 0

    while True:
        for i in node[v]:
            if not visited[i]:
                w = i
                if w != None:
                    break
        while(w):
            visited[w] = True
            stack.append(w)
            v=w
            w = None
            for i in node[v]:
                if not visited[i]:
                    w = i
                    if w != None:
                        break
            
        if len(stack)==0 or visited[G]:
            break
        else:
            v = stack[-1]
            stack.pop(-1)
    
    if visited[G]:
        return len(stack)-1
    else:
        return 0

for test_case in range(1,T+1):
    V, E = map(int, input().split()) # V : 노드 수, E : 간선 수

    node = [0]

    for i in range(1,V+1):
        node.append([])
    for j in range(E):
        S, N = map(int, input().split())
        node[S].append(N)
        node[N].append(S)
    
    SP, G = map(int, input().split())

    print("#{0} {1}".format(test_case, GraphLength(SP, G)))
    