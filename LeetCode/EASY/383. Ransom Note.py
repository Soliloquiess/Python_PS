class Solution:
    def canConstruct(self, ransomNote: str, magazine: str):
        if(len(ransomNote) > len(magazine)): #ransomeNote의 길이가 magazine보다 길면 바로 False
            return False
        else:# ransomNote의 요소가 magazine에 있는지 확인한다.
            for letter in ransomNote:
                if letter in magazine:#만약 magazine에 존재한다면 그 요소(1개만큼)지운다.
                    magazine = magazine.replace(letter, '', 1)
                else:#만약 아니라면 False 리턴
                    return False
            return True

if __name__ == "__main__":
    a = Solution()
    ransomNote = "aa";
    magazine = "aa";

    temp=a.canConstruct(ransomNote , magazine)
    print(temp);