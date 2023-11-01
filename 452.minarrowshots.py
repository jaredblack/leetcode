# topic exam 2/5 really had to think
def findMinArrowShots(points: list[list[int]]) -> int:
    points.sort(key=lambda x: x[0])
    start, end = None, None
    arrows = 1
    for point in points:
        if start == None:
            start, end = point[0], point[1]
        if not (point[0] <= end and point[1] >= start):
            arrows += 1
            start, end = point[0], point[1]
        else:
            start = max(start, point[0])
            end = min(end, point[1])

    return arrows
        
print(findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))