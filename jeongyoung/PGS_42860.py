# A를 만나면, A에서 올라가는게 이득인지 거꾸로 가는게 이득인지 계산해야함
# 커서를 움직이는 횟수 + 알파벳 올리는 수(아스키코드활용)
def solution(name):
    answer = 0
    min_move = len(name) - 1 # 정방향으로 움직였을때 커서가 움직이는 최소 횟수
    # 알파벳 계산 = min('A'에서 올리는 횟수, 'Z'에서 올리는 횟수 + 1)
    for i, a in enumerate(name):
        answer += min(ord(a) - ord('A'), ord('Z') - ord(a) + 1)
    # 커서 움직이는 횟수 계산
        # 다음에 연속된 A가 얼마나 나오는지 구하는 while문
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        # 정방향으로 움직인 횟수, 왼>오에서 움직여서 a를 만나고 거꾸로 간 횟수, 바로 거꾸로 가서 다시 돌아온 횟수
        min_move = min([min_move, i * 2 + len(name) - next, i + 2 * (len(name) - next)])
    answer += min_move        
    return answer
