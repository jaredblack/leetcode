def videoStitching(clips: list[list[int]], time: int) -> int:
    coverage_max = 0
    acceptable_start = (0,0)
    num_clips = 0
    while coverage_max < time:
        max_end = 0
        for start, end in clips:
            if acceptable_start[0] <= start <= acceptable_start[1] and end > max_end:
                max_end = end
        if max_end > 0:
            num_clips += 1
            coverage_max = max_end
            acceptable_start = (acceptable_start[1] + 1, max_end)
        else:
            return -1
    return num_clips

print(videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10))