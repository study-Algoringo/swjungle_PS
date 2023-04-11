str_numbers = []

def solution(numbers):
    # 숫자의 가장 앞자리를 기준으로 큰 수를 가져오기
    # 만약 두 수의 앞자리가 같고, 자릿수가 다르면 더 긴 애의 마지막 자릿수와 첫 번째 자릿수 비교
    for num in numbers:
        str_numbers.append(str(num))
    str_numbers.sort(reverse=True)
    
    for i in range(len(str_numbers) - 1):
        if len(str_numbers[i]) > len(str_numbers[i+1]):
            if str_numbers[i][-1] < str_numbers[i][0]:
                (str_numbers[i+1], str_numbers[i]) = (str_numbers[i], str_numbers[i+1])
    answer = ''
    for i in str_numbers:
        answer += i
    return answer