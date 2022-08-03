class LC:
    """
    Desc:
        # 208
        A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
    Link:
        https://leetcode.com/problems/implement-trie-prefix-tree/
    Notes:
    """

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

# add each letter to linked list, mark end of word 
# create a TrieNode -> { children: { ch: TrieNode(), ch: TrieNode }, endOfWord: False }
# TrieNode holds its layer of letters in a hashmap named children,  chars(key) to more children char trienodes (values)  
# Time: O(26) - only have to check 26 letters on startsWith 
# Space: O(26) - key length(chars)
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root 
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

# same as above without extra trie class
class SimpleTrie:    
    def __init__(self):
        self.trie = {}    

    def insert(self, word: str) -> None:
        curr = self.trie
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr['!'] = True # sign end of word 
            
    def search(self, word: str) -> bool:
        curr = self.trie 
        for ch in word:
            if ch not in curr:
                return False
            curr = curr[ch]
        return '!' in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for ch in prefix:
            if ch not in curr:
                return False
            curr = curr[ch]
        return True


# Time: O(n) - number of words  
# Space: O(n) - number of words
class BadTrie:
    def __init__(self):
        self.words = []

    def insert(self, word: str) -> None:
        self.words.append(word)

    def search(self, word: str) -> bool:
        if word in self.words: 
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        length = len(prefix)
        for w in self.words:
            if prefix == w[0:length]:
                return True
        return False

