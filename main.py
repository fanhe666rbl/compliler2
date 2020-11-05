import sys

f = {
    '+': 0,
    '*': 1,
    'i': 2,
    '(': 3,
    ')': 4,
    '#': 5
}
p = [
    [1, -1, -1, -1, 1, 1],
    [1, 1, -1, -1, 1, 1],
    [1, 1, 'N', 'N', 1, 1],
    [-1, -1, -1, -1, 0, 'N'],
    [1, 1, 'N', 'N', 1, 'N'],
    [-1, -1, -1, -1, 'N', 'N']
]


class Stack(object):

    def __init__(self):
        self.list = []

    def is_empty(self):
        return self.list == []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[-1]

    def size(self):
        return len(self.list)


def protocol(t_stack, n_stack):
    o = t_stack.pop()
    # print(o)
    if o == 'i':
        n_stack.push('N')
        return True
    else:
        if not n_stack.is_empty():
            n_stack.pop()
            if not n_stack.is_empty():
                n_stack.pop()
                n_stack.push('N')
                return True
            else:
                return False
        else:
            return False
    pass


def analyse(ob):
    t_stack = Stack()
    n_stack = Stack()
    i = 0
    t_stack.push('#')
    # print(f[ob[i]])
    while i < len(ob):
        o = ob[i]
        if o == '\n' or o == '\r':
            if t_stack.peek() == '#':
                if n_stack.size() == 1:
                    return 0
                if protocol(t_stack, n_stack):
                    print('R')
                else:
                    print("RE")
                    return 0
            else:
                if protocol(t_stack, n_stack):
                    print('R')
                    # print(t_stack.peek())
                    # print(n_stack.size())
                else:
                    print("RE")
                    return 0
        else:
            if p[f[t_stack.peek()]][f[o]] == 'N':
                print('E')
                return 0
            elif p[f[t_stack.peek()]][f[o]] == 1:
                if protocol(t_stack, n_stack):
                    print('R')
                else:
                    print("RE")
                    return 0
            elif p[f[t_stack.peek()]][f[o]] == -1:
                t_stack.push(o)
                print('I'+o)
                i += 1

    pass


def opg(filename):
    fo = open(filename)
    ob = fo.read()
    analyse(ob)
        # print("----------")
    # print(str)
    fo.close()
    return 0


# print("test")


if __name__ == '__main__':
    opg(sys.argv[1])
