"""
attempting dijkstra's to solve d12 rather than DFS
- use the prio queue version to find min distances
-> cuts times from >5min to ~4sec
"""
import heapq

def elev(e):
    """
    Returns the elevation of specfied character `e`.
    - 'a' is 1 and 'z' is 26
    - "S" is 1 and "E" is 26
    """
    if e == "S":
        return 1
    if e == "E":
        return 26 
    return ord(e) - 96

def dijkstra(start, grid):
    """
    Returns the distance from `start`, a tuple of x,y coords,
    to ending point "E"
    """
    dist = {}   #kinda useless but helps to check if it's a valid
                #square later on
    seen = set()
    queue = []
    heapq.heapify(queue)
    source = start #(x,y) of "S"
    heapq.heappush(queue, (0, source))
    end = None #(x,y) of "E"
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            dist[(x,y)] = -1 #arbitary value
            if grid[y][x] == "E":
                end = (x, y)

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        u_dist, u = heapq.heappop(queue)

        if u not in seen:
            seen.add(u)
            if u == end:
                return u_dist
            for x1, y1 in dirs:
                v = (u[0] + x1, u[1] + y1)
                if v in dist: #is valid haha 
                    v_char = grid[v[1]][v[0]]
                    u_char = grid[u[1]][u[0]]
                    if elev(v_char) <= elev(u_char) + 1:
                        heapq.heappush(queue, (u_dist + 1, v))

def get_start(start_char, grid):
    start = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == start_char:
                start.append((x,y))
    return start

def parse():
    with open("12-input.txt", "r") as f:
        grid = f.read().split("\n")
    return grid

def solve():
    """
    Find shortest path from "S" to "E"
    """
    grid = parse()
    return dijkstra(get_start("S", grid)[0], grid)

def solve2():
    """
    Find shortest path from any "a" to "E"
    - can add code to include "S", but can also just 
    manually input S-E distance if min(a,E) is greater 
    than w/e `solve()` returns.
    """
    grid = parse()
    res = [dijkstra(start, grid) for start in get_start("a", grid)]
    return min(i for i in res if i is not None) #filter out Nones

if __name__ == "__main__":
    print(solve())
    print(solve2())