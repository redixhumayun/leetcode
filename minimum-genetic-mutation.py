from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank) -> int:
        #   Method to find the alternates for a given string
        def alternates(string):
            results = []
            possibilities = ['A', 'C', 'T', 'G']
            for index, character in enumerate(string):
                for possibility in possibilities:
                    new_string = string[:index] + possibility + string[index+1:]
                    if new_string != string:
                        results.append(new_string)
            return results

        #   Convert bank to a set for easy comparison
        bank_set = set()
        for b in bank:
            bank_set.add(b)

        queue = deque()   #   start, steps
        queue.append((startGene, 0))
        seen  = set()
        seen.add(startGene)
        while queue:
            mutation, steps = queue.popleft()
            if mutation == endGene:
                return steps
            for alternate in alternates(mutation):
                if alternate not in seen:
                    seen.add(alternate)
                    if alternate in bank_set:
                    #   This is a valid mutation that has not been seen before
                        queue.append((alternate, steps + 1))

        return -1
                    
            

if __name__ == '__main__':
    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    print(Solution().minMutation(startGene, endGene, bank))