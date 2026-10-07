

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        result = []
        visited = {s}
        queue = deque([s])
        found = False

        while queue:
            # Process one level at a time
            level_size = len(queue)
            for _ in range(level_size):
                current = queue.popleft()

                if isValid(current):
                    result.append(current)
                    found = True

               
                if found:
                    continue

                for i in range(len(current)):
                    if current[i] not in ('(', ')'):
                        continue

                    next_str = current[:i] + current[i + 1:]
                    if next_str not in visited:
                        visited.add(next_str)
                        queue.append(next_str)

            
            if found:
                break

        return result