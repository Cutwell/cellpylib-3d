import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.collections as mcoll
import matplotlib.ticker as ticker

def plot3d(ca, timestep=-1, title='', face_color='#1f77b4', edge_color='gray', shade=False, show_grid=False, show_margin=True, scale=0.6, show=True, show_axis=False):
    """
    Plots the state of the given 3D cellular automaton at the given timestep. If no timestep is provided, then the last timestep is plotted.
    The `show_margin` argument controls whether or not a margin is displayed in the resulting plot. When `show_margin` is set to `False`, then the plot takes up the entirety of the window. The `scale` argument is only used when the `show_margins` argument is `False`. It controls the resulting scale (i.e. relative size) of the image when thereare no margins.

    :param ca: the 3D cellular automaton to plot

    :param timestep: the timestep of interest

    :param title: the title to place on the plot

    :param face_color: HTML color code for voxel faces (default '#1f77b4') (supports alpha channel, e.g.: '#1f77b430')

    :param edge_color: HTML color code for voxel edges (default 'gray')

    :param shade: whether to shade the voxels (default False)

    :param show_grid: whether to display a grid (default is False)

    :param show_margin: whether to display the margin (default is True)

    :param scale: the scale of the figure (default is 0.6)

    :param show: show the plot (default is True)

    :param show_axis: show the axis (default is False)

    """

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    plt.title(title)

    if not show_axis:
        ax.xaxis.set_major_locator(ticker.NullLocator())
        ax.yaxis.set_major_locator(ticker.NullLocator())
        ax.zaxis.set_major_locator(ticker.NullLocator())
    else:
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")

    if not show_margin:
        fig.subplots_adjust(left=0, bottom=0, right=1,
                            top=1, wspace=0, hspace=0)

    ax.grid(show_grid)

    ax.voxels(ca[timestep], facecolors=face_color,
              edgecolors=edge_color, shade=shade)

    if show:
        plt.show()


def plot3d_animate(ca, title='evolved', face_color='#1f77b4', edge_color='gray', shade=False, show_grid=False, show_margin=True, scale=0.6, dpi=80, interval=100, save=False, autoscale=False, show=True, show_axis=False):
    """
    Animate the given 3D cellular automaton.
    The `show_margin` argument controls whether or not a margin is displayed in the resulting plot. When `show_margin` is set to `False`, then the plot takes up the entirety of the window. The `scale` argument is only used when the `show_margins` argument is `False`. It controls the resulting scale (i.e. relative size) of the image when there are no margins.
    The `dpi` argument represents the dots per inch of the animation when it is saved. There will be no visible effect of the `dpi` argument if the animation is not saved (i.e. when `save` is `False`).

    :param ca:  the 3D cellular automaton to animate

    :param title: the title to place on the plot (default is "")

    :param face_color: HTML color code for voxel faces (default '#1f77b4') (supports alpha channel, e.g.: '#1f77b430')

    :param edge_color: HTML color code for voxel edges (default 'gray')

    :param shade: whether to shade the voxels (default False)

    :param colormap: the color map to use (default is "Greys")

    :param show_grid: whether to display a grid (default is False)

    :param show_margin: whether to display the margin (default is True)

    :param scale: the scale of the figure (default is 0.6)

    :param dpi: the dots per inch of the image (default is 80)

    :param interval: the delay between frames in milliseconds (default is 50)

    :param save: whether to save the animation to a local file (default is False)

    :param save_path: file path to save animation to (default is 'evolved.gif')

    :param autoscale: whether to autoscale the images in the animation; this should be set to True if the first frame has a uniform value (e.g. all zeroes) (default is False)

    :param show: show the plot (default is True)

    :param show_axis: show the axis (default is False)

    :param imshow_kwargs: keyword arguments for the Matplotlib `imshow` function

    :return: the animation
    """

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if not show_margin:
        fig.subplots_adjust(left=0, bottom=0, right=1,
                            top=1, wspace=0, hspace=0)

    if not show_axis:
        ax.xaxis.set_major_locator(ticker.NullLocator())
        ax.yaxis.set_major_locator(ticker.NullLocator())
        ax.zaxis.set_major_locator(ticker.NullLocator())
    else:
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")

    ax.set_title(title)

    ax.grid(show_grid)
    ax.voxels(ca[0], facecolors=face_color, edgecolors=edge_color, shade=shade)

    def update(i, ca):
        ax.clear()
        ax.collections.clear()

        if not show_axis:
            ax.xaxis.set_major_locator(ticker.NullLocator())
            ax.yaxis.set_major_locator(ticker.NullLocator())
            ax.zaxis.set_major_locator(ticker.NullLocator())
        else:
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_zlabel("z")

        ax.set_title(title)

        ax.grid(show_grid)
        vox = ax.voxels(ca[i], facecolors=face_color,
                        edgecolors=edge_color, shade=shade)

    ani = animation.FuncAnimation(fig, update, fargs=(
        ca,), frames=len(ca), interval=interval, blit=False)

    if save:
        ani.save(f"{title}.gif", dpi=dpi, writer="imagemagick")

    if show:
        plt.show()

    return ani


