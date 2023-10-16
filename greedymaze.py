import heapq

def greedy_best_first_search(maze, start, goal, heuristic):
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    queue = [(heuristic(start, goal), start)]
    visited = {start: None}
    
    while queue:
        _, current = heapq.heappop(queue)
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = visited[current]
            return path[::-1]
        
        for move in moves:
            x, y = current
            next_cell = (x + move[0], y + move[1])
            
            if 0 <= next_cell[0] < len(maze) and 0 <= next_cell[1] < len(maze[0]) and maze[next_cell[0]][next_cell[1]] != '#':
                if next_cell not in visited:
                    visited[next_cell] = current
                    priority = heuristic(next_cell, goal)
                    heapq.heappush(queue, (priority, next_cell))
    
    return None

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

maze = []
for i in range(rows):
    row = [' '] * columns
    maze.append(row)

while True:
    blocked = input("Enter the position of a blocked path (x y), or 'done' to finish: ")
    if blocked == 'done':
        break
    x, y = map(int, blocked.split())
    if 0 <= x < rows and 0 <= y < columns:
        maze[x][y] = '#'
    else:
        print("Invalid position. Please try again.")

start_x = int(input("Enter the starting X coordinate: "))
start_y = int(input("Enter the starting Y coordinate: "))
start = (start_x, start_y)

goal_x = int(input("Enter the goal X coordinate: "))
goal_y = int(input("Enter the goal Y coordinate: "))
goal = (goal_x, goal_y)

def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

path = greedy_best_first_search(maze, start, goal, manhattan_distance)
if path:
    print("Path found:")
    for y in range(len(maze)):
        row = ""
        for x in range(len(maze[0])):
            if (x, y) in path:
                row += 'X '
            else:
                row += maze[y][x] + ' '
        print(row)
else:
    print("No path found.")
