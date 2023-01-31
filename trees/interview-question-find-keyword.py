"""
Given a text and list of keywords, return a list of booleans representing whether a keyword is present in the text
string = "quick brown fox", keywords = ["lazy", "quick", "dog"]
"""


class TrieNode:
    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.head = TrieNode()

    def add_word(self, word):
        node = self.head
        for char in word:
            if char in node.children:
                node = node.children[char]
                continue

            new_node = TrieNode(char)
            node.children[char] = new_node
            node = node.children[char]
        node.is_end = True
        return

    def search_word(self, word):
        node = self.head
        for char in word:
            if char not in node.children:
                return False
            
            node = node.children[char]
        return node.is_end

def search_for_words(string, keywords):
    trie_ds = Trie()
    for word in string.split(" "):
        trie_ds.add_word(word)

    output = []
    for keyword in keywords:
        result = trie_ds.search_word(keyword)
        output.append(result)

    return output

if __name__ == "__main__":
    trie_ds = Trie()
    str = "quick brown fox"
    keywords = ["lazy", "quick", "dog", "fox"]
    print(search_for_words(str, keywords))

    trie_ds = Trie()
    str = ""
    keywords = ["lazy", "random", "word"]
    print(search_for_words(str, keywords))

    trie_ds = Trie()
    str = "Hello World"
    keywords = []
    print(search_for_words(str, keywords))

    trie_ds = Trie()
    str = "qqq qqqq qqqqq qqqqqq"
    keywords = ["qqqq", "qqqqq", "qqqqqq"]
    print(search_for_words(str, keywords))
    

    
