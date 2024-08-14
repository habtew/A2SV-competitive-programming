class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # two state 
        # 1 -total_sum
        # 2 - index i
        memo = {}
        
        def dp(amount, i):
            # base cases
            if amount == 0:
                return 1
            if amount < 0 or i <= 0:
                return 0
            
            if (amount, i) in memo:
                return memo[(amount, i)]
            
            memo[(amount, i)] = dp(amount, i - 1) + dp(amount - coins[i - 1], i)
            return memo[(amount, i)]
        
        return dp(amount, len(coins))