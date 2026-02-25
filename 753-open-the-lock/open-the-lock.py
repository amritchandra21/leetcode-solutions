from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
    
        visit = set(deadends)
        q = deque([("0000", 0)])
        def children(val):
            res = []
            for i in range(4):
                digit = str((int(val[i]) + 1) % 10)
                res.append(val[:i] + digit + val[i+1:])
                digit = str((int(val[i]) - 1) % 10)
                res.append(val[:i] + digit + val[i+1:])
            return res
        while q:
            lockVal, count = q.popleft()
            if lockVal == target:
                return count
            for pattern in children(lockVal):
                if pattern not in visit:
                    visit.add(pattern)
                    q.append((pattern, count + 1))
        return -1