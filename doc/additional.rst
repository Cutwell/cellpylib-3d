Additional Features
-------------------

Custom Rules
~~~~~~~~~~~~

A rule is a callable that contains the logic that will be applied to each cell of the CA at each timestep. Any kind of callable is valid, but the callable must accept 3 arguments: ``n``, ``c`` and ``t``. Furthermore, the callable must return the state of the current cell at the next timestep. 

:py:class:`~cellpylib3d.ca_functions3d.evolve3d`
The ``n`` argument is the neighbourhood, which is a NumPy array of length `(2r + 1, 2r + 1, 2r + 1)` representing the state of the neighbourhood of the cell, where ``r`` is the neighbourhood radius. The state of the current cell will always be located at the "center" of the neighbourhood. The ``c`` argument is the cell identity, which is a scalar representing the index of the cell in the cellular automaton array. Finally, the ``t`` argument is an integer representing the time step in the evolution.

:py:class:`~cellpylib3d.ca_functionsParallel.evolveParallel`
The ``n`` argument is the neighbourhood, which is a NumPy array of length `(2r + 1, 2r + 1, num_layers)` representing the state of the neighbourhood of the cell, where ``r`` is the neighbourhood radius and ``num_layers`` is the number of layers used in the automata. The state of the current cell can be located from the ``z`` component of the cell coordinates ``c``. The ``c`` argument is the cell identity, which is a scalar representing the index of the cell in the cellular automaton array. Finally, the ``t`` argument is an integer representing the time step in the evolution.

Any kind of callable is supported, and this is particularly useful if more complex handling, like statefulness, is required by the rule. For complex rules, the recommended approach is to define a class for the rule, which provides a ``__call__`` function which accepts the ``n``, ``c``, and ``t`` arguments. Using the base CellPyLib library, the :py:class:`~cellpylib.ca_functions.BaseRule` class is provided for users to extend, which ensures that the custom rule is implemented with the correct ``__call__`` signature.

As an example, below is a custom rule that simply keeps track of how many times each cell has been invoked:

.. code-block::

    import cellpylib as cpl
    import cellpylib3d as cpl3d
    from collections import defaultdict

    class CustomRule(cpl.BaseRule):

        def __init__(self):
            self.count = defaultdict(int)

        def __call__(self, n, c, t):
            self.count[c] += 1
            return self.count[c]

    rule = CustomRule()

    cellular_automaton = cpl3d.init_simple3d(10, 10, 10)

    cellular_automaton = cpl3d.evolve3d(cellular_automaton, timesteps=10,
                                    apply_rule=rule)
