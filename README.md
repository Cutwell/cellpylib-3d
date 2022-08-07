# CellPyLib 3D

CellPyLib is a library for working with 1- and 2-dimensional _k_-color Cellular Automata in Python. CellPyLib-3d is an extension of this library, bringing support for 3-dimensional and 2-dimensional layered automata.

[![testing status](https://github.com/Cutwell/cellpylib-3d/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/Cutwell/cellpylib-3d/actions)
[![latest version](https://img.shields.io/pypi/v/cellpylib3d?style=flat-square&logo=PyPi&logoColor=white&color=blue)](https://pypi.org/project/cellpylib3d/)

Example usage:

```python
import cellpylib3d

# empty 3d grid
grid = cellpylib3d.init_simple3d(10, 10, 10, val=0) # init empty 3d grid

# oscilating shape from donut
grid[:, [3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7], 4, [4, 5, 6, 3, 7, 3, 7, 3, 7, 4, 5, 6]] = 1

# run using GOL ruleset for N timesteps
cellular_automaton = cellpylib3d.evolve3d(grid, timesteps=50, neighbourhood='Moore', apply_rule=cellpylib3d.game_of_life_rule_3d)

# animate
cellpylib3d.plot3d_animate(cellular_automaton, title='3D Game of Life')

```

![](/resources/3d_gol.gif)


```python
import cellpylib3d

# empty 3d grid
grid = cellpylib3d.init_simple3d(10, 10, 7, val=0) # init empty 3d grid

# oscilating shape from donut
grid[:, [3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7], 4, [4, 5, 6, 3, 7, 3, 7, 3, 7, 4, 5, 6]] = 1

# each layer requires a separate rule
rules = [cellpylib3d.game_of_life_rule_parallel,] * 7

# run using GOL ruleset for N timesteps
cellular_automaton = cellpylib3d.evolveParallel(grid, timesteps=50, neighbourhood='Moore', apply_rules=rules)

# animate
cellpylib3d.plotParallel_animate(cellular_automaton, title='Parallel Game of Life')

```

![](/resources/parallel_gol.gif)

## Getting Started

CellPyLib can be installed via pip:

`pip install cellpylib3d`

Requirements for using this library are Python 3.7, NumPy, and Matplotlib. This extension library largely followsHave a look at the documentation, located at [cellpylib.org](https://cellpylib.org), for more information.


## 3D extensions

![](/resources/random_3d_gol.gif)

**Initialising 3d automata**
Arguments for tabled functions mirror 2d equivalent CellPyLib `init_simple2d` and `init_random2d` functions, unless noted.

| Func | Special Args | Docs |
|:---:|:---:|:---:|
| `init_simple3d` | Requires additional `layers` arg. | Returns a matrix initialized with zeroes, with its center value set to the specified value, or 1 by default. |
| `init_random3d` |  Requires additional `layers` arg. | Returns a randomly initialized matrix with values consisting of numbers in {0,...,k - 1}, where k = 2 by default. |

**Evolving**
Arguments for tabled functions mirror 2d equivalent CellPyLib `evolve2d` function.

| Func | Docs |
|:---:|:---:|
| `evolve3d` | Evolve cellular automata in 3-dimensional space using 3d-aware ruleset. |

**Plotting**
Arguments for tabled functions mirror 2d equivalent CellPyLib `plot2d` and `plot2d_animate` functions, unless noted

| Func | Special Args | Docs |
|:---:|:---:|:---:|
| `plot3d` | Replaces `cmap` argument with options for voxel cube face color and edge color (defaults `face_color='#1f77b4'`, `edge_color='gray'`) | Plot 3d CA at given timestep using voxels. |
| `plot3d_animate` | Replaces `cmap` argument with options for voxel cube face color and edge color (defaults `face_color='#1f77b4'`, `edge_color='gray'`) | Animate 3d CA using voxels. |

## Parallel extensions

![](/resources/random_parallel_gol.gif)

Parallel CA are a more customisable form of 3d CA. Instead of applying a single 3d-aware ruleset to an entire CA, each layer of a parallel CA can have a seperate ruleset. This can be helpful for simulations with weak interaction between layers.

**Initialising parallel automata**
Initialise your CA using the 3d functions described above. Parallel CA are treated at regular 3d shapes at a base level.

**Evolving**
Arguments for tabled functions mirror 2d equivalent CellPyLib `evolve2d` function.

| Func | Docs |
|:---:|:---:|
| `evolveParallel` | Evolve a layers of a 3d cellular automata using seperate 2D/3d-aware rulesets. |

**Plotting**
Arguments for tabled functions mirror 2d equivalent CellPyLib `plot2d` and `plot2d_animate` functions.

| Func | Docs |
|:---:|:---:|
| `plotParallel` | Slice the 3D CA and subplot each layer for a given timestep. |
| `plotParallel_animate` | Slice the 3D CA and animate each subplot of each layer. |

--------------------
## Development

Create a Conda environment from the provided environment YAML file:
```
$ conda env create -f environment.yml
```

**Documentation**

To build the Sphinx documentation locally, from the `doc` directory:
```
$ make clean html
```
The generated files will be in `_build/html`.

To build the documentation for publication, from the `doc` directory:
```
$ make github
```
The generated files will be in `_build/html` and in the `site/docs` folder.

**Testing**

There are a number of unit tests for this project. To run the tests:
```
$ python3 -m pytest tests
```

If the `pytest-cov` package is installed, a coverage report can be generated by running the tests with:
```
$ python3 -m pytest tests/ --cov=cellpylib3d
```
--------------------

## License
[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)
