from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max = float("-inf")
        result = ""
        for i in range(len(s)):
            #   Even palindrome
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max:
                    result = s[left:right+1]
                    max = right - left + 1
                left -= 1
                right += 1

            #   Odd palindrome
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max:
                    result = s[left:right+1]
                    max = right - left + 1
                left -= 1
                right += 1

        return result

        
if __name__ == '__main__':
    print(Solution().longestPalindrome("babad"))
    print(Solution().longestPalindrome("cbbd"))
    print(Solution().longestPalindrome("a"))
    print(Solution().longestPalindrome("ac"))
    # print(Solution().longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"))
    # print(Solution().longestPalindrome("abbcccbbbcaaccbababcbcabca"))