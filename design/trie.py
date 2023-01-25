from typing import List

class TrieNode:
    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = {}
        self.is_end_of_word = False #   marks the end of a word

class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        node = self.head
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = node.children[char]
        node.is_end_of_word = True
        return

    def search_with_dots(self, word: str) -> bool:
        def backtrack(index, node):
            if index > len(word):
                return True

            for i in range(index, len(word)):
                char = word[i]
                if not char in node.children:
                    if char == ".":
                        for child in node.children:
                            if backtrack(i + 1, node.children[child]):
                                return True
                    return False
                else:
                    node = node.children[char]
            return node.is_end_of_word
        result = backtrack(0, self.head)
        return result


    def search(self, word: str) -> bool:
        node = self.head
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        if node.is_end_of_word is True:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.head
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True

if __name__ == '__main__':
    trie = Trie()

    trie.insert("bad")
    trie.insert("mad")
    trie.insert("dad")
    print(trie.search_with_dots(".ad"))
    print(trie.search_with_dots("b.."))
    # trie.insert("apple")
    # print(trie.search("apple"))   # returns true
    # print(trie.search("app"))     # returns false
    # print(trie.startsWith("app")) # returns true
    # trie.insert("app")   
    # print(trie.search("app"))     # returns true
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)