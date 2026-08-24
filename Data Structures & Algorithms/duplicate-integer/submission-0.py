class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        for x in nums:
            appearTime = 0
            for y in nums:
                if x == y:
                    appearTime += 1
            if appearTime > 1:
                return True
        return False
