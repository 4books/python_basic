from typing import List


class Solution:
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        if nums is None:
            return []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # enumerate로 nums를 for문을 돌리고
        # num을 키값으로 i (index)를 value로 넣음
        # {2:0, 7:2,...}
        table = {num: i for i, num in enumerate(nums)}

        for i, num in enumerate(nums):
            # target에서 현재 num을 뺀 값
            last = target - num
            # 뺀 값이 table에 있고, 지금 현재 index와 같지 않다면
            if (last in table) and (i != table[last]):
                return [i, table[last]]


if __name__ == '__main__':
    s = Solution()
    result = s.twoSum([2, 7, 11, 15], 9)
    print(result)
