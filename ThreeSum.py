# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[
# k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
#  Notice that the solution set must not contain duplicate triplets.
#
#
#  Example 1:
#
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
#
#
#  Example 2:
#
#
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#
#
#  Example 3:
#
#
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#
#
#
#  Constraints:
#
#
#  3 <= nums.length <= 3000
#  -10⁵ <= nums[i] <= 10⁵
#
#
#  Related Topics Array Two Pointers Sorting 👍 26637 👎 2403


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        length = len(nums)
        triplets = []
        found = False

        for _ in range(length):
            if nums[_] >= 0:
                split = _
                found = True
                break

        if found == False:
            return []

        positive = nums[split:]
        negative = nums[:split]

        for i in range(split + 1):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, length):
                if nums[i] + nums[j] > 0:
                    break

                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue

                k = 0 - (nums[i] + nums[j])

                if k < 0:
                    if k in negative:
                        ans = sorted([nums[i], nums[j], k])
                        if nums.count(k) >= ans.count(k) and ans not in triplets:
                            triplets.append(ans)

                if k >= 0:
                    if k in positive:
                        ans = sorted([nums[i], nums[j], k])
                        if nums.count(k) >= ans.count(k) and ans not in triplets:
                            triplets.append(ans)
        return triplets
# leetcode submit region end(Prohibit modification and deletion)
