from TestSuite import Assert
"""
Given two non-diagonally placed rectangles, find the rectangle of interception between the two.
A rectangle is represented as:

rect = {
    left_x
    bottom_y
    height
    width
}

"""


def find_overlap(l1, w1, l2, w2):
    r1 = l1 + w1
    r2 = l2 + w2
    if r1 <= l2 or r2 <= l1:
        return None, None

    highest_left = max(l1, l2)
    lowest_right = min(r1, r2)

    return highest_left, lowest_right - highest_left


def find_intersection(rectangle_1, rectangle_2):
    left_x, width = find_overlap(rectangle_1['left_x'], rectangle_1['width'], rectangle_2['left_x'],
                                 rectangle_2['width'])

    bottom_y, height = find_overlap(rectangle_1['bottom_y'], rectangle_1['height'], rectangle_2['bottom_y'],
                                    rectangle_2['height'])

    if left_x is None or bottom_y is None:
        return {'left_x': None, 'bottom_y': None, 'width': None, 'height': None}

    else:
        return {'left_x': left_x, 'bottom_y': bottom_y, 'width': width, 'height': height}


def test():
    f = find_intersection
    r1 = {'left_x':0,'bottom_y':0,'width':5,'height':10}
    r2 = {'left_x':3,'bottom_y':1,'width':3,'height':12}
    Assert({'left_x': 3, 'bottom_y': 1, 'width': 2, 'height': 9}, f, r1, r2)

    r1 = {'left_x': 0, 'bottom_y': 1, 'width': 4, 'height': 2}
    r2 = {'left_x': 3, 'bottom_y': 0, 'width': 3, 'height': 2}
    Assert({'left_x': 3, 'bottom_y': 1, 'width': 1, 'height': 1}, f, r1, r2)

    r1 = {'left_x': 0, 'bottom_y': 0, 'width': 10, 'height': 10}
    r2 = {'left_x': 1, 'bottom_y': 1, 'width': 3, 'height': 3}
    Assert(r2, f, r1, r2)

    r1 = {'left_x': 0, 'bottom_y': 0, 'width': 2, 'height': 2}
    r2 = {'left_x': 2, 'bottom_y': 2, 'width': 3, 'height': 3}
    Assert({'left_x': None, 'bottom_y': None, 'width': None, 'height': None}, f, r1, r2)


if __name__ == '__main__':
    test()
