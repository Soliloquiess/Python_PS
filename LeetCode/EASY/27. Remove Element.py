class Solution:

    def removeElement(self, nums, val):
        for i in range(len(nums) - 1, -1, -1):  # 맨 끝에서 0번 인덱스까지 -1해가면서 내려감
            if nums[i] == val:
                del nums[i]
        return len(nums)

    # def removeElement(self, nums, val):
    #     i = 0
    #     for x in nums:
    #         if x != val:
    #             nums[i] = x
    #             i += 1
    #     return i

    # def removeElement(self, nums, val):
    #     """
    #     :type nums: List[int]
    #     :type val: int
    #     :rtype: int
    #     """
    #     i, j = 0, len(nums) - 1
    #     while True:
    #         while i < len(nums) and nums[i] != val:
    #             i += 1
    #         while j >= 0 and nums[j] == val:
    #             j -= 1
    #         if i < j:
    #             nums[i], nums[j] = nums[j], nums[i]
    #             i, j = i + 1, j - 1
    #         else:
    #             return i


if __name__ == "__main__":
    a = Solution()
    # nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    nums = [3,2,2,3];
    val = 3
    temp = a.removeElement(nums,val)
    print(temp);
    # print(temp, nums);
