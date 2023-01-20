import math

class Solution:
    def calculate(self, s: str) -> int:
        operators = ['-', '+', '/', '*']

        def perform_math(left, right, operator):
            match operator:
                case '*':
                    return left * right
                case '/':
                    return math.floor(left / right)
                case '+':
                    return left + right
                case '-':
                    return left - right

        def parse(expression, operator_index):
            expression = expression.strip()
            if len(expression) == 1:
                return int(expression)

            if operator_index > 3:
                return

            result = None
            for index, char in enumerate(expression):
                if char == " ":
                    continue
                    
                if char == operators[operator_index]:
                    left = parse(expression[:index], operator_index)
                    right = parse(expression[index + 1:], operator_index)
                    result = perform_math(left, right, operators[operator_index])
                    return result
            if result is None:
                return parse(expression, operator_index + 1)
            return result

        return parse(s, 0)

if __name__ == "__main__":
    print(Solution().calculate("3+2*2+4*2"))
    print(Solution().calculate(" 3 / 2 "))
    print(Solution().calculate(" 3 + 5 / 2 "))
