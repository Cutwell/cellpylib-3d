import cellpylib3d as cpl3d

# initialize a 3d CA with 20x20x20 dimensions, randomly initialised with values {0, 1}
cellular_automaton = cpl3d.init_random3d(20, 20, 20, k=2)

# evolve the CA for 100 time steps, using a 3d adaptation of Conway's Game of Life ruleset
cellular_automaton = cpl3d.evolve3d(cellular_automaton, timesteps=20, 
                                apply_rule=cpl3d.game_of_life_rule_3d)

# plot the final generation of the CA evolution
cpl3d.plot3d_animate(cellular_automaton, save=True, title='Random Game of Life')