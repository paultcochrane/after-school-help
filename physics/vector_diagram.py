# -*- coding: utf-8 -*-

import matplotlib.colors as mcolors
from fractions import Fraction
from matplotlib.patches import Arc
import numpy as np
import matplotlib.pyplot as plt


def plot_vector(
        *, r=5, theta=Fraction('1/4'), subscript=1, plot_projections=False):
    fig, ax = plt.subplots()
    fig.canvas.draw()  # Need to draw the figure to define renderer
    ax.axis('equal')
    ax.grid(which='both', axis='both')

    max_xy = r
    center = (0, 0)
    p1 = [(-max_xy, 0), (max_xy, 0)]
    p2 = [(0, -max_xy), (0, max_xy)]
    axis_colour = mcolors.TABLEAU_COLORS['tab:blue']
    x_axis, = ax.plot(*zip(*p1), color=axis_colour)
    y_axis, = ax.plot(*zip(*p2), color=axis_colour)
    ax.text(max_xy, 0, 'x', verticalalignment='bottom')
    ax.text(0, max_xy, 'y', horizontalalignment='left')

    phi = theta*np.pi

    horizontal_alignment = 'left'

    if 0 <= phi < 2*np.pi:
        vertical_alignment = 'baseline'
    else:
        vertical_alignment = 'top'

    vector = [(0, 0), (r*np.cos(phi), r*np.sin(phi))]
    vector_props = {
        "arrowstyle": "-|>"
    }
    ax.annotate("", xy=vector[1], xytext=(0, 0), arrowprops=vector_props)
    ax.annotate(
        rf"$r_{subscript} = {r}$", vector[1],
        horizontalalignment=horizontal_alignment,
        verticalalignment=vertical_alignment,
    )

    if plot_projections:
        x_projection_props = vector_props
        x_projection_props |= {
            "color": 'r',
        }
        ax.annotate(
            "",
            xy=(vector[1][0], 0),
            xytext=(0, 0),
            arrowprops=x_projection_props
        )

        y_projection_props = vector_props
        y_projection_props |= {
            "color": 'g',
        }
        ax.annotate(
            "",
            xy=(0, vector[1][1]),
            xytext=(0, 0),
            arrowprops=y_projection_props
        )

    theta2 = np.rad2deg(np.arctan2(vector[1][1], vector[1][0]))
    scale_factor = r/3
    size = 2*scale_factor
    if phi < 0:
        arc = Arc(center, size, size, angle=0, theta1=theta2, theta2=0)
    else:
        arc = Arc(center, size, size, angle=0, theta1=0, theta2=theta2)
    ax.add_patch(arc)

    angle_path = arc.get_path()
    angle_half_way_index = int(np.ceil(len(angle_path.vertices)/2))
    angle_half_way_point = \
        scale_factor*angle_path.vertices[angle_half_way_index]

    angle_text = rf"$\theta_{subscript} = {theta} \cdot \pi$"
    ax.annotate(
        angle_text, angle_half_way_point,
        horizontalalignment=horizontal_alignment,
        verticalalignment=vertical_alignment,
    )

# vim: expandtab shiftwidth=4 softtabstop=4
