def solution(s):
    answer = []
    ans = []
    # 집합을 만들어서 집합에 원소 다 때려넣어
    s = s.split('},')

    for i in s:
        answer.append(str(i).strip("{""}"))
        
    answer.sort(key=len)
    for a in answer:
        for b in list(a.split(',')):
            if int(b) in ans:
                continue
            else:
                ans.append(int(b))
                
    return ans