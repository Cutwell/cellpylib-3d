def game_of_life_rule_parallel(neighbourhood, c, t):
    """
    Conway's Game of Life, in 3D using 2D parallel layers.

    :param neighbourhood: the current cell's neighbourhood

    :param c: the index of the current cell

    :param t: the current timestep

    :return: the state of the current cell at the next timestep
    """

    # neighbourhood is 3 x 3 x num_layers, so current cell in vertical slice is at z index
    x, y, z = c

    center_cell = neighbourhood[1][1][z]

    # restrict neighbourhood to 3 x 3 x 3, centered on current cell
    neighbourhood = neighbourhood[:, :, z - 1:z + 2]

    total = neighbourhood.sum(-1).sum(-1).sum() -1

    # Rule 1: Any live cell with <3 or >4 neighbours dies.
    if (total < 2 or total > 4) and center_cell == 1:
        return 0
    
    # Rule 2: Any dead cell with 4 neighbours becomes a live cell.
    elif total == 2 and center_cell == 0:
        return 1

    # Rule 3: Any other cell stays in same state
    else:
        return center_cell

def game_of_life_rule_3d(neighbourhood, c, t):
    """
    Conway's Game of Life, in 3D.

    :param neighbourhood: the current cell's neighbourhood

    :param c: the index of the current cell

    :param t: the current timestep

    :return: the state of the current cell at the next timestep
    """

    center_cell = neighbourhood[1][1][1]
    total = neighbourhood.sum(-1).sum(-1).sum() -1

    # Rule 1: Any live cell with <3 or >4 neighbours dies.
    if (total < 2 or total > 4) and center_cell == 1:
        return 0
    
    # Rule 2: Any dead cell with 4 neighbours becomes a live cell.
    elif total == 2 and center_cell == 0:
        return 1

    # Rule 3: Any other cell stays in same state
    else:
        return center_cell