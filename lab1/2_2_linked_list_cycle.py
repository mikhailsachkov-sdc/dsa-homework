# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Implementation detail: 'slow' is always 1/2 of 'fast'
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # same element -> cycle
            if slow == fast:
                return True

        # if reached this point -> no cycle
        return False

