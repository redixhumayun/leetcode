from collections import defaultdict
from typing import List
import copy

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        #   Find score of each word
        #   First dump all letters and their scores in a hash map with the score reocurring as many times as the letter is
        letters_hm = defaultdict(list)
        for letter in letters:
            letters_hm[letter].append(score[ord(letter) - 97])
        
        #   Form each word individually and find score to put into a separate hash map
        word_hm = defaultdict(int)
        for word in words:
            not_able_to_form = False
            word_score = 0
            for char in word:
                if letters_hm[char]:
                    word_score += letters_hm[char][0]
                else:
                    not_able_to_form = True
                    break
            if not_able_to_form is False:
                word_hm[word] = word_score

        def can_word_be_formed_with_remaining_letters(word, letters_hm_copy):
            can_form = True
            for char in word:
                if letters_hm_copy[char] and len(letters_hm_copy[char]) > 0:
                    letters_hm_copy[char].pop()
                else:
                    can_form = False
                    break
            return can_form

        ans = 0
        def backtrack(index, letters_hm, tally):
            nonlocal ans
            for i in range(index, len(words)):
                word = words[i]
                if can_word_be_formed_with_remaining_letters(word, copy.deepcopy(letters_hm)) is True:
                    for char in word:
                        letters_hm[char].pop()
                    backtrack(i + 1, letters_hm, tally + word_hm[word])
                    for char in word:
                        letters_hm[char].append(score[ord(char) - 97])
            ans = max(ans, tally)
            return ans     
        
        ans = backtrack(0, letters_hm, 0)
        return ans

if __name__ == '__main__':
    print(Solution().maxScoreWords(["dog","cat","dad","good"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]))
    print(Solution().maxScoreWords(["xxxz","ax","bx","cx"], ["z","a","b","c","x","x","x"], [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]))
    print(Solution().maxScoreWords(["leetcode"], ["l","e","t","c","o","d"], [0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))