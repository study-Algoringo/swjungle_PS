def solution(cacheSize, cities):
    # 캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.
    # cache hit일 경우 실행시간은 1이다.
    # cache miss일 경우 실행시간은 5이다.
    stack = []
    time = 0

    while(cities):
        city = cities.pop(0).upper()

        if city in stack:
            time += 1
            # stack에서 해당 city를 찾아서 제일 뒤로 넣는다.(갱신)
            f_idx = stack.index(city)
            stack.append(city)
            stack.remove(stack[f_idx])
            continue
        else:
            time += 5
            stack.append(city)
            if len(stack) > cacheSize:
                stack.pop(0)
        
    return time

# cacheSize = 3
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(cacheSize, cities))