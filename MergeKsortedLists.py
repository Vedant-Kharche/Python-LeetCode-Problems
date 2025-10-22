# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]]:
        """
        Merges k sorted linked lists into one sorted linked list.
        Approach: Sequentially merge each list with the previous merged result.
        Time complexity: O(k * n), where n is the average number of nodes per list.
        """

        # If there are no lists, simply return None (no nodes to merge)
        if len(lists) == 0:
            return None

        # Iteratively merge each list with the previously merged one
        # Example: (((list1 + list2) + list3) + list4) ...
        for i in range(1, len(lists)):
            lists[i] = self.mergeList(lists[i - 1], lists[i])

        # After merging all, the last list contains the fully merged sorted list
        return lists[-1]


    def mergeList(self, l1, l2):
        """
        Helper function to merge two sorted linked lists (l1 and l2)
        and return the merged sorted list.
        Similar to the merge step in merge sort.
        """

        # Create a dummy node to simplify edge cases (e.g., empty lists)
        dummy = ListNode()
        tail = dummy  # Tail points to the last node in the merged list

        # Traverse both lists until one becomes empty
        while l1 and l2:
            if l1.val < l2.val:
                # If l1's value is smaller, append it to the merged list
                tail.next = l1
                l1 = l1.next
            else:
                # If l2's value is smaller or equal, append it to the merged list
                tail.next = l2
                l2 = l2.next
            # Move the tail pointer forward
            tail = tail.next

        # Attach the remaining nodes (only one list may have leftovers)
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        # Return the merged list, skipping the dummy node
        return dummy.next
