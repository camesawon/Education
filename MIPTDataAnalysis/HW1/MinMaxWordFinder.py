
class MinMaxWordFinder:

    def __init__(self):
        self.text_words = dict()
        self.min_len = -1
        self.max_len = 0

    def add_sentence(self, sentence):
        for word in sentence.split():
            if self.min_len == -1:
                self.min_len = len(word)
            self.min_len = min(len(word), self.min_len)
            self.max_len = max(len(word), self.max_len)
            if len(word) not in self.text_words:
                self.text_words[len(word)] = []
            self.text_words[len(word)].append(word)

    def shortest_words(self):
        return sorted(self.text_words[self.min_len])

    def longest_words(self):
        return sorted([el for el in set(self.text_words[self.max_len])])
