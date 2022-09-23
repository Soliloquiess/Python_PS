class Solution:
    def romanToInt(self, s: str) -> int:
        last = None

        values_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        for c in s:
            if last is None:
                last = c
            elif values_map[last] < values_map[c]:
                total += values_map[c] - values_map[last]
                last = None
            else:
                total += values_map[last]
                last = c

        if last is not None:
            total += values_map[last]

        return total





if __name__ == "__main__":
    a = Solution()
    s = "MCMXCIV"
    temp=a.romanToInt(s)
    print(temp);