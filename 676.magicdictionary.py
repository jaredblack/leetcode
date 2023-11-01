class MagicDictionary:

    def __init__(self):
      self.set = set()
        

    def buildDict(self, dictionary: List[str]) -> None:
        self.set = {word for word in dictionary}

    def search(self, searchWord: str) -> bool:
      for i, letter in enumerate(searchWord):
        for j in range(26):
          if chr(ord('a') + j) != letter:
            new_word = searchWord[:i] + (chr(ord('a') + j)) + searchWord[i+1:]
            if new_word in self.set:
              return True
      return False