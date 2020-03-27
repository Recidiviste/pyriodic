import json
import requests

class Element(dico):
    def __init__(self, dico):
        self.symbol = dico['symbol']
        self.name = dico['name']
        self.mass = dico['atomicMass']
        self.number = dico['']
        self.radius = dico['']
        self.boilingPoint = dico['']
        self.bondingType = dico['']
        self.density = dico['']
        self.electronAffinity = dico['']
        self.electronegativity = dico['']
        self.electronicConfiguration = dico['']
        self.groupBlock = dico['']
        self.ionRadius = dico['']
        self.ionizationEnergy = dico['']
        self.meltingPoint = dico['']
        self.oxidationStates = dico['']
        self.standardState = dico['']
        self.vanDerWaalsRadius = dico['']
        self.yearDiscovered = dico['']


def get_info(parameter):
    url = "https://neelpatel05.pythonanywhere.com/element/atomicnumber"
    raw = requests.get(url, parameter)
    if raw.status_code != 200:
        print(raw.status_code)
        return 1
    jformatted = json.dumps(raw.json(), indent=4)
    print(type(jformatted))
    print(type(raw.json()))

parameter = {"atomicnumber":input("What number ? :")}
get_info(parameter)
