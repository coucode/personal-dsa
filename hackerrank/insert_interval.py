def insert_interval(intervals, newInterval):
    answer = []
        # [6, 7, 8, 9] --> intervals[0], intervals[1] 
        # [3, 4, 5, 6] --> newInterval[0], newInterval[1] 
    while len(intervals) > 0:
        # check for larger interval
        # check for even lengths
        # create a new interval if necessary
        interval = intervals.pop()
        if (len(interval) > len(newInterval)):
            # 2 is >= 6 and <= 9
            # OR
            # 5 is >= 6 and <= 9
            if (newInterval[0] >= interval[0] and newInterval[0] <= interval[1]) or (newInterval[1] >= interval[0] and newInterval[1] <= interval[1]):
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
            else: 
                answer.append(interval)
        elif (len(newInterval) > len(interval)):
            if (interval[0] >= newInterval[0] and interval[0] <= newInterval[1]) or (interval[1] >= newInterval[0] and interval[1] <= newInterval[1]):
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
            else: 
                answer.append(interval)
        else: 
            if (interval[0] >= newInterval[0] and interval[0] <= newInterval[1]) or (interval[1] >= newInterval[0] and interval[1] <= newInterval[1]):
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
            else: 
                answer.append(interval)
    answer.append(newInterval)
    answer.sort()
    return answer