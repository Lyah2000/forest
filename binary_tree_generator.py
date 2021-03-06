#
# Copyright (c) 2021, Elizaveta Lyahovskaya
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

def preorder(node):
    if node == None:
        return
    yield node
    yield from preorder(node.left)
    yield from preorder(node.right)


def inorder(node):
    if node == None:
        return
    yield from inorder(node.left)
    yield node
    yield from inorder(node.right)


def postorder(node):
    if node == None:
        return
    yield from postorder(node.left)
    yield from postorder(node.right)
    yield node


def levelorder(node):

    def _levelorder(queue):

        if len(queue) == 0:
            return
        current = queue.pop()
        yield current
        if current.left:
            queue.insert(0, current.left)
        if current.right:
            queue.insert(0, current.right)
        yield from _levelorder(queue)

    return _levelorder([node])
