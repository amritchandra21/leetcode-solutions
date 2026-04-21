class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = defaultdict(int)

        for ind, char in enumerate(s):
            lastIndex[char] = ind

        res = []
        size = 0
        end = 0

        for ind, char in enumerate(s):
            end = max(end, lastIndex[char])
            size += 1
            if ind == end:
                res.append(size)
                size = 0
        return res

            