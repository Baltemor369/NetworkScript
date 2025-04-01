def int_input(question:str, min:int=None, max:int=None):
    while True:
        try:
            number = int(input(question))
        except:
            number = None
        if number:
            if (min is None or min <= number) and (max is None or number <= max):
                return number
        else:
            print("Please enter a valid answer.")

def closed_question(question:str, answers:list[str]):
    _ = input(question)
    
    for answer in answers:
        if _ and _ in answer:
            return answer
    
    return None


def generate_vlan_config(vlans, switch_name):
    """
    Génère un script de configuration pour des VLAN sur un switch.
    :param vlans: Liste des VLANs (id et nom) sous forme de tuple (id, nom).
    :param switch_name: Nom du switch.
    :return: Script de configuration en tant que chaîne de caractères.
    """
    script = f"Configurer VLANs pour le switch {switch_name}:\n"
    script += "-" * 50 + "\n"
    
    for vlan_id, vlan_name in vlans:
        script += f"vlan {vlan_id}\n"
        script += f"name {vlan_name}\n"
        script += "exit\n"

    script += "-" * 50 + "\nFin de configuration.\n"
    return script

def generate_trunk_config(trunk_interfaces, vlans):
    """
    Génère un script de configuration pour les interfaces en mode trunk.
    :param trunk_interfaces: Liste des interfaces à configurer en mode trunk.
    :param vlans: Liste des VLANs disponibles.
    :return: Script de configuration en tant que chaîne de caractères.
    """
    allowed_vlans = ",".join(str(vlan[0]) for vlan in vlans)
    script = "Configurer les interfaces en mode trunk:\n"
    script += "-" * 50 + "\n"

    for interface in trunk_interfaces:
        script += f"interface {interface}\n"
        script += "switchport mode trunk\n"
        script += f"switchport trunk allowed vlan {allowed_vlans}\n"
        script += "exit\n"

    script += "-" * 50 + "\nFin de configuration des trunks.\n"
    return script

def generate_interface_config(interfaces):
    """
    Génère un script de configuration pour des interfaces.
    :param interfaces: Liste des interfaces et de leurs paramètres sous forme de dictionnaire.
    :return: Script de configuration en tant que chaîne de caractères.
    """
    script = "Configurer les interfaces:\n"
    script += "-" * 50 + "\n"

    for interface in interfaces:
        script += f"interface {interface['name']}\n"
        
        if interface['mode'] == 'access':
            script += " switchport mode access\n"
            script += f" switchport access vlan {interface['vlan']}\n"
        elif interface['mode'] == 'trunk':
            script += " switchport mode trunk\n"
            vlans = ",".join(str(vlan) for vlan in interface['allowed_vlans'])
            script += f" switchport trunk allowed vlan {vlans}\n"
        
        script += " exit\n"

    script += "-" * 50 + "\nFin de configuration des interfaces."
    return script
