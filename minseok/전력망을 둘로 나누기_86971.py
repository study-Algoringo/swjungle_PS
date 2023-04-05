def solution(n, wires):
    answer = int(1e9)

    # 경로를 하나씩 끊어보면서 경로를 탐색한다
    # wires 가 [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]] 경우 
    # [1,3]을 끊어서 a=[1], b=[3] 리스트를 만든 뒤 [1,3]을 제외한 wires를 탐색하며 탐색된 리스트의 원소가 a 혹은 b 리스트에 들어있는 원소와 겹칠경우 append 해준다  
    # 결과적으로 1과 연결될수 있는 송전탑 리스트를 3과 연결될수 있는 송전탑 리스트가 만들어 지고 set를 이용해 겹치는 원소를 지운 뒤 두 리스트 길이의 차이가 가장 작은 경우를 구한다
    for i in wires:
        lst = []
        for j in wires:             
            if j != i:
                lst.append(j)
        a_lst = [i[0]]              
        b_lst = [i[1]]

        while len(set(a_lst)) + len(set(b_lst)) < n:
            for k in lst:
                if k[0] in a_lst or k[1] in a_lst:
                    a_lst.append(k[0]) 
                    a_lst.append(k[1])
 
                elif k[0] in b_lst or k[1] in b_lst:
                    b_lst.append(k[0]) 
                    b_lst.append(k[1])

        answer = min(answer, abs(len(set(a_lst)) - len(set(b_lst))))
            
    return answer




print((solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])))

