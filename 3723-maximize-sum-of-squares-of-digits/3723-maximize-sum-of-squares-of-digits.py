class Solution:

    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # If the requested sum exceeds what `num` 9s can produce
        if sum > 9 * num:
            return ""

        q = sum // 9
        r = sum % 9

        nines = "9" * q
        remainder = str(r) if r > 0 else ""
        zeros = "0" * (num - q - (1 if r > 0 else 0))

        return nines + remainder + zeros