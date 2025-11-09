from typing import List

from utils.disjoint_sets import DisjointSets


class ConnectedComponentsInLCMGraph:
    def __init__(self, nums: List[int], threshold: int):
        self.nums = nums
        self.threshold = threshold
        self.disjoint_sets = DisjointSets(threshold)
        self.single_components = []
        self.below_threshold_nums = []
        self.setup()

    def setup(self):
        for num in self.nums:
            if num > self.threshold:
                self.single_components.append(num)
                continue
            self.below_threshold_nums.append(num)
            m = 1
            while num * m <= self.threshold:
                self.disjoint_sets.union_sets(num, num * m)
                m += 1

    def count_components(self) -> int:
        results = [
            self.disjoint_sets.find_root(num) for num in self.below_threshold_nums
        ]
        return len(set(results)) + len(self.single_components)
