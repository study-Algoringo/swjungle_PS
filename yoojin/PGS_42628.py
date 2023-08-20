import heapq
arr = []

def solution(operations):
    answer = []
    
    for line in operations:
        operation, num = line.split()
        if operation == 'I':
            insert(num)
        elif operation == 'D':
            if num == '1':
                delete_max()
            else:
                delete_min()
    if len(arr) == 0:
        answer = [0, 0]
    else:
        max_val = delete_max()
        min_val = delete_min()
        answer = [max_val, min_val]

    return answer

def insert(num):
    heapq.heappush(arr, int(num))

def delete_max():
    if len(arr) == 0:
        return
    # 리스트로 바꿔 모든 원소들에 -를 붙인 후 heapify
    # 최솟값 뽑기
    # 다시 -를 붙인 후 heapify
    for i in range(len(arr)):
        arr[i] = arr[i] * (-1)
    heapq.heapify(arr)
    ret = -heapq.heappop(arr)
    for i in range(len(arr)):
        arr[i] = arr[i] * (-1)
    heapq.heapify(arr)
    return ret

def delete_min():
    if len(arr) == 0:
        return
    return heapq.heappop(arr)