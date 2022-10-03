class Solution:
    def searchInsert(self, nums, target) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            # checking middle position
            idx = (left + right) // 2
            num = nums[idx]
            if num == target:
                return idx
            # halving the range
            if num < target:
                left = idx + 1
            else:
                right = idx - 1
        # target not  found
        return left

if __name__ == "__main__":
    a = Solution()
    nums = [1, 3, 5, 6];
    target = 5

    # temp = a.searchInsert(nums, target)
    temp = a.searchInsert([2, 7, 11, 15], 1)
    print(temp);
