"""Word Break II

Start with a recursive approach, then try to optimise.

Some ideas:
    - use a trie to minimise whole words comparison
    - for long word, check whether it's breakable in the first place (see Word Break I)
        before trying to actually break it.
    -
"""
import functools


def word_break(s, wordDict):
    """Sample recursive implementation.

    Returns:
        List[str]: The list of valid sentences that we can find.
    """

    @functools.lru_cache(None)
    def dfs(s):
        """We use a helper function here since we can only cache 's',
        wordDict is a list so we can't use it as the cache key.
        """
        if not s:
            return ['']
        res = []
        for word in wordDict:
            if s.startswith(word):
                for sub in dfs(s[len(word):]):
                    if sub:
                        res.append(word + ' ' + sub)
                    else:
                        res.append(word)
        return res

    return dfs(s)


if __name__ == "__main__":
    print(
        word_break(
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ",
            ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"])
    )
    print(word_break("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    print(word_break("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
    print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
