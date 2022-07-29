"""
Desc:
    # 211
    Design a data structure that supports adding new words and finding if a string matches any previously added string.
Link: 
    https://leetcode.com/problems/design-add-and-search-words-data-structure/
Notes:
"""

# using a trie 
# Time: O()
# Space: O()
class WordDictionary:
    def __init__(self):
        self.trie = {} # create {} as trie, add any symbol (!) for end of word

    def addWord(self, word: str) -> None:
        curr = self.trie
        
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr['!'] = True # end of word
        
    def search(self, word: str) -> bool:
        def search_in_node(word, node):
            for i, ch in enumerate(word):
                if not ch in node:
                    # wild card, check all nodes on level
                    if ch == '.':
                        for x in node:
                            if x != '!' and search_in_node(word[i + 1:], node[x]):
                                return True
                    # no words
                    return False
                # char found, move to next
                else:
                    node = node[ch]
            return '!' in node
            
        return search_in_node(word, self.trie)


# nc solution
# Time: O(n) number of letter * 26 ?
# Space: O(n) number of letters
# create trie class
class TrieNode:
    def __init__(self):
        self.children = {} # a : TrieNode
        self.word = False # end of word

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        
            
        return dfs(0, self.root)