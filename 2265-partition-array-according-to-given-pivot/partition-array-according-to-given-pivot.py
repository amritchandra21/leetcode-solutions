class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        p = []
        greater = []

        for n in nums:
            if n > pivot:
                greater.append(n)
            elif n < pivot:
                less.append(n)
            else:
                p.append(n)
        return less + p + greater