class Solution:
    def __init__(self):
        self.hash_map = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }

    def removeLeadingZeroes(self, string):
        pointer = 0
        counter = 0
        while pointer < len(string) - 1:
            if self.hash_map[string[pointer]] == 0:
                counter += 1
            else:
                break
            pointer += 1
        return string[counter:]

    def product(self, digit1, digit2, carry):
        ans = (digit1 * digit2) + carry
        prod = carry = 0
        if ans > 9:
            prod = ans % 10
            carry = ans // 10
        else:
            prod = ans
        return (carry, prod)

    def add(self, digit, carry):
        ans = digit + carry
        sum = carry = 0
        if ans > 9:
            sum = ans % 10
            carry = ans // 10
        else:
            sum = ans
        return (carry, sum)

    def sum(self, arr):
        pointer = 0
        max_length = float("-inf")
        for string in arr:
            max_length = max(len(string), max_length)

        output = ""
        carry = 0
        for i in range(max_length):
            sum = 0
            for string in arr:
                if pointer >= len(string):
                    continue
                digit = self.hash_map[string[pointer]]
                sum += digit
            (carry, sum) = self.add(sum, carry)
            output = str(sum) + output
            pointer += 1
        if carry == 1:
            output = str(carry) + output
        return output

    def multiply(self, num1: str, num2: str) -> str:
        
        length = 0
        lower_string = ""
        upper_string = ""
        if len(num1) < len(num2):
            length = len(num1)
            lower_string = num1
            upper_string = num2
        else:
            length = len(num2)
            lower_string = num2
            upper_string = num1
        pointer = 0
        lower_string = "".join(reversed(lower_string))
        carry = 0
        sum = ""
        output = []
        while pointer < length:
            lower_digit_str = lower_string[pointer]
            lower_digit = self.hash_map[lower_digit_str]
            if pointer > 0:
                sum = "0" * pointer
            for index in range(len(upper_string) - 1, -1, -1):
                upper_digit = self.hash_map[upper_string[index]]
                (carry, prod) = self.product(upper_digit, lower_digit, carry)
                sum = sum + str(prod)
            if carry != 0:
                sum = sum + str(carry)
                carry = 0
            output.append(sum)
            sum = ""
            pointer += 1
        ans = self.sum(output)
        ans = self.removeLeadingZeroes(ans)
        return ans

if __name__ == "__main__":
    num1 = "2"
    num2 = "3"
    result = Solution().multiply(num1, num2)
    print(result)

    num1 = "456"
    num2 = "123"
    result = Solution().multiply(num1, num2)
    print(result)

    num1 = "0"
    num2 = "0"
    result = Solution().multiply(num1, num2)
    print(result)

    num1 = "123456789"
    num2 = "987654321"
    result = Solution().multiply(num1, num2)
    print(result)

    num1 = "9133"
    num2 = "0"
    result = Solution().multiply(num1, num2)
    print(result)

    num1 = "999"
    num2 = "999"
    result = Solution().multiply(num1, num2)
    print(result)

    num1 = "140"
    num2 = "721"
    result = Solution().multiply(num1, num2)
    print(result)

    # num1 = "123456789"
    # num2 = "987654321"
    # result = Solution().multiply(num1, num2)
    # print(result)