def volume(histograms):

    def find_max(start,end):
        if start < 0 or start >= end:
            return 0, 0

        res = start,histograms[start]
        for i in range(start, end + 1):
            cur = i, histograms[i]
            res = max(res, cur, key=lambda x: x[1])
        return res

    def fill(start, end, val):
        for i in range(start,end):
            histograms[i] = val - histograms[i]

    def vol(start, end):
        if start <= end:
            max_for_range = find_max(start, end)
            max_left = find_max(start, max_for_range[0]-1)
            if max_left != (0, 0):
                fill(max_left[0] + 1, max_for_range[0], min(max_left[1], max_for_range[1]))
                vol(start, max_left[0] - 1)
                histograms[max_left[0]] = 0

            max_right = find_max(max_for_range[0] + 1, end)
            if max_right != (0, 0):
                fill(max_for_range[0] + 1, max_right[0], min(max_right[1], max_for_range[1]))
                vol(max_right[0], end)
                histograms[max_right[0]] = 0
            histograms[max_for_range[0]] = 0
    vol(0, len(histograms) - 1)

    print(histograms, sum(histograms))

# volume([4, 0, 0 ,6])
# volume([5, 0, 1])
volume([4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0])

