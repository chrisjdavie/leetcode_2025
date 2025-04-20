from interviews.binary_tree_max_depth.solution import Node, max_depth


def test_deep():

    aaa: Node = Node()
    aab: Node = Node()
    aba: Node = Node()
    aa: Node = Node(left=aaa, right=aab)
    ab: Node = Node(left=aba)
    a_trunk: Node = Node(left=aa, right=ab)

    actual_depth = max_depth(a_trunk)

    assert actual_depth == 3


def test_none():

    assert max_depth(None) == 0
