def solution(clothes):

    dic = {}
    clothes.sort()
    cnt = []
    num = 1
    while clothes:
        cloth = clothes.pop(0)
        x, y = cloth
        if y == clothes[0]:
            num += 1
        else:
            cnt.append(num)
    

    
    




    answer = 0
    return answer





tmp1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

solution(tmp1)
