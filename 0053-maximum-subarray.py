# class Solution:
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#         sum_max = None
#         for index_left in range(len(nums)):
#             sum_partial = 0
#
#             for index_right in range(index_left, len(nums)):
#                 sum_partial += nums[index_right]
#                 sum_max = sum_partial if sum_max is None else max(sum_max, sum_partial)
#
#         return sum_max


class Solution:
    @staticmethod
    def max_sub_array_rec(nums, index_left, index_right):
        nums_effective = nums[index_left:index_right + 1]

        length = index_right - index_left + 1

        if length == 1:
            return nums[index_left]

        index_mid = index_left + length // 2

        sum_max_left = Solution.max_sub_array_rec(nums, index_left, index_mid - 1)
        sum_max_right = Solution.max_sub_array_rec(nums, index_mid, index_right)

        if sum_max_left > 0 and sum_max_right > 0:
            return sum_max_left + sum_max_right
        elif sum_max_left <= 0 and sum_max_right <= 0:
            return max(sum_max_left, sum_max_right)
        elif sum_max_left <= 0 < sum_max_right:
            return sum_max_right
        elif sum_max_left > 0 >= sum_max_right:
            return sum_max_left

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return Solution.max_sub_array_rec(nums, 0, len(nums) - 1)


def main():
    sol = Solution()
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    # print(sol.maxSubArray([-1]))


if __name__ == '__main__':
    main()
