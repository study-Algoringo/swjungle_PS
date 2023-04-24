from collections import deque
def solution(prices):
  answer = []
  prices = deque(prices)
  while prices:
      ans = 0
      price = prices.popleft()
      
      for i in prices:
          ans += 1
          if price>i:
              break
          
      answer.append(ans)
                
  return answer
print(solution([1, 2, 3, 2, 3]))

