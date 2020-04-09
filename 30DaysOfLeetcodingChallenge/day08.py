# Middle of the Linked List

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        a = [head]
        
        while a[-1].next:
      
            a.append(a[-1].next)
    
     
        return a[len(a)//2]

class Solution2(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow