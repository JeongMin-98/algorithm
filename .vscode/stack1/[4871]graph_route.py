""" V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.

두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
 

예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경로를 찾는 경우, 경로가 존재하므로 1을 출력한다.
 


 

노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

 
 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
 

다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000
 

테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.
 

E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

 """

 # 입력 값 test_case , V (node의 개수) E (route의 개수), 출발노드 S, 도착노드 N

def GRAPHROUTE(SP, G):
    
    global NODE

    visited = [False] * len(NODE)
    stack = [] # 연결된 노드 
    v = SP # v가 Start point 시작
    
     
    visited[v] = True
    stack.append(v) # Start point에 v가 방문
    i = 0
    while True: # do while문 python에서 구현
        for i in NODE[v]: # v노드와 연결된 노드를 순서대로 불러오기
            if not visited[i]: # 연결된 첫번째 노드에 방문하지 않았다면
                w = i # W 에 i를 저장
                if w != None: # w에 값이 있기 떄문에 for문에서 break
                    break
        while(w): # w에 값이 있는 동안 반복실행
            visited[w] = True # w에 있는 노드를 방문함, stack에 저장
            stack.append(w)
            v = w # v에 w의 값을 저장, w는 NONE 저장
            w = None
            for i in NODE[v]: # 최근에 방문한 노드에 연결된 다음 노드에 방문하지 않았다면, 
                if not visited[i]: 
                    w = i # w 에 그 다음 노드를 저장
                    if w != None:
                        break 
        if len(stack)==0 or visited[G]: # stack에 없거나 목표지점에 방문했다면 종료
            break
        else:
            v = stack[-1] # stack에 있다면 반목문을 지속적으로 실행
            stack.pop(-1)

    if visited[G]: # 목표지점에 방문했다면 1을 반환 
        return 1
    else:          # 목표지점에 방문하지 못했다면 0을 반환
        return 0

        


T = int(input())

for test_case in range(1,T+1): 
    V, E = map(int, input().split()) # V: node의 개수 , E: route의 개수
    NODE = [0]
    for i in range(1, V+1):
        NODE.append([])
    for j in range(E):
        S, N = map(int, input().split()) # 출발노드와 연결된 노드의 루트 입력
        NODE[S].append(N)
    SP, G = map(int, input().split()) # 출발노드(SF)와 도착노드(G)연결되어있는지?
    print("#{0} {1}".format(test_case, GRAPHROUTE(SP, G)))