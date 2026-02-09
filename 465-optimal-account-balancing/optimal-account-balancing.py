class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = defaultdict(int)

        for f, t, amount in transactions:
            balance[f] -= amount
            balance[t] += amount

        debts = [v for v in balance.values() if v != 0]

        def dfs(start):
            while start < len(debts) and debts[start] == 0:
                start += 1
            if start == len(debts):
                return 0

            res = float('inf')

            for i in range(start + 1, len(debts)):
                if debts[start] * debts[i] < 0:

                    debts[i] += debts[start]
                    res = min(res, 1 + dfs(start + 1))
                    debts[i] -= debts[start]

                    if debts[i] + debts[start] == 0:
                        break
            return res
            
        return dfs(0)
