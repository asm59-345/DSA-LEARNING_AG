class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key = lambda x : x[1])

        arrows = 1
        arrow_pos = points[0][1]

        for i in range(1, len(points)):
            if points[i][0] > arrow_pos:
                arrows += 1
                arrow_pos = points[i][1]
        return arrows