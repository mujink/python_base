def solution(prices):
    answer = [0]*len(prices)
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[i]>prices[j]:break
    return answer


prices = [1,2,3,2,3]
a = solution(prices)
print(a)