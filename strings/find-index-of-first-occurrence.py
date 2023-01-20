class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        sliding_window_size = len(needle)
        left = 0

        def check_if_strings_equal(string1, string2):
            return string1 == string2

        for right in range(0, len(haystack)):
            current_window_size = right - left + 1
            while current_window_size > sliding_window_size:
                left += 1
                current_window_size = right - left + 1
            if current_window_size == sliding_window_size and check_if_strings_equal(haystack[left : right + 1], needle):
                return left
            right += 1
        return -1

if __name__ == '__main__':
    print(Solution().strStr("sadbutsad", "sad"))
    print(Solution().strStr("leetcode", "leeto"))