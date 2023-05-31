def solution(cacheSize, cities):
    answer = 0
    data = []
    # cacheSize가 0인 경우
    if cacheSize == 0:
        return 5 * len(cities)
    
    # cacheSize가 0이 아닌 경우
    for city in cities:
        city = city.lower()
        if city not in data:
            if len(data) == cacheSize:
                data.pop(0)
            answer+=5
            data.append(city)
        else:
            data.remove(city)
            answer+=1
            data.append(city)

    return answer

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
