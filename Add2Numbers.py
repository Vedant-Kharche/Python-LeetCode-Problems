# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify handling of the resulting linked list.
        # 'cur' will be used to build the result list step by step.
        dummy = ListNode()
        cur = dummy

        # Initialize carry to handle sums greater than 9.
        carry = 0

        # Loop until both lists are exhausted AND there is no carry left.
        while l1 or l2 or carry:
            # Extract current values from l1 and l2, or 0 if one list is shorter.
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Compute the new sum (digit + digit + carry).
            val = v1 + v2 + carry

            # Compute the new carry for the next iteration.
            carry = val // 10  # Integer division gives carry (e.g., 15 // 10 = 1)

            # The current digit for the new node (remainder after removing carry).
            val = val % 10  # e.g., 15 % 10 = 5

            # Create a new node for the current digit and attach it to the result list.
            cur.next = ListNode(val)

            # Move the current pointer to the newly created node.
            cur = cur.next

            # Advance l1 and l2 pointers if possible.
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the actual head of the new list (skipping the dummy node).
        return dummy.next
