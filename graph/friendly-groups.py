from collections import deque, defaultdict

def can_be_divided(num_of_people, dislike1, dislike2):
    """
    Args:
     num_of_people(int32)
     dislike1(list_int32)
     dislike2(list_int32)
    Returns:
     bool
    """
    # Write your code here.
    #   Build adjacency list
    adj_list = defaultdict(list)
    for i in range(len(dislike1)):
        adj_list[dislike1[i]].append(dislike2[i])
        adj_list[dislike2[i]].append(dislike1[i])
    
    #   Create the two possible lists
    list_a = []
    list_b = []

    seen = set()

    def bfs(node):
        queue = deque([node])
        while len(queue) > 0:
            current_node = queue.popleft()

            #   Check which list this can be added to
            if len(list_a) == 0:
                list_a.append(current_node)
            elif len(list_b) == 0:
                list_b.append(current_node)

            #   neither list is empty
            #   first check if list_a is viable
            else:
                list_a_flag = True
                for element in list_a:
                    if element in adj_list[current_node]:
                        list_a_flag = False

                if list_a_flag is True:
                    list_a.append(current_node)
                else:
                    list_b_flag = True
                    for element in list_b:
                        if element in adj_list[current_node]:
                            list_b_flag = False

                    if list_b_flag is True:
                        list_b.append(current_node)
                    else:
                        #   This node cannot be added to either list
                        return False

            for neighbour in adj_list[current_node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    queue.append(neighbour)
        return True

    #   Perform a BFS on the graph
    for i in range(num_of_people):
        result = bfs(i)
        if result is False:
            return False

    return True



if __name__ == "__main__":
    num_of_people = 5
    dislike1 = [0, 1, 1, 2, 3]
    dislike2 = [2, 2, 4, 3, 4]
    print(can_be_divided(num_of_people, dislike1, dislike2))

    num_of_people = 4
    dislike1 = [0, 0, 0, 1, 2]
    dislike2 = [1, 2, 3, 2, 3]
    print(can_be_divided(num_of_people, dislike1, dislike2))