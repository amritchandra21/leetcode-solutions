class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        vals = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for key, val in count.items():
            vals[val].append(key)
        
        res = []
        for i in range(len(vals) - 1, 0, -1):
            for j in vals[i]:
                res.append(j)
                if len(res) == k:
                    return res
