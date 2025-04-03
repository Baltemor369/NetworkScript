from Switch import Switch
from Routeur import Routeur

class Network:
    def __init__(self, name):
        self.name = name
        self.switchs:list[Switch] = []
    
    def add_switch(self, switch:Switch):
        self.switchs.append(switch)

    def del_switch(self, switch:Switch):
        self.switchs.remove(switch)
    
    def generate_config(self):
        """
        Génère un script de configuration.
        """
        script = "\nSwitchs Configuration\n"
        script += "-" * 50 + "\n"
        for switch in self.switchs:
            script += switch.generate_config()
            print("\n")
        script += "-" * 50 + "\n\n"
        
        script += "Routeurs Configuration\n"
        script += "-" * 50 + "\n"
        script += "-" * 50 + "\n\n"

        return script