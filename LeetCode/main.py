a = [1, 2, 3, 4, 5, 6]


# # # Definition for singly-linked list.
class ListNode:
    def __init__(self, a11=None, a1=None):
        self.val = a11
        self.nex = a1

    def __repr__(self):
        return "ListNode{val: " + str(self.val) + ", next: " + str(self.nex) + '}'

    def __call__(self):
        return [i for i in self.val if self.val != None]


class Solution:
    def middleNode(self, head):
        nodeList = []
        while head != None:
            nodeList.append(head)
            head = head.nex
        return nodeList[len(nodeList) // 2]


def make_linked_list(value):
    while len(value) > 0:
        return ListNode(value[0], make_linked_list(value[1:]))


tmp = make_linked_list(a)

b = Solution().middleNode(tmp)

print(b)
output = []
while True:
    output.append(b.val)
    b = b.nex

    if b == None:
        break
print(output)
