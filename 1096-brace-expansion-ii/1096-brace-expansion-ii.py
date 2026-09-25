class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.i = 0
        self.s = expression
        
        def parse_expression() -> set[str]:
            res = set()
            while True:
                res |= parse_term()
                if self.i < len(self.s) and self.s[self.i] == ',':
                    self.i += 1  # Skip ','
                else:
                    break
            return res

        def parse_term() -> set[str]:
            # Multiplicative identity for string concatenation is {""}
            res = {""}
            while self.i < len(self.s) and self.s[self.i] not in ",}":
                factor = parse_factor()
                # Cartesian product concatenation
                res = {a + b for a in res for b in factor}
            return res

        def parse_factor() -> set[str]:
            if self.s[self.i] == '{':
                self.i += 1  # Skip '{'
                res = parse_expression()
                self.i += 1  # Skip '}'
                return res
            else:
                # Sequence of lowercase letters
                start = self.i
                while self.i < len(self.s) and self.s[self.i].isalpha():
                    self.i += 1
                return {self.s[start:self.i]}

        return sorted(list(parse_expression()))