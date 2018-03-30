class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pos2num = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            j = pos2num.get(target-num)
            if j and i != j:
                return [i, j]

    def twoSum1(self, nums, target):
        pos2num = {}
        for i, num in enumerate(nums):
            m = target - num
            if m in pos2num:
                return [pos2num[m], i]
            else:
                pos2num[num] = i


def test_solution():
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]