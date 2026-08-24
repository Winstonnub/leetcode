class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Sort the array to use two pointer.
        nums.sort()
        res = []

        # Step 2: For loop to fix a. (a+b+c = 0)
        for i, a in enumerate(nums): # i is index of value a.
            if i > 0 and a == nums[i-1]: # if the value of a is same as previous
                continue # we go to the next pair of i, a
            
            # Step 3: Define the two pointers (left = the one next to a, right = last)
            l = i + 1
            r = len(nums) - 1

            # Step 4: while l and r don't cross, check of a + num[l] + num[r] = 0. 
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r = r - 1 # we move r to smaller
                elif threeSum < 0:
                    l = l + 1 # we move l to larger
                else:
                    res.append([a,nums[l],nums[r]]) # We found sum of abc to be 0.
                    l += 1
                    while nums[l] == nums[l-1] and l < r: 
                        # Step 5: we continue with the same a. 
                        # But we skip values of b that duplicates with current one.
                        l = l + 1
        return res
