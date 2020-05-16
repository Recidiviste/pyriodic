import json
import requests

class Element():
    def __init__(self, dico):
        for i in dico.keys():
            exec('self.' + i + ' =  dico[i]')

    def display(self):
        c = []
        dc = [
        for i in vars(self):
            c.append(i)

def get_info(dtype, parameter):
    if dtype in ["atomicNumber", "atomicName", "atomicSymbol"]:
        url = "https://periodic-table-api.herokuapp.com"
        raw = requests.get("/".join([url, dtype, parameter]))
        if raw.status_code != 200:
            return("Wrong parameter, code :", raw.status_code)
        else:
            return raw.json()
    else:
        return("dtype error")


if __name__ == "__main__":
    parameter = input("What number ? :")
    telement = Element(get_info("atomicNumber", parameter))
    exec( telement.name + " = telement ")
    del telement
    Hydrogen.display()
