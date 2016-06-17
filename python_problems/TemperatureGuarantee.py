from collections import defaultdict


class TempTracker:
    def __init__(self):
        self.min = None
        self.max = None
        self.total_sum = 0
        self.n_temps = 0
        self.data = defaultdict(int)
        self.mode = None
        self.max_occurrences = 0

    def insert(self, temperature):

        self.min = min(self.min, temperature) if self.min else temperature

        self.max = max(self.max, temperature) if self.max else temperature

        self.total_sum += temperature
        self.n_temps += 1

        self.data[temperature] += 1
        if self.data[temperature] > self.max_occurrences:
            self.mode = temperature
            self.max_occurrences = self.data[temperature]

    def get_min(self):
        return self.min

    def get_max(self):
        return self.max

    def get_mean(self):
        return None if self.n_temps == 0 else self.total_sum/self.n_temps

    def get_mode(self):
        return self.mode

    def __repr__(self):
        return "Min: %i\nMax: %i\nMean: %f\nMode: %i" % (self.get_min(), self.get_max(), self.get_mean(), self.get_mode())

temps = [1,1,3,5,7,8,3,1]
print(sum(temps)/len(temps))
ts = TempTracker()
for t in temps:
    ts.insert(t)
print(ts)
