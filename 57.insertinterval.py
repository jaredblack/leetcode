# https://stackoverflow.com/questions/325933/determine-whether-two-date-ranges-overlap/325964#325964

def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    if len(intervals) == 0:
        return [newInterval]


    mod_intervals = list(intervals)
    for interval in intervals:
        if interval[0] <= newInterval[1] and interval[1] >= newInterval[0]:
            newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
            mod_intervals.remove(interval)
    intervals = mod_intervals
    i = 0
    for i, interval in enumerate(intervals):
        if interval[0] > newInterval[0]:
            break
    else:
        i += 1
    intervals.insert(i, newInterval)
    
    return intervals

print(insert([[1,3],[6,9]],[2,5]))