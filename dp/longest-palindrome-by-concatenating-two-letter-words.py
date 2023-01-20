from typing import List
from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        """
        This is the greedy approach that should ideally run in O(n) time complexity
        and probably uses O(n) additional space
        """

        words_hash_map = defaultdict(str)
        words_set = set()
        def pre_process_words(words):
            for word in words:

                #   Do this for words with the same characters
                if word[0] == word[1]:
                    words_set.add(word)
                    continue

                reversed_string = word[1] + word[0]
                if reversed_string in words_hash_map:
                    words_hash_map[reversed_string] = word
                    continue

                if word not in words_hash_map:
                    words_hash_map[word] = ""

        pre_process_words(words)
        count = 0
        for key, value in words_hash_map.items():
            if value != "":
                count += 2
        if len(words_set) > 0:
            return count * 2 + 2
        else:
            return count * 2
        
        
        
        
        
        """
        This is the naive solution that uses backtracking and checks if each string is a palindrome
        Runs in O(n!*n) complexity
        Uses O(n) additional space
        where n is the size of the input
        """
        # longest_palindrome_length = float("-inf")

        # def check_if_palindrome(string):
        #     #   Empty string cannot be a palindrome
        #     if len(string) == 0:
        #         return False
        #     left_pointer = 0
        #     right_pointer = len(string) - 1
        #     while left_pointer <= right_pointer:
        #         if string[left_pointer] == string[right_pointer]:
        #             left_pointer += 1
        #             right_pointer -= 1
        #         else:
        #             return False
        #     return True

        # def backtrack(words_input, curr):
        #     nonlocal longest_palindrome_length
        #     #   Base case of input being finished
        #     if len(words) == 0:
        #         current_string = "".join(curr)
        #         if check_if_palindrome(current_string):
        #             length = len(current_string)
        #             longest_palindrome_length = max(longest_palindrome_length, length)
        #         return

        #     current_string = "".join(curr)
        #     if check_if_palindrome(current_string):
        #         length = len(current_string)
        #         longest_palindrome_length = max(longest_palindrome_length, length)

        #     for index, word in enumerate(words_input):
        #         curr.append(word)
        #         backtrack(words_input[:index] + words_input[index + 1:], curr)
        #         curr.pop()
        #     return

        # backtrack(words, [])
        # if longest_palindrome_length == float("-inf"):
        #     return 0
        # return longest_palindrome_length

if __name__ == "__main__":
    words = ["lc","cl","gg"]
    print(Solution().longestPalindrome(words))

    words = ["ab","ty","yt","lc","cl","ab"]
    print(Solution().longestPalindrome(words))

    words = ["cc","ll","xx"]
    print(Solution().longestPalindrome(words))