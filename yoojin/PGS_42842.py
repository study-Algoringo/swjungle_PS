def solution(brown, yellow):
    # b + y의 값이 전체 넓이, 단 가로 >= 세로
    # ret[a, b]일 때 (a-2)(b-2)의 값이 yellow 값과 같음
    height = 0
    
    for i in range(brown, 1, -1):
    #가로를 둘 중 최대 값으로 두고, 반복문을 통해 조건과 일치하는 답이 있다면 리턴한다
        width = i
        height = (brown + yellow) // width
        if yellow == (width - 2) * (height -2):
            break
    
    answer = [width, height]
    return answer