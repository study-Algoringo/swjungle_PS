def solution(people, limit):
    people.sort()
    boat = 0
    lightest = 0
    heaviest = len(people) - 1
    
    while lightest <= heaviest:
        if people[lightest] + people[heaviest] <= limit:
            lightest += 1
            heaviest -= 1
        else:
            heaviest -= 1
        boat += 1
    
    answer = boat
    return answer

solution([70, 50, 80, 50], 100)



