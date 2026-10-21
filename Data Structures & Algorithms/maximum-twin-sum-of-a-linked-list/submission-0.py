# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next
        arr = []
        res = 0

        while fast:
            arr.append(slow.val)
            fast = fast.next
            if not fast:
                continue
            fast = fast.next
            slow = slow.next
        for i in range(len(arr) - 1, -1, -1):
            slow = slow.next
            ans = arr[i] + slow.val
            arr[i] = ans
            res = max(ans, res) 
        return res