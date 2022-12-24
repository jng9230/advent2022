def is_visible(row, col, grid):
    """
    returns True if the tree at the specified row and column 
    is visible. False otherwise.
    """

    def check(row, col, row_delta, col_delta):
        """
        traverses the given grid based on deltas and 
        returns True if tree is visible from that direction
        """
        height0 = grid[row][col]
        while row > 0 and row < len(grid)-1 and col > 0 and col < len(grid[0])-1:
            row += row_delta 
            col += col_delta 
            if grid[row][col] >= height0:
                return False 

        return True

    left = check(row, col, -1, 0)
    right = check(row, col, 1, 0)
    bottom = check(row, col, 0, -1)
    top = check(row, col, 0, 1)
        
    return left or right or bottom or top

def parse():
    grid = []
    to_int = lambda x : int(x)
    with open('8-input.txt', 'r') as f:
        for line in f: 
            grid.append(list(map(to_int,list(line)[:-1])))#[-1] to drop the newline
    return grid 

def solve():
    """
    """
    grid = parse()

    """
    -for each block:
        -try to find a block of higher height in any direction
        - O(Nm + Nk), where N = num_blocks and m,k = num rows, cols
    """
    count = 0 
    for row in range(1, len(grid)-1):#start later and end earlier to skip edge trees
        for col in range(1, len(grid[0])-1):
            count += 1 if is_visible(row, col, grid) else 0

    count += len(grid)*2 + len(grid[0])*2 - 4#add edge trees, -4 as we double count corners

    return count

def get_score(row, col, grid):
    """
    Compute the "scenic score" of the `grid's` specific `row` and `column`.
    The scenic score is the multiple of the number trees visible
    from each direction (left, right, up, down).
    """
    def check(row, col, row_delta, col_delta):
        """
        Traverses the given grid based on deltas. Returns the number of 
        trees visible traveling along that direction
        """
        height0 = grid[row][col]
        count = 1 #at least is always visible (the immediate tree)
        row += row_delta 
        col += col_delta 
        while row > 0 and row < len(grid)-1 and col > 0 and col < len(grid[0])-1:
            if grid[row][col] >= height0: #break if sightline is blocked
                break
            row += row_delta 
            col += col_delta 
            count += 1

        return count

    left = check(row, col, 0, -1)
    right = check(row, col, 0, 1)
    bottom = check(row, col, 1, 0)
    top = check(row, col, -1, 0)
    
    # print(f"{row},{col}:\nleft:{left}")
    # print(f"right:{right}")
    # print(f"bottom:{bottom}")
    # print(f"top:{top}")
    # print(f"overall:{left*right*bottom*top}\n")
    return left*right*bottom*top

def solve2():
    grid = parse()
    max_score = 0 
    for row in range(1, len(grid)-1):#start later and end earlier to skip edge trees
        for col in range(1, len(grid[0])-1):
            max_score = max(max_score, get_score(row, col, grid))

    return max_score

if __name__ == "__main__":
    print(solve())
    print(solve2())