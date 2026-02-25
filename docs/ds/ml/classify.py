import sys
from collections import Counter
import plotly.express as px
import pandas as pd

# knn where k=3
K = 3

labeled_data_path, unlabeled_data_path = (
    sys.argv[1:3]
    if len(sys.argv) > 1
    else ("viz.csv", "lost-penguin.csv")
)

labeled_df = pd.read_csv(
    labeled_data_path,
    header=None,
    names=["Species", "Flipper Len (mm)", "Mass (g)", "Sex"],
    dtype={"Flipper Len (mm)": int, "Mass (g)": int}
)

unlabeled_df = pd.read_csv(
    unlabeled_data_path,
    header=None,
    names=["Species", "Flipper Len (mm)", "Mass (g)", "Sex"],
    dtype={"Flipper Len (mm)": int, "Mass (g)": int}
)

###
# Update here.
# Given the lost penguin and the labeled dataframe of penguins,
# find the closest k=3, "vote", and return winner.
###
def distance(lost_penguin, k=K):
    k_penguins = labeled_df["Species"].sample(k)
    k_penguins = sorted((v,k) for k,v in Counter(k_penguins).items())
    print(k_penguins)
    return k_penguins[-1][1]

for i, lost_penguin in unlabeled_df.iterrows():
    fl = lost_penguin["Flipper Len (mm)"]
    ma = lost_penguin["Mass (g)"]

    classification = distance(lost_penguin)

    unlabeled_df.at[i, "Species"] = classification

fig = px.scatter(
    pd.concat((labeled_df, unlabeled_df)),
    x="Mass (g)", y="Flipper Len (mm)",
    color="Species", symbol="Sex",
    title="Penguin Flipper Length vs Mass"
)

fig.update_traces(marker=dict(size=12))

fig.show()
