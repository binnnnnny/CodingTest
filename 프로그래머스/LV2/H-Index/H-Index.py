def solution(citations) :    
    answer = 0
    citations.sort()
    n = len(citations)
    for i in range(n) :
        h_index = n-i
        if citations[i] >= h_index :
            answer = h_index
            break

    
    return answer


# 더 쉬운 풀이
def solution(citations) :
  answer = 0
  citations.sort()
  answer = max(map(min, enumerate(citations, start=1)))
  retrun answer
