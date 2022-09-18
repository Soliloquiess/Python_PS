class Solution(object):
    def fizzBuzz(self, n):
        answer = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 5 == 0:
                answer.append("Buzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            else:
                answer.append(str(i))
        return answer

# if __name__ == "__main__":
#     a = Solution()
#     n = 3
#     temp=a.maximumWealth(n)
#     print(temp);