def evolve3d(
    cellular_automaton, timesteps, apply_rule, r=1, neighbourhood="Moore"
):
    """Evolve cellular automata in 3-dimensional space using 3d-aware ruleset.

    :param cellular_automaton: a 3D cellular automaton numpy array.

    :param timesteps: the number of timesteps to evolve the cellular automata for.

    :param apply_rule: the ruleset to apply to each layer (provides layer index, to allow for different behaviour per layer).

    :param r: the radius of the neighbourhood.

    :param neighbourhood: the neighbourhood type to use.

    """

    von_neumann_mask = np.zeros((2 * r + 1, 2 * r + 1, 2 * r + 1), dtype=bool)

    for i in range(len(von_neumann_mask)):
        mask_size = np.absolute(r - i)

        von_neumann_mask[i][:mask_size][:mask_size] = 1

        if mask_size != 0:
            von_neumann_mask[i][-mask_size:][:-mask_size] = 1

    _, rows, cols, layers = cellular_automaton.shape
    neighbourhood_indices = _get_neighbourhood_indices(rows, cols, layers, r)

    # TODO: add dynamic evolution option
    return _evolve3d_fixed(
        cellular_automaton,
        timesteps,
        apply_rule,
        neighbourhood,
        rows,
        cols,
        layers,
        neighbourhood_indices,
        von_neumann_mask,
        r,
    )


def _evolve3d_fixed(
    cellular_automaton,
    timesteps,
    apply_rule,
    neighbourhood,
    rows,
    cols,
    layers,
    neighbourhood_indices,
    von_neumann_mask,
    r,
):
    """ Evolves 3d cellular automaton for a fixed of timesteps.

    :param cellular_automaton: a 3D cellular automaton numpy array.

    :param timesteps: the number of timesteps to evolve the cellular automata for.

    :param apply_rule: the ruleset to apply to each layer (can simulate different rules per layer using layer index).

    :param neighbourhood: the neighbourhood type to use.

    :param r: the radius of the neighbourhood.

    :param neighbourhood_indices: the neighbourhood indices for each cell.

    :param von_neumann_mask: the von neumann mask for the neighbourhood.

    :param cell_indices: the cell indices for each cell.

    :param cell_idx_to_neigh_idx: the cell indices to neighbourhood indices mapping.

    :param r: the radius of the neighbourhood.

    """

    initial_conditions = cellular_automaton[-1]

    array = np.zeros((timesteps, rows, cols, layers),
                     dtype=cellular_automaton.dtype)

    array[0] = initial_conditions

    for t in range(1, timesteps):
        generation = array[t - 1]

        for row, cell_row in enumerate(generation):
            for col, cell_col in enumerate(cell_row):
                for layer, cell_layer in enumerate(cell_col):

                    n = _get_neighbourhood(
                        generation, neighbourhood_indices, row, col, layer, neighbourhood, von_neumann_mask)

                    array[t][row][col][layer] = apply_rule(
                        n, (row, col, layer), t)

    return np.concatenate((cellular_automaton, array[1:]), axis=0)


