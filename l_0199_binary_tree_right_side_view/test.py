from l_0199_binary_tree_right_side_view.solution import Solution, TreeNode

import pytest

@pytest.mark.parametrize(
    "input,expected_output",
    (
        ([1,2,3,None,5,None,4], [1,3,4]),
        ([1,2,3,4,None,None,None,5], [1,3,4,5]),
        ([1,None,3], [1,3]),
    )
)
def test(input, expected_output):

    nodes = [TreeNode(v) if v else None for v in input]

    i = 1
    for n in nodes:
        if i >= len(nodes):
            break
        n.left = nodes[i]
        i += 1
        if i >= len(nodes):
            break
        n.right = nodes[i]
        i += 1

    assert Solution().rightSideView(nodes[0]) == expected_output


def test_empty():

    assert Solution().rightSideView(None) == []
