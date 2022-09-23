from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        # self.val: int = val
        # self.next: ListNode = next
        self.val = val
        self.next = next

def create_link(nums: List[int]):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    cur = head
    for num in nums[1:]:
        node = ListNode(num)
        cur.next = node
        cur = node
    return head

def search_link(head) :
    nums = []
    if head is None:
        return nums
    while head:
        nums.append(head.val)
        head = head.next
    return nums

class Solution:
    def middleNode(self, head) :
        slow, fast = head, head
        while fast:
            fast = fast.next
            if not fast:
                return slow
            fast = fast.next
            slow = slow.next
        return slow


if __name__ == "__main__":
    head1 = create_link([1, 2, 3, 4, 5])
    head = Solution().middleNode(head1)
    print(search_link(head))


    head1 = create_link([1, 2, 3, 4, 5, 6])
    head = Solution().middleNode(head1)
    print(search_link(head))





a = [1, 2, 3, 4, 5, 6]


# # # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, a11=None, a1=None):
#         self.val = a11
#         self.nex = a1
#
#     def __repr__(self):
#         return "ListNode{val: " + str(self.val) + ", next: " + str(self.nex) + '}'
#
#     def __call__(self):
#         return [i for i in self.val if self.val != None]
#
#
# class Solution:
#     def middleNode(self, head):
#         nodeList = []
#         while head != None:
#             nodeList.append(head)
#             head = head.nex
#         return nodeList[len(nodeList) // 2]
#
#
# def make_linked_list(value):
#     while len(value) > 0:
#         return ListNode(value[0], make_linked_list(value[1:]))
#
#
# tmp = make_linked_list(a)
#
# b = Solution().middleNode(tmp)
#
# print(b)
# output = []
# while True:
#     output.append(b.val)
#     b = b.nex
#
#     if b == None:
#         break
# print(output)




# from typing import List
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         # self.val: int = val
#         # self.next: ListNode = next
#         self.val = val
#         self.next = next
#
# def create_link(nums: List[int]):
#     if len(nums) == 0:
#         return None
#     head = ListNode(nums[0])
#     cur = head
#     for num in nums[1:]:
#         node = ListNode(num)
#         cur.next = node
#         cur = node
#     return head
#
# def search_link(head) :
#     nums = []
#     if head is None:
#         return nums
#     while head:
#         nums.append(head.val)
#         head = head.next
#     return nums
#
# class Solution:
#     def middleNode(self, head) :
#         slow, fast = head, head
#         while fast:
#             fast = fast.next
#             if not fast:
#                 return slow
#             fast = fast.next
#             slow = slow.next
#         return slow
#
#
# if __name__ == "__main__":
#     head1 = create_link([1, 2, 3, 4, 5])
#     head = Solution().middleNode(head1)
#     print(search_link(head))
#
#
#     head1 = create_link([1, 2, 3, 4, 5, 6])
#     head = Solution().middleNode(head1)
#     print(search_link(head))
#
