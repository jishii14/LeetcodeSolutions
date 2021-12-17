# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# PROBLEM STATEMENT: Remove nth node from back of linked list
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if (not head):
            return head
        
        if (not head.next and n == 1):
            return None
        
        cur = head
        leader = head.next
        distance = 1
        while (cur.next):
            if (distance < n and leader.next):
                distance += 1
                leader = leader.next
            else:
                if (distance < n):
                    return head.next
                elif (leader.next):
                    cur = cur.next;
                    leader = leader.next;
                else:
                    if (not cur.next):
                        cur.next = None;
                    else:
                        cur.next = cur.next.next;
                        break
                    
        return head
        