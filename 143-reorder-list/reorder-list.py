# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        sec = slow.next
        slow.next, prev = None, None

        while sec:
            tmp = sec.next
            sec.next = prev
            prev = sec
            sec = tmp
        front, back = head, prev
        while back:
            t1, t2 = front.next, back.next
            front.next = back
            back.next = t1
            front, back = t1, t2


        