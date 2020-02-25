from typing import List


class Solution:

  def rob(self, nums: List[int]) -> int:
    maxSum = {
        0: nums[0] if len(nums) >= 1 else 0,
        1: nums[1] if len(nums) >= 2 else 0
    }

    for index, val in enumerate(nums[2:], 2):
      maxPrev = maxSum[index - 2]
      if index >= 3:
        maxPrev = maxSum[index - 2] if (
            maxSum[index - 2] > maxSum[index - 3]) else maxSum[index - 3]
      maxSum[int(index)] = val + maxPrev

    if len(nums) < 2:
      return maxSum[0]
    return max(maxSum[len(nums) - 1], maxSum[len(nums) - 2])


my = Solution()

n0 = [2, 7, 9, 3, 1, 1, 10]
n1 = []
n2 = [1]
n3 = [1, 1000, 1, 1]

ans = my.rob(n3)
print('ans %d' % ans)

# [2, 7, 9, 3, 1, 1, 1, 10]
#  2  7 11 10 12 12 13  22

# [0, 0, 2, 7, 9, 9, 3, 1]

# Runtime: 24 ms, faster than 92.66% of Python3 online submissions for House Robber.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for House Robber.