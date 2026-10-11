# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Summand number construction using 10-base raddix representation:
# Construct each summand by multiplying each digit by its radix rased to the
# power of the digit's significance, and taking the sum of those numbers:
# [2, 4, 3] -> 3(10^2) + 4(10^1) + 2(10^0)

# sigma[i*10^(n-1)] where i is an array of n digits

# NOTE: the numbers are given as a linked list in REVERSE order

# This method is very slow as it requires converting each linked list into an
# int by the reverse order of digits, finding the sum, and then converting that
# rusult BACK into a linked list while reversing the order of the digits again.

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        l1_value = 0
        i = 0
        current = l1
        while current is not None:
            l1_value += current.val * (10**i)
            i += 1
            current = current.next
        
        l2_value = 0
        i = 0
        current = l2
        while current is not None:
            l2_value += current.val * (10**i)
            i += 1
            current = current.next
        sum = l1_value + l2_value

        dummy = ListNode()
        current = dummy
        while current is not None:
            current.next = ListNode(sum % 10)
            current = current.next
            sum //= 10
            if sum == 0:
                break
        
        return dummy.next
