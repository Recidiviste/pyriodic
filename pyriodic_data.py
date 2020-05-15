import json
import requests

class Element():
    def __init__(self, dico):
        self.symbol = dico['symbol']
        self.name = dico['name']
        self.atomicMass = dico['atomicMass']
        self.atomicNumber = dico['atomicNumber']
        self.atomicRadius = dico['atomicRadius']
        self.boilingPoint = dico['boilingPoint']
        self.bondingType = dico['bondingType']
        self.density = dico['density']
        self.electronAffinity = dico['electronAffinity']
        self.electronegativity = dico['electronegativity']
        self.electronicConfiguration = dico['electronicConfiguration']
        self.groupBlock = dico['groupBlock']
        self.ionRadius = dico['ionRadius']
        self.ionizationEnergy = dico['ionizationEnergy']
        self.meltingPoint = dico['meltingPoint']
        self.oxidationStates = dico['oxidationStates']
        self.standardState = dico['standardState']
        self.vanDerWaalsRadius = dico['vanDelWaalsRadius']
        self.yearDiscovered = dico['yearDiscovered']


def get_info(parameter):
    url = "https://periodic-table-api.herokuapp.com/atomicNumber"
    raw = requests.get("/".join([url, parameter]))
    if raw.status_code != 200:
        print(raw.status_code)
        return 1
    else:
        return raw.json()

if __name__ == "__main__":
    parameter = input("What number ? :")
    telement = Element(get_info(parameter))
    exec( telement.name + " = telement ")
    del telement
    print(Hydrogen.density)
