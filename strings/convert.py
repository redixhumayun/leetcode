from collections import defaultdict

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        hash_map = defaultdict(list)
        counter = -1
        operator = 1
        pointer = 0
        while pointer < len(s):
            if counter == 0:
                operator = 1
            elif counter == numRows - 1:
                operator = -1
            counter = counter + operator
            hash_map[counter].append(s[pointer])
            pointer += 1
        
        return_string = ""
        for key in hash_map:
            return_string += "".join(hash_map[key])
        return return_string

if __name__ == '__main__':
    print(Solution().convert("PAYPALISHIRING", 3))
    print(Solution().convert("PAYPALISHIRING", 4))
    print(Solution().convert("A", 1))