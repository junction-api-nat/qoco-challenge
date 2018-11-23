from src.api import client
from src import mongo


def compare_attributes(old_data_object, new_data_object):
    attributes = [
        'cancelled',
        'estimated_dep_datetime',
        'estimated_arr_datetime',
        'capacity_volume',
        'capacity_weight',
        'actual_arr_station',
    ]
    changed_attributes = []
    for attribute in attributes:
        if old_data_object[attribute] != new_data_object[attribute]:
            changed_attributes.append(attribute)
    return changed_attributes


def get_changed_data(db_data, api_data):
    changed_data = {}
    for db_data_object in db_data:
        transport_number = db_data_object['transport_number']
        # Find an object with same transport_number from API data if it exists. 
        api_data_object = next((x for x in api_data if x['transport_number'] == transport_number), None)
        if api_data_object:
            changed_attributes = compare_attributes(db_data_object, api_data_object)
            if changed_attributes:
                changed_data[transport_number] = changed_attributes
    return changed_data


def handle_data():
    db_data = mongo.getAllTransports()
    api_data = client.get_all_transports()['transports']
    changed_data = get_changed_data(db_data, api_data)
    return changed_data


if __name__ == '__main__':
    handle_data()
