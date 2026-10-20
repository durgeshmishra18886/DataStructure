class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        
        def can_sort(k: int) -> bool:
            for start in range(0, n, k):
                # Count drops in the circular subarray
                # A valid rotated sorted array has at most 1 drop across adjacent circular pairs
                drops = 0
                drop_idx = -1
                for j in range(k - 1):
                    if nums[start + j] > nums[start + j + 1]:
                        drops += 1
                        drop_idx = j
                        if drops > 1:
                            return False
                
                # Check the wrap-around edge from last element to first element
                if k > 1 and nums[start + k - 1] > nums[start]:
                    drops += 1
                    if drops > 1:
                        return False
                
                # If drops == 0, the block is already sorted; rotation offset = 0
                # If drops == 1, rotation starts at drop_idx + 1
                offset = (drop_idx + 1) if drops == 1 else 0
                
                # Verify that rotating by offset matches sorted_nums directly in O(k)
                for j in range(k):
                    if nums[start + (offset + j) % k] != sorted_nums[start + j]:
                        return False
            return True

        # Find all divisors of n in O(sqrt(n)) and sort them
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
        divisors.sort()

        total_k_sum = 0
        for k in divisors:
            if can_sort(k):
                total_k_sum += k

        return total_k_sum