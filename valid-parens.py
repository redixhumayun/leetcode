class Solution:
    stack = []
    def checkTopChar(self, char: str) -> bool:
        try:
            if char == ")":
                return self.stack.pop() == "("
            elif char == "}":
                return self.stack.pop() == "{"
            elif char == "]":
                return self.stack.pop() == "["
            else:
                self.stack.append(char)
        except IndexError as err:
            return False
    
    def isValid(self, s: str) -> bool:
        bool_value = True
        for index, char in enumerate(s):
            bool_value = self.checkTopChar(char)
            if bool_value == False:
                break
        if len(self.stack) > 0:
            return False
        else:
            return bool_value

if __name__ == '__main__':
    print(Solution().isValid("{[]}"))