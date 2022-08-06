import cellpylib3d


# empty 3d grid
grid = cellpylib3d.init_simple3d(10, 10, 10, val=0) # init empty 3d grid

# oscilating shape from donut
grid[:, [3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7], 4, [4, 5, 6, 3, 7, 3, 7, 3, 7, 4, 5, 6]] = 1

# visualise grid
#cellpylib3d.plot3d(grid, title='3D Game of Life')

# run using GOL ruleset for N timesteps
cellular_automaton = cellpylib3d.evolve3d(
    grid, timesteps=50, neighbourhood='Moore', apply_rule=cellpylib3d.game_of_life_rule_3d)

# animate
cellpylib3d.plot3d_animate(cellular_automaton, title='3D Game of Life', save=True)
