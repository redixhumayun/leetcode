from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:

        if endWord not in wordList:
            return 0

        #   Do some pre-processing to build the hash list for all intermediate words
        intermediate_hash_map = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                intermediate_hash_map[word[:i] + "*" + word[i+1:]].append(word)

        queue = deque([(beginWord, 1)]) #   word, steps
        seen = {beginWord}

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            
            for index, char in enumerate(word):
                intermediate_word = word[:index] + "*" + word[index+1:]
                for option in intermediate_hash_map[intermediate_word]:
                    if option not in seen:
                        seen.add(option)
                        queue.append((option, steps + 1))
        return 0

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(Solution().ladderLength(beginWord, endWord, wordList))