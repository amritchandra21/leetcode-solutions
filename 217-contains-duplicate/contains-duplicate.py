class Solution(object):
    def containsDuplicate(self, nums):
        output = set()
        for num in nums:
            if num in output:
                return True
            else:
                output.add(num)
        return False
        
        