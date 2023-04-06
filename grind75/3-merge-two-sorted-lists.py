class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        answer = merged

        while l1 and l2:
            if l1.val < l2.val:
                merged.next = ListNode(l1.val)
                l1 = l1.next
            else: 
                merged.next = ListNode(l2.val)
                l2 = l2.next
            merged = merged.next
        merged.next = l1 or l2
        return answer.next
