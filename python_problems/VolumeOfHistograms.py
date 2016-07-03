"""
Imagine a histogram. Design an algorithm to compute the volume of water it could hold if someone poured water across
the top.
          |
  ________|              |
 |        |______________|
 |        |        |     |
 |        |        |     |_____
 |        |        |     |     |
[4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0] => 26

"""

def volume(histograms):
    """
    Preprocess the running max at index i.
    Start from the right of the histograms, determining the second tallest bar.
    If the second_tallest is taller than the current bar,
        increment the vol <- second_tallest - cur
    :param histograms: list of non-negative integers
    :return: the volume of the filled histograms
    """
    left_max = histograms[0]
    left_maxes = list()
    for elem in histograms:
        left_max = max(left_max, elem)
        left_maxes.append(left_max)

    print(left_maxes)

    max_right = 0
    vol = 0

    for i in reversed(range(0, len(histograms))):
        max_right = max(max_right, histograms[i])
        second_tallest = min(max_right, left_maxes[i])

        if second_tallest > histograms[i]:
            vol += second_tallest - histograms[i]

    return vol


print(volume([4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]))

