from utils import *
from const import *
from Switch import Switch
from Network import Network
from Routeur import Routeur

print('-'*10 + " Network Configuration " + "-"*10+"\n")
#TODO load config from the file
net = Network("localhost")

while True:
    print("\n" + MAIN_MENU)
    choice = input("=> ")
    if choice == "0":
        #TODO transformer objet net en dict
        #TODO save net configuration
        break
    elif choice == "1":
        # ----- Config du network -----
        while True:
            print("\n" + NETWORK_MENU)
            choice = input("=> ")
            if choice == "0":
                break
            elif choice == "1":
                print(net.generate_config())

    elif choice == "2":
        # ----- Config du switch -----
        #TODO regex checking onname
        switch_name = input("Nom du Switch : ")
        switch_nb_int = int_input("Nombre d'interface : ",1,48)
        sw = Switch(switch_name, switch_nb_int)
        net.add_switch(sw)
        
        while True:
            print("\n" + SWITCH_MENU)
            choice = input("=> ")
            if choice == "0":
                break

            elif choice == "1":
                print(sw.generate_config())
            
            elif choice == "2":
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
            
            elif choice == "3":
                # ----- Config Trunk ------
                trunk_interfaces = []
                nb_trunks = int_input("Nombre de lien trunk", 0)

                vlans = []
                _ = 1
                while _ > 0:
                    _ = int_input("ID d'une VLAN autorisé (0 Tous, -1 stop) : ", -1)
                    if _ == 0:
                        vlans = sw.vlans
                        break
                    elif _ == -1:
                        break
                    vlans.append(_)

                for _ in range(nb_trunks):
                    interface = input("Nom de l'interface (ex GigabitEthernet0/1): ")
                    print(sw.add_interface(interface, "trunk", vlans))

            elif choice == "4":
                # ----- Config VTP ------
                #TODO regex checking domaine & password
                vtp_domain = input("VTP domain : ")
                vtp_password = input("VTP password: ")
                vtp_mode = closed_question("VTP mode (client/server): ", ["client", "server"])

                print(sw.set_vtp(vtp_domain, vtp_password, vtp_mode))
            
            elif choice == "5":
                # ----- Config Access Interface ------
                #TODO regex checking intf
                access_vlan = int_input("ID VLAN: ", 0)
                access_intf = input("Nom de l'interface (ex GigabitEthernet0/1): ")

                print(sw.add_interface(access_intf,"access", access_vlan))
    
    elif choice == "3":
        # ----- Config Router -----
        router_name = input("Nom du Routeur : ")
        rt = Routeur(router_name)

        while True:
            print("\n" + ROUTEUR_MENU)
            choice = input("=> ")
            if choice == "0":
                break
            elif choice == "1":
                print(rt.generate_config())
            
            elif choice == "2":
                # add interface
                intf = input("Nom de l'interface : ")
                ip_add = input("IP: ")
                subnet_mask = input("Masque de sous-réseau: ")
                description = input("Description (optionel): ")
                rt.add_interface(intf, ip_add, subnet_mask, description)