MAIN_MENU = "--- MENU ---\n"\
    "1. Network Config\n" \
    "2. Switch Config\n" \
    "3. Routeur Config\n\n" \
    "0. Sortir\n"

SWITCH_MENU = "--- SWITCH MENU ---\n" \
    "1. Switch Liste\n" \
    "2. Ajouter un Switch\n" \
    "3. Supprimer Switch\n" \
    "4. Modifier Switch\n\n" \
    "0. Sortir\n"
SWITCH_MODIFY_MENU = "--- SWITCH MODIFY MENU ---\n" \
    "1. VTP config\n" \
    "2. VLANs config\n" \
    "3. Trunk Interface\n" \
    "4. Access Interface\n" \
    "0. Sortir\n" \

ROUTEUR_MENU = "--- ROUTEUR MENU ---\n" \
    "1. Routeur Liste\n" \
    "2. Ajouter un Routeur\n" \
    "3. Supprimer Routeur\n" \
    "4. Modifier Routeur\n\n" \
    "0. Sortir\n"
ROUTEUR_MODIFY_MENU = "--- ROUTEUR MODIFY MENU ---\n" \
    "1. Interface config\n" \
    "2. Static Route\n" \
    "0. Sortir\n"

HOST_MENU = "--- HOST MENU ---\n" \
    "1. Host Liste\n" \
    "2. Ajouter un Host\n" \
    "3. Supprimer Host\n" \
    "4. Modifier Host\n\n" \
    "0. Sortir\n"

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
