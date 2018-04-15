
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        visit = [[sr, sc]]
        oldColor = image[sr][sc]

        if oldColor == newColor:
            return image

        image[sr][sc] = newColor

        while len(visit) != 0:
            x = visit[0][0]
            y = visit[0][1]

            visit.pop(0)
            if x > 0 and image[x - 1][y] == oldColor:
                image[x - 1][y] = newColor
                visit.append([x - 1, y])

            if y + 1 < len(image[0]) and image[x][y + 1] == oldColor:
                image[x][y + 1] = newColor
                visit.append([x, y + 1])

            if x + 1 < len(image) and image[x + 1][y] == oldColor:
                image[x + 1][y] = newColor
                visit.append([x + 1, y])

            if y > 0 and image[x][y - 1] == oldColor:
                image[x][y - 1] = newColor
                visit.append([x, y - 1])

        return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
newColor = 1

s = Solution()
print(s.floodFill(image, sr, sc, newColor))