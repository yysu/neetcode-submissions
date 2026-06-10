"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        rooms = 0
        
        start_list = sorted([i.start for i in intervals])
        end_list = sorted([i.end for i in intervals])

        start_index, end_index = 0, 0
        current_rooms = 0
        while start_index < len(start_list):
            if start_list[start_index] < end_list[end_index]:
                current_rooms += 1
                start_index += 1
            else:
                current_rooms -= 1
                end_index += 1
            rooms = max(rooms, current_rooms)
        return rooms