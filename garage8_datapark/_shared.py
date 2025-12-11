import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import scipy.stats as stats
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

#import os


"""
Config, constants, functions that are shared by all solution notebooks.
"""

### Chart configs.
titlesize = 16
labelsize = 16
legendsize = 16
xticksize = 16
yticksize = xticksize

plt.rcParams['legend.markerscale'] = 1.5     # the relative size of legend markers vs. original
plt.rcParams['legend.handletextpad'] = 0.5
plt.rcParams['legend.labelspacing'] = 0.4    # the vertical space between the legend entries in fraction of fontsize
plt.rcParams['legend.borderpad'] = 0.5       # border whitespace in fontsize units
plt.rcParams['font.size'] = 12
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['axes.labelsize'] = labelsize
plt.rcParams['axes.titlesize'] = titlesize
plt.rcParams['figure.figsize'] = (10, 6)

plt.rc('xtick', labelsize=xticksize)
plt.rc('ytick', labelsize=yticksize)
plt.rc('legend', fontsize=legendsize)


def print_kwargs(**kwargs):
    """Prints keyword agruments with their names (thus, requires named argument call)."""
    for (k, v) in kwargs.items():
        print('{} = {}'.format(k, v))


def generate_run_dates(start_date, end_date, cadence, step):
    res = ""
    current = start_date

    if cadence == 'years':
        rd = relativedelta(years=step)
    elif cadence == 'months':
        rd = relativedelta(months=step)
    elif cadence == 'weeks':
        rd = relativedelta(weeks=step)
    elif cadence == 'days':
        rd = relativedelta(days=step)
    else:
        raise ValueError('Unacceptable cadence!')
        return
    
    while current <= end_date:
        date_str = current.strftime('%Y-%m-%d')
        res += """echo '>>>""" + date_str + """<<<' && dbt run -s io_mid --vars "{'dt': '""" + date_str + """'}" && \n"""
        current += rd
        
    return res

        
def generate_run_dicts(start_date, end_date):
    res = []
    current = start_date
    
    while current <= end_date:
        date_str = current.strftime('%Y-%m-%d')
        dct = {
          "start_date": (current - relativedelta(days=1)).strftime('%Y-%m-%d'),
          "end_date": current.strftime('%Y-%m-%d'),
          "select": "+ug_bloomreach_campaign_events +mu_bloomreach_campaign_events"
        }
        res.append(dct)
        current += relativedelta(months=2)
        
    return res

