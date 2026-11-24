class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0

        for i in range(n):
            prod = 1
            curr_gcd = 0
            curr_lcm = 1

            for j in range(i, n):
                prod *= nums[j]
                curr_gcd = math.gcd(curr_gcd, nums[j])
                curr_lcm = math.lcm(curr_lcm, nums[j])

                if prod == curr_gcd * curr_lcm:
                    max_len = max(max_len, j - i + 1)
                elif prod > curr_gcd * curr_lcm:
                    break

        return max_len