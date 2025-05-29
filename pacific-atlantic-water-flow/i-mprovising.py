"""
TIme, space complexity O(m * n)
"""

from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def bfs(q):
            visited = [[False for _ in range(n)] for _ in range(m)]
            dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
            while q:
                x, y = q.popleft()
                visited[x][y] = True
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < m and 0 <= ny < n:
                        if heights[x][y] <= heights[nx][ny]:
                            if not visited[nx][ny]:
                                q.append((nx, ny))

            return visited 

        pacific, atlantic = deque(), deque()

        for i in range(m):
            for j in range(n):
                if i == 0:
                    pacific.append((i, j))
                elif j == 0:
                    pacific.append((i, j))
                if i == m-1:
                    atlantic.append((i, j))
                elif j == n-1:
                    atlantic.append((i, j))
        
        pacific = bfs(pacific)
        atlantic = bfs(atlantic)
        
        answer = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    answer.append([i, j])
        
        return answer