# def solution(s):
#     str_tuples = s[1:-1]
#     idx = 0
#     temp = ''
#     data = []
#     for st in str_tuples:
#         if st == '{':
#             continue
#         elif st == '}':
#             if temp[0] == ',':
#                 temp = temp[1:]
#             data.append(temp.split(','))
#             idx +=1
#             temp =''
#         else:
#             temp += st

    
#     data.sort(key=lambda x : len(x))
#     answer = []  

#     for x in data:
#         for d in x:
#             temp = int(d)
#             if temp not in answer:
#                 answer.append(temp)
            

#     return answer

# 간단한 파싱 풀이
def solution(s):
    answer = []
    s1 = s.lstrip('{').rstrip('}').split('},{')
    for data in s1:
        answer.append(data.split(','))

    answer.sort(key=lambda x : len(x))

    result = []
    for x in answer:
        for y in x:
            temp = int(y)
            if temp not in result:
                result.append(temp)
    return result

# print(solution("{{20,111},{111}}"))