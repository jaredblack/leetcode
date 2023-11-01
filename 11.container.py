def maxArea(height: list[int]) -> int:
    p1 = 0
    p2 = len(height) - 1
    def calc_area(p1, p2):
        return (p2 - p1) * min(height[p1], height[p2])

    max_area = calc_area(p1, p2)
    while p1 != p2:
        if height[p1] < height[p2]:
            p1 += 1
        else:
            p2 -= 1
        max_area = calc_area(p1, p2) if calc_area(p1, p2) > max_area else max_area

    return max_area