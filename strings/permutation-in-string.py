from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False

        s1_counter = Counter(s1)
        required_counter = len(s1_counter)

        s2_counter = defaultdict(int)
        formed_counter = 0

        left = 0
        for right in range(len(s2)):
            character = s2[right]
            s2_counter[character] += 1

            if s2_counter[character] == s1_counter[character]:
                formed_counter += 1

            while right - left + 1 > k and left <= right:
                left_character = s2[left]
                s2_counter[left_character] -= 1

                if s2_counter[left_character] == 0:
                    del s2_counter[left_character]
                    if left_character in s1_counter:
                        formed_counter -= 1

                left += 1

            if formed_counter == required_counter:
                return True
                
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkInclusion("ab", "eidbaooo"))
    print(solution.checkInclusion("adc", "dcda"))