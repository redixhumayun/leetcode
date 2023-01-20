class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        def check_if_palindrome(string):
            left_pointer = 0
            right_pointer = len(string) - 1
            while left_pointer <= right_pointer:
                if string[left_pointer] != string[right_pointer]:
                    return False
                left_pointer += 1
                right_pointer -= 1
            pass

        pointer = 0

        #   Run through the string left to right
        while pointer < len(palindrome):       
            current_char = palindrome[pointer]
            if current_char == 'a':
                pointer += 1
                continue

            #   Try to replace with every character from ['a', current character]
            replacement_char = 'a'
            while replacement_char != current_char:
                new_string = palindrome[:pointer] + replacement_char + palindrome[pointer + 1:]
                if check_if_palindrome(new_string) is False:
                    return new_string
                replacement_char = chr(ord(replacement_char) + 1)
            pointer += 1

        #   Run through the string right to left
        pointer = len(palindrome) - 1
        while pointer >= 0:
            current_char = palindrome[pointer]

            #   Try to replace every character from [current character, 'z']
            while current_char != 'z':
                current_char = chr(ord(current_char) + 1)
                new_string = palindrome[:pointer] + current_char + palindrome[pointer + 1:]
                if check_if_palindrome(new_string) is False:
                    return new_string
            pointer -= 1
        
        return ""

if __name__ == '__main__':
    print(Solution().breakPalindrome("abccba"))
    print(Solution().breakPalindrome("a"))
    print(Solution().breakPalindrome("aa"))
    print(Solution().breakPalindrome("aba"))