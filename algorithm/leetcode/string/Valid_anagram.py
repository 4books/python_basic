class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    b = s.isAnagram('rat', 'car')
    print(b)
