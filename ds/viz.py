import sys
import plotly.express as px
import pandas as pd

csv_path = sys.argv[1] if len(sys.argv) > 1 else "viz.csv"

df = pd.read_csv(
    csv_path,
    header=None,
    names=["Species", "Flipper Len (mm)", "Mass (g)", "Sex"]
)

fig = px.scatter(
    df,
    x="Mass (g)", y="Flipper Len (mm)",
    color="Species", symbol="Sex",
    title="Penguin Flipper Length vs Mass"
)

fig.update_traces(marker=dict(size=12))

fig.show()
