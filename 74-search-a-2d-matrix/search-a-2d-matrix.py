class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        [[1,3,5,7]
        [10,11,16,20]
        [23,30,34,60]]

        '''
        rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, rows - 1
        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[mid][m]:
                l = m + 1
            elif target < matrix[mid][m]:
                r = m - 1
            else:
                return True
        return False
        