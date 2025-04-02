class Switch:
    def __init__(self, name, nb_interfaces):
        """
        Initialise un objet Switch.
        :param name: Nom du switch.
        :param nb_interfaces: Nombre total d'interfaces sur le switch.
        """
        self.name = name
        self.nb_interfaces = nb_interfaces
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
            self.vtp_config = {"domain": domain, "password": password, "mode": mode}
            return True
        return False
    
    def add_interface(self, interface_id:str, mode:str, vlans:list):
        """
        Ajoute ou met à jour une interface au switch.
        :param interface_id: Nom ou numéro de l'interface (ex: "GigabitEthernet0/1").
        :param mode: Mode d'interface (access/trunk).
        :param kwargs: Options spécifiques pour la configuration (ex: vlan, description).
        """
        # Validation du mode
        if mode not in ["access", "trunk"]:
            return False
        
        if mode == "access":
            self.interfaces.append({"name": interface_id, "mode": mode, "vlans": vlans})
            return True
        elif mode == "trunk":
            self.interfaces.append({"name": interface_id, "mode": mode, "vlans": vlans})
            return True
        return False


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

    def generate_config(self):
        """
        Génère un script de configuration.
        """
        script = "Interfaces Configuration:\n"
        script += "-" * 50 + "\n"
        for interface in self.interfaces:
            script += f"interface {interface['name']}\n"
            script += f"switchport mode {interface["mode"]}\n"
            if interface['mode'] == 'access':
                script += f"switchport access vlan {interface['vlans']}\n"
            elif interface['mode'] == 'trunk':
                vlans = ",".join(str(vlan["id"]) for vlan in interface['vlans'])
                script += f"switchport trunk allowed vlan {vlans}\n"
            script += " exit\n"
        script += "-" * 50 + "\n\n"

        script += "VTP Configuration :\n"
        script += "-" * 50 + "\n"
        if self.vtp:
            script += f"vtp mode {self.vtp["mode"]}\n"
            script += f"vtp domain {self.vtp["name"]}\n"
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
        
        script += "\nFin de configuration des interfaces access."
        return script
