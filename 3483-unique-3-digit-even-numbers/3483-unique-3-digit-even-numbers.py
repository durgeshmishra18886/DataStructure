class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        available = Counter(digits)
        valid_count = 0

        # Iterate through all 3-digit even numbers (100 to 998, step 2)
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10

            needed = Counter((d1, d2, d3))

            # Verify we have enough copies of each digit
            if all(available[d] >= count for d, count in needed.items()):
                valid_count += 1

        return valid_count