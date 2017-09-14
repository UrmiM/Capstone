import pandas as pd
import numpy as np
import datetime as dt
import pylab as pl
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns
import itertools
import scipy.stats as scs
from scipy.spatial.distance import pdist, squareform
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.cm as cm
from IPython.display import HTML, display
from collections import Counter


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
    df["weekday_name"] = df['last_activity_date'].dt.weekday_name
    df["month"] = df['last_activity_date'].dt.month
    df["weekday"] = df['last_activity_date'].dt.dayofweek
    df["hour"] = df['last_activity_time'].dt.hour
    df["hour"] = df[df["hour"] > 11] - 12
    df["hour"] = df[df["hour"] < 12] + 12
    df["time_spent_mins"] = df["time_spent_in_seconds"]/60.
    df["time_of_day"].replace({0 : 1, 1 : 1, 2 : 1, 3 : 1, 4 : 1, 5 : 1}, inplace = True)
    df["time_of_day"].replace({6 : 2, 7 : 2, 8 : 2, 9 : 2, 10 : 2, 11 : 2}, inplace = True)
    df["time_of_day"].replace({12 : 3, 13 : 3, 14 : 3, 15 : 3, 16 : 3, 17 : 3}, inplace = True)
    df["time_of_day"].replace({18 : 4, 19 : 4, 20 : 4, 21 : 4, 22 : 4, 23 : 4,}, inplace = True)
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

def feat_engg_for_es(df):
    """
    Creates columns for viewing_device and browser for E2S.
    """
    df.rename(columns={'user_os': 'viewing_device'}, inplace=True)
    df["viewing_device"].replace({"MAC_OS_X" : "Laptop/Desktop", "WEB" : "Laptop/Desktop", \
    "WINDOWS_10" : "Laptop/Desktop", "WINDOWS_7" : "Laptop/Desktop", "WINDOWS_81" : "Laptop/Desktop", \
    "CHROME_OS" : "Laptop/Desktop"}, inplace = True)
    df["viewing_device"].replace({"ANDROID_MOBILE" : "Phone", "ANDROID6" : "Phone", "ANDROID4" : "Phone", \
    "ANDROID5" : "Phone","ANDROID7" : "Phone", "MAC_OS_X_IPHONE" : "Phone", "iOS7_IPHONE" : "Phone", \
    "iOS8_1_IPHONE" : "Phone", "iOS8_3_IPHONE" : "Phone", "iOS9_IPHONE" : "Phone"}, inplace=True)
    df["viewing_device"].replace({"ANDROID4_TABLET" : "Tablet", "ANDROID6_TABLET" : "Tablet", "iOS9_IPAD" : "Tablet",\
    "MAC_OS_X_IPAD" : "Tablet"}, inplace = True)
    df.rename(columns={'viewing_app': 'browser'}, inplace=True)
    df["browser"].replace({"CHROME45" : "CHROME", "CHROME49" : "CHROME", "CHROME41" : "CHROME", \
    "CHROME48" : "CHROME", "CHROME28" : "CHROME", "FIREFOX34" : "FIREFOX", "FIREFOX46" : "FIREFOX", \
    "FIREFOX48" : "FIREFOX", "EDGE12" : "EDGE"}, inplace = True)
    df["browser"].replace({"IE11" : "IE", "IE7" : "IE", "EDGE14" : "EDGE", "SAFARI5" : "SAFARI", \
    "SAFARI9" : "SAFARI"}, inplace=True)
    return df

def feat_engg_for_tw(df):
    """
    Creates columns for viewing_device and browser for E2S.
    """
    df.rename(columns={'user_os': 'viewing_device'}, inplace=True)
    df["viewing_device"].replace({"MAC_OS_X" : "Laptop/Desktop", "WINDOWS_XP" : "Laptop/Desktop",\
    "WINDOWS_8" : "Laptop/Desktop", "WINDOWS_10" : "Laptop/Desktop", "WINDOWS_7" : "Laptop/Desktop", \
    "WINDOWS_81" : "Laptop/Desktop", "CHROME_OS" : "Laptop/Desktop"}, inplace = True)
    df["viewing_device"].replace({"ANDROID_MOBILE" : "Phone", "ANDROID6" : "Phone", "ANDROID4" : "Phone",\
    "ANDROID5" : "Phone","ANDROID7" : "Phone", "MAC_OS_X_IPHONE" : "Phone", "iOS7_IPHONE" : "Phone",\
    "iOS8_1_IPHONE" : "Phone", "iOS8_3_IPHONE" : "Phone", "iOS9_IPHONE" : "Phone"}, inplace=True)
    df["viewing_device"].replace({"ANDROID4_TABLET" : "Tablet", "ANDROID6_TABLET" : "Tablet",\
    "iOS8_1_IPAD" : "Tablet", "MAC_OS_X_IPAD" : "Tablet"}, inplace = True)
    df.rename(columns={'viewing_app': 'browser'}, inplace=True)
    df["browser"].replace({"CHROME45" : "CHROME", "CHROME49" : "CHROME", "CHROME41" : "CHROME", \
    "CHROME48" : "CHROME", "CHROME28" : "CHROME", "FIREFOX34" : "FIREFOX", "FIREFOX46" : "FIREFOX", \
    "FIREFOX48" : "FIREFOX", "EDGE12" : "EDGE"}, inplace = True)
    df["browser"].replace({"EDGE13" : "EDGE", "EDGE14" : "EDGE", "SAFARI5" : "SAFARI", \
    "SAFARI9" : "SAFARI"}, inplace=True)
    return df

