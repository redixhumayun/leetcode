from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        required_counter = len(t_counter)
        
        s_counter = defaultdict(int)
        formed_counter = 0

        left = 0

        min_window_size = float("inf")

        string_indexes = (-1, -1)
        for right in range(len(s)):
            character = s[right]
            s_counter[character] += 1

            if s_counter[character] == t_counter[character]:
                formed_counter += 1


            #   Try to reduce the size of the window until the condition is no longer met
            while left <= right and formed_counter == required_counter:
                if right - left + 1 < min_window_size:
                    min_window_size = right - left + 1
                    string_indexes = (left, right)
                s_counter[s[left]] -= 1

                if s_counter[s[left]] < t_counter[s[left]]:
                    formed_counter -= 1

                left += 1

        if string_indexes[0] == -1 and string_indexes[1] == -1:
            return ""
        return s[string_indexes[0] : string_indexes[1] + 1]
            





if __name__ == '__main__':
    solution = Solution()
    # print(solution.minWindow("ADOBECODEBANC", "ABC"))
    # print(solution.minWindow("a", "a"))
    print(solution.minWindow("a", "aa"))
    # print(solution.minWindow("a", "b"))