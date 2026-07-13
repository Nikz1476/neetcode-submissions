class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #O(n^2),O(1)
        # area = 0
        # maximum = 0

        # for i in range(0,len(heights)):
        #     for j in range(i+1,len(heights)):
        #         width = j-i
        #         height = min(heights[j],heights[i])

        #         area = width * height

        #         if area > maximum:
        #             maximum = area

        # return maximum

        #O(n),O(1)
        left = 0 
        right = len(heights) - 1 
        maximum = 0

        while left < right:

            width = right - left
            height = min(heights[left], heights[right])
            area = width * height

            if area > maximum:
                maximum = area

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maximum





