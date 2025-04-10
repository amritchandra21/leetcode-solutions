class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hMap = defaultdict(int)
        res = []
        maj = len(nums) // 3
        for n in nums:
            hMap[n] += 1
        
        for k, v in hMap.items():
            if v > maj:
                res.append(k)
        return res
