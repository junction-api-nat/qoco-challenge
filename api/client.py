import requests
import os
import sys


apikey_env_var = "QOCO_X_API_KEY"
if not apikey_env_var in os.environ:
    raise Exception("%s not found from environment variables!" % (apikey_env_var,))

api_baseurl = "https://qocojunction2018.northeurope.cloudapp.azure.com"
headers = {"content-type": "application/json", "x-api-key": os.environ[apikey_env_var]}


def get_all_bookings():
    r = requests.get("%s/bookings" % (api_baseurl,), headers=headers)
    r.raise_for_status()
    return r.json()


def get_all_stations():
    r = requests.get("%s/stations" % (api_baseurl,), headers=headers)
    r.raise_for_status()
    return r.json()


def get_all_transports():
    r = requests.get("%s/bookings" % (api_baseurl,), headers=headers)
    r.raise_for_status()
    return r.json()



if __name__ == "__main__":
    allowed_cmds = ("bookings", "stations", "transports")

    if len(sys.argv) != 2 or sys.argv[1] not in allowed_cmds:
        print("Usage: %s [%s]" % (sys.argv[0], "|".join(cmd for cmd in allowed_cmds)))
        exit(1)

    command = sys.argv[1]

    ret = None
    if command == "bookings":
        ret = get_all_bookings()
    elif command == "stations":
        ret = get_all_stations()
    elif command == "transports":
        ret = get_all_transports()

    print(ret)
