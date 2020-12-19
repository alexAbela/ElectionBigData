from urllib.request import urlopen
import plotly.express as px
import pandas as pd
import json

with urlopen('https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json') as response:
    states1 = json.load(response)

df = pd.read_csv('./data/stateSentiment.csv', dtype={"state" : str, "biden" : float, "trump" : float})

print(px.colors.qualitative.Plotly)


# DC / WA er den samme

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

d = '#1015B1'
r = '#CC2B1D'

colors = [d, r, d, r, d, r, d, r, d, r, d, r, d, r, d, r, d, r, d, r,
  d, r, d, r, d, r, d, r, d, r, d, r, d, r, d, r, d, r, d, r, d, r, d,
  r, d, r, d, r, d, r]



fig = px.choropleth(df, geojson=states1, locations=states, locationmode="USA-states", color=colors, scope="usa")

#fig = px.choropleth(df, geojson=states, locations="Alabama", scope="usa", color_continuous_scale="Viridis")

#fig = px.choropleth(df, geojson=counties, locations='state', color='biden',
#                           color_continuous_scale="Viridis",
#                           range_color=(0, 12),
#                           scope="usa",
#                           labels={'unemp':'unemployment rate'}
#                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()