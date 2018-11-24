import networkx


def create_nodes_from_stations(stations_json):
    G = networkx.Graph()
    for station, station_data in stations_json.items():
        location = station_data['location']
        pos = (int(location['latitude']), int(location['longitude']))
        G.add_node(station, pos=pos)
    return G


if __name__ == "__main__":
    try:
        import api.client
    except (ValueError, ModuleNotFoundError):
        print("Run this test from the project root folder like so: 'python -m src.graph'")
        exit(1)
    stations_json = api.client.get_all_stations()
    create_nodes_from_stations(stations_json)

    g = create_nodes_from_stations(stations_json)

    # Draw
    import matplotlib.pyplot as plt
    pos = networkx.get_node_attributes(g, 'pos')
    networkx.draw(g, pos, with_labels=True)
    labels = networkx.get_edge_attributes(g, 'weight')
    networkx.draw_networkx_edge_labels(g, pos=pos, edge_labels=labels)
    plt.show()
