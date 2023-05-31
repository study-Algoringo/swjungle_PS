from collections import deque

def solution(cacheSize, cities):
    answer = 0; cache = deque([])
    if cacheSize == 0:
        return len(cities) * 5
    # 큐에서 도시를 찾고, 있는 경우 맨 뒤로, ans + 1
    for i in cities:
        city = i.upper()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        # 없는 경우 
        else:
            # 만약 리스트가 꽉 차있다면 맨 앞 도시 pop, 맨 뒤에 새 도시 추가하고 + 5
            if len(cache) >= cacheSize:
                cache.popleft()    
            # 만약 리스트에 자리가 남아있다면 맨 뒤에 새 도시 추가하고 + 5
            cache.append(city)
            answer += 5

    return answer