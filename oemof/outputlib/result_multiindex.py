from collections import UserDict, UserList
from itertools import groupby
from ..solph.network import Storage
from ..solph.options import Investment
import pandas as pd


def results_to_multiindex(es, om):
    """
    Returns a multi-indexed dataframe of the results of an optimization model.
    """

    # create empty dict with flows
    results = {(source, target): None for source, target in om.flows}

    # add data
    for source, target in om. flows:
        data = [om.flow[source, target, t].value for t in om.TIMESTEPS]
        results[(source, target)] = pd.DataFrame(data, index=es.timeindex)

    return print(results)
