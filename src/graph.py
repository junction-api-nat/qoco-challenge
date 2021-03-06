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


def create_graph(stations_json, transports_json):
    g = networkx.MultiDiGraph()
    add_nodes_as_stations(g, stations_json)
    add_transports_as_edges(g, transports_json['transports'])
    return g


def draw_graph(g):
    import matplotlib.pyplot as plt
    pos = networkx.get_node_attributes(g, 'pos')
    networkx.draw(g, pos, with_labels=True)
    labels = networkx.get_edge_attributes(g, 'weight')
    networkx.draw_networkx_edge_labels(g, pos=pos, edge_labels=labels)
    plt.show()


if __name__ == "__main__":
    import api.client

    g = create_graph(api.client.get_all_stations(),
                     api.client.get_all_transports())
    draw_graph(networkx.DiGraph(g))
