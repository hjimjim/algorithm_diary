## Understand problems better by thinking about complex cases.
example 1 
- [1, 10, 2, 3, 10] --> ans = 20
1. Rob 1 + Rob 3 + Rob 5 ==> max of (Rob 1, Rob 2, Rob 3) + Rob 5
2. Rob 1 + Rob 4 ==> max of (Rob 1, Rob 2) + Rob 4
3. Rob 2 + Rob 4  
...  
Rob 1 = Rob 1  
Rob 2 = Rob 2  
Rob 3 = max(Rob 1) + Rob 3  
Rob 4 = max(Rob 1, Rob 2) + Rob 4   
Rob 5 = max(Rob 2, Rob 3) + Rob 5  
 
## Write the solution in human language
Rob N can be calculated by adding Rob N to max(Rob N-2, Rob N-1)

## Make draft code
```
if n <= 2: return nums[n-1]

rob = [] * (n+1)
rob[1] = nums[0]
rob[2] = nums[1]
rob[3] = nums[2] + nums[0]
for i in range(4, n+1):
    rob[i] = max(rob[i-3],rob[i-2]) + nums[i-1]

return max(rob[n], rob[n-1])
```
## Write code
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])


        rob = [0] * (n+1)
        rob[1] = nums[0]
        rob[2] = nums[1]
        rob[3] = nums[2] + nums[0]
        for i in range(4, n+1):
            rob[i] = max(rob[i-3],rob[i-2]) + nums[i-1]
        
        return max(rob[n], rob[n-1])
```

## Look for improvements
code is simpler
``` python
class Solution:
    def rob(self, nums: List[int]) -> int:
        first, second = 0, 0

        for current in nums:
            rob = max(current + first, second)
            first = second
            second = rob
        
        return rob    
```
