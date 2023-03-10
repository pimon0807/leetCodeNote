class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        count = 0
        while dummy != None:
            dummy = dummy.next
            count += 1

        middle = count // 2
        while middle > 0:
            head = head.next
            middle -= 1
    
        return head