class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [1,2,2,3,3,3,3]
        # store count {1:1, 2:2, 3:4}
        # Put them into buckets
        # [[1][2][][4][][][]] # for 1 element, we have key 1
        # Then we go from back and pick until the len of result is equal to k
        count = Counter(nums)
        freq = [[] for _ in range(len(nums)+1)]
        for number, cnt in count.items():
            freq[cnt].append(number)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return []
