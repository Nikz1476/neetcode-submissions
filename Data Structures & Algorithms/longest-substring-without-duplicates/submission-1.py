class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # n = len(s)
        # ans = 0
        # for i in range(n):
        #     seen = set()
        #     for j in range(i,n):
        #         if s[j] in seen:
        #             break
        #         seen.add(s[j])
        #         ans = max(ans,j-i+1)
        # return ans


        # left = 0
        # seen = set()
        # ans = 0

        # for right in range(len(s)):
        #     while s[right] in seen:
        #         seen.remove(s[left])
        #         left +=1 
        #     seen.add(s[right])
        #     ans = max(ans, right - left + 1)
        # return ans


        last = {}
        left = 0
        ans = 0

        for right, ch in enumerate(s):
            if ch in last:
                left = max(left, last[ch] + 1)

            last[ch] = right
            ans = max(ans, right - left + 1)

        return ans
                