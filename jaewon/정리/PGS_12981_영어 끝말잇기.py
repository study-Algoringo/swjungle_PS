def solution(n, words):
    answer = [0, 0]

    for i in range(1, len(words)):
        if words[i - 1][-1] != words[i][0]:
            return [i % n + 1, i // n + 1]
        elif words[i] in words[:i]:
            return [i % n + 1, i // n + 1]

    return answer

arr = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
arr1 = ["hello", "tne"]

print(solution(3, arr))
# [3,3] 탈락자 번호, 차례 번호 => 3번사람이 3번쨰에 탈락
