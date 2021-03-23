import osmnx as ox
import matplotlib.pyplot as plt

place_name = "Kamppi, Helsinki, Finland"
graph = ox.graph_from_place(place_name)
#type(graph)

fig, ax = ox.plot_graph(graph)
#plt.tight_layout()

fig, ax = ox.plot_graph(graph)
#plt.tight_layout()

area = ox.gdf_from_place(place_name)
buildings = ox.footprints_from_place(place_name)

#type(area)
#type(buildings)

nodes, edges = ox.graph_to_gdfs(graph)

#nodes.head()
#edges.head()

fig, ax = plt.subplots()
area.plot(ax=ax, facecolor='black')
edges.plot(ax=ax, linewidth=1, edgecolor='#BC8F8F')
buildings.plot(ax=ax, facecolor='khaki', alpha=0.7)
plt.tight_layout()