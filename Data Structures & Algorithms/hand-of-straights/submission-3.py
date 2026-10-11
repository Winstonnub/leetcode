class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Solution fast enough for duplicates
        # Use frequency list
        # [1,2,3,2,3,6,4,7,8]
        count = Counter(hand)
        for start in sorted(count): # sorted does not modify
            need = count[start] # we need at least 1 ones from each of the consecutive groupSize
            if need == 0:
                continue
            for card in range(start, start + groupSize):
                if count[card] < need:
                    return False
                count[card] -= need
        return True


