def solution(s):
    answer = []
    s = s[2:-2]
    slist = s.split('},{')
    slist.sort(key = len)
    for s_num in slist:
        s_num = s_num.split(",")
        for num in s_num:
            if int(num) not in answer:
                answer.append(int(num))
    return answer

print(solution('{{1,2,3},{2,1},{1,2,4,3},{2}}'))