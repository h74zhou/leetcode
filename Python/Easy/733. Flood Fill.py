class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        width = len(image[0])
        height = len(image)
        oldColor = image[sr][sc]

        map = {}

        def fill(sr, sc):
            if sr >= 0 and sr < height and sc >= 0 and sc < width:
                if image[sr][sc] == oldColor and (sr, sc) not in map:
                    image[sr][sc] = newColor
                    map[(sr, sc)] = 1
                    fill(sr, sc + 1)
                    fill(sr, sc - 1)
                    fill(sr + 1, sc)
                    fill(sr - 1, sc)

        fill(sr, sc)
        return image
