from utils import *
from const import *
from Switch import Switch
from Network import Network
from Routeur import Routeur

# Ajouter un switch au network
def add_switch(net:Network):
    #TODO regex checking
    switch_name = input("Nom du Switch : ")
    if not any(switch_name == sw.name for sw in net.switchs):
        sw = Switch(switch_name)
        net.add_switch(sw)

def del_switch(net:Network):
    #TODO regex checking
    switch_name = input("Nom du Switch : ")
    
    if any(switch_name == sw.name for sw in net.switchs):
        net.del_switch(switch_name)

# afficher list switch
def listing_switch(net:Network):
    for sw in net.switchs:
        print(sw.generate_config())

# config VLANs
def config_vlans(sw:Switch):
    nb_vlans = int_input("Nombre de vlan: ",0)

    i = 0
    while i < nb_vlans:
        vlan_name = input("Nom: ")
        vlan_id = int_input("ID: ", 0)

        exists = any(vlan_id == vlan["id"] or vlan_name == vlan["name"] for vlan in sw.vlans)

        if exists:
            print("Error: Une VLAN avec ce nom ou cette id existe déjà.")
        else:
            print(sw.add_vlan(vlan_id, vlan_name))
            i += 1 

# config VTP
def config_VTP(sw:Switch):
    #TODO regex checking domaine & password
    vtp_domain = input("VTP domain : ")
    vtp_password = input("VTP password: ")
    vtp_mode = closed_question("VTP mode (client/server): ", ["client", "server"])

    print(sw.set_vtp(vtp_domain, vtp_password, vtp_mode))

# config trunk
def config_trunk_intf(sw:Switch):
    nb_trunks = int_input("Nombre de lien trunk", 0)

    vlans = []
    V = input("VLANs autoriser sur le trunk:")
    V = V.split(" ")

    for _ in range(nb_trunks):
        interface = input("Nom de l'interface (ex GigabitEthernet0/1): ")
        print(sw.add_interface(interface, "trunk", vlans))

# config access intf
def config_access_intf(sw:Switch):
    access_intf = input("Nom de l'interface (ex GigabitEthernet0/1): ")
    access_vlan = int_input("ID VLAN: ", 0)

    print(sw.add_interface(access_intf,"access", access_vlan))

# modify a switch
def modify_switch(net:Network):
    sw_name = input("Nom du switch: ")
    target_sw = None
    for sw in net.switchs:
        if sw.name == sw_name:
            target_sw = sw
    
    if target_sw:
        while True:
            print(SWITCH_MODIFY_MENU)
            choice = input("=> ")
            print("\n")

            if choice == "0":
                break
            elif choice == "1":
                config_VTP(target_sw)
                pass
            elif choice == "2":
                config_vlans(target_sw)
                pass
            elif choice == "3":
                config_trunk_intf(target_sw)
                pass
            elif choice == "4":
                config_access_intf(target_sw)
                pass




# Ajouter un routeur au network
def add_routeur(net:Network):
    #TODO regex checking
    router_name = input("Nom du Routeur : ")
    if not any(router_name == rt.name for rt in net.routeurs):
        rt = Routeur(router_name)
        net.add_routeur(rt)

def del_routeur(net:Network):
    #TODO regex checking
    router_name = input("Nom du Routeur : ")
    if any(router_name == rt.name for rt in net.routeurs):
        net.del_routeur(router_name)

# afficher list routeur
def listing_routeur(net:Network):
    for rt in net.routeurs:
        print(rt.generate_config())

# config interface
def config_routeur_intf(rt:Routeur):
    intf = input("Nom de l'interface : ")
    ip_add = input("IP: ")
    subnet_mask = input("Masque de sous-réseau: ")
    dhcp_helper = input("DHCP_helper(optionnel): ")
    description = input("Description (optionnel): ")
    print(rt.add_interface(intf, ip_add, subnet_mask, description))
    if dhcp_helper:
        print(rt.add_dhcp_helper(intf, dhcp_helper))

# config static route
def config_static_route(rt:Routeur):
    # add static route
    network_add = input("Adresse réseau: ")
    subnet_mask = input("Masque de sous-réseau: ")
    next_hop = input("Passerelle: ")
    print(rt.add_route(network_add, subnet_mask, next_hop))

def modify_routeur(net:Network):
    rt_name = input("Nom du routeur: ")
    target_rt = None
    for rt in net.routeurs:
        if rt.hostname == rt_name:
            target_rt = rt
    
    if target_rt:

        while True:
            print(ROUTEUR_MODIFY_MENU)
            choice = input("=> ")
            print("\n")

            if choice == "0":
                break
            elif choice == "1":
                config_routeur_intf(target_rt)
                pass
            elif choice == "2":
                config_static_route(target_rt)
                pass



# afficher network config
def network_config(net:Network):
    print(net.generate_config())




###########################

print('-'*10 + " Network Configuration " + "-"*10+"\n\n")
net = Network("localhost")
_ = load_config(FILE)

if not _[0] :
    print(_[1])
else:
    net.load_config(_[1])
    while True:
        print(MAIN_MENU)
        choice = input("=> ")
        print("\n")
        if choice == "0":
            print("sauvegarde de la config réseau...")
            _ = save_config(FILE, net.to_dict())
            if not _ :
                print(_[1])
                input("Entrer pour quitter")
            else:
                print("[OK]")
            break
        elif choice == "1":
            print(net.generate_config())
            pass
        elif choice == "2":
            
            # SWITCH 
            while True:
                print(SWITCH_MENU)
                choice = input("=> ")
                print("\n")
                if choice == "0":
                    break
                elif choice == "1":
                    if net.switchs:
                        for sw in net.switchs:
                            print(sw.generate_config())
                    else:
                        print("Aucun Switch enregistré")
                elif choice == "2":
                    add_switch(net)
                    pass
                elif choice == "3":
                    del_switch(net)
                    pass
                elif choice == "4":
                    modify_switch(net)
                    pass
            pass
        elif choice == "3":
            
            # ROUTEUR
            while True:
                print("\n" + ROUTEUR_MENU)
                choice = input("=> ")
                print("\n")
                if choice == "0":
                    break
                elif choice == "1":
                    if net.routeurs:
                        for rt in net.routeurs:
                            print(rt.generate_config())
                    else:
                        print("Aucun Routeur enregistré")
                elif choice == "2":
                    add_routeur(net)
                    pass
                elif choice == "3":
                    del_routeur(net)
                    pass
                elif choice == "3":
                    modify_routeur(net)
                    pass
            pass