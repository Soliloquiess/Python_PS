class Solution:
    def romanToInt(self, s: str) -> int:
        #s는 str로 받고 함수 끝나고 결과 리턴할 떄 int로 주겠다는 의미(파이썬 개사기인듯.. 함수 타입 없어도 되고..)
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