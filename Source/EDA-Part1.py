import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import scipy.stats as scs
from scipy.spatial.distance import pdist, squareform
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples
import matplotlib.cm as cm
from IPython.display import HTML, display


def load_data(filename):
    """
    Loading Data from csv to pandas for EDA and
    convert column names to standard format.
    Input is filepath, Output is the dataframe.
    """
    df = pd.read_csv(filename)
    df.columns = df.columns.str.lstrip()
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(" ", "_")
    return df

def date_time_conversions(df):
    """
    Converting the shared_date and last_activity_date
    columns to pandas datetime format.
    Input is dataframe and output is dataframe with new columns View Month (month),
    Day of week (weekday), View Hour (hour) and time_spent_mins added.
    """
    df["last_activity_date"] = pd.to_datetime(df["last_activity_date"], format="%d-%b-%Y")
    df["shared_date"] = pd.to_datetime(df["shared_date"], format="%d-%b-%Y")
    df["month"] = pd.to_datetime(df['last_activity_date'], format='%d-%b-%Y').dt.month
    df["weekday"] = df['last_activity_date'].dt.dayofweek
    df["hour"] = pd.to_datetime(df['last_activity_time'], format='%H:%M:%S').dt.hour
    df["time_spent_mins"] = df["time_spent_in_seconds"]/60.
    return df

def add_days_from_share_to_view(df):
    """
    Get the time difference between the share and view dates. Input df output,
    df with column "num_of_day_from_share_view" column added.
    """
    for i in xrange(len(df)):
        if (df["shared_date"] is not "NaT") or (df["shared_date"] is not "NaN") :
            df['num_of_day_from_share_view'] = (df["last_activity_date"] - df["shared_date"]).dt.days
    return df

def create_share_info_df(df):
    """
    New dataframe for all share data.
    Input base dataframe, Output new share_df.
    """
    share_df = df[df.activity_type == "SHARE"]
    share_df = share_df.drop(["user_os", "viewing_app"], axis=1)
    return share_df

def create_view_info_df(df):
    """
    New dataframe for all view data.
    Input base dataframe, Output new view_df.
    """
    view_df = df[(df.activity_type == "VIEW") & (df.user_os != "NaN")]
    view_df = view_df.drop(["share_channel", "user_groups", "shared_date", "shared_time"], axis =1)
    view_app_list = view_df.viewing_app.unique()
    view_app_dict = {}
    for i in xrange(len(view_app_list)):
        view_app_dict[view_app_list[i]]=i
    return view_df

def plot_view_mins_per_hour(df1):
    hour_grouped = df1.groupby("hour")["time_spent_mins"].sum()
    plt.bar(xrange(0,24),hour_grouped)
    return



if __name__ == "__main__":
    df = load_data("shareViewDataRM-ext.csv")
    df = date_time_conversions(df)
    df = add_days_from_share_to_view(df)
    share_df = create_share_info_df(df)
    view_df = create_view_info_df(df)
