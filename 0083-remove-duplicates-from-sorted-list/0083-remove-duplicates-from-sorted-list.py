# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head # assigning a pointer that starts at the head before the list

        while current:
            while current.next and current.val == current.next.val: # compares the current value to the next value
                current.next = current.next.next # skips/deletes the duplicate by updating the current pointer
            current = current.next # moving on to the next node in the list
        return head
