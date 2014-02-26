# -*- coding: utf-8 -*-

"""
    lilkv.merkletree

    This module implements a basic Merkle Tree, which is used for comparing
    chunks of information in trees.
"""


class Child(object):

    def __init__(self, data):
        self.left, self.right = None, None
        self.data = data


class MerkleTree(object):

    def __init__(self):
        self.root = None

    def add_node(self, data):
        return Child(data)

    def insert(self, root, data):
        if root == None:
            return self.add_node(data)
        elif data < root.data:
            # Assign data to left child
            root.left = self.insert(root.left, data)
        else:
            # Assign data to right child
            root.right = self.insert(root.right, data)

        return root

    def find(self, root, data):
        if root == None:
            return False
        else:
            if data == root.data:
                return True
            elif data < root.data:
                return self.find(root.left, data)
            return self.find(root.right, data)

    @staticmethod
    def compare(self, mtree_a, mtree_b):
        pass
