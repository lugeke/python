# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        carry = 0
        current = dummyHead
        while l1 and l2:
            sum = l1.val + l2.val + carry
            carry = sum // 10
            node = ListNode(sum % 10)
            current.next = node
            current = node
            l1 = l1.next
            l2 = l2.next
        if l1 or l2:
            if l1:
                l = l1
            else:
                l = l2
            while l:
                sum = l.val + carry
                carry = sum // 10
                node = ListNode(sum % 10)
                current.next = node
                current = node
                l = l.next
        if carry:
            current.next = ListNode(carry)
        return dummyHead.next

    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        carry = 0
        p = l1
        q = l2
        current = dummyHead
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            sum = x + y + carry
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
            if p:
                p = p.next
            if q:
                q = q.next
        if carry:
            current.next = ListNode(carry)
        return dummyHead.next
