class CountSquares:

    def __init__(self):
        self.posdiag = defaultdict(set)
        self.negdiag = defaultdict(set)
        self.freq = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.freq[tuple(point)] += 1
        x, y = point
        
        self.posdiag[x-y].add((x,y))
        self.negdiag[x+y].add((x,y))
        
    def count(self, point: List[int]) -> int:
        res = 0
        qx, qy = point
        
        for x,y in self.posdiag[qx - qy]:
            if (x,y) != (qx,qy) and (qx, y) in self.freq and (x, qy) in self.freq:
                res += 1 * self.freq[(x,y)] * self.freq[(qx,y)] * self.freq[(x,qy)]
        for x,y in self.negdiag[qx + qy]:
            if (x,y) != (qx,qy) and (qx, y) in self.freq and (x, qy) in self.freq:
                res += 1 * self.freq[(x,y)] * self.freq[(qx,y)] * self.freq[(x,qy)]
        return res
        
