def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers)) # str로 치환
    numbers.sort(key = lambda x : x*3, reverse=True) 
    answer = str(int(''.join(numbers)))
    
    return answer
