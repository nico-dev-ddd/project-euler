class Pyramid:
    child1 = None
    child2 = None

    def __init__(self, pyramid_values):
        self.value = pyramid_values[0][0]
        dim = len(pyramid_values)
        if dim == 1:
            return
        self.child1 = Pyramid([v[0 : (len(v) - 1)] for v in pyramid_values[1:]])
        self.child2 = Pyramid([v[1 : (len(v))] for v in pyramid_values[1:]])

    @staticmethod
    def build_of_str(values_str: str):
        return Pyramid(
            [
                tuple(int(val) for val in line.strip().split(" "))
                for line in values_str.splitlines()
                if line.strip() != ""
            ]
        )

    def max_path_sum(self):
        if self.child1:
            return self.value + max(
                self.child1.max_path_sum(), self.child2.max_path_sum()
            )
        return self.value


if __name__ == "__main__":
    values_str = """
        75
        95 64
        17 47 82
        18 35 87 10
        20 04 82 47 65
        19 01 23 75 03 34
        88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
        41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
        70 11 33 28 77 73 17 78 39 68 17 57
        91 71 52 38 17 14 91 43 58 50 27 29 48
        63 66 04 68 89 53 67 30 73 16 69 87 40 31
        04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    """
    pyramid = Pyramid.build_of_str(values_str)
    print(pyramid.max_path_sum())
