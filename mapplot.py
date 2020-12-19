from urllib.request import urlopen
import plotly.express as px
import pandas as pd
import json

# Initiating and retreiving relevetn data
df = pd.read_csv('data/stateAvgSentiment.csv')

colors = []
for index, row in df.iterrows():
    biden = row['biden']
    trump = row['trump']
    comparedSenti = biden - trump
    colors.append(comparedSenti)

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

colourschema = ['#FF0000', '#FFFFFF', '#0015BC']

fig = px.choropleth(locations=states, locationmode="USA-states", color=colors,
                    scope="usa",
                    color_continuous_scale=colourschema,
                    range_color=(-0.5815833411, 0.5815833411))

fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()



# fig = px.choropleth(df, geojson=states, locations="Alabama", scope="usa", color_continuous_scale="Viridis")

# fig = px.choropleth(df, geojson=counties, locations='state', color='biden',
#                           color_continuous_scale="Viridis",
#                           range_color=(0, 12),
#                           scope="usa",
#                           labels={'unemp':'unemployment rate'}
#                          )
