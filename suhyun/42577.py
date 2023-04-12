# 최적화한 코드
def solution(phone_book):

    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False

    return True

print(solution(["12","123","1235","567","88"]))

# 직접 짠 코드
# def solution(phone_book):
#     answer = True
#     cnt = 0
#     phone_book.sort(key=lambda x : len(x))

#     for i in range(len(phone_book)):
#         length = len(phone_book[i])
#         for j in range(i+1,len(phone_book)):
#             if phone_book[i] == phone_book[j][:length]:
#                 answer = False
#                 return answer

# print(solution(["12","123","1235","567","88"]))