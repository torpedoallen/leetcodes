


"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.

class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "<Node({}, {})>".format(self.val, self.next)


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode('#')
        root = dummy
        while l1 or l2:
            carry, val = divmod((l1 and l1.val or 0) + (l2 and l2.val or 0) + carry, 10) 
            root.next = ListNode(val)
            root = root.next
            l1 = l1 and l1.next or None
            l2 = l2 and l2.next or None
        if carry:
            root.next = ListNode(carry)
            root = root.next

        return dummy.next




if __name__ == "__main__":
    n1 = ListNode(5)
    n2 = ListNode(5)
    print(n1, n2)
    print(Solution().addTwoNumbers(n1, n2))
    




