class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Algorithm:
            # We search rows from left to right.
            # For each pass,
            # we check whether the rightmost element is smaller than target
            #   If yes, we go next
            #   If not (rightmost is larger than target),
            #   Then we perform binary search in that list
        for r in matrix:
            if r[-1] < target:
                continue
            elif r[-1] == target:
                return True
            else: # target might be within this
                hashset = set(r)
                if target in hashset:
                    return True
                else:
                    return False
        return False
        
