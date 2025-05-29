"""
Time complexity O(n)
Space complexity O(n)

Hash table
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        visited = set()
        while node:
            if node in visited:
                return True
            else:
                visited.add(node)
            node = node.next
        
        return False

        