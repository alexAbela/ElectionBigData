import plotly.express as px
import pandas as pd

# Initiating and retreiving relevetn data
df = pd.read_csv('data/stateAvgSentiment.csv')
colors = df['trump'].tolist()

# Initiating colourschema and statelist
colourschema = ['#0015BC', '#FFFFFF', '#FF0000']

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

# Defining params for Map
fig = px.choropleth(locations=states, locationmode="USA-states", color=colors,
                    scope="usa",
                    color_continuous_scale=colourschema,
                    range_color=(-0.16369611, 0.16369611))

fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

fig.show()

#'#FF0000',