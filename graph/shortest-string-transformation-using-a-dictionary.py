from collections import defaultdict, deque

def string_transformation(words, start, stop):
    """
    Args:
     words(list_str)
     start(str)
     stop(str)
    Returns:
     list_str
    """
    # Write your code here.

    #   Put words in a hash map to make existence checking O(1)
    #   O(n)
    words_hash_map = {}
    for word in words:
        words_hash_map[word] = 0

    #   Create an adjacency list
    #   O(len(start) * len(words))
    adj_list = defaultdict(list)
    for index, char in enumerate(start):
        for word in words:
            if char != word[index] and word[index] not in adj_list[index]:
                adj_list[index].append(word[index])

    queue = deque([(start, [start])])
    seen = set()

    #   O(V+E) where V is the number of indexes where the two strings differ and E is the number of 
    #   edges

    while len(queue) > 0:
        word, output = queue.popleft()

        if word == stop:
            return output

        for index, char in enumerate(word):
            current_character = char
            desired_character = stop[index]
            if current_character != desired_character:
                new_word = word[:index] + desired_character + word[index + 1:]
                if new_word == stop:
                    output.append(stop)
                    return output

                for neighbour in adj_list[index]:
                    new_word = word[:index] + neighbour + word[index + 1:]
                    if new_word not in seen:
                        seen.add(new_word)
                        output.append(new_word)
                        queue.append((new_word, output[:]))
                        output.pop()
    return ["-1"]

if __name__ == "__main__":
    words = ["cat", "hat", "bad", "had"]
    start = "bat"
    stop = "had"
    print(string_transformation(words, start, stop))

    words = []
    start = "bbb"
    stop = "bbc"
    print(string_transformation(words, start, stop))

    words = []
    start = "zzzzzz"
    stop = "zzzzzz"
    print(string_transformation(words, start, stop))

    words = ["hot","dot","dog","lot","log","cog"]
    start = "hit"
    stop = "cog"
    print(string_transformation(words, start, stop))