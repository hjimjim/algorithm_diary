from typing import List
class Solution:
    """
        Top Interview 150 (Array/ Medium)
        274. H-Index
        link: https://leetcode.com/problems/h-index/
        Date : July 27, 2023
        
        Runtime : 43 ms, faster than 90.7% 
    """
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1:
            return 0 if citations[0] == 0 else 1
            
        citations.sort()
        count = 0
        total = len(citations)
        for i in range(total):
            if citations[i] < total - i:
                count = citations[i]
            else:
                count = max(count, total - i)
        return count
    
    # solution 3 Runtime : 53 ms, faster than 64.70%
    # def hIndex(self, citations: List[int]) -> int:
    #     if len(citations) == 1:
    #         return 0 if citations[0] == 0 else 1
        
    #     citations.sort(reverse = True)
    #     total = len(citations)

    #     if citations[-1] > total:
    #         return total
        
    #     # max를 구하기 위해 citations 배열을 내림차순으로 정렬
    #     # i + 1 = 내림차순으로 정렬된 citations[i] 이상 인용된 paper의 수
    #     # h-index는 최소한 n번 이상 인용된 paper가 최소한 n개 있을 때의 n의 max값
    #     # 현재 논문의 인용수가 i+1번 이상 인용된 논문의 수 보다 작을때 
    #     # h-index = i+1 보다 내림차순 된 citations[i]가 작을때의 i
    #     # min(i+1, citations)
    #     for i in range(total):
    #         if citations[i] < i+1:
    #             return i
            
    #     return 0
    
    # solution 2
    # def hIndex(self, citations: List[int]) -> int:
    #     return max(min(i+1, c) for i, c in enumerate(sorted(citations, reverse=True)))

    # solution 1
    # def hIndex(self, citations: List[int]) -> int:
    #     if len(citations) == 1:
    #         return 0 if citations[0] == 0 else 1
            
    #     citations_dic = {}
    #     count = 1
    #     citations.sort(reverse=True)
    #     for num in citations:
    #         if num not in citations_dic: citations_dic[num] = 0
    #         citations_dic[num] = count
    #         count += 1
        
    #     for i in range(len(citations), -1, -1):
    #         for key in citations_dic.keys():
    #             if i <= key and citations_dic[key] >= i: return i
