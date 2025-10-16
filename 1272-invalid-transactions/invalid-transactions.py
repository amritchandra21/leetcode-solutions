class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed = []

        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(',')
            parsed.append((name, int(time), int(amount), city, t, i))

        invalid = [False] * len(transactions)
        name_to_txns = defaultdict(list)

        for txn in parsed:
            name_to_txns[txn[0]].append(txn)
        for i in range(len(transactions)):
            name, time, amount, city, original, idx = parsed[i]

            if(amount > 1000):
                invalid[i] = True
            
            for other in name_to_txns[name]:
                _, other_time, _, other_city, _, j = other
                if i != j and abs(other_time - time) <= 60 and other_city != city:
                    invalid[i] = True
                    invalid[j] = True
            
        return [transactions[i] for i in range(len(transactions)) if invalid[i]]