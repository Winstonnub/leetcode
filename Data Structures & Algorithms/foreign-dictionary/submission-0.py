class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Problem: Topological sort of 'alphabets'. Kahn's Algorithm (in-degree)
        # The first difference in char between two words forms a directed edge
            # Only first difference! e.g. "bz" comes before "ca"
        # Idea: we keep popping the nodes with in_degree = 0, then we decrease the in_degree of its neighbors.
        result = []
        in_degree = {c:0 for w in words for c in w} # Need to build whole in_degree, because 0 gets added into the queue
        neighbour = defaultdict(set)
        for i in range(len(words) - 1): # Build edge for each pair of different character from an earlier word to the next word
            for j in range(0, min(len(words[i]), len(words[i+1]))):
                if words[i][j] != words[i+1][j]: # u, v
                    neighbour[words[i][j]].add(words[i+1][j])
                    break
            else:
                if len(words[i]) > len(words[i+1]):
                    return ""
        # Add the in_degrees
        for a in neighbour:
            for b in neighbour[a]:
                in_degree[b] += 1
            
        # Kahn's Algorithm
        q = deque([])
        for node in in_degree:
            if in_degree[node] == 0:
                q.append(node)
        while q:
            node = q.popleft()
            result.append(node)
            for nei in neighbour[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        return "".join(result) if len(result) == len(in_degree) else "" # if no. visited == no. nodes, then no cycle!
            
            

        
