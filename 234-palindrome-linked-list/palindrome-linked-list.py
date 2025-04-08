# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        llArr = []
        ptr = head
        while ptr != None:
            llArr.append(ptr.val)
            ptr = ptr.next
        l, r = 0, len(llArr) - 1

        while l < r:
            if llArr[l] != llArr[r]:
                return False
            l += 1
            r -= 1
        return True