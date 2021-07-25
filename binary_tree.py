#
# Copyright (c) 2021, Elizaveta Lyahovskaya
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

from binary_tree_generator import preorder

class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


if __name__ == '__main__':
    print('Hello world')
    tree = Node(1, 
                Node(2, 
                     Node(4), 
                     Node(5)), 
                Node(3, 
                     Node(6), 
                     Node(7)))
    g = preorder(tree)
    #print(next(g).data, next(g).data)
    for X in map(lambda node: node.data, preorder(tree)):
        print(X)
