import random
class RandomizedSet:

    def __init__(self):
        self.arr = set()

    def insert(self, val: int) -> bool:
        if val not in self.arr:
            self.arr.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.arr:
            self.arr.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.arr))

val = int(input())
obj = RandomizedSet()
param_1 = obj.insert(val)
param_2 = obj.remove(val)
param_3 = obj.getRandom()