# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders a linked list in-place from:
        L0 → L1 → … → Ln-1 → Ln
        to:
        L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
        """

        # Step 1: Find the middle of the linked list using slow and fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next        # move one step
            fast = fast.next.next   # move two steps
        # Now, 'slow' points to the middle of the list

        # Step 2: Reverse the second half of the list
        second = slow.next         # start of the second half
        prev = slow.next = None    # detach first half from second half
        while second:
            tmp = second.next      # store next node
            second.next = prev     # reverse the link
            prev = second          # move prev forward
            second = tmp           # move second forward
        # Now, 'prev' is the head of the reversed second half

        # Step 3: Merge the first half and the reversed second half
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next   # store next nodes
            first.next = second                    # link first node to second
            second.next = tmp1                     # link second node to next of first
            first, second = tmp1, tmp2             # move pointers forward
        # After merging, the list is reordered as required
