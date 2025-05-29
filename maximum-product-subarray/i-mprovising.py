"""
Time complexity O(n)
Space complexity O(1)

Dynamic programming
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp, min_prod, max_prod = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            # 음수끼리 곱해지는 것을 고려하기 위해
            # 현재 숫자, 최소곱, 최대곱 3가지를 후보로 저장해가야한다
            tmp = [nums[i], min_prod*nums[i], max_prod*nums[i]] 
            min_prod, max_prod = min(tmp), max(tmp)
            dp = max(dp, max_prod)
        
        return dp