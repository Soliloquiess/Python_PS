class Solution():
    def runningSum(self, nums):
        ans=[]
        tmp=0
        for i in nums:
            tmp+=i
            ans.append(tmp)
        return ans

#[1, 2, 3, 4] [1, 3, 6, 10]
if __name__ == "__main__":
    a = Solution()
    temp=a.runningSum([1, 2, 3, 4])
    print(temp);