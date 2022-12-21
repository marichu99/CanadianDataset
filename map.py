import folium
import matplotlib.pyplot as plt
world_map=folium.Map(
    location=[56.130, -106.35],
    zoom_start=3,
    tiles="Stamen Toner"
)
#  add a red marker to Ontario
# world_map.add_child(
#     folium.CircleMarker(
#         location=[51.25,-81.25],
#         radius=5,
#         color="red",
#         fill_color="red"
#     )
# )

# # label the marker
# folium.Marker(
#     location=[51.25,-81.35],
#     popup="Ontario"
# ).add_to(parent=world_map)
# world_map.show_in_browser()

world_map.add_child(
    folium.CircleMarker(
        location=[51.25,-81.35],
        radius=5,
        color="red",
        fill_color="red"
    )
)
# label the marker
world_map.add_child(
    folium.Marker(
        location=[51.25,-81.35],
        popup="Ontario",
    )
)

world_map.show_in_browser()
















