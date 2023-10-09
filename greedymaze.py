import heapq

def greedy_best_first_search(maze, start, goal, heuristic):
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    priority_queue = [(heuristic(start, goal), start)]
    visited = {start: None}
    
    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        
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
                    heapq.heappush(priority_queue, (priority, next_cell))
    
    return None

maze = [
    ['G', ' ', ' ', ' ', ' '],
    [' ', '#', '#', ' ', '#'],
    [' ', '#', ' ', ' ', ' '],
    [' ', ' ', ' ', '#', ' '],
    [' ', ' ', ' ', ' ', 'S'],

]

start = (4, 4)
goal = (0, 0)

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

