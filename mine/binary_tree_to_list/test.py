from mine.binary_tree_to_list.solution import TreeNode, binary_tree_to_ordered_list

import pytest

@pytest.mark.parametrize(
    "input,expected_output",
    (
        ([4,2,6,1,3], [1,2,3,4,6]),
        ([1,0,48,None,None,12,49], [0,1,12,48,49]),
        ([1,None,3], [1,3]),
        ([10,-5], [-5,10]),
        ([100,90,110,80,99,101], [80,90,99,100,101,110]),
        ([236,104,701,None,227,None,911], [104,227,236,701,911])
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

    assert binary_tree_to_ordered_list(nodes[0]) == expected_output
