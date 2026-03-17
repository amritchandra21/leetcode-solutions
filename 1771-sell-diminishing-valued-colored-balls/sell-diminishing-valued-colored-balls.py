class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10**9 + 7

        inventory.sort(reverse=True)

        inventory.append(0)

        res = 0
        colors = 1

        for i in range(len(inventory) - 1):
            if inventory[i] > inventory[i + 1]:
                high = inventory[i]
                low = inventory[i + 1]

                height = high - low
                total_balls = colors * height

                if orders >= total_balls:
                    res += colors * (high + low + 1) * height // 2
                    orders -= total_balls
                else:
                    full_rows = orders // colors
                    remainder = orders % colors

                    new_low = high - full_rows
                    res += colors * (high + new_low + 1) * full_rows // 2

                    res += remainder * (new_low)
                    return res % MOD
            res %= MOD
            colors += 1
        return res % MOD