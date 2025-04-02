from utils import *
from const import *
from Switch import Switch
from Network import Network

print('-'*10 + " Network Configuration " + "-"*10+"\n")
#TODO load config from the file
net = Network("localhost")

while True:
    print("\n" + MAIN_MENU)
    choice = input("Enter your choice : ")
    if choice == "0":
        #TODO transformer objet net en dict
        #TODO save net configuration
        break
    elif choice == "1":
        pass
    elif choice == "2":
        # ----- Config du switch -----
        #TODO regex checking onname
        switch_name = input("Name of the Switch : ")
        switch_nb_int = int_input("Number of interfaces : ",1,48)
        sw = Switch(switch_name, switch_nb_int)
        
        while True:
            print("\n" + SWITCH_MENU)
            choice = input("Enter your choice : ")
            if choice == "0":
                break

            elif choice == "1":
                print(sw.generate_config())
            
            elif choice == "2":
                nb_vlans = int_input("How many vlans ? ",0)

                i = 0
                while i < nb_vlans:
                    vlan_name = input("Name of the VLAN: ")
                    vlan_id = int_input("ID of the VLAN: ", 0)

                    exists = any(vlan_id == vlan["id"] or vlan_name == vlan["name"] for vlan in sw.vlans)

                    if exists:
                        print("Error: A VLAN with the same ID or name already exists. Please try again.")
                    else:
                        print(sw.add_vlan(vlan_id, vlan_name))
                        i += 1 
            
            elif choice == "3.":
                # ----- Config Trunk ------
                trunk_interfaces = []
                nb_trunks = int_input("How many trunk interfaces? ", 0)

                vlans = []
                _ = 1
                while _ > 0:
                    _ = int_input("Enter the id of a allowed vlan for the trunk (0 for all, -1 to exit) : ", -1)
                    if _ == 0:
                        vlans = sw.vlans
                        break
                    elif _ == -1:
                        break
                    vlans.append(_)

                for _ in range(nb_trunks):
                    interface = input("Enter the name of the trunk interface (e.g., GigabitEthernet0/1): ")
                    print(sw.add_interface(interface, "trunk", vlans))

            elif choice == "4":
                # ----- Config VTP ------
                #TODO regex checking domaine & password
                vtp_domain = input("Enter the VTP domain name: ")
                vtp_password = input("Enter the VTP domain password: ")
                vtp_mode = closed_question("Enter the VTP mode (client/server): ", ["client", "server"])

                print(sw.set_vtp(vtp_domain, vtp_password, vtp_mode))
            
            elif choice == "5":
                # ----- Config Access Interface ------
                #TODO regex checking intf
                access_vlan = int_input("Enter the id of the access vlan: ", 0)
                access_intf = input("Enter the name of the access interface (e.g., GigabitEthernet0/1): ")

                print(sw.add_interface(access_intf,"access", access_vlan))