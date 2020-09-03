T = int(input()) # test_case
for test_case in range(1,T+1):
    N = int(input()) # 카드 장수 N
    A = input()  # N개의 숫자 ai
    
    card = list(map(int,A)) 
    max_count = 0 # 가장 많은 카드의 장 수
    num = 0 # 가장 많은 카드의 숫자
        
    for i in range(1,10):
        if card.count(i)>=max_count:
            max_count = card.count(i)
            num = i
        else:
            max_count = max_count    

    print("#{0} {1} {2}".format(test_case,num,max_count))       

    