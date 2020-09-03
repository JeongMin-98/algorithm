T = int(input())
for x in range(1,T+1):
    
    # k는 한번에 갈 수 있는 정류장의 개수
    # N은 총 정류장의 개수
    # M은 충전기가 설치된 정류장의 개수

    k,n,m = map(int, input().split())
    line = [0]*(n+1)
    s = map(int, input().split()) # 충전기가 설치되어있는 정류장 번호
    station = list(s)
    count = 0 # 충전횟수
    for y in range(0, len(station)):
        line[station[y]] +=1
    bus = 0
    fuel = k
    while bus<len(line):
        if fuel>1:
            bus+=1
            fuel-=1
        elif fuel=1:
            if line[bus+1]==0:
                if line[bus]==1:
                    fuel+=k
                    count+=1
                else:
                    bus
            else:
                bus+=1
                fuel-=1
        else:
            if line[bus]==1:
                fuel+=k
                count+=1
            else:
                bus-=1
                fuel+=1     
    
    print("#{} {}".format(x, count))

     
    
