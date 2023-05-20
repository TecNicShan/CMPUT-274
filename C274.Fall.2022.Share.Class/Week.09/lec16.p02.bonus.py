# Based on code from previous C274/275 instructors
# Modified by Paul Lu, October 2020


class TreeLeaf:
    def __init__(self, uncompressed_byte):
        self.__value = uncompressed_byte
        return

    def get_value(self):
        return self.__value

    def __str__(self):
        return "Leaf storing " + self.__value


class TreeBranch:
    def __init__(self, lchild, rchild):
        self.__left = lchild
        self.__right = rchild
        return

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def __str__(self):
        s = "(" + str(self.__left) + " <- branch root -> "
        s += str(self.__right) + ")"
        return s


def make_encoding_table(huffman_tree):
    encoding_table = {}
    preorder(huffman_tree, encoding_table, ())
    return encoding_table


# preorder tree traversal
def preorder(tree, table, path):
    if isinstance(tree, TreeLeaf):  # base case
        table[tree.get_value()] = path
    elif isinstance(tree, TreeBranch):
        preorder(tree.get_left(), table, path + (False, ))
        preorder(tree.get_right(), table, path + (True, ))


def main():
    leafA = TreeLeaf('A')
    leafB = TreeLeaf('B')
    leafC = TreeLeaf('C')
    leafD = TreeLeaf('D')

    # LHS
    b1 = TreeBranch(leafB, leafC)
    b2 = TreeBranch(leafA, b1)

    # RHS
    b3 = TreeBranch(None,leafD)
    b4 = TreeBranch(None,b3)
    b5 = TreeBranch(None,b4)

    # Root node
    b6 = TreeBranch(b2,b5)

    mytree = b6
    print(make_encoding_table(mytree))
    return


if __name__ == "__main__":
    main()
