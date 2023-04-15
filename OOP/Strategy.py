from abc import ABC, abstractmethod
from types import resolve_bases


class FilterStrategy(ABC):

    @abstractmethod
    def remove_value(self, val):
        pass


class RemoveNegativeStrategy(FilterStrategy):

    def remove_value(self, val):
        return val < 0


class RemoveOddStrategy(FilterStrategy):

    def remove_value(self, val):
        return val % 2 == 1


class Values():

    def __init__(self, vals):
        self.vals = vals

    def filter(self, strategy):
        res = []

        for item in self.vals:
            if not strategy.remove_value(item):
                res.append(item)

        return res


values = Values([1, 2, 3, 4, -5, 6, 7, 8, -9, 10])

print(values.filter(RemoveNegativeStrategy()))
print(values.filter(RemoveOddStrategy()))
