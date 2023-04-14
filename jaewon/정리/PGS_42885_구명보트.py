def solution(people, limit):
    # people 리스트를 오름차순으로 정렬합니다.
    people.sort()
    
    # 보트의 수를 초기화합니다.
    boats = 0
    
    # 가장 가벼운 사람의 인덱스와 가장 무거운 사람의 인덱스를 설정합니다.
    lightest = 0
    heaviest = len(people) - 1
    
    # 가장 가벼운 사람부터 가장 무거운 사람까지 순차적으로 비교합니다.
    while lightest <= heaviest:
        # 가장 가벼운 사람과 가장 무거운 사람의 무게를 더해서 limit과 비교합니다.
        if people[lightest] + people[heaviest] <= limit:
            # 두 사람을 함께 보낼 수 있으면 보트의 수를 증가시킵니다.
            lightest += 1
            heaviest -= 1
        else:
            # 두 사람을 함께 보낼 수 없으면 가장 무거운 사람만 보낸 후 보트의 수를 증가시킵니다.
            heaviest -= 1
        
        boats += 1
    
    answer = boats
    return answer

solution([70, 50, 80, 50, 50], 100)



