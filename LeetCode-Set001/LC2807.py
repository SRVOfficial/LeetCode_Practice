# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        while current and current.next:
            # GCD = math.gcd(current.val, current.next.val)

            GCD = gcd(current.val, current.next.val)
            
            node = ListNode(GCD)

            node.next = current.next
            current.next = node
            current = node.next
        
        return head