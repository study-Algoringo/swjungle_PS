def solution(cacheSize, cities):
    answer = 0
    cache_list = []
    if not cacheSize:
        answer = 5 * len(cities)
    else:
        for city in cities:
            city = city.lower()
            if city in cache_list:
                answer+= 1
                cache_list.remove(city)
                cache_list.append(city)
            else:
                if len(cache_list) == cacheSize:
                    cache_list.pop(0)
                    cache_list.append(city)
                    answer+= 5
                    
                else:
                    cache_list.append(city)
                    answer+= 5
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))