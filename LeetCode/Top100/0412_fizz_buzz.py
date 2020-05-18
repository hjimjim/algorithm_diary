#2020.05.17

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # 36ms 15MB
        fizz_buzz=[]
        for i in range(1, n+1):
            answer = ""
            if i%3 == 0:
                answer += "Fizz"
            if i%5 == 0:
                answer += "Buzz"
            if answer == "" :
                answer = str(i)
            fizz_buzz.append(answer) 
            
        return fizz_buzz

        """
        # 52 ms 14.8 MB
        answer = []
        for i in range(1, n+1):
            if i%3 == 0 and i%5==0:
                answer.append("FizzBuzz")
            elif i%3 == 0:
                answer.append("Fizz")
            elif i%5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
            
        return answer
        """