def _get_neighbourhood_indices(rows, cols, layers, r):
    """
    Returns a dictionary mapping the coordinates of a cell in a 3D CA to its neighbourhood indices.

    :param layers: the number of layers in the 3D CA

    :param rows: the number of rows in the 3D CA

    :param cols: the number of columns in the 3D CA

    :param r: the radius of the neighbourhood

    :return: a dictionary, where the key is a 3-tuple, (row, col, layer), and the value is a 3-tuple, (row_indices, col_indices, layer_indices)

    """

    indices = {}

    for row in range(rows):
        for col in range(cols):
            for layer in range(layers):

                layer_indices = range(layer - r, layer + r + 1)
                layer_indices = [i - layers if i >
                                 (layers - 1) else i for i in layer_indices]

                row_indices = range(row - r, row + r + 1)
                row_indices = [i - rows if i >
                               (rows - 1) else i for i in row_indices]

                col_indices = range(col - r, col + r + 1)
                col_indices = [i - cols if i >
                               (cols - 1) else i for i in col_indices]

                indices[(row, col, layer)] = (
                    row_indices, col_indices, layer_indices)

    return indices


def _get_neighbourhood(cell_layer, neighbourhood_indices, row, col, layer, neighbourhood, von_neumann_mask):
    """
    Returns the cell neighbourhood for the cell given by the row and column and layer index. If the neighbourhood is `von Neumann`, then an appropriately masked array is returned.

    :param cell_layer: an array with dimensions 2r+1 x 2r+1 x 2r+1

    :param neighbourhood_indices: a 3-tuple containing the row and column and layer indices of the neighbours of the cell given by the row and column index

    :param layer: the layer index of the cell

    :param row: the row index of the cell

    :param col: the column index of the cell

    :param neighbourhood: the neighbourhood type

    :param von_neumann_mask: a boolean array with dimensions 2r+1 x 2r+1 x 2r+1 representing which cells in the neighbourhood should be masked

    :return: a 2r+1 x 2r+1 x 2r+1 array representing the cell neighbourhood of the cell given by row and col, if the neighbourhood type is `von Neumann`, then the array will be masked
    """

    row_indices, col_indices, layer_indices = neighbourhood_indices[(
        row, col, layer)]

    n = cell_layer[np.ix_(row_indices, col_indices, layer_indices)]

    if neighbourhood == 'Moore':
        return n

    elif neighbourhood == 'von Neumann':
        return np.ma.masked_array(n, von_neumann_mask)

    else:
        raise ValueError('unknown neighbourhood type: %s' % neighbourhood)


def init_simple3d(rows, cols, layers, val=1, dtype=np.int32, coords=None):
    """
    Returns a matrix initialized with zeroes, with its center value set to the specified value, or 1 by default.
    If the `coords` argument is specified, then the specified cell at the given coordinates will have its value set to `val`, otherwise the center cell will be set.

    :param layers: the number of layers in the matrix

    :param rows: the number of rows in the matrix

    :param cols: the number of columns in the matrix

    :param val: the value to be used in the center of the matrix (1, by default)

    :param dtype: the data type (np.int32 by default)

    :param coords: a 2-tuple specifying the row and column of the cell to be initialized (None by default)

    :return: a tensor with shape (1, rows, cols), with the center value initialized to the specified value, or 1 by default
    """
    x = np.zeros((rows, cols, layers), dtype=dtype)

    if coords is not None:
        if not isinstance(coords, (tuple, list)) or len(coords) != 3:
            raise TypeError("coords must be a list or tuple of length 3 (x, y, z)")

        x[coords[0]][coords[1]][coords[2]] = val

    else:
        x[x.shape[0]//2][x.shape[1]//2][x.shape[2]//2] = val

    return np.array([x])


def init_random3d(rows, cols, layers, k=2, dtype=np.int32):
    """
    Returns a randomly initialized matrix with values consisting of numbers in {0,...,k - 1}, where k = 2 by default.
    If dtype is not an integer type, then values will be uniformly distributed over the half-open interval [0, k - 1).

    :param layers: the number of layers in the matrix

    :param rows: the number of rows in the matrix

    :param cols: the number of columns in the matrix

    :param k: the number of states in the cellular automaton (2, by default)

    :param dtype: the data type

    :return: a tensor with shape (1, rows, cols, layers), randomly initialized with numbers in {0,...,k - 1}

    """

    if np.issubdtype(dtype, np.integer):
        rand_nums = np.random.randint(
            k, size=(rows, cols, layers), dtype=dtype)

    else:
        rand_nums = np.random.uniform(
            0, k - 1, size=(rows, cols, layers)).astype(dtype)

    return np.array([rand_nums])
