class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # Let's have a hashmap last that stores for each char, where is its last occurence
        # currLength = 0
        # Then we loop through each char c in s
        # We also keep track of "end", which is the max(end, last[s[i]])
        # So we keep extending "end" if we see a char with farther last
        # but if i == end, then we know we reached the end of partition
        # Start a new one
        # 1. Set up the hashmap of character -> its last appearance index
        last = defaultdict(int) # Key: char c, int last_index
        end = 0
        currLength = 0
        res = []
        for i, c in enumerate(s):
            last[c] = i
        
        for i, c in enumerate(s):
            end = max(end, last[s[i]])
            currLength += 1
            if end == i:
                # reached end of partition, so we reset currLength
                res.append(currLength)
                currLength = 0
        return res
        



