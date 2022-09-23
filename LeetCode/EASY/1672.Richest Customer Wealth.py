class Solution:
    def maximumWealth(self, accounts: [[int]]) -> int:
        Wealth = []
        for i in accounts:
            Wealth.append(sum(i))
        return (max(Wealth))

# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         self.wel = []
#         for i in accounts:
#             self.wel.append(sum(i))
#         return (max(self.wel))

#[1, 2, 3, 4] [1, 3, 6, 10]
if __name__ == "__main__":
    a = Solution()
    temp=a.maximumWealth([[1,2,3],[3,2,1]])
    print(temp);

