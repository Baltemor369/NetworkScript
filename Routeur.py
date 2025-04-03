from const import *

import re

class Routeur:
    def __init__(self, hostname: str):
        """
        Initialise un objet Router.
        :param hostname: Nom du routeur.
        :param nb_intf: Nombre total d'interfaces sur le routeur.
        """
        self.hostname = hostname
        self.interfaces = []
        self.routes = []

    def set_hostname(self, hostname: str):
        """
        Définit le nom du routeur.
        """
        self.hostname = hostname

    def add_interface(self, interface_id: str, ip_address: str, subnet_mask: str, description: str = ""):
        """
        Ajoute ou configure une interface au routeur.
        :param interface_id: Nom ou numéro de l'interface (ex: "GigabitEthernet0/0").
        :param ip_address: Adresse IP de l'interface.
        :param subnet_mask: Masque de sous-réseau.
        :param description: Description optionnelle de l'interface.
        """
        # Validation du format de l'adresse IP et du masque de sous-réseau
        if not re.match(REG_IP, ip_address):
            if re.match(REG_MASK_CIDR, subnet_mask) is None and re.match(REG_MASK, subnet_mask) is None:
                return False
            
        self.interfaces.append({
            "name": interface_id,
            "ip_address": ip_address,
            "subnet_mask": subnet_mask,
            "description": description
        })

    def add_route(self, network_address: str, subnet_mask: str, next_hop: str):
        """
        Ajoute une route statique au routeur.
        :param destination: Destination du réseau.
        :param subnet_mask: Masque de sous-réseau.
        :param next_hop: Adresse IP du prochain saut.
        """

        if not re.match(REG_IP, network_address):
            if re.match(REG_MASK_CIDR, subnet_mask) is None and re.match(REG_MASK, subnet_mask) is None:
                return False
            
        self.routes.append({
            "network_address": network_address,
            "subnet_mask": subnet_mask,
            "next_hop": next_hop
        })

    def add_dhcp_helper(self, interface_id: str, helper_address: str):
        """
        Ajoute un DHCP Helper sur une interface.
        :param interface_id: Nom de l'interface.
        :param helper_address: Adresse IP du serveur DHCP.
        """

        if not re.match(REG_IP, helper_address):
            return False
            
        for intf in self.interfaces:
            if intf["id"] == interface_id:
                intf["dhcp_helper"] = helper_address
                break

    def generate_config(self):
        """
        Génère un script de configuration.
        """
        script = f"Router {self.hostname}\n"
        script += "Interfaces Configuration:\n"
        script += "-" * 50 + "\n"
        for interface in self.interfaces:
            script += f"interface {interface['id']}\n"
            if interface["description"]:
                script += f"description {interface['description']}\n"
            script += f"ip address {interface['ip_address']} {interface['subnet_mask']}\n"
            script += f"ip helper-address {interface['helper_address']}"
            script += "exit\n"
        script += "-" * 50 + "\n\n"

        script += "Static Routes:\n"
        script += "-" * 50 + "\n"
        for route in self.routes:
            script += f"ip route {route['destination']} {route['subnet_mask']} {route['next_hop']}\n"
        script += "-" * 50 + "\n\n"

        script += "Fin de configuration du routeur."
        return script
