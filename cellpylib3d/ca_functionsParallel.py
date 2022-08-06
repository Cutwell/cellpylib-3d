from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.collections as mcoll
import matplotlib.ticker as ticker
import numpy as np

from .ca_functions3d import _get_neighbourhood


def plotParallel(ca, timestep=-1, title='', colormap='Greys', show_grid=False, show_margin=True, scale=0.6, show_axis=False, subplot_titles=False, show=True, **imshow_kwargs):
    """
    Plot subplots of each layer of the given 3D cellular automaton at the given timestep. If no timestep is provided, then the last timestep is plotted.

    Generates multiple subplots, one for each parallel layer of the automaton.

    The `show_margin` argument controls whether or not a margin is displayed in the resulting plot. When `show_margin` is set to `False`, then the plot takes up the entirety of the window. The `scale` argument is only used when the `show_margins` argument is `False`. It controls the resulting scale (i.e. relative size) of the image when there are no margins.

    :param ca: the 2D cellular automaton layers to plot

    :param timestep: the timestep of interest

    :param title: the title to place on the plot

    :param colormap: the color map to use (default is "Greys")

    :param scale: the scale of the figure (default is 0.6)

    :param show_grid: whether to display a grid (default is False)

    :param show_margin: whether to display the margin (default is True)

    :param show_axis: whether to display the axis (default is False)

    :param subplot_titles: whether to display the subplot titles (default is False)

    :param show: show the plot (default is True)

    :param imshow_kwargs: keyword arguments for the Matplotlib `imshow` function

    """

    cmap = plt.get_cmap(colormap)

    data = ca[timestep]

    fig, axs = plt.subplots(1, data.shape[2])
    
    fig.suptitle(title)
    
    if not show_margin:
        fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    
    for i, ax in enumerate(axs):
        if subplot_titles:
            ax.set_title('Layer {}'.format(i))

        if not show_axis:
            ax.xaxis.set_major_locator(ticker.NullLocator())
            ax.yaxis.set_major_locator(ticker.NullLocator())

        layer = data[:, :, i]

        _add_grid_lines(layer, ax, show_grid)

        im = ax.imshow(layer, interpolation='none', cmap=cmap, **imshow_kwargs)
    
        if not show_margin:
            baseheight, basewidth = im.get_size()
            fig.set_size_inches(basewidth*scale, baseheight*scale, forward=True)
    
    if show:
        plt.show()


def plotParallel_animate(ca, title='', colormap='Greys', show_grid=False, show_margin=True, scale=0.6, dpi=80,
                         interval=200, save=False, autoscale=False, show=True, show_axis=False, subplot_titles=False, **imshow_kwargs):
    """
    Animate subplots of each layer of the given 3D cellular automaton.

    The `show_margin` argument controls whether or not a margin is displayed in the resulting plot. When `show_margin`
    is set to `False`, then the plot takes up the entirety of the window. The `scale` argument is only used when the
    `show_margins` argument is `False`. It controls the resulting scale (i.e. relative size) of the image when there
    are no margins.

    The `dpi` argument represents the dots per inch of the animation when it is saved. There will be no visible effect
    of the `dpi` argument if the animation is not saved (i.e. when `save` is `False`).

    :param ca:  the 3D cellular automaton to animate

    :param title: the title to place on the plot (default is "")

    :param colormap: the color map to use (default is "Greys")

    :param show_grid: whether to display a grid (default is False)

    :param show_margin: whether to display the margin (default is True)

    :param scale: the scale of the figure (default is 0.6)

    :param dpi: the dots per inch of the image (default is 80)

    :param interval: the delay between frames in milliseconds (default is 50)

    :param save: whether to save the animation to a local file (default is False)

    :param autoscale: whether to autoscale the images in the animation; this should be set to True if the first
                      frame has a uniform value (e.g. all zeroes) (default is False)

    :param show: show the plot (default is True)

    :param imshow_kwargs: keyword arguments for the Matplotlib `imshow` function

    :return: the animation
    """

    cmap = plt.get_cmap(colormap)

    fig, axs = plt.subplots(1, ca.shape[3])
    
    fig.suptitle(title)
    
    if not show_margin:
        fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)

    ims = []
    
    for i, ax in enumerate(axs):
        if subplot_titles:
            ax.set_title('Layer {}'.format(i))

        if not show_axis:
            ax.xaxis.set_major_locator(ticker.NullLocator())
            ax.yaxis.set_major_locator(ticker.NullLocator())
        
        # get 0 frame of i layer
        layer = ca[0, :, :, i]

        _add_grid_lines(layer, ax, show_grid)

        im = ax.imshow(layer, interpolation='none', animated=True, cmap=cmap, **imshow_kwargs)

        ims.append(im)
    
        if not show_margin:
            baseheight, basewidth = im.get_size()
            fig.set_size_inches(basewidth*scale, baseheight*scale, forward=True)

    def updatefig(t):
        for i, im in enumerate(ims):
            # get t frame of i layer
            layer = ca[t, :, :, i]
            ax = axs[i]

            im.set_array(layer)

            _add_grid_lines(layer, ax, show_grid)

            if autoscale:
                im.autoscale()

        return ims
    
    ani = animation.FuncAnimation(
        fig, updatefig, frames=len(ca), interval=interval, blit=True)
    
    if save:
        ani.save(f"{title}.gif", dpi=dpi, writer="imagemagick")
    
    if show:
        plt.show()
    
    return ani


