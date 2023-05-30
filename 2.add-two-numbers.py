#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(0)
        ans = root
        c = 0
        
        while l1 or l2:
            n = 0
            if l1 and l2:
                n = (l1.val + l2.val + c) % 10
                c = (l1.val + l2.val + c) // 10
                l1 = l1.next
                l2 = l2.next
            elif l1:
                n = (l1.val + c) % 10
                c = (l1.val + c) // 10
                l1 = l1.next
            elif l2:
                n = (l2.val + c) % 10
                c = (l2.val + c) // 10
                l2 = l2.next

            ans.val = n
            if l1 or l2:
                ans.next = ListNode(0)
                ans = ans.next
        
        if c:
            ans.next = ListNode(1)

        return root
        
# @lc code=end

