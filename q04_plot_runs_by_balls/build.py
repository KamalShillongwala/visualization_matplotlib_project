# %load q04_plot_runs_by_balls/build.py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    x = ipl_df.groupby(['batsman'])['runs'].sum()
    y = ipl_df.groupby(['batsman'])['delivery'].count()
    plt.scatter(x, y)
    plt.show()


