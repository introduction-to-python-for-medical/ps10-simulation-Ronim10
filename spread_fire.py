import copy


def spread_fire(grid):
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:
                neighbors = []
                if i > 0:
                    neightbors.append(grid[i-1][j])
                if i < grid_size -1:
                    neightbors.append(grid[i+1][j])
                if j > 0:
                    neightbors.append(grid[i][j-1])
                if j < grid_size -1:
                    neightbors.append(grid[i][j+1])
                if 2 in neighbors:
                    update_grid[i][j] = 2

    rreturn update_grid

    return update_grid

