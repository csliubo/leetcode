__author__ = [
    '"liubo" <liubo.cs@hotmail.com>'
]


class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self._numbers = [n for n in range(0, maxNumbers)]
        self._using_cache = set()

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if len(self._numbers) > 0:
            num = self._numbers.pop()
            self._using_cache.add(num)
            return num
        else:
            return -1

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return number not in self._using_cache

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if number in self._using_cache:
            self._using_cache.remove(number)
            self._numbers.append(number)

number = 10
obj = PhoneDirectory(20)
param_1 = obj.get()
param_2 = obj.check(number)
obj.release(param_1)
print(obj._numbers)
