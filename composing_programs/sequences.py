def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)


def root(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


def partition_tree(n, m):
    """Return a partition tree of n using parts of up to m."""
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return tree(m, [left, right])


print(partition_tree(6, 4))

[4, [4, [False], [3, [False], [2, [True], [1, [1, [True], [False]], [False]]]]], [3, [3, [True], [2, [2, [False], [1, [True], [False]]], [1, [1, [1, [True], [False]], [False]], [False]]]], [2, [2, [2, [True], [1, [1, [True], [False]], [False]]], [1, [1, [1, [1, [True], [False]], [False]], [False]], [False]]], [1, [1, [1, [1, [1, [1, [True], [False]], [False]], [False]], [False]], [False]], [False]]]]]
