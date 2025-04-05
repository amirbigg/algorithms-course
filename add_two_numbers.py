class Solution:
    def addTwoNumbers(self, list1, list2):
        dummy_head = ListNode()
        carry, current = 0, dummy_head
        while list1 or list2 or carry:
            sum_ = (list1.value if list1 else 0) + (list2.value if list2 else 0) + carry
            carry, value = divmod(sum_, 10)
            current.next = ListNode(value)
            current = current.next
            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None
        return dummy_head.next
