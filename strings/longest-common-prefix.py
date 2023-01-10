from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pointer = 0
        current_character = ""
        #   Find shortest string
        length = float("inf")
        output = []
        for string in strs:
            length = min(length, len(string))
        while pointer < length:
            break_flag = False
            for string in strs:
                if current_character == "":
                    current_character = string[pointer]
                if string[pointer] != current_character:
                    break_flag = True
                    break
            if break_flag is True:
                break
            output.append(current_character)
            pointer += 1
            current_character = ""
        return "".join(output)

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    result = Solution().longestCommonPrefix(strs)
    print(result)

    strs = ["dog","racecar","car"]
    result = Solution().longestCommonPrefix(strs)
    print(result)

    strs = ["dog","dog","dog"]
    result = Solution().longestCommonPrefix(strs)
    print(result)