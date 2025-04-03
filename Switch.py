class Switch:
    def __init__(self, name):
        """
        Initialise un objet Switch.
        :param name: Nom du switch.
        :param nb_interfaces: Nombre total d'interfaces sur le switch.
        """
        self.name = name
        self.vtp = {}
        self.vlans = []
        self.interfaces = []

    def set_name(self, name:str):
        self.name = name
    
    def set_nb_interfaces(self, nb_interfaces:int):
        self.nb_interfaces = nb_interfaces
    
    def set_vtp(self, domain:str, password:str, mode:str):
        """
        Configure le VTP du switch.
        :param domain: Nom du domaine VTP.
        :param password: Mot de passe VTP.
        :param mode: Mode VTP (client/server).
        """
        if mode in ["client", "server"]:
            #TODO regex checking for domaine & password
            self.vtp = {"domain": domain, "password": password, "mode": mode}
            return True
        return False
    
    def add_interface(self, interface_id:str, mode:str, vlans:list, description:str=""):
        """
        Ajoute ou met à jour une interface au switch.
        :param interface_id: Nom ou numéro de l'interface (ex: "GigabitEthernet0/1").
        :param mode: Mode d'interface (access/trunk).
        :param vlans: Liste des VLANs associées à l'interface.
        :param description: Description de l'interface.
        """
        # Validation du mode
        if mode not in ["access", "trunk"]:
            return False
        
        self.interfaces.append({"name": interface_id, "mode": mode, "vlans": vlans, "description": description})
        return True


    def reset_interface(self, interface_number:int):
        """
        Supprime une interface du switch.
        :param interface_number: Nom ou numéro de l'interface.
        """
        for interface in self.interfaces:
            if interface["interface_number"] == interface_number:
                self.interfaces.remove(interface)
                break

    def add_vlan(self, vlan_id:int, name:str):
        """
        Ajoute une VLAN au switch.
        :param vlan_id: Identifiant de la VLAN.
        :param name: Nom de la VLAN.
        """
        if vlan_id > 0:
            #TODO regex checking for name
            self.vlans.append({"id": vlan_id, "name": name})
            return True
        return False

    def to_dict(self):
        return {
            "name": self.name,
            "vtp": self.vtp,
            "vlans": self.vlans,
            "interfaces": self.interfaces,
        }
    
    def load_config(self, config:dict):
        self.name = config["name"]
        self.vtp = config["vtp"]
        self.vlans = config["vlans"]
        self.interfaces = config["interfaces"]
    
    def generate_config(self):
        """
        Génère un script de configuration.
        """
        script = f"\nSwitch {self.name}\n"
        
        script += "Interfaces Trunk Configuration:\n"
        script += "-" * 50 + "\n"
        for interface in self.interfaces:
            if interface["mode"] == "trunk":
                script += f"interface {interface['name']}\n"
                script += f"switchport mode trunk\n"
                
                # if self.vlans:
                    # vlans = ",".join(str(vlan["id"]) for vlan in interface['vlans'])
                    # script += f"switchport trunk allowed vlan {vlans}\n"
                
                script += "exit\n"
        script += "-" * 50 + "\n\n"

        script += "Interfaces Access Configuration:\n"
        script += "-" * 50 + "\n"
        for interface in self.interfaces:
            if interface["mode"] == "access":
                script += f"interface {interface['name']}\n"
                script += f"switchport mode access\n"
                script += f"switchport access vlan {interface['vlans']}\n"
                script += "exit\n"
        script += "-" * 50 + "\n\n"

        script += "VTP Configuration :\n"
        script += "-" * 50 + "\n"
        if self.vtp:
            script += f"vtp mode {self.vtp["mode"]}\n"
            script += f"vtp domain {self.vtp["domain"]}\n"
            script += f"vtp password {self.vtp["password"]}\n"
            script += "exit\n"
        script += "-" * 50 + "\n\n"

        script += "VLAN Configuration:\n"
        script += "-" * 50 + "\n"
        for vlan in self.vlans:
            script += f"vlan {vlan['id']}\n"
            script += f"name {vlan['name']}\n"
            script += "exit\n"
        script += "-" * 50 + "\n\n"
        
        script += "Fin de configuration\n"
        return script
