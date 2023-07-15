import sys
input = sys.stdin.readline

n = int(input())
A_numbers = list(map(int, input().split()))
m = int(input())
B_numbers = list(map(int, input().split()))
answer_list = []
A_numbers.sort()


def find_num(num):
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end)//2
        if A_numbers[mid] == num:
            answer_list.append(1)
            return
        
        elif A_numbers[mid] > num:
            end = mid -1
            
        else:
            start = mid +1
        
    answer_list.append(0)
    return

for number in B_numbers:
    find_num(number)
    
answer_list = map(str, answer_list)
print(" ".join(answer_list))
    
