def solution(brown, yellow):
    answer = []
    # brown 높이 3부터 시작 높이가 1 늘어날때마다 2의 제곱만큼 세로 길이 증가
    # brown은 항상 짝수
    # yellow는 brown에 둘러싸여있음 > brown의 모서리 4개를 제외하고 b의 개수의 제곱 = y의 개수
    # 카펫이 (3,3) (4,4)일경우 예외
    # 모서리를 뺀 브라운의 개수 /2 
    a = int((brown - 4) /2)
    for i in range(1, int((a+1)/2+1)):
        if i*(a-i) == yellow:

    return answer
