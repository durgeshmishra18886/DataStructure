class ProductOfNumbers:

    def __init__(self):
        # Initialize with 1 to simplify prefix product division
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Reset prefix products because any future product spanning this 0 will be 0
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k is greater than or equal to the current non-zero sequence length,
        # a 0 was encountered within the last k elements
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-k - 1]
