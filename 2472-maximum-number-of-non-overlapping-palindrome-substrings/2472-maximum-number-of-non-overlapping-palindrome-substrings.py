class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        n = len(s)
        ans = 0
        last_end = 0  # Next valid starting index

        for i in range(n):
            # Check for a palindrome of length k ending at i
            if i - k + 1 >= last_end and is_palindrome(i - k + 1, i):
                ans += 1
                last_end = i + 1
            # Check for a palindrome of length k + 1 ending at i
            elif i - k >= last_end and is_palindrome(i - k, i):
                ans += 1
                last_end = i + 1

        return ans