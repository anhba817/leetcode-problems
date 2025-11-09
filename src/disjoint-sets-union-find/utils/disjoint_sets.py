class DisjointSets:
    def __init__(self, n: int):
        self.parent = [i for i in range(n + 1)]
        self.size = [0] * (n + 1)

    def find_root(self, a: int) -> int:
        if self.parent[a] == a:
            return a
        self.parent[a] = self.find_root(self.parent[a])
        return self.parent[a]

    def union_sets(self, a: int, b: int):
        rootA = self.find_root(a)
        rootB = self.find_root(b)
        if rootA != rootB:
            if self.size[rootA] < self.size[rootB]:
                self.parent[rootA] = rootB
                self.size[rootB] += self.size[rootA]
            else:
                self.parent[rootB] = rootA
                self.size[rootA] += self.size[rootB]

    def is_connected(self, a: int, b: int) -> bool:
        return self.find_root(a) == self.find_root(b)
