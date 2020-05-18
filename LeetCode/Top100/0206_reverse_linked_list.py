# 2020.05.18
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 32ms, 15.4MB, 84.55%
        pre_node = None;
        target_node = head
        while target_node != None:
            temp = target_node.next 
            target_node.next = pre_node
            pre_node = target_node 
            target_node = temp 
        return pre_node
        
        # 36ms
        if head == None or head.next == None:
            return head
        
        pre_node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return pre_node

        # 40ms, 15.3MB, 33.01%
        if head == None:
            return head
        pre_node = head
        target_node = head.next
        head.next = None 
        while target_node != None:
            temp = target_node.next 
            target_node.next = pre_node
            pre_node = target_node 
            target_node = temp 
        return pre_node