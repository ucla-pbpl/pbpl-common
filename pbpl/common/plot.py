# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap
from scipy.spatial.transform import Rotation

def setup_plot():
    mpl.rc('font', size=8.0, family='sans-serif')
    mpl.rc('mathtext', fontset='cm')
    # mpl.rc('ps', useafm=True)
    mpl.rc('pdf', use14corefonts=True)
    # mpl.rc('text', usetex=True)
    mpl.rc('lines', linewidth=0.8)
    mpl.rc('xtick.major', size=4, width=0.6)
    mpl.rc('ytick.major', size=4, width=0.6)
    mpl.rc('xtick', direction='in', top=True)
    mpl.rc('xtick.minor', size=2, width=0.6)
    mpl.rc('ytick.minor', size=2, width=0.6)
    mpl.rc('ytick', direction='in', right=True)
    mpl.rc('legend', fontsize=7.0)
    mpl.rc('legend', labelspacing=0.25)
    mpl.rc('legend', frameon=False)
    mpl.rc('path', simplify=False)
    mpl.rc('axes', unicode_minus=False, linewidth=0.8)
    mpl.rc('figure.subplot', right=0.97, top=0.97, bottom=0.15, left=0.13)
    mpl.rc('axes', titlepad=-10)
    mpl.rc('axes', prop_cycle=mpl.cycler(
        'color', [
            '#0083b8', '#e66400', '#93a661', '#ebc944', '#da1884', '#7e48bd']))
    # girl scouts green is 0x00ae58
    # #0083b8 = (0.0, 0.51, 0.72)
    mpl.rc('figure', max_open_warning=False)

def gen_cdict(red, green, blue, midpoint, frac):
    return {'red':   [[0.0,  1.0, 1.0],
                      [midpoint,  red, red],
                      [1.0,  red*frac, red*frac]],
            'green': [[0.0,  1.0, 1.0],
                      [midpoint, green, green],
                      [1.0,  green*frac, green*frac]],
            'blue':  [[0.0,  1.0, 1.0],
                      [midpoint,  blue, blue],
                      [1.0,  blue*frac, blue*frac]]}

blue_cmap = LinearSegmentedColormap(
    'pbpl_blue_cmap', segmentdata=gen_cdict(0, 0.51, 0.72, 0.75, 0.3), N=256)
    # 'pbpl_blue_cmap', segmentdata=gen_cdict(0, 0.51, 0.72, 0.6, 0.3), N=256)

orange_cmap = LinearSegmentedColormap(
    'pbpl_orange_cmap', segmentdata=gen_cdict(0.90, 0.39, 0, 0.75, 0.3), N=256)

BlueOrange_cmap = LinearSegmentedColormap.from_list(
    'BlueOrange_colormap', ['#0083b8', '#ffffff', '#e66400'], 256)