def feat_engg_for_is(df):
    """
    Creates columns for viewing_device and browser for E2S.
    """
    df.rename(columns={'user_os': 'viewing_device'}, inplace=True)
    df["viewing_device"].replace({"WINDOWS_7" : "Laptop/Desktop", "WINDOWS_10" : "Laptop/Desktop", \
    "WINDOWS_81" : "Laptop/Desktop", "WINDOWS_XP" : "Laptop/Desktop", "LINUX" : "Laptop/Desktop", \
    "UBUNTU" : "Laptop/Desktop", "MAC_OS_X" : "Laptop/Desktop"}, inplace = True)
    df["viewing_device"].replace({"ANDROID_MOBILE" : "Phone", "ANDROID6" : "Phone", "ANDROID4" : "Phone", \
    "ANDROID5" : "Phone","ANDROID7" : "Phone", "MAC_OS_X_IPHONE" : "Phone", "iOS7_IPHONE" : "Phone", \
    "iOS8_1_IPHONE" : "Phone", "iOS8_3_IPHONE" : "Phone", "iOS9_IPHONE" : "Phone"}, inplace=True)
    df["viewing_device"].replace({"ANDROID4_TABLET" : "Tablet", "ANDROID6_TABLET" : "Tablet", \
    "iOS8_1_IPAD" : "Tablet", "MAC_OS_X_IPAD" : "Tablet"}, inplace = True)
    df.rename(columns={'viewing_app': 'browser'}, inplace=True)
    df["browser"].replace({"CHROME45" : "CHROME", "CHROME51" : "CHROME", "CHROME33" : "CHROME", \
    "CHROME30" : "CHROME", "CHROME47" : "CHROME", "CHROME49" : "CHROME", "CHROME42" : "CHROME", \
    "CHROME48" : "CHROME", "CHROME38" : "CHROME", "FIREFOX44" : "FIREFOX", "FIREFOX47" : "FIREFOX", \
    "FIREFOX43" : "FIREFOX", "FIREFOX37" : "FIREFOX", "EDGE12" : "EDGE"}, inplace = True)
    df["browser"].replace({"EDGE13" : "EDGE", "EDGE14" : "EDGE", "IE7" : "IE", "IE10" : "IE", "IE11" : "IE", \
    "SAFARI9" : "SAFARI", "APPLE_WEB_KIT" : "SAFARI"}, inplace=True)
    return df

def feat_engg_for_tw(df):
    """
    Creates columns for viewing_device and browser for E2S.
    """
    df.rename(columns={'user_os': 'viewing_device'}, inplace=True)
    df["viewing_device"].replace({"WINDOWS_7" : "Laptop/Desktop", "WINDOWS_10" : "Laptop/Desktop", \
    "MAC_OS_X" : "Laptop/Desktop"}, inplace = True)
    df["viewing_device"].replace({"ANDROID_MOBILE" : "Phone", "ANDROID6" : "Phone", "ANDROID4" : "Phone", \
    "ANDROID5" : "Phone", "MAC_OS_X_IPHONE" : "Phone", "iOS9_IPHONE" : "Phone", "iOS8_1_IPHONE" : "Phone", \
    "iOS8_3_IPHONE" : "Phone", "iOS9_IPHONE" : "Phone"}, inplace=True)
    df.rename(columns={'viewing_app': 'browser'}, inplace=True)
    df["browser"].replace({"CHROME45" : "CHROME", "CHROME51" : "CHROME", "CHROME33" : "CHROME", \
    "CHROME30" : "CHROME", "CHROME47" : "CHROME", "CHROME49" : "CHROME", "CHROME42" : "CHROME", \
    "CHROME48" : "CHROME", "CHROME38" : "CHROME", "FIREFOX44" : "FIREFOX", "FIREFOX47" : "FIREFOX", \
    "FIREFOX43" : "FIREFOX", "FIREFOX37" : "FIREFOX", "EDGE12" : "EDGE"}, inplace = True)
    df["browser"].replace({"EDGE13" : "EDGE", "EDGE14" : "EDGE", "IE7" : "IE", "IE10" : "IE", "IE11" : "IE", \
    "SAFARI9" : "SAFARI", "APPLE_WEB_KIT" : "SAFARI"}, inplace=True)
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

def regr_model(df):
    user_id_list = [j.user_id for i,j in df.iterrows() if j["activity_type"] == "VIEW"]
    num_views = Counter(user_id_list)
    best, views = [], []
    #best = sorted(num_views, key=lambda x : num_views[x])
    for k,v in num_views.iteritems():
        if v<=20:
            best.extend((k,v)), views.append(v)


def clustering(df1,df2,df3,df4):


if __name__ == "__main__":
    df = load_data("shareViewDataRM-ext.csv")
    df = date_time_conversions(df)
    df = add_days_from_share_to_view(df)
    share_df = create_share_info_df(df)
    view_df = create_view_info_df(df)
