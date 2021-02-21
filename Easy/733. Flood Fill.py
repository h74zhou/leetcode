class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        d = {}
        color = image[sr][sc]

        def inBounds(row, col):
            return row >= 0 and row < len(image) and col >= 0 and col < len(image[0])

        def fill(row, col):
            if not inBounds(row, col) or image[row][col] != color:
                return
            else:
                if (row, col) not in d:
                    image[row][col] = newColor
                    d[(row, col)] = 1
                    fill(row - 1, col)
                    fill(row + 1, col)
                    fill(row, col + 1)
                    fill(row, col - 1)

        fill(sr, sc)
        return image
