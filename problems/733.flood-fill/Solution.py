from collections import deque


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        currColor = image[sr][sc]
        if currColor == newColor:
            return image
        n, m = len(image), len(image[0])
        que = deque([(sr, sc)])
        image[sr][sc] = newColor
        while que:
            x, y = que.popleft()
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= mx < n and 0 <= my < m and image[mx][my] == currColor:
                    que.append((mx, my))
                    image[mx][my] = newColor

        return image

