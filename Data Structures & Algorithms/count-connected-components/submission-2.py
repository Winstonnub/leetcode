class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Similar to no. islands
        # 1. Setup
        neighbours = defaultdict(list)
        visited = set()
        for u,v in edges:
            neighbours[u].append(v)
            neighbours[v].append(u)
        components = 0

        def bfs(node):
            q = deque([node])
            visited.add(node)
            while q:
                node = q.popleft()
                for nei in neighbours[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
        
        for node in range(n):
            if node not in visited:
                bfs(node)
                components += 1
        return components
            

