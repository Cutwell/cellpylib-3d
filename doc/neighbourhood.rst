Varying the Neighbourhood Size
------------------------------

The size of the cell neighbourhood can be varied by setting the parameter ``r`` when calling the :py:func:`~cellpylib3d.ca_functions3d.evolve3d` and :py:func:`~cellpylib3d.ca_functionsParallel.evolveParallel` functions. The value of ``r`` represents the number of cells to the left and to the right of the cell under consideration. Thus, to get a neighbourhood size of 3, ``r`` should be 1, and to get a neighbourhood size of 7, ``r`` should be 3.
