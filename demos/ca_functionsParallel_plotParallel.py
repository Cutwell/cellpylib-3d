import cellpylib3d as cpl3d

# empty 3d grid
grid = cpl3d.init_simple3d(10, 10, 10, val=0) # init empty 3d grid

# oscilating shape from donut
grid[:, [3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7], 4, [4, 5, 6, 3, 7, 3, 7, 3, 7, 4, 5, 6]] = 1

# define rules for each layer
rules = [cpl3d.game_of_life_rule_parallel,] * 10

# evolve the CA for 20 time steps, using a 3d adaptation of Conway's Game of Life ruleset
grid = cpl3d.evolveParallel(grid, timesteps=20, apply_rules=rules)

cpl3d.plotParallel(grid)