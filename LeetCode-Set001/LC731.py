class MyCalendarTwo:

    def __init__(self):
        self.bookings = []  # To track all events
        self.overlaps = []  # To track double-booked intervals

    def book(self, start: int, end: int) -> bool:
        # Check if this event would cause a triple booking
        for s, e in self.overlaps:
            if not (end <= s or start >= e):  # There's an overlap with a double-booked interval
                return False

        # Check for overlaps with existing bookings and record double-booked intervals
        for s, e in self.bookings:
            if not (end <= s or start >= e):  # There's an overlap
                overlap_start = max(start, s)
                overlap_end = min(end, e)
                self.overlaps.append((overlap_start, overlap_end))

        # Add the new event to the bookings
        self.bookings.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)