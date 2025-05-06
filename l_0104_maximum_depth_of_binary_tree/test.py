from l_0104_maximum_depth_of_binary_tree.solution import Solution, TreeNode

import pytest

@pytest.mark.parametrize(
    "input,expected_output",
    (
        ([3,9,20,None,None,15,7], 3),
        ([1,None,2], 2),
    )
)
def test(input, expected_output):

    nodes = [TreeNode(v) if v else None for v in input]

    i = 1
    for n in nodes:
        n.left = nodes[i]
        i += 1
        n.right = nodes[i]
        i += 1
        if i >= len(nodes):
            break

    assert Solution().maxDepth(nodes[0]) == expected_output


def test_zero():

    assert Solution().maxDepth(None) == 0
