class Solution(object):
    def twoSum(self, nums, target):
        lengthOfArray = len(nums)
        for i in range(lengthOfArray):
            for j in range(lengthOfArray):
                if nums[i] + nums[j] == target and i != j:
                    return i, j
        # break_check = False
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target:
        #             break_check = True
        #             return [i,j]
        #             break
        #     if break_check:
        #         break


if __name__ == "__main__":
    a = Solution()
    temp=a.twoSum([2,7,11,15],9)
    print(temp);
