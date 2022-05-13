"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q, lvl, prev = deque(), 1, None
        q.append((root, lvl))
        while len(q) > 0:
            curr = q.popleft()
            if curr[0] == None:
                continue
            if lvl == curr[1]:
                if prev != None:
                    prev.next = curr[0]
                    prev = curr[0]
            else:
                prev = curr[0]
                lvl += 1
            q.append((curr[0].left, lvl + 1))
            q.append((curr[0].right, lvl + 1))
        return root