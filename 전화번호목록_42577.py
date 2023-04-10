def solution(phone_book):
    answer = True
    
    # 전화번호를 오름차순으로 정렬하여 비교를 더 빠르게 하도록 합니다.
    phone_book = sorted(phone_book)
    
    for i in range(len(phone_book) - 1):
        # 현재 번호와 다음 번호가 서로 접두어 관계인지 확인합니다.
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
        
    return answer

'''
# 해시
# 딕셔너리 사용
def solution(phone_book):
    answer = True
    
    phone_dict = {}
    for key in phone_book:
        phone_dict[key] = 1
    
    for phone_num in phone_dict:        #각각 폰번호마다 검사
        tmp = ''
        for num in phone_num:           #폰번호를 한글자로 쪼개서 반복문
            tmp += num                  #쪼갠 숫자를 반복문이 돌아갈 때마다 붙인다  
            if tmp in phone_dict and tmp != phone_num:      # 딕셔너리의 키로 존재하는지 검사
                answer = False
                return answer
    
    return answer
'''