# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = tail = None
        while(list1 or list2):
            if(list1 and not list2):
                if(tail == None):
                    tail = list1
                    head = tail
                else:
                    tail.next = list1
                list1=None

            elif(list2 and not list1):
                if(tail == None):
                    tail = list2
                    head = tail
                else:
                    tail.next = list2
                list2=None

            elif(list1.val >= list2.val):
                if(head == None):
                    head = ListNode(list2.val, None)
                    tail = head
                    list2 = list2.next
                else:
                    tail.next = ListNode(list2.val,None)
                    list2 = list2.next
                    tail = tail.next

            elif(list1.val < list2.val):
                if(head == None):
                    head = ListNode(list1.val, None)
                    tail = head
                    list1 = list1.next
                else:
                    tail.next = ListNode(list1.val,None)
                    list1 = list1.next
                    tail = tail.next 
        return head