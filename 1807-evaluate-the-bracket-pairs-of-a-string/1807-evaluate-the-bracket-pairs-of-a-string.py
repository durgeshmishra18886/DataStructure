class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge_map = {key: val for key, val in knowledge}
        
        result = []
        key = []
        inside_bracket = False
        
        for char in s:
            if char == '(':
                inside_bracket = True
                key = []
            elif char == ')':
                inside_bracket = False
                key_str = "".join(key)
                # Append the value if present, else '?'
                result.append(knowledge_map.get(key_str, '?'))
            else:
                if inside_bracket:
                    key.append(char)
                else:
                    result.append(char)
                    
        return "".join(result)