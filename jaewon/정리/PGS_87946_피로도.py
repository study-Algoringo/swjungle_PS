from itertools import permutations

def solution(k, dungeons):
    cnt_arr = []
    tmp = k
    for per in permutations(dungeons, len(dungeons)):
        tmp_d = list(per)
        cnt = 0
        while tmp_d:
            x, y = tmp_d.pop(0)
            if x > tmp:
                continue
            else:
                tmp -= y
                cnt += 1
        cnt_arr.append(cnt)
        tmp = k

    answer = max(cnt_arr)
    return answer

solution(80, [[80,20],[50,40],[30,10]])
