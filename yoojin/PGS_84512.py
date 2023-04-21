from itertools import product

def solution(word):
    answer = 0; dictionary = []
    # 가능한 모든 경우의 수 구하기
    for i in range(1, 6):
        for j in product(['A', 'E', 'I', 'O', 'U'], repeat = i):
            insert_word = ''.join(map(str, j))
            dictionary.append(insert_word)

    dictionary.sort()
    answer = dictionary.index(word)
    # 경우의 수 배열에서 주어진 word의 index 찾기
    return answer + 1

print(solution("AAAE"))