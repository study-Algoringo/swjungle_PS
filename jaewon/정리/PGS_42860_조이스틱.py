def solution(name):
	# 조이스틱 조작 횟수 
    answer = 0
    # 기본 최소 좌우이동 횟수는 길이 - 1 => 이 말은 즉, 왼쪽에서 오른쪽으로 순서대로 커서를 이동하는 경우이다.
    # min_move를 선언해주는 이유는 알파벳변경 최솟값은 아래 코드에서 구해지므로 결국 커서의 최소 이동횟수를 
    # 알파벳 변경 최솟값에 더하면 해당 알파벳을 변경하기 위한 총 이동횟수가 나오게 된다. 그중 최솟값을 구해야 하므로
    # min()함수를 사용하여 카운트를 해준다.
    min_move = len(name) - 1
    print(min_move)
    for i, char in enumerate(name):
    	# 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        # 결국 next는 연속된 A의 끝부분 인덱스를 나타낸다.
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        # 기존
        # >>>>>>>>
        # JEEAAAZE
        # 왼쪽 시작방식 : i가 커서위치 이므로 해당 인덱스 * 2 + len(name) - next로 이동횟수 산출
        # >>>
        # <<<   <<   
        # JEEAAAZE
        # 오른쪽 시작방식 : 해당 인덱스 + 2 * (len(name) -next)로 이동횟수 산출
        #       <<
        # >>>   >>   
        # JEEAAAZE
        # 위 3가지 방식을 비교하여 최솟값으로 갱신을 해준다.
        print(f"기존 : {min_move}, 왼쪽 : {(2 * i) + (len(name) - next)}, 오른쪽 : {i + (2 * (len(name) -next))}")
        min_move = min([min_move, (2 * i) + (len(name) - next), i + (2 * (len(name) -next))])
    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer

solution("JEEAAAZE")
# solution("JAAASDAAE")


# 참고사이트
# https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy#%EC%B6%94%EA%B0%80-%EC%84%A4%EB%AA%85