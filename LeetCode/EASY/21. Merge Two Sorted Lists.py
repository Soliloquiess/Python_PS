# <<<<<<< Updated upstream
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 2개 리스트가 None일 경우
        if not list1 and not list2:
            return None

        # 2개 리스트 중 하나만 None일 경우
        elif not list1 or not list2:
            return list1 or list2

        # 2개 리스트 모두 None이 아닌 경우
        else:
            tail = answer = ListNode()

            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
            tail.next = list1 or list2

        return answer.next
# =======
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     # @param two ListNodes
#     # @return a ListNode
#     def mergeTwoLists(self, l1, l2):
#         result = ListNode(-1)
#         cur = result
#         while(l1 and l2):
#             if l1.val <= l2.val:
#                 cur.next = l1
#                 l1 = l1.next
#             else:
#                 cur.next = l2
#                 l2 = l2.next
#             cur = cur.next
#         l3 = l1 and l1 or l2
#         cur.next = l3
#         return result.next;
#
#
# # class Solution:
# #     def mergeTwoLists(self, list1, list2):
# #         if list1 != None and list2 == None:
# #             return list1
# #         elif list1 == None and list2 != None:
# #             return list2
# #         elif list1 == None and list2 == None:
# #             return None
# #         elif list1.val <= list2.val:
# #             return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
# #         else:
# #             return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
# >>>>>>> Stashed changes
