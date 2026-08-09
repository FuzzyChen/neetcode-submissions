class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.endOfNode = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i]==None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.endOfNode = True

    def search(self, word: str) -> bool:
        def dfs(node,index):
            if index == len(word):
                return node.endOfNode
            if word[index] == ".":
                for child in node.children:
                    if child and dfs(child, index+1):
                        return True
                return False

            i = ord(word[index]) - ord('a')
            if node.children[i] == None:
                return False
            
            return dfs(node.children[i],index + 1)
        
        
        return dfs(self.root,0)
        
