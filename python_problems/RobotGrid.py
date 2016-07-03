from TraceCalls import TraceCalls

def in_bounds(maze, r, c):
    return r >= 0 and c >= 0 and r < len(maze) and c < len(maze[0]) and maze[r][c] == 1


def robot_grid(maze):
    """
    Given a maze, find all paths from start to finish moving only down and right. A 1 in the maze
    means the position is accessible.
    :param maze: an N*M matrix where 1 means the cell is accessible.
    :return:
    """
    end = len(maze) - 1, len(maze[0]) - 1
    start = (0,0)
    results = []

    def traverse(position, cur_path):
        if position == start:
            results.append([start] + cur_path)
        elif in_bounds(maze, *position):
            adj_left = position[0],position[1]-1
            adj_top = position[0]-1, position[1]
            left_path = [position] + cur_path
            top_path = [position] + cur_path
            traverse(adj_left,left_path)
            traverse(adj_top,top_path)

    traverse(end, [])
    return results


def robot_grid_count_paths(maze):
    """
    Given a maze, find the number of paths from start to finish moving only down and right. A 1 in the maze
    means the position is accessible.
    :param maze: an N*M matrix where 1 means the cell is accessible.
    :return:
    """
    end = len(maze) - 1, len(maze[0]) - 1
    start = (0,0)
    cache = dict()

    @TraceCalls()
    def traverse(position):
        if position in cache:
            return cache[position]
        if position == start:
            return 1
        elif in_bounds(maze, *position):
            adj_left = position[0],position[1]-1
            adj_top = position[0]-1, position[1]
            cache[position] = traverse(adj_left) + traverse(adj_top)
            return cache[position]
        else:
            return 0

    return traverse(end)

def robot_grid_is_there_path(maze):
    """
    Given a maze, find the number of paths from start to finish moving only down and right. A 1 in the maze
    means the position is accessible.
    :param maze:
    :return:
    """
    end = len(maze)-1,len(maze[0])-1
    start = (0,0)
    cache = dict()
    @TraceCalls()
    def traverse(position):
        if position in cache:
            return cache[position]
        if in_bounds(maze, *position):
            if position == start:
                return True
            cache[position] = traverse((position[0]-1,position[1])) or traverse((position[0],position[1]-1))
            return cache[position]
        else:
            return False
    return traverse(end)

N = 3
maze = [[1 for i in range(N)] for j in range(N)]
print(maze)
print(robot_grid(maze))