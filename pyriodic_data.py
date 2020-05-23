import json
import requests

class Element():
    def __init__(self, dico):
        for i in dico.keys():
            setattr(self, i, dico[i])

    def display(self):
        l = ["symbol", "atomicMass", "yearDiscovered", "boilingPoint", "atomicRadius", "ionRadius", "bondingType", "electronAffinity", "vanDelWaalsRadius", "electronegativity"]
        r = ["name", "atomicNumber", "groupBlock", "standardState", "meltingPoint", "density", "ionizationEnergy", "oxidationStates", "electronicConfiguration", "cpkHexColor"]
        dl = ["Symbol: ", "Atomic Mass: ", "Discovered in: ", "Boiling at: ", "Atomic Radius: ", "Ion Radius: ", "Bonding Type: ", "Electron Affinity: ", "VanDerWaals Radius: ", "Electronegativity: "]
        dr = ["Name: ", "Atomic Number: ", "Group and Block: ", "Standard State: ", "Melting Point: ", "Density: ", "Ionization Energy: ", "Oxidation States: ", "Electronic Configuration: ", "Hexadecimal Color: "]
        for i in range(10):
            if getattr(self, l[i]) != '':
                ltext = dl[i] + getattr(self, l[i])
            else:
                ltext = dl[i] + '\033[91mNo Information\033[0m'
            if getattr(self, r[i]) != '':
                rtext = dr[i] + getattr(self, r[i])
            else:
                rtext = dr[i] + '\033[91mNo Information\033[0m'
            print(f"{ltext:<34}\t{rtext:<70}")

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


def print_info(dtype, parameter):
    raw = get_info(dtype, parameter)
    if type(raw) == "<class 'str'>":
        if raw == "dtype error":
            print('Error with the search argument')
        else:
            print(raw)
    else:
        el = Element(raw)
        el.display()

if __name__ == '__main__':
    print_info("atomicNumber", "1")
