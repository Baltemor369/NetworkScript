from Switch import Switch
from Routeur import Routeur

class Network:
    def __init__(self, name):
        self.name = name
        self.switchs:list[Switch] = []
        self.routeurs: list[Routeur] = []
    
    def add_switch(self, switch:Switch):
        self.switchs.append(switch)

    def del_switch(self, switch:Switch):
        self.switchs.remove(switch)
    
    def to_dict(self):
        return {
            "name": self.name,
            "routeurs": [routeur.to_dict() for routeur in self.routeurs],
            "switchs": [switch.to_dict() for switch in self.switchs],
        }
    
    def load_config(self, config:dict):
        self.name = config["name"]
        self.routeurs = [Routeur.load_config(routeur_config) for routeur_config in config["routeurs"]]
        self.switchs = [Switch.load_config(switch_config) for switch_config in config["switchs"]]

    def generate_config(self):
        """
        Génère un script de configuration.
        """
        script = "\nSwitchs Configuration\n"
        script += "#" * 50 + "\n"
        for switch in self.switchs:
            script += switch.generate_config()
            print("\n")
        script += "#" * 50 + "\n\n"
        
        script += "Routeurs Configuration\n"
        script += "#" * 50 + "\n"
        script += "#" * 50 + "\n\n"

        return script