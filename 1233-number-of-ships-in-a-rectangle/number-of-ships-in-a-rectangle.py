# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:

        def findShips(topRight, bottomLeft):
            if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y:
                return 0
            if not sea.hasShips(topRight, bottomLeft):
                return 0
            elif topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
                return int(sea.hasShips(topRight, bottomLeft))
            midX = (bottomLeft.x + topRight.x) // 2
            midY = (bottomLeft.y + topRight.y) // 2

            bottomLeftP = findShips(Point(midX, midY), bottomLeft)
            bottomRightP = findShips(Point(topRight.x, midY), Point(midX + 1, bottomLeft.y))
            topLeftP = findShips(Point(midX, topRight.y), Point(bottomLeft.x, midY + 1))
            topRightP = findShips(topRight, Point(midX + 1, midY + 1))

            return bottomLeftP + bottomRightP + topLeftP + topRightP

        return findShips(topRight, bottomLeft)