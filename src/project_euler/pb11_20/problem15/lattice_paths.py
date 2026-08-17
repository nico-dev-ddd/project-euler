class LatticePaths:
    cache = {(1, 1): 2}

    def get(self, n, m):
        return self.cache[n, m]

    def set(self, n, m, value):
        self.cache[n, m] = value

    def nb_paths(self, n: int, m: int) -> int:
        if n == 1:
            return m + 1
        if m == 1:
            return n + 1
        if (n, m) in self.cache.keys():
            return self.get(n, m)
        if (m, n) in self.cache.keys():
            return self.get(m, n)
        nb = self.nb_paths(n - 1, m) + self.nb_paths(n, m - 1)
        self.set(n, m, nb)
        return nb


if __name__ == "__main__":
    lattice_paths = LatticePaths()
    print(lattice_paths.nb_paths(20, 20))
