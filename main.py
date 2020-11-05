import sys

op = {
    '+': 0,
    '*': 1,
    'i': 2,
    '(': 3,
    ')': 4,
}
p = [
    [1, -1, -1, -1, 1],
    [1, 1, -1, -1, 1],
    [1, 1, None, None, 1],
    [-1, -1, -1, -1, 0],
    [1, 1, None, None, 1],
]


class Stack:
    def __init__(self):
        self.items = []
        self.top = 0

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[self.top]

    def push(self, item):
        self.items.append(item)
        self.top += 1

    def pop(self):
        self.top -= 1
        return self.items[self.top]


def analyse(ob):
    stack = Stack()
    for s in ob:
        print(s)
    pass


def opg(filename):
    fo = open(filename)

    now = fo.readline()
    analyse(now)
    # print(str)
    fo.close()


# print("test")


if __name__ == '__main__':
    opg(sys.argv[1])
