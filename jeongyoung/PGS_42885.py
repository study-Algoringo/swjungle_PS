# 가장 큰 사람이랑 작은 사람 동시에
def solution(people, limit):
    answer = 0
    people.sort()
    s = 0
    b = len(people) - 1
    while s <= b:
        answer += 1
        if people[s] + people[b] <= limit:
            s += 1
        b -= 1
    return answer
