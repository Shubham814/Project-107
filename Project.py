import pandas as pd
import plotly.express as px

df = pd.read_csv('data.csv')
mean_attempts = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig = px.scatter(mean_attempts, x="student_id", y="level", color="attempt", size = "attempt")
fig.show()
