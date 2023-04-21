'''
# 오답코드
# 가장 가까운 A를 찾아 좌우를 선택하는 방식으로 연속된 A열이 여러개 있을경우 결과가 틀릴수 있다.
def solution(name):
    answer = 0
    name_lst = [min(ord(i)-ord('A'), ord('Z')-ord(i)+1) for i in name]
    
    idx = 0
    
    while True:
        answer += name_lst[idx]
        name_lst[idx] = 0
        if sum(name_lst) == 0:
            break
        l = 1
        r = 1
        
        while name_lst[idx + r] == 0:
            r += 1
            
        while name_lst[idx -l] == 0:
            l += 1
            
        if l < r:
            answer += l
        else:
            answer += r
        if l < r:
            idx -= l
        else:
            idx += r

    return answer

'''

def solution(name):

	# 조이스틱 조작 횟수 
    answer = 0
    
    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1
    
    for i, char in enumerate(name):
    	# 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
        
    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer