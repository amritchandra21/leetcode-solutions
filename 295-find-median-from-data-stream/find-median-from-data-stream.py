class MedianFinder:

    def __init__(self):
        self.totalNums = []

    def addNum(self, num: int) -> None:
        self.totalNums.append(num)

    def findMedian(self) -> float:
        self.totalNums.sort()
        arrLen = len(self.totalNums)
        if arrLen % 2 == 0:
            return (self.totalNums[(arrLen // 2) - 1] + self.totalNums[(arrLen // 2)]) / 2
        else:
            return self.totalNums[arrLen // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()