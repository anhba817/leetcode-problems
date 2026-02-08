from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        count = k
        first = True
        prev = None
        while current is not None:
            if count == k:
                firstNode = current
            tempNode = current.next
            current.next = prev
            prev = current
            current = tempNode
            count -= 1
            if count == 0:
                if first:
                    first = False
                    result = prev
                else:
                    temp.next = prev
                temp = firstNode  # temp is the first node of last batch
                count = k
                prev = None

        if count != 0:
            prev2 = None
            # Revert the incomplete batch to get the original
            while prev:
                tempNode = prev.next
                prev.next = prev2
                prev2 = prev
                prev = tempNode
            
            temp.next = prev2
        return result

