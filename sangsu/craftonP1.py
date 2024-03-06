def solution(S, C):
    result = [line.split(',') for line in S.split('\n')]

    columns = result[0]
    k = -1
    for i, column in enumerate(columns):
        if column == C:
            k = i
            
   
    maximum = max(int(row[k]) for row in result[1:])
    
    return maximum

print(solution("id,name,age,act,room,dep\n1,jack,68,T,13,8\n17,Betty,28,F,15,7", "age"))

