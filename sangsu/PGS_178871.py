def solution(players, callings):
    answer = []
    for calling in callings:
        for i, player in enumerate(players):
            if player == calling:
                front_player = players[i-1]
                back_player = players[i]
                players[i-1] = back_player
                players[i] = front_player
                break
            
    answer = players
            
    return answer

print(solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"] ))