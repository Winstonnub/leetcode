class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict() # or defaultdict(int) for 0
        for num in nums:
            count[num] = 1 + count.get(num, 0) # default 0 if keyError
        
        freq = [[] for i in range(len(nums) + 1)] # +1, since we need 0,1,2 for length num to be 2
        for num, cnt in count.items(): # Return key pair value
            freq[cnt].append(num) # freq[1] contains all numbers that appeared once

        res = []
        for i in range(len(freq) - 1, 0 , -1):
            for num in freq[i]: # freq[i] contains number that has i appearance
                res.append(num)
                if len(res) == k:
                    return res
            
            
