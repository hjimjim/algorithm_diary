문제 : https://leetcode.com/problems/generate-parentheses/


## 복잡한 예제 떠올리기
이 문제의 경우 복잡한 예제는 없다. 입력값은 1 <= n <= 8 로 고정되어 있기 때문이다.
따라서 n = 8일 경우 시간 초과가 뜨지 않도록 코드를 작성하는 것이 핵심이라 판단했다.

## 문제 해결 방법을 줄글로 풀어서 설명하기
1. 괄호의 성질을 확인해서 
    1.1 stack 과 dictionary를 사용하여 괄호 확인 
    1.2 open 괄호 갯수 >= close 괄호 갯수 늘 이 상태가 유지됨 
2. 괄호 combination을 만드는 방법
    2.1 (이전 결과) + 이전 결과 () + () 이전 결과 => 다음결과 
    2.2 주어진 괄호들을 이용해 무작해로 모든 combination을 만들고 check_parenthesis()로 통과된 것들만 저장
    2.3 open 괄호 갯수 >= close 괄호 갯수 성질을 이용하여 combination 수를 줄임 

## 코드를 초안 끄적거리기 (draft)
처음에는 1.1, 2.2를 이용하여 문제를 풀어보기로 하였다. 

candidates = "()" * n #무작위로 호출할 괄호 후보 만들기 
def check_parenthesis(parentheses):
    # parentheses 규칙에 맞는지 확인하여 True, False return 하기
    parentheses == ")"이면 stack안에 넣기 
    그렇지 않을 경우 stack pop해서 짝 맞추고 마지막에 stack 혹은 parentheses 에 아무것도 없어야함.

def build_parenthese안
    candidates length가 0이면 check_parenthese 하기 
        check_parenthesis 가 True일 경우
            res.append(parentheses)
    n번 for문을 돌면서 candidates에 있는 candidate combination 만들기  
    

## 코드 직접 작성해서 돌려보기

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        candidates = "()" * n
        res = []
        def isParenthesis(parentheses):
            parenStack = []
            for paren in parentheses:
                if paren == "(":
                    parenStack.append("(")
                else:
                    if not len(parenStack): return False
                    parenStack.pop() 

            return True

        def buildParenthesis(candi, paren):
            if len(paren) == n*2:
                #res.append(paren)
                if paren not in res: 
                    res.append(paren)
                    return

            for i in range(len(candi)):
                if isParenthesis(paren + candi[i]): 
                    buildParenthesis(candi[:i]+candi[i+1:], paren + candi[i])
        
        buildParenthesis(candidates, "")
        return res
```

## 내 코드 개선점 찾기
위의 코드는 시간 초과가 걸린다. 한마디로 효율이 똥이다. 
이 문제는 괄호의 특성을 이용하여 combination을 만들때 효율적으로 만들어야 한다. 
1.2, 2.3 이용하여 문제 해결 

``` python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def buildParenthesis(paren, open_count, close_count):
            if len(paren) == n*2:
                res.append(paren)
        
            if open_count < n:
                buildParenthesis(paren + "(", open_count+1, close_count)
            if close_count < open_count:
                buildParenthesis(paren + ")", open_count, close_count+1)
        
        buildParenthesis("", 0, 0)
        return res
```
