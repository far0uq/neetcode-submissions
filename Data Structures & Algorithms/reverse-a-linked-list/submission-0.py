# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverseHead = None
        while(head != None):
            if(reverseHead == None):
                reverseHead = ListNode(val=head.val, next=None)
            else:
                newNode = ListNode(val=head.val,next=reverseHead)
                reverseHead = newNode
            head = head.next
        return reverseHead