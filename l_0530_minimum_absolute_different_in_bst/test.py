from l_0530_minimum_absolute_different_in_bst.solution import Solution, TreeNode

import pytest

@pytest.mark.parametrize(
    "input,expected_output",
    (
        ([4,2,6,1,3], 1),
        ([1,0,48,None,None,12,49], 1),
        ([1,None,3], 2),
        ([3,1], 2),
        ([10,-5], 15),
        ([100,90,110,80,99,101], 1), # difference between trunk and grandchild nodes
        ([236,104,701,None,227,None,911], 9) # difference between trunk and grandchild
    )
)
def test(input, expected_output):

    nodes = [TreeNode(v) if v is not None else None for v in input]

    i = 1
    for n in nodes:
        if n is None:
            continue
        if i >= len(nodes):
            break
        n.left = nodes[i]
        i += 1
        if i >= len(nodes):
            break
        n.right = nodes[i]
        i += 1

    assert Solution().getMinimumDifference(nodes[0]) == expected_output
