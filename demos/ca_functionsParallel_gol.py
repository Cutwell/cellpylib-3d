import cellpylib3d


# empty 3d grid
grid = cellpylib3d.init_simple3d(10, 10, 7, val=0) # init empty 3d grid

# oscilating shape from donut
grid[:, [3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7], 4, [4, 5, 6, 3, 7, 3, 7, 3, 7, 4, 5, 6]] = 1

# each layer requires a separate rule
rules = [cellpylib3d.game_of_life_rule_parallel,] * 7

# visualise grid
#cellpylib3d.plotParallel(grid, title='3D Game of Life')

# run using GOL ruleset for N timesteps
cellular_automaton = cellpylib3d.evolveParallel(
    grid, timesteps=50, neighbourhood='Moore', apply_rules=rules)

# animate
cellpylib3d.plotParallel_animate(cellular_automaton, title='Parallel Game of Life', save=True)