def _add_grid_lines(ca, ax, show_grid):
    """
    Adds grid lines to the plot.
    
    :param ca: the 2D cellular automaton to plot
    
    :param ax: the Matplotlib axis object
    
    :param show_grid: whether to display the grid lines
    
    :return: the grid object
    
    """
    
    grid_linewidth = 0.0

    nx, ny = ca.shape
    
    if show_grid:
        ax.set_xticks(np.arange(-.5, nx, 1), "")
        ax.set_yticks(np.arange(-.5, ny, 1), "")
        ax.tick_params(axis='both', which='both', length=0)
        grid_linewidth = 0.5
    
    vertical = np.arange(-.5, ny, 1)
    horizontal = np.arange(-.5, nx, 1)
    
    lines = ([[(x, y) for y in (-.5, horizontal[-1])] for x in vertical] +
             [[(x, y) for x in (-.5, vertical[-1])] for y in horizontal])
    
    grid = mcoll.LineCollection(lines, linestyles='-', linewidths=grid_linewidth, color='grey')
    
    ax.add_collection(grid)

    return grid


def evolveParallel(
    cellular_automaton, timesteps, apply_rules, neighbourhood="Moore", r=1,
):
    """ Evolve multiple layers in parallel.

    :param cellular_automaton: the layers to evolve

    :param timesteps: the number of timesteps to evolve the layers for

    :param apply_rules: the function to apply the rules to the layers, index corresponding to layer

    :param neighbourhood: the neighbourhood to use (default is "Moore")

    :param r: the radius of the neighbourhood (default is 1)

    """

    # von neumann mask of radius from cell, with full vertical height of layers
    _, rows, cols, layers = cellular_automaton.shape
    von_neumann_mask = np.zeros((2 * r + 1, 2 * r + 1, layers), dtype=bool)

    for i in range(len(von_neumann_mask)):
        mask_size = np.absolute(r - i)
        von_neumann_mask[i][:mask_size][:layers] = 1
        if mask_size != 0:
            von_neumann_mask[i][-mask_size:][:-layers] = 1

    neighbourhood_indices = _get_neighbourhood_indices(rows, cols, layers, r)

    # NOTE: to simplify total copied code, can only run this as fixed number of epochs.
    # TODO: add dynamic evolution.
    return _evolveParallel_fixed(
        cellular_automaton,
        timesteps,
        apply_rules,
        neighbourhood,
        rows,
        cols,
        layers,
        neighbourhood_indices,
        von_neumann_mask,
        r,
    )


def _evolveParallel_fixed(
    cellular_automaton,
    timesteps,
    apply_rules,
    neighbourhood,
    rows,
    cols,
    layers,
    neighbourhood_indices,
    von_neumann_mask,
    r,
):
    """
    Evolves the layers of cellular automaton in parallel for a fixed of timesteps.

    :param cellular_automaton: the layers to evolve

    :param timesteps: the number of timesteps to evolve the layers for

    :param apply_rules: the function to apply the rules to the layers, index corresponding to layer

    :param neighbourhood: the neighbourhood to use (default is "Moore")

    :param r: the radius of the neighbourhood (default is 1)

    :return: the evolved cellular automaton

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
                        generation,
                        neighbourhood_indices,
                        row,
                        col,
                        layer,
                        neighbourhood,
                        von_neumann_mask,
                    )

                    array[t][row][col][layer] = apply_rules[layer](
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

                layer_indices = range(0, layers)    # all layers
                layer_indices = [i - layers if i >
                                 (layers - 1) else i for i in layer_indices]

                row_indices = range(row - r, row + r + 1)   # rows within radius
                row_indices = [i - rows if i >
                               (rows - 1) else i for i in row_indices]

                col_indices = range(col - r, col + r + 1)   # columns within radius
                col_indices = [i - cols if i >
                               (cols - 1) else i for i in col_indices]

                indices[(row, col, layer)] = (
                    row_indices, col_indices, layer_indices)

    return indices