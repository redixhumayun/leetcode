from typing import List
from collections import defaultdict, OrderedDict

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        hash_map = defaultdict(list)
        string_length = len(votes[0])
        for vote in votes:
            for index, char in enumerate(vote):
                hash_map[char].append(string_length - index)
        
        for key in hash_map.keys():
            scores = hash_map[key]
            hash_map[key] = (scores, sum(scores))

        sorted_hash_map = OrderedDict(sorted(hash_map.items(), key=lambda item: item[1][1], reverse=True))
        output_list = []
        for key, value in sorted_hash_map.items():
            output_list.append(key)
        return "".join(output_list)


if __name__ == '__main__':
    print(Solution().rankTeams(["ABC","ACB","ABC","ACB","ACB"]))
    print(Solution().rankTeams(["WXYZ","XYZW"]))
    print(Solution().rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))