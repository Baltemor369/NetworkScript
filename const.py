MAIN_MENU = "--- MENU ---\n1. Network Configuration\n2. Ajouter un Switch\n3. Ajouter un Routeur\n\n0. Sortir\n"
SWITCH_MENU = "--- SWITCH MENU ---\n1. Generer config script\n2. Ajouter VLANs\n3. Configurer trunk\n4. Configurer VTP\n5. Configurer Interface\n\n0. Sortir\n"
NETWORK_MENU = "--- NETWORK MENU ---\n1. Generer config script\n\n0. Sortir\n"
ROUTEUR_MENU = "--- ROUTEUR MENU ---\n1. Generer config script\n2. Ajouter interface\n3. Ajouter Route Statique\n\n0. Sortir\n"

FILE="config.json"

YESNO= [ "yes", "no"]

# REGEX 
REG_IP = r"^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\." \
              r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\." \
              r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\." \
              r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
REG_MASK_CIDR = r"^\/([0-9]|[1-2][0-9]|3[0-2])$"
REG_MASK = r"^(255|254|252|248|240|224|192|128|0)\." \
              r"(255|254|252|248|240|224|192|128|0)\." \
              r"(255|254|252|248|240|224|192|128|0)\." \
              r"(255|254|252|248|240|224|192|128|0)$"
