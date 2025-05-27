class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        pMap = {}
        for i in range(numCourses):
            pMap[i] = []

        for crs, pre in prerequisites:
            pMap[crs].append(pre)
        
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if pMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in pMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            pMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True