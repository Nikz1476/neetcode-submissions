class Solution:
    def findMin(self, nums: List[int]) -> int:
        #O(n)
        # minimum = nums[0]

        # for num in nums:
        #     if num < minimum:
        #         minimum = num

        # return minimum

        #O(logn)
        left = 0
        right = len(nums) - 1

        while left < right:

            # Already sorted
            if nums[left] < nums[right]:
                return nums[left]

            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]