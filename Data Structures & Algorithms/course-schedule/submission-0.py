class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)} # list of prerequisites
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # visitSet = ALL courses along the current DFS path
        visitSet = set() 
        def dfs(crs): # current course we looking at: can it be completed? 
            if crs in visitSet: # we have a loop! We find ourselves from dfs
                return False
            if preMap[crs] == []: # if the current course has no prerequisites
                return True 
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False # Found a cycle and cannot be completed
            visitSet.remove(crs)
            preMap[crs] = [] # we can return true immediately that this course can be completed
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

