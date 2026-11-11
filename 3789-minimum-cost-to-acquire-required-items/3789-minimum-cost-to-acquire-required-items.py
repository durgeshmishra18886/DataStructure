class Solution:
        def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
            common = min(need1, need2)
            ans = common * min(cost1 + cost2, costBoth)
            
            rem1 = need1 - common
            rem2 = need2 - common
            
           
            ans += rem1 * min(cost1, costBoth)
            ans += rem2 * min(cost2, costBoth)
            
            return ans
        