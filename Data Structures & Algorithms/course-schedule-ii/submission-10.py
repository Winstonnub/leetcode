class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # e.g. 
        #0 -> 1 -> 3
        #  -> 2 -> 4
        
        # 1. Make an adjacency list: {node: [neigbours]} in directed fashion

        # 2. DFS. 
                # we start on an UNVISITED node and go through each neighbour there.
                # When we finish visiting, we put that into our result array.
                # but if we visit a node that is in visiting, it means a cycle is formed we return []
        
        # 3. We need to reverse the list to give the right order
        adj = defaultdict(list)
        for v, u in prerequisites:
            adj[v].append(u)
        
        visiting = set()
        visited = set()
        res = []
        def dfs(node): # basically we want to find whether the course is valid (so no cycles)]
            if node in visiting:
                return False
            if node in visited:
                return True

            visiting.add(node)
            for nei in adj[node]:
                if dfs(nei) == False:
                    return False
            visiting.remove(node)
            visited.add(node)
            res.append(node)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res
        
