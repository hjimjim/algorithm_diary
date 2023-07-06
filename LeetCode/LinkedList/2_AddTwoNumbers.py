# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
        Top Interview 150 (Linked List/ Easy)
        2. Add Two Numbers
        link : https://leetcode.com/problems/add-two-numbers/
        Date : July 6, 2023
        
        Runtime : 67 ms, faster than 97.24%
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        next_num = 0
        while l1 or l2:
            new_num = next_num
            if l1:
                new_num += l1.val
                l1 = l1.next
            if l2:
                new_num += l2.val
                l2 = l2.next

            cur.next = ListNode(new_num % 10)
            next_num = new_num // 10
            cur = cur.next

        if next_num != 0:
            cur.next = ListNode(next_num)
            cur = cur.next

        return dummy.next