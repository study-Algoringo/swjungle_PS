def solution(s):
    min_deletions = float('inf')
    
    for i in range(len(s) + 1):
        # 처음 i개의 B를 제거하고, 나머지 A를 제거
        deletions = s[:i].count('B') + s[i:].count('A')
        min_deletions = min(min_deletions, deletions)

    return min_deletions

print(solution("BAAABAB")) # Output: 2
print(solution("BBABAA"))  # Output: 3
print(solution("AABBBB"))  # Output: 0