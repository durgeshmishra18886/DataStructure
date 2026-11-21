class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        
        # 1. Build the adjacency list for the initial tree
        adj = defaultdict(list)
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        # Tracks the closest ancestor node index for each character
        last_seen = {}
        new_parent = list(parent)
        
        # 2. First DFS to determine the new parent for every node simultaneously
        def find_new_parents(u: int):
            char = s[u]
            prev_ancestor = last_seen.get(char, -1)
            
            # If an ancestor with the same character exists, update parent
            if prev_ancestor != -1:
                new_parent[u] = prev_ancestor
                
            # Mark current node u as the closest ancestor for `char`
            last_seen[char] = u
            
            for v in adj[u]:
                find_new_parents(v)
                
            # Backtrack: restore the previous ancestor state before leaving u's subtree
            if prev_ancestor != -1:
                last_seen[char] = prev_ancestor
            else:
                del last_seen[char]

        find_new_parents(0)
        
        # 3. Build the new tree using `new_parent`
        new_adj = defaultdict(list)
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        # 4. Second DFS to compute subtree sizes in the final tree
        answer = [1] * n
        def compute_sizes(u: int) -> int:
            for v in new_adj[u]:
                answer[u] += compute_sizes(v)
            return answer[u]
            
        compute_sizes(0)
        return answer