# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node before the head.
        # This helps handle edge cases (like removing the first node).
        dummy = ListNode(0, head)
        
        # Initialize two pointers: left starts at dummy, right starts at head
        left = dummy
        right = head

        # Step 1: Move the right pointer n steps ahead
        # So that the gap between left and right is n nodes
        while n > 0:
            right = right.next
            n -= 1

        # Step 2: Move both pointers until right reaches the end
        # At this point, left will be just before the node we want to remove
        while right:
            left = left.next
            right = right.next

        # Step 3: Skip the target node
        # left.next is the node to be removed, so we "unlink" it
        left.next = left.next.next

        # Step 4: Return the new head (dummy.next handles case when head is removed)
        return dummy.next
