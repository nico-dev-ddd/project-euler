from __future__ import annotations

from enum import Enum


def sum_of_numbers_on_the_diagonals(size: int) -> int:
    spiral = SpiralDiagonals(size)
    return spiral.sum_of_numbers_on_the_diagonals()


class Coord:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Coord) -> Coord:
        return Coord(self.x + other.x, self.y + other.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coord):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return 10243 * self.x - 437811 * self.y


class Direction(Enum):
    RIGHT = Coord(1, 0)
    DOWN = Coord(0, -1)
    LEFT = Coord(-1, 0)
    UP = Coord(0, 1)

    def next(self) -> Direction:
        return _TABLE_ROTATION[self]


_TABLE_ROTATION = {
    Direction.RIGHT: Direction.DOWN,
    Direction.DOWN: Direction.LEFT,
    Direction.LEFT: Direction.UP,
    Direction.UP: Direction.RIGHT,
}


class SpiralDiagonals:
    def __init__(self, size: int) -> None:
        self.spiral = dict()
        self.current_coord = Coord(0, 0)
        self.direction = Direction.UP
        self.spiral[Coord(0, 0)] = 1
        for value in range(2, size**2 + 1):
            if self.can_turn_right():
                self.direction = self.direction.next()
            self.current_coord += self.direction.value
            self.spiral[self.current_coord] = value

    def can_turn_right(self) -> bool:
        return (self.current_coord + self.direction.next().value) not in self.spiral

    def sum_of_numbers_on_the_diagonals(self) -> int:
        return sum(v for k, v in self.spiral.items() if abs(k.x) == abs(k.y))


if __name__ == "__main__":
    print(sum_of_numbers_on_the_diagonals(1001))
