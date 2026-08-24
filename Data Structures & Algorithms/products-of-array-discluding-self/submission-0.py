from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix postfix: two arrays storing numbers before and after it (product)
        #use two passes
        
        #1. Prefix Loop
        prefixArr = deque([])
        postfixArr = deque([])
        prefix = 1
        for num in nums:
            prefix = prefix*num
            prefixArr.append(prefix)
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix = postfix*nums[i]
            postfixArr.appendleft(postfix)
        res = deque([postfixArr[1]])
        for i in range(1, len(nums)-1):
            res.append(prefixArr[i-1] * postfixArr[i+1])
        res.append(prefixArr[-2])

        return list(res)
            

            
            