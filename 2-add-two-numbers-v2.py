# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            col_sum = l1_val + l2_val + carry
            carry = col_sum // 10
            output_node = ListNode(col_sum % 10)
            current.next = output_node
            current = output_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

solution = Solution()
output_head = solution.addTwoNumbers(l1, l2)

output_array = []
current = output_head
while current is not None:
    output_array.append(current.val)
    current = current.next

print(output_array)
