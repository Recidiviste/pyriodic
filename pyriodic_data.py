import json
import requests

class Element():
    def __init__(self, dico):
        for i in dico.keys():
            print(i)
            exec('self.' + i + ' =  dico[i]')

def get_info(dtype, parameter):
    if dtype in ["atomicNumber", "atomicName", "atomicSymbol"]:
        url = "https://periodic-table-api.herokuapp.com"
        raw = requests.get("/".join([url, dtype, parameter]))
        if raw.status_code != 200:
            return("", raw.status_code)
        else:
            return raw.json()
    else:
        return("dtype error")
