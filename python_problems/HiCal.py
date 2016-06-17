from TestSuite import Assert
"""
Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.
To do this, you’ll need to know when any team is having a meeting. In HiCal, a meeting is stored as tuples ↴ of integers (start_time, end_time).
These integers represent the number of 30-minute blocks past 9:00am.

ex: (0,1) 9:00AM - 9:30AM
    (6,9) 12:00PM - 1:30PM
"""

def condense_meeting_times(arr):
    sorted_meets = sorted(arr)
    result = []
    cur_meeting = sorted_meets[0]
    for i, meeting in enumerate(sorted_meets):
        if i == 0:
            continue

        start, end = meeting
        early_start, cur_end = cur_meeting

        if start <= cur_end: # should be one interval
            late_start = max(cur_end, end)
            cur_meeting = early_start, late_start
        else:
            result.append(cur_meeting)
            cur_meeting = meeting

    result.append(cur_meeting)
    return result


def test():
    f = condense_meeting_times
    arr = [(2,3),(1,2)]
    Assert([(1,3)], f, arr, descrip='intervals start and end at same time')
    arr = [(1,2),(3,4)]
    Assert([(1,2),(3,4)], f, arr, descrip="intervals dont overlap")
    arr = [(1,5),(4,9)]
    Assert([(1,9)], f, arr, descrip="intervals overalp")
    arr = [(0,3),(2,5),(3,4),(7,8),(8,9),(10,11),(11,13)]
    Assert([(0,5),(7,9),(10,13)], f, arr)
    arr = [(0,3),(2,5),(3,4),(7,8),(8,9),(10,11),(12,13)]
    Assert([(0,5),(7,9),(10,11),(12,13)], f, arr)
    arr = [(1, 10), (2, 6), (3, 5), (7, 9)]
    Assert([(1,10)], f, arr, descrip='All intervals are consumed')

if __name__ == '__main__':
    test()