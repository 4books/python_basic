class Solution:
    def climbStairs(self, n: int) -> int:
        stair = [0, 1, 2]
        for i in range(3, n + 1):
            stair.append(stair[i - 2] + stair[i - 1])
        return stair[n]


if __name__ == '__main__':
    s = Solution()
    result = s.climbStairs(3)
    print(result)
