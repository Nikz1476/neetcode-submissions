# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #brute force 
        # length = 0
        # temp = head
        # while temp:
        #     length += 1
        #     temp = temp.next
        # if length == n:
        #     return head.next
        # temp = head
        # for _ in range(length - n- 1):
        #     temp = temp.next
        # temp.next = temp.next.next
        # return head


        dummy = ListNode(0)
        dummy.next = head

        fast = head
        slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next