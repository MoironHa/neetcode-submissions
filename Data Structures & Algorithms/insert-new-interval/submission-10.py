class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = newInterval[0]
        end = newInterval[1]
        i = 0

        if not intervals:
            return [newInterval]

        while i < len(intervals):
            if intervals[i][1] < start:
                i += 1
                continue
            else:
                break

        # New interval goes at the beginning
        if i == 0 and end < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals

        # New interval goes at the end
        if i == len(intervals):
            intervals.append(newInterval)
            return intervals

        # New interval goes between two intervals
        if i > 0 and intervals[i - 1][1] < start and end < intervals[i][0]:
            intervals.insert(i, newInterval)
            return intervals

        # Merge
        if i > 0 and intervals[i - 1][1] >= start:
            i -= 1

        start = min(start, intervals[i][0])

        while i < len(intervals) and intervals[i][0] <= end:
            end = max(end, intervals[i][1])
            intervals.pop(i)

        intervals.insert(i, [start, end])

        return intervals