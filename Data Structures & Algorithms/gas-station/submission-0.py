class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # define net[i] to be gas[i] + cost[i], which is refill g then use c.
        # Idea is if net is negative, then it is impossible.
        # Else, it should be possible.
        # so we calculate net[i]:
        # [-2, -2, -2, 3, 3]: sum is == 0 -> GOOD, else return -1
        # then we find the first element that we don't have to reset
        # we reset when tank < 0
        n = len(gas)
        net = [0] * n
        for i in range(n):
            net[i] = gas[i] - cost[i]
        if sum(net) < 0: return -1
        tank = 0
        starting_indice = 0
        for i, s in enumerate(net):
            tank += s
            if tank < 0:
                starting_indice = i + 1
                tank = 0
        return starting_indice

            

        