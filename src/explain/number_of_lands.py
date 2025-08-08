def find_number_of_lands(self, grid):
    num = 2
    for x in range(0, len(grid)):
        for y in range(0, len(grid[x])):
            if (grid[x][y] == 1):
                num += 1
                _mark_neighboring_lands(grid, x, y, num)

    return num - 2

def _mark_neighboring_lands(grid, x, y, num):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 1:
        return
    grid[x][y] = num
    _mark_neighboring_lands(grid, x - 1, y, num)
    _mark_neighboring_lands(grid, x + 1, y, num)
    _mark_neighboring_lands(grid, x, y - 1, num)
    _mark_neighboring_lands(grid, x, y + 1, num)