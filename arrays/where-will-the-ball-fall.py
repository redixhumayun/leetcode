from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        balls = [n for n in range(n)]
        for row in range(len(grid)):
            for index, ball in enumerate(balls):
                if ball < 0 or ball > n - 1:
                    #   If the ball is stuck do nothing
                    continue
                col_value = grid[row][ball]
                if col_value == 1:
                    #   Check if this ball will crash into the right wall
                    if ball == n - 1:
                        balls[index] = -1
                        continue

                    #   Check value to the right
                    if grid[row][ball + 1] == -1:
                        balls[index] = -1
                        continue
                    else:
                        balls[index] += 1

                elif col_value == -1:
                    #   Check if this will ball will crash into the left wall
                    if ball == 0:
                        balls[index] = -1
                        continue
                    
                    #   Check the value to the left
                    if grid[row][ball - 1] == 1:
                        balls[index] = -1
                        continue
                    else:
                        balls[index] -= 1
        return balls

if __name__ == "__main__":
    grid = [
        [1, 1, 1, -1, -1],
        [1, 1, 1, -1, -1],
        [-1, -1, -1, 1, 1],
        [1, 1, 1, 1, -1],
        [-1, -1, -1, -1, -1]
    ]
    result = Solution().findBall(grid)
    print(result)

    grid = [
        [-1]
    ]
    result = Solution().findBall(grid)
    print(result)

    grid = [
        [1,1,1,1,1,1],
        [-1,-1,-1,-1,-1,-1],
        [1,1,1,1,1,1],
        [-1,-1,-1,-1,-1,-1]
    ]
    result = Solution().findBall(grid)
    print(result)