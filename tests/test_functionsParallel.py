import unittest
import pytest
import matplotlib

import numpy as np
import os

import cellpylib3d as cpl
import warnings

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
matplotlib.use("Agg")

class TestCellularAutomataFunctionsParallel(unittest.TestCase):

    def test_game_of_life_rule(self):
        # load expected array from /resources/donut_5_timesteps.npy
        expected = np.load(os.path.join(os.path.dirname(__file__), "resources", "donut_5_timesteps.npy"))

        cellular_automaton = cpl.init_simple3d(10, 10, 10, val=0)

        rules = [cpl.game_of_life_rule_parallel,] * 10

        # donut
        cellular_automaton[:, [3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7], 4, [4, 5, 6, 3, 7, 3, 7, 3, 7, 4, 5, 6]] = 1

        cellular_automaton = cpl.evolveParallel(cellular_automaton, timesteps=5, neighbourhood='Moore',
                                          apply_rules=rules)

        np.testing.assert_equal(expected, cellular_automaton[-1])

    def test_plotParallel(self):
        # this test ensures that the following code can run successfully without issue
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            cpl.plotParallel(np.array([
                [[[1, 0, 1], [1, 1, 1], [1, 1, 1]]]
            ]), title="some test")

    def test_plotParallel_with_timestep(self):
        # this test ensures that the following code can run successfully without issue
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            cpl.plotParallel(np.array([
                [[[1, 0, 1], [1, 1, 1], [1, 1, 1]]],
                [[[1, 1, 1], [0, 1, 1], [1, 0, 1]]]
            ]), timestep=1, title="some test")

    def test_plotParallel_animate(self):
        # this test ensures that the following code can run successfully without issue
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            cpl.plotParallel_animate(np.array([
                [[[1, 0, 1], [1, 1, 1], [1, 1, 1]]],
                [[[1, 1, 1], [0, 1, 1], [1, 0, 1]]],
                [[[1, 1, 1], [0, 1, 1], [1, 0, 1]]]
            ]), title="some test")
