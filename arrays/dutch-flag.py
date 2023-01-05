from enum import Enum

class Color(Enum):
    RED = 'R'
    GREEN = 'G'
    BLUE = 'B'

def dutch_flag_sort(balls):
    """
    Args:
     balls(list_char)
    Returns:
     list_char
    """
    #   Solution using Lomuto's partitioning
    # blue = 0
    # green = red = -1
    # while blue < len(balls):
    #     if balls[blue] == Color.RED.value:
    #         green += 1
    #         balls[green], balls[blue] = balls[blue], balls[green]

    #         red += 1
    #         balls[red], balls[green] = balls[green], balls[red]
    #     elif balls[blue] == Color.GREEN.value:
    #         green += 1
    #         balls[green], balls[blue] = balls[blue], balls[green]
    #     blue += 1
    # return balls
    
    #   Solution using Hoare's partitioning
    #   Hoare's partitioning uses two pointers at the end one runner pointer
    blue = len(balls) - 1
    green = red = 0
    while green <= blue:
        if balls[green] == Color.RED.value:
            balls[green], balls[red] = balls[red], balls[green]
            red += 1
            green += 1
        elif balls[green] == Color.BLUE.value:
            balls[green], balls[blue] = balls[blue], balls[green]
            blue -= 1
        else:
            green += 1
    return balls


if __name__ == '__main__':
    print(dutch_flag_sort(['R', 'G', 'B', 'R', 'B']))
    # print(dutch_flag_sort(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
    # print(dutch_flag_sort(["G", "B", "G", "G", "R", "B", "R", "G"]))
    # print(dutch_flag_sort(["B", "G", "G", "R", "B", "G", "G", "R"]))
    # print(dutch_flag_sort(["R", "R", "G", "B", "B", "B", "B", "R", "G", "G", "G", "G"]))
    print(dutch_flag_sort(["G", "R"]))