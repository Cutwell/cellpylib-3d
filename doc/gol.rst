Conway's Game of Life in 3D
---------------------------

Conway's Game of Life is a very famous 2D Cellular Automaton. It uses a simple rule to give rise to a complex system that is capable of universal computation, in addition to its ability to entertain and fascinate.

Multiple variations extending this ruleset into 3-dimensions. CellPyLib has a built-in function, :py:func:`~cellpylib.ca_functions3d.game_of_life_rule_3d`, that can be used to produce
the Game of Life 3D CA:

.. code-block::

    import cellpylib3d as cpl3d

    # empty 3d grid
    grid = cpl3d.init_simple3d(10, 10, 10, val=0) # init empty 3d grid

    # oscilating shape from donut
    grid[:, [3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7], 4, [4, 5, 6, 3, 7, 3, 7, 3, 7, 4, 5, 6]] = 1

    # evolve the CA for 20 time steps, using a 3d adaptation of Conway's Game of Life ruleset
    grid = cpl3d.evolve3d(grid, timesteps=20, apply_rule=cpl3d.game_of_life_rule_3d)

    # plot the final generation of the CA evolution
    cpl3d.plot3d_animate(cellular_automaton, save=True, title='Random Game of Life')

.. image:: _static/3d_gol.gif
    :width: 350

**References:**

*Conway, J. (1970). The game of life. Scientific American, 223(4), 4.*
