from itertools import permutations  
def solution(k, dungeons):
    answer =0 
    num = len(dungeons)
    dungeons_orders = list(permutations(dungeons, num))
    for dun_order in  dungeons_orders:
        ans = 0
        piro = k
        for i in range(num):
            if piro < dun_order[i][0]:
                break
            else:
                piro -= dun_order[i][1]
                ans += 1    
        answer = max(ans, answer)
    
    return answer