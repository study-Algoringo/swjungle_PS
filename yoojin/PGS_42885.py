def solution(people, limit):
    answer = len(people)
    # 합이 최대한 limit에 가깝게 만들기
    people.sort()
    # 양 쪽 끝에서 i, j 출발
    i = 0; j = len(people) - 1
    # i < j일 때, 반복
    while i < j:        
    # i + j <= limit이면 answer -= 1
        if people[i] + people[j] <= limit:
            answer -= 1
            i += 1; j-= 1
        # 작으면 i 1 증가, 크면 j 1 감소
        else:
            if people[i] + people[j] > limit:
                j -= 1
            else:
                i += 1
    return answer

print(solution([70, 50, 80, 50], 100))