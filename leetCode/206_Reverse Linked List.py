from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp


        return prev


head = [1, 2, 3, 4, 5]
print(Solution().reverseList(head))
