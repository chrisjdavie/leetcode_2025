import pytest

from l_0208_implement_trie.solution import Trie


@pytest.mark.parametrize(
    "commands,args,expected_output",
    (
        (
            ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
            [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
            [None, None, True, False, True, None, True],
        ),
        (
            ["Trie","insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"],
            [[],["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]],
            [None,None,None,None,None,None,None,False,True,False,False,False,False,False,True,True,False,True,True,False,False,False,True,True,True],
        ),
    ),
)
def test(commands,args,expected_output):

    trie = Trie()
    for (com, word, eo) in zip(commands[1:], args[1:], expected_output[1:]):
        print(com, word, eo)
        if com == "insert":
            trie.insert(word[0])
        if com == "search":
            assert trie.search(word[0]) == eo
        if com == "startsWith":
            assert trie.startsWith(word[0]) == eo
