class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # we make a count dictionary
        freq = [[] for i in range(len(nums) + 1)] # so we have 0,1,2 if length of nums is 2

        for num in nums:
            count[num] = 1 + count.get(num, 0) # get the value of num, else default 0
        for num, cnt in count.items(): # for key and value in the count dict, return (key, value)
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1): # Traverse backwards: freq has 4 slots, so index ends at 4 - 1 = 3. 
            for num in freq[i]:
                res.append(num)
                if len(res) == k: # Stop appending when we reached k number
                    return res
        
