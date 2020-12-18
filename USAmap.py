import matplotlib.pyplot as plt
import geopandas

states = geopandas.read_file('./data_gp/usa-states-census-2014.shp')
type(states)

states.head()

states = states.to_crs("EPSG:3395")

states.plot()