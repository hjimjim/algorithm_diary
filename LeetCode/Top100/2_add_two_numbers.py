# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number = 0
        count = 0
        while l1.next != None:
            number += l1.val*(10**count)
            l1 = l1.next
            count += 1
        number += l1.val*(10**count)
        count = 0
        while l2.next != None:
            number += l2.val*(10**count)
            l2 = l2.next
            count += 1
        number += l2.val*(10**count)
        
       
        l3 = ListNode(number%10)
        
        next_l3 = l3
        while number//10 != 0 :
            number = (number - number%10)//10
            next_l3.next = ListNode(number%10)
            next_l3 = next_l3.next
        return l3

result = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

l3 = result.addTwoNumbers(l1, l2)
"""
while l3.next != None:
    print(l3.val)
    l3 = l3.next
print(l3.val)
"""