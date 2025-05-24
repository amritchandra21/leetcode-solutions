class Solution(object):
    def largestVariance(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_var = 0
        freq = {}
        for char in s:
            freq[char] = 1 + freq.get(char, 0)
        
        for a in freq: #dceeedce (d,c), (c,e) (c,d) (e,c) (e,d) (d,e) 
            for b in freq:
                if a == b:
                    continue
                
                diff = 0
                has_b = False
                remaining_b = freq[b]

                for c in s:
                    if c != a and c != b:
                        continue
                    if c == a:
                        diff += 1
                    elif c == b:
                        diff -= 1
                        has_b = True
                        remaining_b -= 1

                    if has_b:
                        max_var = max(max_var, diff)
                
                    if diff < 0 and remaining_b > 0:
                        diff = 0
                        has_b = False
            
        return max_var

                
