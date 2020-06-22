class Root:

    def __init__(self):
        self.char = []
        self.endOfWord = 0
        self.count = 0

    def fill(self):
        for it in range(128):
            self.char.append(Root())


def insert(current, word):

    if len(word) == 0: return 0
    for it in range(0, len(word)):
        if len(current.char) < 128:
            current.fill()
        if ord(word[it]) < 128:
            current = current.char[ord(word[it])]

    current.endOfWord += 1
    return current.endOfWord


def find(current, word):

    if len(word) == 0: return 0
    for it in range(0, len(word)):
        if len(current.char) == 0:
            current.fill()
        if ord(word[it]) < 128:
            current = current.char[ord(word[it])]
    return current.endOfWord
