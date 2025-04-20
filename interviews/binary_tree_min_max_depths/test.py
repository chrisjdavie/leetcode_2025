from interviews.binary_tree_min_max_depths.solution import min_max_depths, Node


def test_balanced():

    aaa: Node = Node()
    aab: Node = Node()
    aba: Node = Node()
    aa: Node = Node(left=aaa, right=aab)
    ab: Node = Node(left=aba)
    a_trunk: Node = Node(left=aa, right=ab)

    assert (2, 3) == min_max_depths(a_trunk)


def test_unbalanced():

    aaa: Node = Node()
    aa: Node = Node(left=aaa)
    a_trunk: Node = Node(left=aa)

    assert (1, 3) == min_max_depths(a_trunk)


def test_none():

    assert (0, 0) == min_max_depths(None)
