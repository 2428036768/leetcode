def insert(intervals,newInterval):
    for i in intervals:
        if newInterval[0]>i[1]:
            if i==intervals[-1]:
                intervals.append(newInterval)
            else:
                continue
        elif newInterval[1]
