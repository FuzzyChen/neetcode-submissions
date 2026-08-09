class PrefixTree:

    def __init__(self):
        self.word = set()
        self.prefix = set()

    def insert(self, word: str) -> None:
        for index in range(1,len(word)+1):
            self.prefix.add(word[:index])
        self.word.add(word)


    def search(self, word: str) -> bool:
        if word in self.word:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.prefix:
            return True
        else:
            return False
        
        