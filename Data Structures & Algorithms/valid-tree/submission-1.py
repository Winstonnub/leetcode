class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Idea: we run DFS. If we travelled to a graph that is in visited (not including the previous node), then we found a cycle -> not valid
        # Step 1. Initiate the adjencency list with defaultDict

        neighbours = defaultdict(list)
        for u, v in edges:
            neighbours[u].append(v)
            neighbours[v].append(u)
        
        # Step 2. Perform DFS
        # 1. Check if the node is already visited
        # 2. Put node to be visited
        # 3. Go through each neighbour. If nei is prev, ignore. If not run dfs see if true.
        visited = set() # Can be global, since we only traversing once
        def dfs(node, prev): # Returns whether a CYCLE was found.
            if node in visited:
                return False
            visited.add(node)
            for nei in neighbours[node]:
                if nei == prev:
                    continue
                else:
                    if not dfs(nei, node):
                        return False
            return True # If all nodes in this DFS doesnt form cycle
        
        return dfs(0, -1) and len(visited) == n # if we didnt visit all, means there are singled out nodes, so it cannot be a tree