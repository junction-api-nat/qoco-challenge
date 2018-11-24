from datetime import datetime
import networkx


def add_nodes_as_stations(g, stations_json):
    for station, station_data in stations_json.items():
        location = station_data['location']
        pos = (int(location['latitude']), int(location['longitude']))
        g.add_node(station, pos=pos)


def add_transports_as_edges(g, transports):
    now = datetime.now()
    for transport in transports:
        dep_station = transport['dep_station']
        arr_station = transport['scheduled_arr_station']
        estimated_arr_datetime = datetime.strptime(transport['estimated_arr_datetime'], "%Y-%m-%dT%H:%M:%S")
        deltatime_seconds = (estimated_arr_datetime - now).total_seconds()
        deltatime_hours = deltatime_seconds // 3600
        g.add_edge(dep_station, arr_station, weight=deltatime_hours)


if __name__ == "__main__":
    try:
        import api.client
    except (ValueError, ModuleNotFoundError):
        print("Run this test from the project root folder like so: 'python -m src.graph'")
        exit(1)

    g = networkx.DiGraph()

    stations_json = api.client.get_all_stations()
    add_nodes_as_stations(g, stations_json)


    transports = api.client.get_all_transports()['transports']
    add_transports_as_edges(g, transports)

    # Draw
    import matplotlib.pyplot as plt
    pos = networkx.get_node_attributes(g, 'pos')
    networkx.draw(g, pos, with_labels=True)
    labels = networkx.get_edge_attributes(g, 'weight')
    networkx.draw_networkx_edge_labels(g, pos=pos, edge_labels=labels)
    plt.show()
