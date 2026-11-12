class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # idea is to go from the back, add t + num[i] for each t in set
        # We are trying to iterate and generate all possible subsets basically
        dp = set()
        total = sum(nums)
        if total % 2 == 1:
            return False # cannot partition an odd total
        target = total / 2
        dp.add(0)
        for i in range(len(nums)-1,-1,-1):
            nextDP = set()
            for t in dp:
                if t + nums[i] == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return target in dp
