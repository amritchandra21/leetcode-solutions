class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = [0] * 26

        for c in word:
            freq[ord(c) - ord('a')] += 1
        for i in range(len(freq)):
            if freq[i] == 0:
                continue
            
            freq[i] -= 1

            frequencies = []
            for j in range(len(freq)):
                if freq[j] != 0:
                    frequencies.append(freq[j])
            if len(set(frequencies)) == 1:
                return True
            freq[i] += 1
        return False