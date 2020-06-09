# for number in [1, 2, 3]:
#     print number
#
# for letter in "Hello World":
#     print(letter)

import random

class LotteryMachine:
    def __iter__(self):
        self.numbers = []
        return self

    def __next__(self):
        if len(self.numbers) == 6:
            raise StopIteration
        else:
            number = random.randint(1, 49)

        if number not in self.numbers:
            self.numbers.append(number)
            return number
        else:
            return self.__next__()

machine = LotteryMachine()

for number in machine:
    print(number)
