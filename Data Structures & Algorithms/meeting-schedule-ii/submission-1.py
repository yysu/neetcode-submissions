"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        max_rooms = 0

        start_list = sorted([interval.start for interval in intervals])
        end_list = sorted([interval.end for interval in intervals])

        start_index = 0
        end_index = 0

        current_rooms = 0
        while start_index < len(start_list):
            if start_list[start_index] < end_list[end_index]:
                current_rooms += 1
                start_index += 1
            else:
                current_rooms -= 1
                end_index += 1
            max_rooms = max(max_rooms, current_rooms)
        return max_rooms