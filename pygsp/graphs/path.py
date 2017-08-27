# -*- coding: utf-8 -*-

import numpy as np
from scipy import sparse

from . import Graph  # prevent circular import in Python < 3.5


class Path(Graph):
    r"""
    Create a path graph.

    Parameters
    ----------
    N : int
        Number of vertices (default = 32)

    Examples
    --------
    >>> from pygsp import graphs
    >>> G = graphs.Path(N=16)

    References
    ----------
    See :cite:`strang1999discrete` for more informations.

    """

    def __init__(self, N=16, **kwargs):

        inds_i = np.concatenate((np.arange(0, N-1), np.arange(1, N)))
        inds_j = np.concatenate((np.arange(1, N), np.arange(0, N-1)))
        weights = np.ones(2 * (N-1))
        W = sparse.csc_matrix((weights, (inds_i, inds_j)), shape=(N, N))
        plotting = {"limits": np.array([-1, N, -1, 1])}

        super(Path, self).__init__(W=W, gtype='path',
                                   plotting=plotting, **kwargs)

        self.set_coordinates('line2D')
