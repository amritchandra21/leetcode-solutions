class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        countBoats = 0
        people.sort()
        l, r = 0, len(people) - 1

        while l <= r:
            if people[l] + people[r] <= limit and l != r:
                l += 1
                r -= 1
            else:
                r -= 1
            countBoats += 1
        return countBoats