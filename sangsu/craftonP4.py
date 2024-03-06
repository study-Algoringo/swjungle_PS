def solution(S):
    digram_positions = {}
    max_distance = -1
    

    for i in range(len(S) - 1):
        digram = S[i:i+2]
        
        if digram in digram_positions:
            distance = i - digram_positions[digram][0]
            max_distance = max(max_distance, distance)
        
            digram_positions[digram].append(i)
        else:
            digram_positions[digram] = [i]

    return max_distance

print(solution("aakmaakmakda"))
print(solution("codilty"))
