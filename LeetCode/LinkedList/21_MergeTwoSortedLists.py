class Solution:
    """
        Top Interview 150 (Linked List/ Easy)
        221. Merge Two Sorted Lists
        link : https://leetcode.com/problems/merge-two-sorted-lists/
        Date : July 22, 2023
        
        Runtime : 47 ms, faster than 86.7%
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = ans = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next     
            else :
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 if list1 else list2

        print(cur.next)
        print(ans.next)

        return ans.next