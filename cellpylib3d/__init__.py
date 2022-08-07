"""
CellPyLib3D
=========

CellPyLib3D is an extension of CellPyLib, enabling multi-layer cellular automaton.

For complete documentation, see: https://github.com/Cutwell/cellpylib-3d
"""

__version__ = "1.0.1"

from .ca_functions3d import evolve3d, init_random3d, init_simple3d, plot3d, plot3d_animate

from .ca_functionsParallel import evolveParallel, plotParallel, plotParallel_animate

from .ca_rules import game_of_life_rule_3d, game_of_life_rule_parallel