#
# Copyright (c) 2021, Elizaveta Lyahovskaya
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#
class Node:
    def __init__(self, base):
        self.left = None
        self.right = None
        self.base = base

    def print_(self):
        print(self.base)


if __name__ == '__main__':
    print('Hello world')
    one = Node(15)
    one.print_()
