class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        # [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]
        # Idea:
        # Go through each triplet.
        # If triplet[i] > target[i]: break (reject)
        # If triplet[i] == target[i]: perfect, set checked[i] = True
            # If all(checked) == True then we return True
        # if nothing, then we keep go on
        checked = [False for _ in range(len(target))]
        for triplet in triplets:
            temp_checked = [False for _ in range(len(target))]
            skip = False
            for i in range(len(triplet)):
                if triplet[i] > target[i]:
                    skip = True
                    break
                elif triplet[i] == target[i]:
                    temp_checked[i] = True
            if not skip:
                for i, c in enumerate(temp_checked):
                    if c == True:
                        checked[i] = True
            if all(checked): return True
        return False