class Solution:
    def removeDuplicates(self, nums):
        x = 1
        for i in range(len(nums)):
            if(nums[i]!=nums[i+1]):
                nums[x] = nums[i+1]
                x+=1
        return(x)

# class Solution:
#     def removeDuplicates(self, nums) -> int:
#         nums[:] = sorted(list(set(nums)))
#         print((list(set(nums))))
#         return len(list(set(nums)));
#         # return len(nums)


# class Solution:
#     def removeDuplicates(self, nums) -> int:
#         # nums[:] = sorted(list(set(nums)))
#         print(set(nums))
#
#         return len(set(nums))


# class Solution:
#     def removeDuplicates(self, nums) -> int:
#         nums[:] = sorted(list(set(nums)))
#
#         return len(nums)

class Solution:
    def removeDuplicates(self, nums):
        temp = []
        for element in nums:
            if element not in temp:
                temp.append(element)
        temp.sort();
        print(temp);
        return len(temp)


if __name__ == "__main__":
    a = Solution()
    # nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    nums= [1,1,2]
    temp=a.removeDuplicates(nums)
    print(temp);
    # print(temp, nums);