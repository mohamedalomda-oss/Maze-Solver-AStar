import heapq

# # Maze Solver - CF321 Project 1
# 0 = Empty cell
# 1 = Wall

maze = [
    ["S", 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, "G"],
]


def display_maze(maze):
    for row in maze:
        for cell in row:
            if cell == 1:
                print("#", end=" ")
            else:
                print(cell, end=" ")
        print()


def find_position(maze, target):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == target:
                return (row, col)


def manhattan_distance(position, goal):
    row_distance = abs(position[0] - goal[0])
    col_distance = abs(position[1] - goal[1])
    return row_distance + col_distance


def get_neighbors(maze, position):
    row, col = position
    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1),   # Right
    ]

    neighbors = []
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if (0 <= new_row < len(maze) and 
            0 <= new_col < len(maze[0]) and 
            maze[new_row][new_col] != 1):
            neighbors.append((new_row, new_col))

    return neighbors


def astar_search(maze, start, goal):
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start, goal), start))

    came_from = {}
    g_score = {start: 0}
    visited = set()

    while open_list:
        _, current = heapq.heappop(open_list)

        if current in visited:
            continue

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, len(visited)

        visited.add(current)

        for neighbor in get_neighbors(maze, current):
            if neighbor in visited:
                continue

            tentative_g = g_score[current] + 1

            if tentative_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + manhattan_distance(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))

    return None, len(visited)



start = find_position(maze, "S")
goal = find_position(maze, "G")

print("Maze:")
display_maze(maze)

print("\nStart position:", start)
print("Goal position:", goal)

distance = manhattan_distance(start, goal)
print("Manhattan distance:", distance)

path, explored = astar_search(maze, start, goal)

print("\nA* Search Results:")
if path:
    print("Solution found!")
    print("Path:", path)
    print("Path cost:", len(path) - 1)
    print("Nodes explored:", explored)
else:
    print("No path found!")
