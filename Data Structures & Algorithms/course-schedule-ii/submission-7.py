class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: setup
        preq = defaultdict(list)
        for u,v in prerequisites:
            preq[u].append(v) 
        output = []
        visited, cycle = set(), set() # THIS TIME, visited means PROCESSED. 
        # Step 2. DFS
        # Note that if we found a cycle, then not possible -> return empty array
        # If no cycle, then we return the path we travelled
        def dfs(node):
            if node in cycle: # We detected a cycle in current path
                return False
            if node in visited: # We have already processed this node
                return True
            cycle.add(node)
            for nei in preq[node]:
                if dfs(nei) == False: # If theres a cycle
                    return False
            cycle.remove(node) # remove this node from current path
            visited.add(node) # This node is fully processed
            output.append(node) # The base case always append first in this case!
        
        for node in range(numCourses):
            if dfs(node) == False: return []
        return output
